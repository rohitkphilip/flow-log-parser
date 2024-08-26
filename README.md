# Flow Log Parser

## Overview

Python script that parses log files and maps each row to a tag based on a lookup table

## Assumptions

- Supported Log Format: **default** only
- Supported Version: **2** only
  
- Input file as well as the file containing tag mappings are **plain text (ascii)files**
- The flow log file size can be up to **10 MB**
- The lookup file can have up to **10000 mappings**
- The tags can map to more than one port, protocol combinations.  
- The matches should be **case insensitive**

## Requirements

- Python 3.x

## File Structure

- `main.py`: The main script to run the parser.
- `log_parser.py`: Python file containing the LogParser class.
- `utils.py`: Python file containing utility functions to load the lookup table and protocol numbers.
- `resources/lookup-table.csv`: CSV file containing the lookup table.
- `resources/protocol-numbers.csv`: CSV file containing protocol numbers and corresponding names.
- `log.txt`: Sample log file to be parsed.
- `output.txt`: Generated Output file containing tag counts.

## Usage

To run the script, use the following command:
    
    python3 main.py -i <input-file> -o <output-file>

- -i or --input: Path to the input log file (required)
- -o or --output: Path to the output file (optional, defaults to `output.txt`)

## Example

    python3 main.py -i log.txt -o output.txt