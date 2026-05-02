from assembler.src.parser import tokenize, parse_immediate

instructions = {
    'ADD': '0001',
    'SUB': '0010',
    'XOR': '0011',
    'XNOR': '0100',
    'AND': '0101',
    'NAND': '0110',
    'OR': '0111',
    'NOR': '1000',
    'LOAD': '1001',
    'HALT': '1010',
    'JUMP': '1011',
    'JUMPIF': '1100',
}

registers = {
    'R0': '0000',
    'R1': '0001',
    'R2': '0010',
    'R3': '0011',
    'R4': '0100',
    'R5': '0101',
    'R6': '0110',
    'R7': '0111',
    'R8': '1000',
    'R9': '1001',
    'R10': '1010',
    'R11': '1011',
    'R12': '1100',
    'R13': '1101',
    'R14': '1110',
    'R15': '1111',
}

ALU_OPS = {'ADD', 'SUB', 'XOR', 'XNOR', 'AND', 'NAND', 'OR', 'NOR'}

def encode_instruction(line, labels):
    tokens = tokenize(line)
    if not tokens:
        return None

    mnemonic = tokens[0].upper()
    if mnemonic not in instructions:
        raise ValueError(f'Unknown opcode: {mnemonic}')

    opcode = instructions[mnemonic]
    operands = tokens[1:]

    if mnemonic in ALU_OPS:
        if len(operands) != 3:
            raise ValueError(f'{mnemonic} requires 3 register operands')
        dest, src1, src2 = operands
        return opcode + registers[dest.upper()] + registers[src1.upper()] + registers[src2.upper()]

    if mnemonic == 'LOAD':
        if len(operands) != 2:
            raise ValueError('LOAD requires register and immediate')
        reg, imm_token = operands
        reg_code = registers[reg.upper()]
        imm_value = parse_immediate(imm_token)
        if imm_value < 0 or imm_value > 0xFF:
            raise ValueError(f'LOAD immediate out of range: {imm_token}')
        return opcode + reg_code + format(imm_value, '08b')

    if mnemonic == 'HALT':
        if operands:
            raise ValueError('HALT does not take operands')
        return opcode + '0' * 12

    if mnemonic in {'JUMP', 'JUMPIF'}:
        if len(operands) != 1:
            raise ValueError(f'{mnemonic} requires exactly one target operand')
        target = operands[0]
        address = labels[target] if target in labels else parse_immediate(target)
        if address < 0 or address > 0xFFF:
            raise ValueError(f'{mnemonic} address out of range: {target}')
        return opcode + format(address, '012b')

    raise ValueError(f'Unsupported mnemonic: {mnemonic}')