from assembler.src.parser import LABEL_PATTERN

def build_label_table(lines):
    labels = {}
    address = 0

    for line in lines:
        if line.endswith(':'):
            label = line[:-1]
            if not LABEL_PATTERN.match(label):
                raise ValueError(f'Invalid label: {label}')
            if label in labels:
                raise ValueError(f'Duplicate label: {label}')
            labels[label] = address
        else:
            address += 1

    return labels