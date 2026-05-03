import sys

from .assembler import assemble

def main():
    if len(sys.argv) != 3:
        print('Usage: python cli.py <input.asm> <output.txt>')
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        binary_instructions = assemble(input_path)
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for binary in binary_instructions:
                output_file.write(binary + '\n')
        print(f'Assembled {len(binary_instructions)} instructions to {output_path}')
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()