# Examples

## Directory structure

- `asm/`: Assembly language source files (`.asm`)
- `expected/`: Expected outputs from running examples
  - `*.bin`: Binary output from the assembler
  - `*.out`: Execution trace output from the emulator

## Example programs

### multiply.asm

Multiplies two numbers (4 and 5) using repeated addition.

**How to run:**
```bash
./assemble.py examples/asm/multiply.asm examples/expected/multiply.bin
./emulate.py examples/expected/multiply.bin examples/expected/multiply.out
cat examples/expected/multiply.out
```

**Expected result:**
- R3 = 20 (4 * 5)
- Execution time: 24 instructions
- Zero flag: 1

## Testing examples

Integration tests verify that example programs produce expected results. Run them with:
```bash
python3 -m pytest tests/integration/
```
