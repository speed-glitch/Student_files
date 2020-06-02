import pandas as pd
import numpy as np
import re

#Read tempstud.txt file
with open('tempstud.txt') as f:
    data = f.read()

mytemp = re.findall(r"[\w']+", data)
r0=mytemp[0]
r1=mytemp[2]
r2=mytemp[4]
r3=mytemp[6]

#Read student.txt file for column name
f = open('student.txt', 'r')
line = f.readline()
f.close()

myline = re.findall(r"[\w']+", line)
l0=myline[0]
l1=myline[1]
l2=myline[2]
l3=myline[3]

#Read student.txt file in a pandas dataframe
df = pd.read_csv('student.txt', sep="\s*,\s*",header=None,engine='python',skiprows=[0])

#Name columns according to the order of data present in student.txt
df.columns = [l0,l1,l2,l3]

#Store names of columns based on template columns 
a0 = myline[myline.index(mytemp[1])]
a1 = myline[myline.index(mytemp[3])]
a2 = myline[myline.index(mytemp[5])]
a3 = myline[myline.index(mytemp[7])]

#split dataframe to multiple dataframes based on Ids
for i, g in df.groupby('Rollno'):
    #calculate total marks for each student
    Total = g['Marks'].sum()

    #get the name of student from data file
    k = g.iloc[0]['StudName']

    #start writing to a file
    with open("%s.%d.txt"%(k,i), 'a') as f:

        #iterate over multiple rows in dataframe to write in a file
        for index,row in g.iterrows():
            f.write("{%s: %s,%s:%s , %s: %s, %s:%s}\n"%(r0,row[a0],r1,row[a1],r2,row[a2],r3,row[a3]))

        #print total at the end    
        f.write("\t\t\t\t\tTotal:%s"%Total)
