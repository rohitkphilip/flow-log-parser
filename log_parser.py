import io
import csv
from collections import defaultdict
from typing import Dict, Tuple
import sys



class LogParser:
    LOOKUP_TABLE_FILE = 'lookup-table.csv'
    PROTOCOL_NUMS_FILE = 'protocol-numbers.csv'

    def __init__(self):
        self._protocol_mapping:     Dict[ str, str ]             = {}
        self._lookup_table:         Dict[ Tuple[str, str], str ] = {}
        self._tag_count =           defaultdict(int)
        self._combination_count =   defaultdict(int)

        self._load_lookup_table()
        self._create_protocol_map()

    def _load_lookup_table(self) -> None:
        try:
            with io.open(self.LOOKUP_TABLE_FILE, mode='r', buffering=1) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    key = ( row['dstport'].strip(), row['protocol'].strip() )
                    self._lookup_table[key] = row['tag'].strip()

                print("Lookup table - ", self._lookup_table)
        except FileNotFoundError:
            print(f"FILE {self.LOOKUP_TABLE_FILE} NOT FOUND")
            sys.exit(1)
        except Exception as e:
            print(f"ERROR READING {self.LOOKUP_TABLE_FILE} : {e}")
            sys.exit(1)


    def _create_protocol_map(self) -> None:
        try:
            with io.open(self.PROTOCOL_NUMS_FILE, mode='r', buffering=1) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    decimal_value = row['Decimal']
                    keyword = row['Keyword'].lower()
                    self._protocol_mapping[decimal_value] = keyword
    
        except FileNotFoundError:
            print(f"FILE {self.PROTOCOL_NUMS_FILE} NOT FOUND")
            sys.exit(1)
        except Exception as e:
            print(f"ERROR READING {self.PROTOCOL_NUMS_FILE} : {e}")
            sys.exit(1)
            

    def parse_log_file(self, log_file: str) -> None:
        try:
            with io.open(log_file, mode='r', buffering=1) as file:
                for line in file:
                    if not line.strip():
                        continue
                    
                    parts = line.strip().split()                    
                    if len(parts) < 8:
                        print(f"Invalid log line format: {line.strip()}")
                        continue

                    dstport = parts[6]
                    protocol_num = parts[7]
                    protocol = self._protocol_mapping.get(protocol_num, 'unknown')
                    key = ( dstport, protocol )
                    tag = self._lookup_table.get(key, 'Untagged')
                    self._combination_count[key] += 1
                    self._tag_count[tag] += 1
        
        except FileNotFoundError:
            print(f"FILE {log_file} NOT FOUND")
            sys.exit(1)        
        except KeyError as e:
            print(f"Key error encountered: {e}")
        except Exception as e:
            print(f"ERROR PROCESSING log file {log_file} : {e}")
            sys.exit(1)

        
    def print_counts(self) -> None:
        print("\nTag Counts:")
        for tag, count in self._tag_count.items():
            print( f"{tag},{count}")

        print("\n\nPort/Protocol Combination Counts:")
        for key, count in self._combination_count.items():
            print( f"{key[0]},{key[1]},{count}")


    def export_counts(self, file_name) -> None:
        with io.open(file_name, mode='w') as file:
            file.write("Tag Counts:\n")
            file.write("Tag,Count\n")
            for tag, count in self._tag_count.items():
                file.write(f"{tag},{count}\n")

            file.write("\n\nPort/Protocol Combination Counts:\n")
            file.write("Port,Protocol,Count\n")
            for key, count in self._combination_count.items():
                file.write(f"{key[0]},{key[1]},{count}\n")