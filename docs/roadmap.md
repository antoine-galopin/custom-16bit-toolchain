# Roadmap

## Current status

- **Completed**
  - ISA specification
  - Assembly language specification
  - Assembler implementation and tests
  - Emulator implementation and tests
- **Planned**
  - C-like language
  - Compiler

## Completed work

### Phase 1 - ISA
- [x] Define registers
- [x] Define flags
- [x] Define memory model
- [x] Define instruction encoding
- [x] Define instruction set

### Phase 2 - Assembly language
- [x] Define syntax
- [x] Define labels and resolution
- [x] Define comments
- [x] Decide directive support for v0.1 (none supported)
- [x] Define file format expectations

### Phase 3 - Assembler
- [x] Implement parser and tokenizer
- [x] Implement label resolution
- [x] Implement binary generation
- [x] Add unit tests

### Phase 4 - Emulator
- [x] Design binary loader
- [x] Implement fetch / decode / execute loop
- [x] Implement registers and memory
- [x] Add execution traces
- [x] Add integration tests

## Next work

### Phase 5 - C-like language
- [ ] Define grammar
- [ ] Define supported types
- [ ] Define statements and expressions
- [ ] Define language limitations

### Phase 6 - Compiler
- [ ] Implement lexer
- [ ] Implement parser
- [ ] Build AST
- [ ] Add semantic checks
- [ ] Generate assembly
- [ ] Add end-to-end tests
