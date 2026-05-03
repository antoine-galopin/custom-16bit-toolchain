import sys

from emulator.src.emulator import Emulator


def main():
    if len(sys.argv) != 3:
        print('Usage: python cli.py <input_binary.txt> <output_trace.txt>')
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, 'r', encoding='utf-8') as f:
        instructions = [line.strip() for line in f if line.strip()]

    emulator = Emulator()
    try:
        emulator.load_program(instructions)
        emulator.run()
    except Exception as error:
        print(f'Error: {error}')
        sys.exit(1)

    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(f'Execution finished after {emulator.instruction_count} instructions\n')
        out.write(f'Registers: {emulator.registers}\n')
        out.write(f'Zero flag: {emulator.zero_flag}\n')


if __name__ == '__main__':
    main()
