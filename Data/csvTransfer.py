#transfer to csv

import csv

def txt_to_csv(txt_file_path, csv_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file, \
         open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(txt_file, delimiter='\t')
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["User", "Bot"])  # Optional: add header row
        for row in reader:
            writer.writerow(row)

txt_file_path = 'merged_file.txt'  # TXT文件路径
csv_file_path = 'train_data.csv'  # CSV输出文件路径

txt_to_csv(txt_file_path, csv_file_path)
print("TXT file has been converted to CSV.")
