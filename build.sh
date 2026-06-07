#!/bin/bash
# build.sh - Script de build para o Render

echo "🚀 Starting build process..."

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Install gunicorn for production
echo "📦 Installing gunicorn..."
pip install gunicorn

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p static
mkdir -p templates

# Set permissions
echo "🔧 Setting permissions..."
chmod -R 755 static templates

echo "✅ Build completed successfully!"