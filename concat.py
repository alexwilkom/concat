import sys
import os

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