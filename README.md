# Concat

## Description

This Python utility mimics functionalities of the Unix `cat` command with additional features like displaying file contents, appending files, and numbering lines. It's designed for command line use in Unix-like environments.

## Features

- **Display File Contents**: Show the contents of a file, similar to the Unix `cat` command.
- **Append Files**: Append the contents of one file to another.
- **Number Lines**: Add line numbers to the file output, with options for numbering all lines or only non-empty lines.
- **Standard Input Handling**: Capable of processing data piped from standard input.

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/alexwilkom/concat.git
    cd concat
    ```

2. **Important**: Ensure that the script has a shebang line at the top to specify the Python interpreter. This might be `#!/usr/bin/env python3` or `#!/usr/bin/env python`, depending on your system setup and Python version.

3. **Ensure the script is executable**:

    ```bash
    chmod +x concat.py
    ```

4. **Create a symbolic link** in a directory that's in your system's PATH. This allows you to run the script from any location without moving it from the repository:

    - First, find the full path of your script. In the terminal, navigate to the repository where the file is and run:
      
      ```bash
      pwd
      ```

    - Then, create a symlink in `/usr/local/bin` (or any other directory in your PATH):

      ```bash
      sudo ln -s /full/path/to/concat.py /usr/local/bin/concat
      ```

      Replace `/full/path/to/concat.py` with the actual path obtained from the previous command (`pwd`).

      In `/usr/local/bin/concat` you can replace `concat` with the desired name for the symlink. This will be the name you use to call the script from the command line.

5. **Run the script** from anywhere in your system by simply typing:

    ```bash
    concat
    ```

    You don't need to navigate to the script's directory or specify the `.py` extension.


### Usage

Run the script using the following commands:

    ```bash
    # Display file contents
    concat file.txt

    # Append file1.txt to file2.txt
    concat file1.txt file2.txt

    # Number all lines
    concat -n file.txt

    # Number non-empty lines
    concat -b file.txt

    # Piping
    head -n5 file.txt | concat -n
    ```
