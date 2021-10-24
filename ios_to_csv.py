# Defines a function that writes textfsm ntc template Cisco IOS output to CSV file.
import csv
def ios_to_csv(ios_output):
    # Automatically create column header out of the Rows "keys" or command output from textfsm.
    header = []
    column_list = list(ios_output[0].keys())
    for column in column_list:
        header.append(column)

    # Write to CSV File.  Header and Rows.
    with open('csvtest.csv', 'a', encoding = 'UTF8', newline='') as file:
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(ios_output)

