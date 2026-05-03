# Assembly language specification

## Overview

This document defines the human-readable assembly syntax for the custom 16-bit ISA defined in [isa.md](../isa.md).

## Syntax

### General rules
- One statement per line
- Instructions use mnemonics
- Operands separated by single spaces
- No commas between operands
- Leading/trailing whitespace ignored
- Blank lines ignored

### Instruction syntax
MNEMONIC [operand1] [operand2] [operand3]

**Three-register form** (ALU):

ADD R3 R1 R2
SUB R3 R1 R2

**Register + immediate**:

LOAD R1 42

**Immediate-only**:

JUMP 12
JUMPIF 24

**No-operand**:

HALT

### Register syntax
- R0 to R15
- Case-insensitive

### Numeric literals
- Decimal, hexadecimal (0x prefix), or binary (0b prefix)
- No negative numbers
- Values must fit the target instruction field:
  - `LOAD`: 0–255
  - `JUMP` / `JUMPIF`: 0–4095

## Labels

### Declaration

label_name:

- Starts with letter/underscore
- Letters, digits, underscore only
- Case-sensitive
- Max 32 chars
- Unique per file
- Start of line only

### Usage

loop:
JUMP loop
JUMPIF loop

## Directives

**None supported in v0.1.**

## Comments

Start with `;` to end of line:

ADD R1 R0 R0 ; clear R1

- Own line or after instruction
- Ignored by assembler

## File format expectations

### Valid content
1. Instructions
2. Labels  
3. Comments
4. Blank lines

### Rules
- UTF-8 encoding
- LF or CRLF line endings
- Extension: `.asm`
- No size limit

## Error cases

Assembler rejects:
1. Unknown mnemonic
2. Wrong operand count
3. Invalid register
4. Invalid number
5. Duplicate label
6. Undefined label

## Examples

**Valid**:

; Simple loop
start:
LOAD R1 10
loop:
SUB R1 R1 R0
JUMPIF loop
HALT

**Invalid**:

add r1 r2 r3 ; lowercase
LOAD RX 42 ; invalid register
JUMP 5000 ; too large
ADD R1 ; too few operands