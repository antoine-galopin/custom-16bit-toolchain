import pytest
from assembler.src.parser import normalize_line, tokenize, parse_immediate

def test_normalize_line_removes_comment():
    assert normalize_line("ADD R1 R2 R3 ; comment") == "ADD R1 R2 R3"

def test_normalize_line_trims_whitespace():
    assert normalize_line("   LOAD R1 42   ") == "LOAD R1 42"

def test_tokenize_instruction():
    assert tokenize("ADD R3 R1 R2") == ["ADD", "R3", "R1", "R2"]

def test_tokenize_rejects_commas():
    with pytest.raises(ValueError, match="Commas are not allowed"):
        tokenize("ADD R3, R1, R2")

def test_parse_decimal_immediate():
    assert parse_immediate("42") == 42

def test_parse_hex_immediate():
    assert parse_immediate("0x2A") == 42

def test_parse_binary_immediate():
    assert parse_immediate("0b101010") == 42