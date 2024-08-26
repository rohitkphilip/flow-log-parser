from log_parser import LogParser



flow_log_parser = LogParser()

flow_log_parser.parse_log_file("log.txt")
flow_log_parser.export_counts("output.txt")