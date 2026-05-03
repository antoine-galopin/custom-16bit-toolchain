"""Integration tests for assembler and emulator."""
import tempfile
import os

from assembler.src.assembler import assemble
from emulator.src.emulator import Emulator


def test_multiply_example():
    """Test assembling and emulating the multiply example."""
    # Assemble the multiply.asm example
    asm_path = 'examples/asm/multiply.asm'
    binary = assemble(asm_path)

    # Verify we got 9 instructions (as per the expected output)
    assert len(binary) == 9, f'Expected 9 instructions, got {len(binary)}'

    # Emulate the program
    emulator = Emulator()
    emulator.load_program(binary)
    emulator.run()

    # Verify results
    # R1 should be 4 (multiplicand)
    assert emulator.registers[1] == 4, f'Expected R1=4, got {emulator.registers[1]}'

    # R2 should be 0 (multiplier decremented to 0)
    assert emulator.registers[2] == 0, f'Expected R2=0, got {emulator.registers[2]}'

    # R3 should be 20 (4 * 5)
    assert emulator.registers[3] == 20, f'Expected R3=20, got {emulator.registers[3]}'

    # R4 should be 1 (constant 1)
    assert emulator.registers[4] == 1, f'Expected R4=1, got {emulator.registers[4]}'

    # Zero flag should be 1 (last operation was SUB R2 R2 R4 resulting in 0)
    assert emulator.zero_flag == 1, f'Expected zero_flag=1, got {emulator.zero_flag}'

    # Instruction count should be 24
    assert emulator.instruction_count == 24, f'Expected 24 instructions, got {emulator.instruction_count}'

    # Emulator should be halted
    assert emulator.halted is True, f'Expected halted=True, got {emulator.halted}'
