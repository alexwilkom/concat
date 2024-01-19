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
        print(f"Content from '{source_file}' appended to '{destination_file}' successfully.\n")
    except FileNotFoundError:
        print("One or both of the files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")