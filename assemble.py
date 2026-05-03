#!/usr/bin/env python3
"""Run the assembler CLI."""
import sys
import os

# Add the assembler package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'assembler'))

from assembler.src.cli import main

if __name__ == '__main__':
    main()