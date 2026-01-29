#!/bin/bash

echo "🔧 Setting up BNRA development environment..."
echo "============================================"

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo "=================="
echo "To activate virtual environment:"
echo "  source venv/bin/activate"
echo ""
echo "To run the API:"
echo "  python api/main.py"
echo ""
echo "To run the dashboard:"
echo "  python dashboard/app.py"
