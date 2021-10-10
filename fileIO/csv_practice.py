import csv

# csv.reader(f)
# with open("example.csv") as f:
#     # print(f.read())
#     reader = csv.reader(f)
#     for line in reader:
#         print(line[2])


# csv.DictReader(f)
# with open("example.csv") as f:
#     reader = csv.DictReader(f)
#     for line in reader:
#         # print(line)
#         print(line["Country"])  # DictReader を使うと1行目をヘッダー(Key)、2行目以降をvalueに取ることができる


# csv.writer(f)
# with open("sample.csv", mode='w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['value1', 'value2'])
#     writer.writerow(['value3', 'value4'])

# csv.DictWriter(f)
with open("sample.csv", mode='w', newline="") as f:  # windowsでは、newline="" を指定することで改行が入らなくなる
    writer = csv.DictWriter(f, ['col1', 'col2'])
    # writer.writeheader()
    writer.writerow({'col1': 'value1', 'col2': 'value2'})
    writer.writerow({'col1': 'value3', 'col2': 'value4'})
    writer.writerow({'col1': 'value5', 'col2': 'value6'})