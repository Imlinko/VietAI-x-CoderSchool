#Phân tích dữ liệu và thống kê, đồ thị hóa dữ liệu
#Sử dụng thư viện pandas để Thống kê hoặc làm sạch dữ liệu
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sn
df = pd.read_csv(r"C:/Users/shiji/OneDrive/Máy tính/AI-x-Code/VietAI-x-CoderSchool/Week4/Week4_1_data.csv")
#In ra toàn bộ dữ liệu
print(df) 
#Kích thước dữ liệu : [486 rows x 12 columns]
# Thống kế sử dụng hàm describe()
print(df.describe())
#Có 13 ô bị mất của cột 'annual_income' 
print(df.isnull())
#Loại bỏ các sample thiếu giá trị 
df = df.dropna()
#1.Thống kê thành phần khách hàng theo học vấn
customer_level = df["educational_level"].unique()
customer_fre =  list(pd.Series(df["educational_level"]).value_counts())
#Vẽ pie chart dựa trên học vấn 
plt.figure(figsize=(10,20))
plt.title("Biểu đồ thống kế thành phần khách hàng theo mức độ học vấn")
plt.pie(customer_fre,labels=customer_level,colors=['r','g','c','y','b'],autopct="%0.1f%%")
plt.show()
#2.In ra khách hàng có mức thu nhập cao nhất
df_high_income = df.sort_values(by=("annual_income"), ascending=False).head(20)
print(df_high_income)
#3.
print(df.loc[(df["year_of_birth"] >= 1960) & (df["annual_income"] >=50_000)])
#4.
print(df.loc[(df["year_of_birth"] >= 1960) & (df["annual_income"] >=50_000)].sort_values(by="annual_income",ascending=False).head(20))
#5.
print(df.loc[(df["marital_status"]=='Divored') | (df["marital_status"]=="Married")])
#6
print(df.groupby("educational_level")["annual_income"].mean().reset_index())
#7.
print(df.groupby(["educational_level","marital_status"])["annual_income"].mean().reset_index())
#8. Kết luận 
# So sánh giữa Income và Education_level
plt.figure(figsize=(8,6))

sn.boxplot(x='educational_level',y='annual_income',palette=['red', 'blue', 'green', 'purple','yellow'],hue='educational_level',data = df)
plt.title("Income Distribution by Education Level")
plt.xlabel("Education level")
plt.ylabel("Income")

plt.show()
#So sánh giữa income và tình trạng hôn nhân
plt.figure(figsize=(5,10))

sn.boxplot(x='marital_status',y='annual_income',palette=['red', 'blue', 'green', 'purple','yellow','orange'],hue="marital_status",data = df)
plt.title("Income Distribution by relationship")
plt.xlabel("Marital")
plt.ylabel("Income")

plt.show()
#Kết luận 
# Single có mức thu nhập, thu nhập trung bình cao nhất 
# window có mức thu nhập trung bình thấp nhất
# PhD có mức thu nhập trung bình cao nhất
