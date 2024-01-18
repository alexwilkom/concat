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