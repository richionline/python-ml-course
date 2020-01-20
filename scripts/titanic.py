import pandas as pd
import os


# Example 1. Get a csv file
print('**************** EXAMPLE 1 ****************')
mainpath = '../datasets'
filename = 'titanic/titanic3.csv'
fullpath = os.path.join(mainpath, filename)

# Función read_csv de libreria pandas
# Parametros:
# sep: separador por defecto es la coma
# dtype: Para indicar los tipos, pej: dtype={"col1": numpy.float64, "col2":numpy.int32}
# head: Por defecto 0 que es la primera linea, indicar cual es la cabecera
# names: Para indicar los nombres de las columnas
# skiprows: None por defecto o entero para saltarse un determinado numero de filas
# index_col: None por defecto o secuencia de enteros
# skip_blank_lines: Saltar las líneas en blanco, por defecto es True
# na_filter: Boolean, si es True detecta marcadores que faltan y descarta esas filas, cuidado puede descartar todo
data = pd.read_csv(fullpath)

print('Procesando fichero:', fullpath)
print('Data1 example: \n', data.head())


# Example 2_1. Get a txt file
print('**************** EXAMPLE 2_1 ****************')
filename = 'customer-churn-model/Customer Churn Model.txt'
fullpath = os.path.join(mainpath, filename)
data2 = pd.read_csv(fullpath)
print('Data2_1 example: \n', data2.head())
# Show the columns names
print('Columns names: \n', data2.columns.values)


# Ejemplo 2_2. Get a columns name file and set this columns in other dataset
print('**************** EXAMPLE 2_2 ****************')
filename = 'customer-churn-model/Customer Churn Columns.csv'
fullpath = os.path.join(mainpath, filename)
datacols = pd.read_csv(fullpath)
datacolsList = datacols['Column_Names'].tolist()

filename = 'customer-churn-model/Customer Churn Model.txt'
fullpath = os.path.join(mainpath, filename)
data2 = pd.read_csv(fullpath, header=None, skiprows=1, names=datacolsList)
print('Data2_2 example: \n', data2.head())


# Example 3. Get a file with open function
print('**************** EXAMPLE 3 ****************')
data3 = open(fullpath, "r")  # Primary function to open files for reading in python, the parameter "r" is read only mode
# The next step is to read every line with readline
# strip() clean blank characters at the end and begining
# split(",") look for the "," char in the line and get every stream of characters between ","
cols = data3.readline().strip().split(",")
n_cols = len(cols)

# Read all the lines of the data3 object and save in a dictionary object
counter = 0
main_dict = {}
# Creating the dictionary keys, they are the column names
for col in cols:
    main_dict[col] = []
for line in data3:
    values = line.strip().split(",")
    for i in range(len(cols)):
        main_dict[cols[i]].append(values[i])
    counter += 1
print('The data3 example has %d columns and %d lines' % (n_cols, counter))

# Now we get the dataframe
df3 = pd.DataFrame(main_dict)
print('Dataframe created: \n', df3.head())
