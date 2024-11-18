from itertools import groupby

import pandas as pd
from sklearn.utils.fixes import np_version

df = pd.read_csv(r"C:/Users/shiji/OneDrive/Máy tính/Code/AI-x-Code/VietAI-x-CoderSchool/Week4/Iris (1).csv")
print(df)
#1.a
print(df.groupby("Species")[["SepalLengthCm","PetalWidthCm"]].mean())
#1.b
print(df.sort_values(by=("SepalLengthCm"),ascending = True).groupby("Species").head(10))
#2.a
print(df.groupby("Species")[["SepalLengthCm","PetalWidthCm"]].max())
#2.b
df_sum = df.copy()
df_sum["Sepal_sum_length_width_cm"] = df_sum["SepalLengthCm"]+df_sum["SepalWidthCm"]
top_50 = df_sum[["Species","SepalLengthCm","SepalWidthCm","Sepal_sum_length_width_cm"]].nlargest(50,"Sepal_sum_length_width_cm").reset_index().groupby("Species")["Sepal_sum_length_width_cm"].value_counts()
list_species = df_sum["Species"].unique()

print(top_50[list_species].groupby("Species").sum())
#3.a
Length_flower = int(input("Nhập chiều dài của bông hoa (theo mm): "))
Width_flower = int(input("Nhập chiều rộng của bông hoa (theo mm): "))
while Length_flower < 0 and Width_flower < 0:
    Width_flower = int(input("Nhập chiều dài của bông hoa (theo mm): "))
    Length_flower = int(input("Nhập chiều rộng của bông hoa (theo mm): "))
df_space = df.copy()
import numpy as np
df_space["distance"] = np.sqrt(abs(pow(Length_flower*10-df_space["PetalLengthCm"],2)+pow(Width_flower*10-df_space["PetalWidthCm"],2)))
condition_1= df_space[["Species","distance"]].iloc[df_space["distance"].idxmin(),0]
condition_2 = df_space.groupby("Species")["distance"].mean().idxmin()
if condition_1 == condition_2:
    print(condition_1)
else:
    print("This not Iris-setora or Iris versicolor or Irris-virginica")
#3.b

int_length = np.random.uniform(low = 4,high = 8 )
int_width = np.random.uniform(low = 2,high = 5)
df_cp3b = df.copy()
df_cp3b["distance"] = np.sqrt(
    np.power(int_length*10-df_cp3b["SepalLengthCm"],2)+
    np.power(int_width*10-df_cp3b["SepalWidthCm"],2)
)
fake_row = df_cp3b.iloc[df_cp3b["distance"].idxmin()].copy()
fake_df = fake_row.to_frame().T
fake_df = pd.concat([df_cp3b,fake_df])
fake_df_2 = fake_df.copy()
found = False

while not found:
    min_distance = fake_df_2[fake_df_2["distance"].min() == fake_df_2["distance"]]
    if len(min_distance["Species"].unique()) !=1:
        found = True
        print(f"{min_distance['Species'].unique()[0]}")


    else:
        print(f"Found {min_distance['Species'].unique()}")
        fake_df_2.drop(index = min_distance.index,inplace = True)
#3.b.b
print(df_cp3b.nsmallest(n = 7, columns = 'distance')['Species'].mode())

df_cp3c = df.copy()
df_cp3c['distance'] = np.sqrt(np.power(int_length*10-df_cp3c["SepalLengthCm"])+np.power(int_width-df_cp3c["SepalWidthCm"]))

df_radius = df_cp3c[df_cp3c["distance"] < 2]['species'].mode().unique()
if len(df_radius) !=1:
    print("Không thuộc bất kì class nào cả")
else:
    print(df_radius)