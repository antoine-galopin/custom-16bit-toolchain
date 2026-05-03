class EmulatorError(Exception):
    """Emulator runtime error."""


class Emulator:
    MEMORY_SIZE = 4096
    ALU_OPCODES = {
        0x1: 'ADD',
        0x2: 'SUB',
        0x3: 'XOR',
        0x4: 'XNOR',
        0x5: 'AND',
        0x6: 'NAND',
        0x7: 'OR',
        0x8: 'NOR',
    }

    def __init__(self):
        self.reset()

    def reset(self):
        self.memory = [0] * self.MEMORY_SIZE
        self.registers = [0] * 16
        self.pc = 0
        self.zero_flag = 0
        self.halted = False
        self.instruction_count = 0

    def load_program(self, binary_lines):
        self.reset()
        for address, line in enumerate(binary_lines):
            if address >= self.MEMORY_SIZE:
                raise EmulatorError('Program too large for memory')
            raw = line.strip()
            if len(raw) != 16 or any(c not in '01' for c in raw):
                raise EmulatorError(f'Invalid binary instruction: {line!r}')
            self.memory[address] = int(raw, 2)

    def run(self, max_steps=100000):
        while not self.halted:
            self.step()
            if self.instruction_count >= max_steps:
                raise EmulatorError('Maximum execution steps exceeded')

    def step(self):
        if self.halted:
            raise EmulatorError('Emulator is halted')

        if self.pc < 0 or self.pc >= self.MEMORY_SIZE:
            raise EmulatorError(f'Program counter out of range: {self.pc}')

        instruction = self.memory[self.pc]
        opcode = (instruction >> 12) & 0xF

        if opcode in self.ALU_OPCODES:
            self._execute_alu(opcode, instruction)
            self.pc += 1
        elif opcode == 0x9:
            self._execute_load(instruction)
            self.pc += 1
        elif opcode == 0xA:
            self.halted = True
        elif opcode == 0xB:
            self._execute_jump(instruction)
        elif opcode == 0xC:
            self._execute_jumpif(instruction)
        else:
            raise EmulatorError(f'Invalid opcode: {opcode:04b}')

        self.instruction_count += 1

    def _execute_alu(self, opcode, instruction):
        rd = (instruction >> 8) & 0xF
        rs1 = (instruction >> 4) & 0xF
        rs2 = instruction & 0xF
        a = self.registers[rs1]
        b = self.registers[rs2]

        if opcode == 0x1:  # ADD
            result = (a + b) & 0xFFFF
        elif opcode == 0x2:  # SUB
            result = (a - b) & 0xFFFF
        elif opcode == 0x3:  # XOR
            result = a ^ b
        elif opcode == 0x4:  # XNOR
            result = ~(a ^ b) & 0xFFFF
        elif opcode == 0x5:  # AND
            result = a & b
        elif opcode == 0x6:  # NAND
            result = ~(a & b) & 0xFFFF
        elif opcode == 0x7:  # OR
            result = a | b
        elif opcode == 0x8:  # NOR
            result = ~(a | b) & 0xFFFF
        else:
            raise EmulatorError(f'Unsupported ALU opcode: {opcode:04b}')

        self.registers[rd] = result
        self.zero_flag = 1 if result == 0 else 0

    def _execute_load(self, instruction):
        rd = (instruction >> 8) & 0xF
        imm = instruction & 0xFF
        self.registers[rd] = imm

    def _execute_jump(self, instruction):
        address = instruction & 0xFFF
        self._validate_address(address)
        self.pc = address

    def _execute_jumpif(self, instruction):
        address = instruction & 0xFFF
        if self.zero_flag == 1:
            self._validate_address(address)
            self.pc = address
        else:
            self.pc += 1

    def _validate_address(self, address):
        if address < 0 or address >= self.MEMORY_SIZE:
            raise EmulatorError(f'Invalid jump address: {address}')
