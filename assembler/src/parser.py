import re

LABEL_PATTERN = re.compile(r'^[A-Za-z_][A-Za-z0-9_]{0,31}$')

def normalize_line(line):
    return line.split(';', 1)[0].strip()

def tokenize(line):
    parts = re.split(r'[\s,]+', line.strip())
    return [part for part in parts if part]

def parse_immediate(value):
    if value.startswith(('0x', '0X')):
        return int(value, 16)
    if value.startswith(('0b', '0B')):
        return int(value, 2)
    return int(value, 10)