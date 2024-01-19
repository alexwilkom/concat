import sys
import os
import argparse

def read(source_file):
    try:
        with open(source_file, 'r') as source:
            return source.read()
    except FileNotFoundError:
        print("File not found. Try checking the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def print_file(source):
    try:
        print(read(source))
    except FileNotFoundError:
        print("File not found. Try checking the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_file(source_file, destination_file):
    try:
        content = read(source_file)
        with open(destination_file, 'a') as destination:
            destination.write(content)
        print(f"\nContent from '{source_file}' appended to '{destination_file}' successfully.\n")
        print(read(destination_file))
    except FileNotFoundError:
        print("One or both of the files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def numbered_lines(input, option):
    if os.path.isfile(input):
        input = read(input)
    text_array = input.splitlines()
    if option == "-n":
        for i, line in enumerate(text_array, start=1):
            print(f"{i} {line}")
    if option == "-b":
        for i, line in enumerate(filter(None, text_array), start=1):
            print(f"{i} {line}")
            print()

def main():
    parser = argparse.ArgumentParser(description='Custom cat-like utility')
    parser.add_argument('files', nargs='*', help='Files to process')
    parser.add_argument('-n', '--number-lines', action='store_true', help='Number all output lines')
    parser.add_argument('-b', '--number-nonblank', action='store_true', help='Number non-empty output lines')

    args = parser.parse_args()
    
    # Check if any data is being piped into stdin
    if not sys.stdin.isatty():
        stdin_text = sys.stdin.read()
        option = '-n' if args.number_lines else '-b' if args.number_nonblank else None
        if option:
            numbered_lines(stdin_text, option)
        else:
            print(stdin_text, end='')
    else:
        if args.number_lines or args.number_nonblank:
            option = '-n' if args.number_lines else '-b'
            for file in args.files:
                numbered_lines(file, option)
        elif len(args.files) == 1:
            print(read(args.files[0]))
        elif len(args.files) == 2:
            append_file(args.files[0], args.files[1])
        else:
            parser.print_usage()
        
if __name__ == "__main__":
    main()