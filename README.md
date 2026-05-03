# custom-16bit-toolchain

A personal project to design and implement a custom 16-bit instruction set, an assembler, an emulator, and a small C-like compiler targeting this architecture.

## Project status

Early development.

Current status:
- ISA defined
- Assembly language specified
- Assembler implemented and tested

Current focus:
- Emulator design and implementation
- C-like language definition and compiler planning

## Usage

### Assembling and running code

1. Write your assembly code in a `.asm` file (see `examples/asm/`).
2. Assemble it to binary: `./assemble.py input.asm output.bin`
3. Run the binary in the emulator: `./emulate.py output.bin output.txt`
4. Check `output.txt` for final register values and execution summary.

Example:
```bash
./assemble.py examples/asm/multiply.asm temp.bin
./emulate.py temp.bin temp.out
cat temp.out
```

This will show the result of the multiplication in the registers (e.g., R1 contains the result).

## Project status
- 16-bit fixed-size ISA
- 16 registers R0 to R15
- 12 defined opcodes
- ALU instructions use 3-register encoding
- LOAD uses register + 8-bit immediate
- JUMP and JUMPIF use 12-bit absolute addresses

## Goals

- Define a custom 16-bit ISA
- Design a readable assembly language for this ISA
- Build an assembler that generates binary code
- Build an emulator able to execute this binary
- Define a minimal C-like language
- Build a compiler from the C-like language to the custom assembly langage

## Repository structure

```text
docs/        Specifications and design documents
assembler/   Assembler source code and tests
compiler/    Compiler source code and tests
emulator/    Emulator source code and tests
examples/    Example programs
tests/       Integration tests
```
