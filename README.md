# custom-16bit-toolchain

A personal project to design and implement a custom 16-bit instruction set, an assembler, an emulator, and a small C-like compiler targeting this architecture.

## Project status

Early development.

Current focus :
- ISA specification
- Assembly language specification
- Assembler implementation

## Overview

This project is organized around a custom 16-bit architecture.

Planned toolchain :

```text
C-like source code
    ↓
Compiler
    ↓
Custom assembly
    ↓
Assembler
    ↓
16-bit binary
    ↓
Emulator
```

Current instruction set :
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
