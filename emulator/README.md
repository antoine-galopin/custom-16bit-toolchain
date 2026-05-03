# Emulator

This module executes binary produced for the custom 16-bit ISA by simulating the target machine.

## Usage

Load a binary program represented as text lines of 16-bit `0`/`1` values and run the emulator.

The emulator provides:
- `Emulator.load_program(binary_lines)`
- `Emulator.run()`
- `Emulator.registers`, `Emulator.pc`, `Emulator.zero_flag`, and `Emulator.halted`

A small CLI is available in `emulator/src/cli.py` for running a binary text file and printing the final register state.
