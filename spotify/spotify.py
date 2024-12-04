import csv

file_path = "/home/minka69btw/Code/Python/spotify/spotify.csv"

file = open(file_path, mode='r', newline='', encoding='utf-8')

csv_reader = csv.reader(file)

for row in csv_reader:
    print(row)

file.close()