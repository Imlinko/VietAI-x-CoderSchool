# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
import numpy as np
arr = np.array([12,13,14,15,16])
print(arr[::-1])
# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]
arr_1 = [0,10,20,40,60]
arr_2 = [10,30,40]
print(sum(np.in1d(arr_1,arr_2)))
# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]
a = [1,6,4,8,9,-4,-2,11]
print(np.argmax(a,axis= 0))
print(np.argmin(a,axis = 0))
# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...
import re
with open('story.txt','r') as file:
    data = file.read()
data = re.sub(r'[^\w\s]',' ',data)
data = re.sub(r'\s+',' ',data).strip()
data_dict = {}
for word in data.split():
    data_dict.setdefault(word,0)
    data_dict[word]+=1
print(dict(sorted(data_dict.items(),key = lambda x:x[1],reverse =True)))