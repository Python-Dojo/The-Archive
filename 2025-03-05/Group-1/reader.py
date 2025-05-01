import csv

def return_emails():
    with open ('emails.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        print(type(reader))
        emails = []
        for row in reader:
            # print(type(row))
            # print(len(row))
            emails.append(row[0])
        # print(emails)
    return emails


if __name__ == "__main__":
    emails = return_emails()
    import typing
    assert isinstance(emails, typing.Iterable)
    assert isinstance(next(iter(emails)), str)
