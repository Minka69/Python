import csv

file_path = "/home/minka69btw/Code/Python/spotify/spotify.csv"

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        print(row[0], "-", row[1], row[3], row[4], row[5])