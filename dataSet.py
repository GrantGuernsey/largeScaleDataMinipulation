import csv
import matplotlib.pyplot as plt 
import pandas
import numpy as np
from functools import reduce

#average function for averaging their monthly spendings
def Average(lst): 
    return reduce(lambda a, b: a + b, lst) / len(lst) 


number = []
ageRange = []
marital = []
income = []
homeOwner = []
houseHold = []
houseHoldSize = []
date = []
dateRow = []
transaction = []
transactionRow = []
sumAccounts = []


#this is opening and running through the CSV file of the banking data 
#using the , as the delimeter because it is a csv
#This loop saves all of the data into their own arrays for easier acess in the code
#and allows me to close the csv file sooner so I can open another
with open('Demographics Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:

        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(f'\t{row[0]} is their ID, {row[1]} is their age range, their marital status is {row[2]}.')
            line_count += 1
            
            number.append(row[0])
            ageRange.append(row[1])
            marital.append(row[2])
            income.append(row[3])
            homeOwner.append(row[4])
            houseHold.append(row[5])
            houseHoldSize.append(row[6])
    print(f'Processed {line_count} lines.')
    
range = (0,100000)
ident = 1
summ = 0
#This is opening and running another CSV file that has spending data in this
#For this I just wanted to find the average of each of the users spending data
with open('Card Transactions by Household.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(f'\t{row[0]} is their ID, {row[1]} is their age range, their marital status is {row[2]}.')
            line_count += 1
            if(ident != int(row[0])):
                print("The account number is {0} and the sum total of their purchases is {1:.2f}".format(ident,summ))
                sumAccounts.append(summ)
                summ = 0
                date.append(dateRow)
                transaction.append(transactionRow)
                ident = int(row[0])
                dateRow = []
                transactionRow = []
                dateRow.append(row[1])
                transactionRow.append(float(row[2]))
            else:
                dateRow.append(row[1])
                transaction.append(float(row[2]))
                summ += float(row[2])
                #print("The account number is {0} and the total is: ".format(row[1]))
                #print(float(row[2]))
    print(f'Processed {line_count} lines.')

#I didnt get to this part was I was planning on using numpy as a way to save
#more of the arrays and to create a linked list type structure to store all
#the types of data for each individual user, which would allow me to
#create accurate graphing as well as plot their spending locations which would
#enable me to find probable fraud by observing the zipcodes and creating a frequency plot
dateToID = np.array(date, dtype="object")
transactionToID = np.array(transaction, dtype="object")
print(Average(sumAccounts))


