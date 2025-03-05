import csv
"""
def return_emails():
    with open ('emails.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        the_list = []
        for row in reader:
            the_list.append(row)
            print(the_list)
    return the_list
"""


def simple_open(csv_path):
    file = open(csv_path, "r")
    output = []
    for line in file:
        output.append(line.strip().split(",")[0])
    file.close()
    return output

print(simple_open("emails.csv"))