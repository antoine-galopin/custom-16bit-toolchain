import pytest
from assembler.src.symbol_table import build_label_table

def test_build_label_table_simple():
    lines = [
        "start:",
        "LOAD R1 42",
        "loop:",
        "ADD R2 R2 R1",
        "JUMP loop",
    ]
    labels = build_label_table(lines)
    assert labels == {"start": 0, "loop": 1}

def test_duplicate_label_raises():
    lines = [
        "start:",
        "LOAD R1 42",
        "start:",
        "HALT",
    ]
    with pytest.raises(ValueError, match="Duplicate label"):
        build_label_table(lines)

def test_invalid_label_raises():
    lines = [
        "123bad:",
        "HALT",
    ]
    with pytest.raises(ValueError, match="Invalid label"):
        build_label_table(lines)