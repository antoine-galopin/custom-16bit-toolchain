# Binary format

## Overview

This project currently represents assembled programs as UTF-8 text files containing one encoded instruction per line.
The assembler CLI writes each 16-bit instruction as a binary string of `0` and `1` characters.

## File layout

- UTF-8 encoded text file
- One instruction per line
- Each line contains exactly 16 characters: `0` or `1`
- Lines are terminated by LF or CRLF
- No blank lines are written between instructions
- File extension is not enforced by the assembler, but `.bin` or `.txt` are reasonable conventions

## Instruction encoding

Each instruction is encoded on 16 bits:
- bits 15..12: opcode
- bits 11..0: operands or immediate fields, depending on the instruction

The current ISA uses the following instruction encoding families:
- ALU instructions encode three registers in bits 11..0
- LOAD encodes a destination register and an 8-bit immediate
- JUMP and JUMPIF encode a 12-bit absolute address
- HALT sets bits 11..0 to zero

## Example output

For the assembly program:

```
LOAD R1 42
ADD R2 R1 R0
JUMP 12
HALT
```

The assembler currently produces:

```
1001000100101010
0001001000010000
1011000000001100
1010000000000000
```

## Labels and resolution

Labels are resolved during assembly to absolute instruction addresses.
After resolution, the binary output contains only numeric jump targets, not label names.
