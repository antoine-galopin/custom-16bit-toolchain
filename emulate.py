#!/usr/bin/env python3
"""Run the emulator CLI."""
import sys
import os

# Add the emulator package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'emulator'))

from emulator.src.cli import main

if __name__ == '__main__':
    main()