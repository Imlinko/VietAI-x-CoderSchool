import pandas as pd
import numpy as np
from scipy.odr import polynomial
from ydata_profiling import ProfileReport
path = ".\dataset_1.csv"
df= pd.read_csv(path)
#In ra top 10 thanh pho co dan so dong nhat
#print(df.sort_values(by="Population",ascending=True)["City"].head(10).reset_index())
#In ra top 10 thanh pho co dan so thap nhat
#print(df.sort_values(by="Population",ascending=False)["City"].head(10).reset_index())
#
#rp = ProfileReport(df)
#rp.to_file("report.html")
#In ra tên các quốc gia có tối thiểu 3 thành phố trong danh sách này
# df_f= df.groupby("Country")["City"].value_counts()
# lst = df["Country"].unique()
# count = df_f[lst].groupby("Country").sum()
# for i in range(len(count.index)):
#     if count[i] > 2:
#         print(count.index[i])
#In ra Top 5 quốc gia có nhiều thành phố xuất hiện trong bảng này nhất
#print(count.nlargest(n=5))
# In ra các thành phố có dân số & diện tích đều nằm trong Top 20
#print(df.sort_values(by=["Population","Area KM2"]).head(20)["City"].reset_index().drop("index",axis=1))
#Thống kê mật độ dân số theo quốc gia
import matplotlib.pyplot as plt
import re
#Mật độ dân số = tống dân số / diện tích quốc gia (người/km2)
df_p = df.copy()
for num in range(len(df_p["Population"])):
    df_p.at[num,"Population"] = re.sub(r",","_",df_p.iloc[num,2])
population  = df_p.groupby("Country")["Population"].sum()
area = df_p.groupby("Country")["Area KM2"].sum()
area[0] = "43996"


for i in range(len(area)-1):
    area[i] = int(area[i])
for j in range(len(population)-1):
    population[j] = int(population[j])
df_p["Density_of_population"] = population/area
print(df_p["Density_of_population"])
