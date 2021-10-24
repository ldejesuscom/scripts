# Import csv module
import csv

#Rows of information
info = [
    {
        'Nombre' : 'Sebastian',
        'Apellido' : 'De Jesus',
        'Edad' : 5,
        'Sexo' : 'Masculino'
    },
    {
        'Nombre' : 'Amaia',
        'Apellido' : 'De Jesus',
        'Edad' : 2,
        'Sexo' : 'Femenino'
    },
    {
        'Nombre' : 'Aida',
        'Apellido' : 'Izquierdo',
        'Edad' : 50,
        'Sexo' : 'Femenino'
    },
    {
        'Nombre' : 'Victor',
        'Apellido' : 'Paz',
        'Edad' : 53,
        'Sexo' : 'Masculino'
    },
]
# Automatically create column header out of the Rows "keys" or command output from textfsm.
header = []
column_list = list(info[0].keys())
for column in column_list:
    header.append(column)

# Write to CSV File.  Header and Rows.
with open('csvtest.csv', 'a', encoding = 'UTF8', newline='') as file:
    writer = csv.DictWriter(file, header)
    writer.writeheader()
    writer.writerows(info)
