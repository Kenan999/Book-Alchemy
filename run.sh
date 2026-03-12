#!/bin/bash

# Book Alchemy Setup & Run Script
# This script automates the installation and execution of the application.

echo "🧪 Initializing Book Alchemy..."

# 1. Determine the correct Python command
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Error: Python 3 is not installed. Please install it to continue."
    exit 1
fi

# 2. Check for virtual environment and create if missing
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    $PYTHON_CMD -m venv venv
    if [ $? -ne 0 ]; then
        echo "❌ Error: Failed to create virtual environment. Ensure 'venv' is installed."
        exit 1
    fi
fi

# 3. Activate the environment based on OS
case "$(uname -s)" in
    Darwin*|Linux*)
        echo "🍎/🐧 Activating environment (Unix-like)..."
        source venv/bin/activate
        ;;
    CYGWIN*|MINGW*|MSYS*)
        echo "🪟 Activating environment (Windows)..."
        source venv/Scripts/activate
        ;;
    *)
        echo "❓ Unknown OS. Attempting cross-platform activation..."
        source venv/bin/activate || source venv/Scripts/activate
        ;;
esac

# 4. Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# 5. Seed the database
echo "🌱 Seeding database..."
$PYTHON_CMD seed.py

# 6. Run the application
echo "🚀 Starting Book Alchemy on port 5002..."
$PYTHON_CMD app.py
