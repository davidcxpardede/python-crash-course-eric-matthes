from pathlib import Path
import csv

path = Path('16_downloading_data/weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(f"{index}. {column_header}")