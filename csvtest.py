# Import csv module
import csv

#Rows of information
info = [
    {
        'Nombre' : 'Eustakio',
        'Apellido' : 'Maldonado',
        'Edad' : 7,
        'Sexo' : 'Masculino'
    },
    {
        'Nombre' : 'Florinda',
        'Apellido' : 'Mesa',
        'Edad' : 4,
        'Sexo' : 'Femenino'
    },
    {
        'Nombre' : 'Petunia',
        'Apellido' : 'Perindingo',
        'Edad' : 50,
        'Sexo' : 'Femenino'
    },
    {
        'Nombre' : 'Marta',
        'Apellido' : 'Jaramillo',
        'Edad' : 46,
        'Sexo' : 'Femenino'
    },
    {
        'Nombre' : 'Pablo',
        'Apellido' : 'Escobar',
        'Edad' : 70,
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
