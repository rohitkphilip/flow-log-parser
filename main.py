from utils import load_lookup_table, load_protocol_map
from log_parser import LogParser
import logging

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    lookup_table = load_lookup_table("resources/lookup-table.csv")
    logger.info(f"Successfully loaded lookup table")
    protocol_map = load_protocol_map("resources/protocol-numbers.csv")
    logger.info(f"Successfully loaded protocol map")

    # print("main - lookup_table -", lookup_table)
    # print("main - protocol_map -", protocol_map)
    flow_log_parser = LogParser(lookup_table, protocol_map)

    flow_log_parser.parse_log_file("log.txt")
    flow_log_parser.export_counts("output.txt")

if __name__ == "__main__":
    main()