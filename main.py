from utils import load_lookup_table, load_protocol_map
from log_parser import LogParser
import logging
import argparse

def parse_args():
    arg_parser = argparse.ArgumentParser(
                    prog='Flow Log Record Parser',
                    description='Maps each row in the log to a tag based on a lookup table',
                    epilog='')
    
    arg_parser.add_argument('-i', '--input', required=True)         #input_file
    arg_parser.add_argument('-o', '--output', default="output.txt") #output_file

    return arg_parser.parse_args()

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    args = parse_args()

    lookup_table = load_lookup_table("resources/lookup-table.csv")
    logger.info(f"Successfully loaded lookup table")
    protocol_map = load_protocol_map("resources/protocol-numbers.csv")
    logger.info(f"Successfully loaded protocol map")
    
    flow_log_parser = LogParser(lookup_table, protocol_map)

    flow_log_parser.parse_log_file(args.input)
    flow_log_parser.export_counts(args.output)

if __name__ == "__main__":
    main()