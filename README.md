# Flow Log Parser

## Overview

Python script that parses log files and maps each row to a tag based on a lookup table

## Requirements

- Python 3.x

## File Structure

- `main.py`: The main script to run the parser.
- `resources/lookup-table.csv`: CSV file containing the lookup table.
- `resources/protocol-numbers.csv`: CSV file containing protocol numbers and corresponding names.
- `log.txt`: Sample log file to be parsed.
- `output.txt`: Generated Output file containing tag counts.

## Usage

To run the script, use the following command:

    ```bash
    python3 main.py -i <input-file> -o <output-file>

    * `-i` or `--input`: Path to the input log file (required)
    * `-o` or `--output`: Path to the output file (optional, defaults to `output.txt`)

## Example

    ```bash
    python3 main.py -i log.txt -o output.txt