from utils import load_lookup_table, load_protocol_map
from log_parser import LogParser


lookup_table = load_lookup_table("resources/lookup-table.csv")
protocol_map = load_protocol_map("resources/protocol-numbers.csv")

# print("main - lookup_table -", lookup_table)
# print("main - protocol_map -", protocol_map)
flow_log_parser = LogParser(lookup_table, protocol_map)

flow_log_parser.parse_log_file("log.txt")
flow_log_parser.export_counts("output.txt")