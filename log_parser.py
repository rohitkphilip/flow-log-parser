import io
from collections import defaultdict
import sys

class LogParser:    
    def __init__(self, lookup_table, protocol_mapping):
        self._protocol_mapping = protocol_mapping
        self._lookup_table = lookup_table
        self._tag_count = defaultdict(int)
        self._combination_count = defaultdict(int)
        
    def parse_log_file(self, log_file: str) -> None:
        try:
            with io.open(log_file, mode='r', buffering=1) as file:
                for line in file:
                    self._process_line(line)
        
        except FileNotFoundError:
            print(f"FILE {log_file} NOT FOUND")
            sys.exit(1)                
        except Exception as e:
            print(f"ERROR PROCESSING log file {log_file} : {e}")
            sys.exit(1)

    def _process_line(self, line: str) -> None:
        try:
            if not line.strip():
                return
            
            parts = line.strip().split()                    
            if len(parts) < 8:
                print(f"Invalid log line format: {line.strip()}")
                return
                        
            key = self._create_key(parts)
            tag = self._lookup_table.get(key, 'Untagged')
            self._combination_count[key] += 1
            self._tag_count[tag] += 1
                
        except Exception as e:
            print(f"ERROR PROCESSING log line {line} : {e}")
            sys.exit(1)

    def _create_key(self, parts: list) -> tuple:    
        dst_port = parts[6]
        protocol_num = parts[7]
        protocol = self._protocol_mapping.get(protocol_num, 'unknown')                    
        return dst_port, protocol

        
    def print_counts(self) -> None:
        print("\nTag Counts:")
        for tag, count in self._tag_count.items():
            print( f"{tag},{count}")

        print("\n\nPort/Protocol Combination Counts:")
        for key, count in self._combination_count.items():
            print( f"{key[0]},{key[1]},{count}")


    def export_counts(self, file_name: str) -> None:
        try:
            with io.open(file_name, mode='w') as file:
                file.write("Tag Counts:\n")
                file.write("Tag,Count\n")
                for tag, count in self._tag_count.items():
                    file.write(f"{tag},{count}\n")

                file.write("\n\nPort/Protocol Combination Counts:\n")
                file.write("Port,Protocol,Count\n")
                for key, count in self._combination_count.items():
                    file.write(f"{key[0]},{key[1]},{count}\n")
        except IOError as e:
            print(f"Error writing to file {file_name}: {e}")
            sys.exit(1)
