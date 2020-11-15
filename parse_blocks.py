import csv
import argparse

## Constants
BLOCK_ID = 'ID'
NEIGHBORHOOD_ID = 'Neighborho'

## argument handling
parser = argparse.ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()

result = []
seen = set()

with open(args.path, newline='') as f:
    csv_reader = csv.DictReader(f, dialect='excel')
    for row in csv_reader:
        if row[BLOCK_ID] not in seen:
            result.append((str(int(float(row[BLOCK_ID]))), int(row[NEIGHBORHOOD_ID])))
            seen.add(row[BLOCK_ID])

print(result, len(result))
