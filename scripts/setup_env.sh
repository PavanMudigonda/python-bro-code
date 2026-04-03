#!/bin/bash
# This script sets up a Python virtual environment and installs project dependencies.

echo "Creating python virtual environment (venv)..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing main requirements..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping."
fi

echo "Installing documentation requirements..."
if [ -f "requirements-docs.txt" ]; then
    pip install -r requirements-docs.txt
else
    echo "requirements-docs.txt not found. Skipping."
fi

echo "========================================================="
echo "Setup complete! To activate the environment, run:"
echo "source venv/bin/activate"
echo "========================================================="
