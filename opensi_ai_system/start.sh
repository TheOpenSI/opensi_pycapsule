#!/bin/sh

# Check if main.py exists
if [ -f /usr/src/app/main.py ]; then
    echo "Executing main.py..."
    python3 /usr/src/app/main.py
else
    echo "Nothing to execute, shutting down."
fi
