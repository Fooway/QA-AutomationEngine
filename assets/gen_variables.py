""" Generates variables for HIS system testing based on random data (seeded) """
import argparse
import os
import random
import pyodbc

parser = argparse.ArgumentParser()
parser.add_argument('--count')
args = parser.parse_args()

count = int(args.count)

with open('variables.csv', 'w') as variables_file:
    variables_file.write('VariableCode,VariableName,VariableUnitsName,DataType,' +
                         'SampleMedium,ValueType,IsRegular,TimeSupport,' +
                         'TimeUnitsName,GeneralCategory,NoDataValue\n')

random.seed(4)


def get_cv(cv_table, col):
    driver = '{ODBC Driver 13 for SQL Server}'
    sql_server = os.environ['GENSERVER']
    db_name = os.environ['GENDB']
    user = os.environ['GENUSER']
    passwd = os.environ['GENPASSWD']
    cnxn = pyodbc.connect('DRIVER={};PORT={};'.format(driver, 1433) +
                          'SERVER={};PORT={};'.format(sql_server, 1443) +
                          'DATABASE={};UID={};PWD={};'.format(db_name, user, passwd))
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM {};'.format(cv_table))
    records = cursor.fetchall()
    cv_list = [record[col] for record in records]
    return cv_list


var_names = get_cv('VariableNameCV', 0)
units = get_cv('Units', 1)
data_types = get_cv('DataTypeCV', 0)
sample_mediums = get_cv('SampleMediumCV', 0)
value_types = get_cv('ValueTypeCV', 0)
is_regulars = ['TRUE', 'FALSE']
general_cats = get_cv('GeneralCategoryCV', 0)

for i in range(0, count):
    var_code = str(i+1)
    var_name = var_names[random.randint(0, len(var_names)-1)]
    var_units = units[random.randint(0, len(units)-1)]
    data_type = data_types[random.randint(0, len(data_types)-1)]
    sample_medium = sample_mediums[random.randint(0, len(sample_mediums)-1)]
    value_type = value_types[random.randint(0, len(value_types)-1)]
    is_regular = is_regulars[random.randint(0, len(is_regulars)-1)]
    time_support = '0'
    time_units = units[random.randint(0, len(units)-1)]
    general_cat = general_cats[random.randint(1, len(general_cats)-1)]
    no_data = '-9999'
    unquoted_row = [var_code, var_name, var_units, data_type, sample_medium,
                    value_type, is_regular, time_support, time_units,
                    general_cat, no_data]
    row = ['"{}"'.format(field) for field in unquoted_row]
    with open('variables.csv', 'a') as variables_file:
        variables_file.write(','.join(row) + '\n')
