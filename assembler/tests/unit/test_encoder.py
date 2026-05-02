import pytest
from assembler.src.encoder import encode_instruction

def test_encode_add():
    labels = {}
    binary = encode_instruction("ADD R3 R1 R2", labels)
    assert binary == "0001001100010010"

def test_encode_load():
    labels = {}
    binary = encode_instruction("LOAD R1 42", labels)
    assert binary == "1001000100101010"

def test_encode_halt():
    labels = {}
    binary = encode_instruction("HALT", labels)
    assert binary == "1010000000000000"

def test_encode_jump_numeric():
    labels = {}
    binary = encode_instruction("JUMP 12", labels)
    assert binary == "1011000000001100"

def test_encode_jump_label():
    labels = {"loop": 7}
    binary = encode_instruction("JUMP loop", labels)
    assert binary == "1011000000000111"

def test_invalid_opcode_raises():
    with pytest.raises(ValueError, match="Unknown opcode"):
        encode_instruction("FOO R1 R2", {})

def test_load_out_of_range_raises():
    with pytest.raises(ValueError, match="LOAD immediate out of range"):
        encode_instruction("LOAD R1 999", {})

def test_jump_out_of_range_raises():
    with pytest.raises(ValueError, match="address out of range"):
        encode_instruction("JUMP 5000", {})