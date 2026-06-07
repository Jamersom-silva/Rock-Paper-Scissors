from flask import Flask, render_template, request, session, redirect, url_for
import random
import os

app = Flask(__name__)
# Use environment variable for secret key in production
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))

# ============================================
# CONSTANTS
# ============================================

ROCK = 1
SCISSORS = 2
PAPER = 3

# Result matrix [player][computer]
RESULT_MATRIX = [
    [None, None, None, None],
    [None, "tie", "player", "computer"],
    [None, "computer", "tie", "player"],
    [None, "player", "computer", "tie"]
]

NAMES = {
    ROCK: "🪨 ROCK",
    SCISSORS: "✂️ SCISSORS",
    PAPER: "📄 PAPER"
}

# ============================================
# HELPER FUNCTIONS
# ============================================

def determine_winner(player_move, computer_move):
    """Returns 'player', 'computer' or 'tie'"""
    return RESULT_MATRIX[player_move][computer_move]

# ============================================
# ROUTES
# ============================================

@app.route('/')
def index():
    """Home page - Main menu"""
    session.clear()
    return render_template('index.html')

@app.route('/config')
def config():
    """Configuration page - Choose number of rounds"""
    return render_template('config.html')

@app.route('/start', methods=['POST'])
def start_game():
    """Initialize game with number of rounds"""
    try:
        option = int(request.form.get('option'))
        
        if option == 1:
            total_rounds = 3
        elif option == 2:
            total_rounds = 5
        elif option == 3:
            total_rounds = 7
        elif option == 4:
            total_rounds = int(request.form.get('custom_rounds', 3))
            if total_rounds < 1 or total_rounds > 20:
                total_rounds = 3
        else:
            total_rounds = 3
    except (TypeError, ValueError):
        total_rounds = 3
    
    session['total_rounds'] = total_rounds
    session['current_round'] = 1
    session['score'] = {'player': 0, 'computer': 0}
    session['history'] = []
    session['game_over'] = False
    
    return redirect(url_for('game'))

@app.route('/game')
def game():
    """Main game page"""
    if 'total_rounds' not in session:
        return redirect(url_for('index'))
    
    if session.get('game_over', False):
        return redirect(url_for('result'))
    
    return render_template('game.html', 
                         round_num=session['current_round'],
                         total_rounds=session['total_rounds'],
                         score=session['score'])

@app.route('/play', methods=['POST'])
def play():
    """Process a single round"""
    if session.get('game_over', False):
        return redirect(url_for('result'))
    
    # Get player move from form
    try:
        player_move = int(request.form.get('move'))
        if player_move not in [ROCK, SCISSORS, PAPER]:
            return redirect(url_for('game'))
    except (TypeError, ValueError):
        return redirect(url_for('game'))
    
    # Computer move (random)
    computer_move = random.randint(ROCK, PAPER)
    
    # Determine winner
    winner = determine_winner(player_move, computer_move)
    
    # Create round result
    round_result = {
        'round': session['current_round'],
        'player_move': NAMES[player_move],
        'computer_move': NAMES[computer_move],
        'winner': winner
    }
    
    # Update score based on winner
    if winner == 'player':
        session['score']['player'] += 1
        round_result['message'] = '🎉 YOU WIN THIS ROUND! +1 point 🎉'
    elif winner == 'computer':
        session['score']['computer'] += 1
        round_result['message'] = '💀 COMPUTER WINS THIS ROUND! +1 point 💀'
    else:
        round_result['message'] = '🤝 TIE! No points awarded! 🤝'
    
    # Save to history
    session['history'].append(round_result)
    
    # Check if game is over
    if session['current_round'] >= session['total_rounds']:
        session['game_over'] = True
        return redirect(url_for('result'))
    
    # Next round
    session['current_round'] += 1
    
    return redirect(url_for('game'))

@app.route('/result')
def result():
    """Show final results"""
    if 'total_rounds' not in session:
        return redirect(url_for('index'))
    
    final_score = session['score']
    total_rounds = session['total_rounds']
    history = session.get('history', [])
    
    # Determine overall winner
    if final_score['player'] > final_score['computer']:
        winner = 'player'
        winner_message = '🏆 CONGRATULATIONS! YOU WON THE GAME! 🏆'
    elif final_score['computer'] > final_score['player']:
        winner = 'computer'
        winner_message = '🤖 THE COMPUTER WON THE GAME! 🤖'
    else:
        winner = 'tie'
        winner_message = '🤝 THE GAME ENDED IN A TIE! 🤝'
    
    return render_template('result.html',
                         final_score=final_score,
                         total_rounds=total_rounds,
                         history=history,
                         winner=winner,
                         winner_message=winner_message)

@app.route('/reset')
def reset():
    """Reset game completely"""
    session.clear()
    return redirect(url_for('index'))

# ============================================
# RUN THE APP
# ============================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV', 'development') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)