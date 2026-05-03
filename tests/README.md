# Tests

## Directory structure

- `assembler/`: Assembler unit tests (already present)
- `integration/`: End-to-end tests for assembler + emulator

## Running tests

Run all tests:
```bash
python3 -m pytest
```

Run only unit tests:
```bash
python3 -m pytest assembler/tests/
```

Run only integration tests:
```bash
python3 -m pytest tests/integration/
```

## Test coverage

- **Unit tests**: Parser, encoder, symbol table, emulator core
- **Integration tests**: Full assembly → emulation pipeline for examples
