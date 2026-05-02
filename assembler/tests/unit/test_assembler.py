from pathlib import Path
from assembler.src.assembler import assemble

def test_assemble_simple_program(tmp_path: Path):
    source = tmp_path / "simple.asm"
    source.write_text(
        "start:\n"
        "LOAD R1 42\n"
        "ADD R2 R1 R1\n"
        "HALT\n",
        encoding="utf-8"
    )

    result = assemble(str(source))

    assert result == [
        "1001000100101010",
        "0001001000010001",
        "1010000000000000",
    ]