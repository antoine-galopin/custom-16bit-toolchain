import os

from assembler.src.parser import normalize_line
from assembler.src.symbol_table import build_label_table
from assembler.src.encoder import encode_instruction

def assemble(source_path):
    if not os.path.isfile(source_path):
        raise FileNotFoundError(source_path)

    useful_lines = []
    with open(source_path, 'r', encoding='utf-8') as file:
        for raw_line in file:
            line = normalize_line(raw_line)
            if not line:
                continue
            useful_lines.append(line)

    labels = build_label_table(useful_lines)

    binary_lines = []
    for line in useful_lines:
        if line.endswith(':'):
            continue
        binary_lines.append(encode_instruction(line, labels))

    return binary_lines