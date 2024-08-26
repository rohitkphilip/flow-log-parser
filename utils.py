import io
import csv
from typing import Dict, Tuple
import sys

def load_lookup_table(lookup_table_file: str) -> Dict[Tuple[str, str], str]:
    try:
        lookup_table={}
        with io.open(lookup_table_file, mode='r', buffering=1) as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = ( row['dstport'].strip(), row['protocol'].strip() )
                lookup_table[key] = row['tag'].strip()
        return lookup_table
            
    except FileNotFoundError:
        print(f"FILE {lookup_table_file} NOT FOUND")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR READING {lookup_table_file} : {e}")
        sys.exit(1)


def load_protocol_map(protocol_nums_file: str) -> Dict[str, str]:
    try:
        protocol_mapping = {}
        with io.open(protocol_nums_file, mode='r', buffering=1) as file:
            reader = csv.DictReader(file)
            for row in reader:
                decimal_value = row['Decimal']
                keyword = row['Keyword'].lower()
                protocol_mapping[decimal_value] = keyword
        return protocol_mapping
    
    except FileNotFoundError:
        print(f"FILE {protocol_nums_file} NOT FOUND")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR READING {protocol_nums_file} : {e}")
        sys.exit(1)
