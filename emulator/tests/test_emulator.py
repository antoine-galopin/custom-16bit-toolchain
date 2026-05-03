import pytest

from ..src.emulator import Emulator, EmulatorError


def test_emulator_load_and_run_add():
    program = [
        '1001000100000000',  # LOAD R1 0
        '0001001000010000',  # ADD R2 R1 R0
        '1010000000000000',  # HALT
    ]

    emulator = Emulator()
    emulator.load_program(program)
    emulator.run()

    assert emulator.registers[1] == 0
    assert emulator.registers[2] == 0
    assert emulator.halted is True
    assert emulator.instruction_count == 3


def test_emulator_zero_flag_and_jumpif():
    program = [
        '1001000100000000',  # LOAD R1 0
        '0010001000010001',  # SUB R2 R1 R1
        '1100000000000100',  # JUMPIF 4
        '1001001100000001',  # LOAD R3 1 (skipped when branch taken)
        '1010000000000000',  # HALT
    ]

    emulator = Emulator()
    emulator.load_program(program)
    emulator.run()

    assert emulator.registers[2] == 0
    assert emulator.zero_flag == 1
    assert emulator.pc == 4
    assert emulator.instruction_count == 4


def test_emulator_invalid_instruction_raises():
    program = [
        '0000000000000000',  # invalid opcode 0
    ]

    emulator = Emulator()
    emulator.load_program(program)

    with pytest.raises(EmulatorError, match='Invalid opcode'):
        emulator.run()


def test_emulator_invalid_binary_line_raises():
    emulator = Emulator()

    with pytest.raises(EmulatorError, match='Invalid binary instruction'):
        emulator.load_program(['010101'])
