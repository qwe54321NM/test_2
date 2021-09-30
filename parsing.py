import numpy
from pprint import pprint
f = open('inputF.txt', 'r', encoding='utf-8')

data = f.readlines()
data[len(data)-1] = data[len(data)-1] + '\r'
sorted_name = list()
sorted_inhour = []
sorted_hours = []
sorted_allsum = []
sorted_dopinf = []
for i in range(0, len(data)):
    str1 = data[i].split(' ')
    if i == 0:
        sorted_name.append(str1[0])
        sorted_inhour.append(int(str1[1]))
        sorted_hours.append(int(str1[2]))
        sorted_allsum.append(int(str1[1]) * int(str1[2]))
        sorted_dopinf.append(str1[3])
    else:
        if sorted_name.count(str1[0]) == 0:
            sorted_name.append(str1[0])
            sorted_inhour.append(int(str1[1]))
            sorted_hours.append(int(str1[2]))
            sorted_allsum.append(int(str1[1]) * int(str1[2]))
            sorted_dopinf.append(str1[3])
        else:
            ind = sorted_name.index(str1[0])
            sorted_inhour[ind] = sorted_inhour[ind] + int(str1[1])
            sorted_hours[ind] = sorted_hours[ind] + int(str1[2])
            sorted_allsum[ind] = sorted_allsum[ind] + int(str1[1]) * int(str1[2])
            sorted_dopinf[ind] = str1[3]

print(sorted_name)
print(sorted_inhour)
print(sorted_hours)
print(sorted_allsum)
print(sorted_dopinf)

q1 = sorted(sorted_name)
q2 = sorted(sorted_inhour)
q3 = sorted(sorted_hours)
q4 = sorted(sorted_allsum)
q5 = sorted(sorted_dopinf)

print(q1)
print(q2)
print(q3)
print(q4)
print(q5)

a = []
a.append(sorted_name[0] + ' ' + str(sorted_hours[0]) + ' ' + str(sorted_inhour[0]) + ' ' + str(sorted_allsum[0]) + ' ' + sorted_dopinf[0])
a.append(sorted_name[1] + ' ' + str(sorted_hours[1]) + ' ' + str(sorted_inhour[1]) + ' ' + str(sorted_allsum[1]) + ' ' + sorted_dopinf[1])
a.append(sorted_name[2] + ' ' + str(sorted_hours[2]) + ' ' + str(sorted_inhour[2]) + ' ' + str(sorted_allsum[2]) + ' ' + sorted_dopinf[2])
a.append(sorted_name[3] + ' ' + str(sorted_hours[3]) + ' ' + str(sorted_inhour[3]) + ' ' + str(sorted_allsum[3]) + ' ' + sorted_dopinf[3])
a.append(sorted_name[4] + ' ' + str(sorted_hours[4]) + ' ' + str(sorted_inhour[4]) + ' ' + str(sorted_allsum[4]) + ' ' + sorted_dopinf[4])
a.append(sorted_name[5] + ' ' + str(sorted_hours[5]) + ' ' + str(sorted_inhour[5]) + ' ' + str(sorted_allsum[5]) + ' ' + sorted_dopinf[5])
a.append(sorted_name[6] + ' ' + str(sorted_hours[6]) + ' ' + str(sorted_inhour[6]) + ' ' + str(sorted_allsum[6]) + ' ' + sorted_dopinf[6])
a.append(sorted_name[7] + ' ' + str(sorted_hours[7]) + ' ' + str(sorted_inhour[7]) + ' ' + str(sorted_allsum[7]) + ' ' + sorted_dopinf[7])
pprint(str(a[0]))

with open('output.txt', 'w') as f1:
    f1.writelines(a)
    f1.close()