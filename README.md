# 🎮 Rock Paper Scissors

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com)
[![Render](https://img.shields.io/badge/Render-Deployed-purple.svg)](https://render.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> A classic Rock Paper Scissors game with a modern web interface. Play against the computer, customize rounds, and track your match history.

## 🎮 Live Demo

**Deployed on Render:** [https://rock-paper-scissors.onrender.com](https://rock-paper-scissors.onrender.com)

> *Replace the URL above with your actual Render URL after deployment*

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎮 **Classic Gameplay** | Traditional Rock Paper Scissors rules |
| 🎯 **Customizable Rounds** | Best of 3, 5, 7, or custom (1-20 rounds) |
| 🤖 **Fair Computer** | Random moves, no cheating |
| 📊 **Match History** | Track every round with detailed results |
| 🏆 **Score Tracking** | Real-time score updates after each round |
| 📱 **Responsive Design** | Works on desktop, tablet, and mobile |
| 🎨 **Modern UI** | Gradient design with smooth animations |
| ⚡ **Lightweight** | Only one dependency (Flask) |
| 🔄 **Play Again** | Easy restart with different configurations |

---

## 📖 How to Play

### Game Rules

| Your Move | Beats | Loses to |
|-----------|-------|----------|
| 🪨 **Rock** | ✂️ Scissors | 📄 Paper |
| ✂️ **Scissors** | 📄 Paper | 🪨 Rock |
| 📄 **Paper** | 🪨 Rock | ✂️ Scissors |

### Step-by-Step

1. **Configure the Game**
   - Choose number of rounds (Best of 3, 5, 7, or Custom)
   - Click "Start Game"

2. **Play Rounds**
   - Click on Rock (🪨), Scissors (✂️), or Paper (📄)
   - Computer makes its choice simultaneously
   - Winner receives +1 point

3. **Track Progress**
   - Score updates instantly
   - Match history shows all plays
   - Remaining rounds counter keeps you informed

4. **Game Over**
   - Final score displayed
   - Complete match history
   - Options to play again or return to menu

---

## 🚀 Local Development

### Prerequisites

| Requirement | Version |
|-------------|---------|
| Python | 3.8 or higher |
| pip | Latest version |
| Git | (Optional) |

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/rock-paper-scissors.git
cd rock-paper-scissors

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
Access Locally
Open your browser and navigate to:

text
http://localhost:5000
🚢 Deploy on Render
This project is configured for easy deployment on Render.

Files Included for Deployment
File	Purpose
render.yaml	Render service configuration
build.sh	Build script for Render
runtime.txt	Python version specification
requirements.txt	Python dependencies
Deploy Steps
Step 1: Push to GitHub
bash
git add .
git commit -m "Initial commit"
git push origin main
Step 2: Deploy on Render
Create an account on render.com

Click "New +" → "Web Service"

Connect your GitHub repository

Configure the service:

Setting	Value
Name	rock-paper-scissors
Region	Oregon (US West)
Branch	main
Runtime	Python
Build Command	./build.sh
Start Command	gunicorn app:app
Plan	Free
Step 3: Add Environment Variables
Key	Value
SECRET_KEY	(Click "Generate" or use a strong key)
FLASK_ENV	production
PYTHON_VERSION	3.11.0
Step 4: Deploy
Click "Create Web Service"

The deployment will take 2-5 minutes. You'll see the build logs in real-time.

Step 5: Access Your App
After successful deployment:

text
https://rock-paper-scissors.onrender.com
*Note: The free tier spins down after 15 minutes of inactivity. The first request after inactivity may take 30-50 seconds to wake up.*

🏗️ Project Architecture
Structure
text
rock-paper-scissors/
│
├── app.py                 # Flask backend with game logic
├── requirements.txt       # Python dependencies
├── build.sh              # Render build script
├── render.yaml           # Render configuration
├── runtime.txt           # Python version
├── .gitignore            # Git ignore rules
│
├── templates/            # HTML templates
│   ├── index.html        # Main menu
│   ├── config.html       # Round configuration
│   ├── game.html         # Game interface
│   └── result.html       # Results screen
│
└── static/               # Static assets
    └── style.css         # Custom styling
Game Logic Flow
text
Main Menu → Configure Rounds → Game Screen
                                    ↓
                            Player Chooses Move
                                    ↓
                            Computer Chooses Move
                                    ↓
                            Determine Winner
                                    ↓
                            Update Score & History
                                    ↓
                    ┌───────────────┴───────────────┐
                    │                               │
                More Rounds?                     Game Over
                    │                               │
                    ↓                               ↓
            Back to Game Screen              Results Screen
                                                  ↓
                                            Play Again?
🔧 Tech Stack
Category	Technology	Version
Backend	Python	3.11
Web Framework	Flask	3.0.0
Frontend	HTML5	-
Styling	CSS3	-
Interactivity	Vanilla JavaScript	ES6
Production Server	Gunicorn	21.2.0
Deployment	Render	-
📦 Dependencies
txt
Flask==3.0.0
gunicorn==21.2.0
🎨 Customization
Change Game Rules
Edit the RESULT_MATRIX in app.py:

python
RESULT_MATRIX = [
    [None, None, None, None],
    [None, "tie", "player", "computer"],  # Rock
    [None, "computer", "tie", "player"],  # Scissors
    [None, "player", "computer", "tie"]   # Paper
]
Change Colors
Modify the CSS in static/style.css:

css
/* Main gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
Change Round Limits
In app.py, modify the start_game() function:

python
if total_rounds > 20:  # Change 20 to your preferred max
    total_rounds = 20
🧪 Testing
Manual Test Cases
Test Case	Expected Result
Rock vs Scissors	Player wins
Rock vs Paper	Computer wins
Rock vs Rock	Tie
Best of 3 rounds	Game ends after 2 wins
Custom rounds (5)	Exactly 5 rounds played
Invalid input	Falls back to default
Run Local Tests
bash
python app.py
# Manually test all scenarios above
🐛 Troubleshooting
Common Issues
Issue	Solution
Build fails on Render	Check build.sh is executable: git update-index --chmod=+x build.sh
Static files not loading	Verify static/ folder is in root directory
Session errors	Set SECRET_KEY environment variable
Port binding error	Ensure PORT environment variable is used in app.py
View Render Logs
Go to your service on render.com

Click "Logs" tab

See real-time build and runtime logs

📝 To-Do List
Add sound effects

Create dark/light theme toggle

Add difficulty levels

Implement keyboard shortcuts (1,2,3 keys)

Add multiplayer mode

Create statistics dashboard

Add achievements system

🤝 Contributing
Contributions are welcome!

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open a Pull Request

Guidelines
Keep code simple and readable

Test all changes manually

Update README if needed

Follow PEP 8 style guide

📄 License
Distributed under the MIT License.

text
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions...

Full license text: https://opensource.org/licenses/MIT
👤 Author
Your Name

GitHub: @yourusername

LinkedIn: Your Name

Email: your.email@example.com

🙏 Acknowledgments
Thanks to	For
Flask	Web framework
Render	Free hosting
Google Fonts	Poppins font
Unicode	Game emojis
Shields.io	Badges
📞 Support
Open an Issue → GitHub Issues

Email → your.email@example.com

🌟 Show Your Support
If you like this project:

⭐ Star the repository

🐛 Report bugs

💡 Suggest features

🔄 Share with others

📊 Project Status
Metric	Status
Active Development	✅ Yes
Deployed	✅ Render
Documentation	✅ Complete
Test Coverage	🟡 Manual
🚀 Quick Links
GitHub Repository

Live Demo on Render

Report Bug

Request Feature

Made with 🎮 by [Your Name]

Enjoy the game! May luck be on your side! 