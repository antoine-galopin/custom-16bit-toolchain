# ISA specification

## Overview

This document defines version 0.1 of the custom 16-bit instruction set architecture used by this project.

The current ISA is built around fixed-size 16-bit instructions :
- 4 bits for the opcode
- 12 bits for operands or parameters

This first version focuses on :
- arithmetic and logic instructions
- immediate loading
- control flow
- a minimal execution model suitable for an assembler and emulator

## Global assumptions

- Word size : 16 bits
- Instruction size : 16 bits
- Opcode size : 4 bits
- Operand field size : 12 bits
- Register count : 16 registers
- Register names : R0 to R15
- Program counter : PC
- The program counter points to the next instruction
- After a normal instruction, PC increments by 1
- JUMP and JUMPIF replace PC with the target address
- JUMPIF uses the zero result of the last ALU operation

## Register model

The architecture currently defines 16 general-purpose registers :
- R0
- R1
- R2
- R3
- R4
- R5
- R6
- R7
- R8
- R9
- R10
- R11
- R12
- R13
- R14
- R15
Each register is encoded on 4 bits

## Flags

One Z flag, set to 1 when the result of the last ALU operation is 0, otherwise 0.

## Memory model

4096 16-bit words, word-addressed, shared for instructions and data, addresses from 0 to 4095

## Execution model

The processor executes instructions using a basic fetch-decode-execute cycle :
1. Read the instruction pointed to by PC
2. Decode the opcode and operands
3. Execute the instruction
4. Update PC

For most instructions, PC is incremented by 1 after execution.
For jump instructions :
- JUMP addr sets PC = addr
- JUMPIF addr sets PC = addr only if the last ALU result is equal to 0

## Instruction format

All instructions are encoded on 16 bits.
General layout :
- bits 15..12 opcode
- bits 11..0 operands or parameters
Different instructions families use the 12-bit operand field differently.

## ALU instruction format

Used by :
- ADD
- SUB
- XOR
- XNOR
- AND
- NAND
- OR
- NOR
Bit layout :
- bits 11..8 : destination register
- bits 7..4 : source register 1
- bits 3..0 : source register 2
Form :
- OP RD RS1 RS2
Example :
- ADD R3 R1 R2
Meaning :
- R3 ← R1 + R2

## Load instruction format

Used by :
- LOAD
Bit layout :
- bits 11..8 : destination register
- bits 7..0 : 8-bit immediate value
Form :
- LOAD RD IMM8
Example :
- LOAD R1 42
Meaning :
- R1 ← 42

## JUMP instruction format

Used by :
- JUMP
- JUMPIF
Bit layout :
- bits 11..0 : 12-bit absolute address
Form :
- JUMP ADDR12
- JUMPIF ADDR12
Examples :
- JUMP 12
- JUMPIF 24
Meaning :
- PC ← 12
- PC ← 24 if the last ALU result is 0

## HALT instruction format

Used by :
- HALT
Bit layout :
- bits 11..0 : unused, set to 0
Form :
- HALT
Meaning :
- stop execution

## Opcode table

| Opcode | Mnemonic | Category | Description |
|---|---|---|---|
| 0001 | ADD | ALU | Add two registers and store the result |
| 0010 | SUB | ALU | Subtract two registers and store the result |
| 0011 | XOR | ALU | XOR two registers and store the result |
| 0100 | XNOR | ALU | XNOR two registers and store the result |
| 0101 | AND | ALU | AND two registers and store the result |
| 0110 | NAND | ALU | NAND two registers and store the result |
| 0111 | OR | ALU | OR two registers and store the result |
| 1000 | NOR | ALU | NOR two registers and store the result |
| 1001 | LOAD | Data movement | Load an 8-bit immediate into a register |
| 1010 | HALT | Control | Stop execution |
| 1011 | JUMP | Control | Jump to an absolute address |
| 1100 | JUMPIF | Control | Jump to an absolute address if last ALU result is zero |
| 1101 | — | Reserved | Undefined |
| 1110 | — | Reserved | Undefined |
| 1111 | — | Reserved | Undefined |

## Current limitations

This ISA version is intentionally minimal.
Not yet defined :
- memory access instructions other than LOAD
- stack operations
- function call conventions
- relative jumps
