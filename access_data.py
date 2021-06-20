#! /usr/bin/env python3.9
import csv
global S0_array, S1_array, S2_array, S3_array
S0_array=[]
S1_array=[]
S2_array=[]
S3_array=[]
S1_mag=[]
S2_mag=[]
S3_mag=[]
S4_mag=[]
start_row=[]
start_column=[]

def read_csv():
    with open('sensor_values.csv', 'r') as file:
        reader = csv.reader(file)
        for i in range(3):
            next(reader)
        S0_array.clear()
        S1_array.clear()
        S2_array.clear()
        S3_array.clear()
        S1_mag.clear()
        S2_mag.clear()
        S3_mag.clear()
        S4_mag.clear()
        start_row.clear()
        start_column.clear()
        for row in reader:
            if row[8] == '':
                continue
            elif row[8] == '-':
                break
            else:
                start_row.append(row[2])
                start_column.append(row[3])
                S0_array.append(row[13])
                S1_array.append(row[20])
                S2_array.append(row[27])
                S3_array.append(row[34])
                S1_mag.append(row[12])
                S2_mag.append(row[18])
                S3_mag.append(row[24])
                S4_mag.append(row[30])

#for i in range(len(S0_array)):
#    print(S0_array[i],S1_array[i],S2_array[i],S3_array[i])