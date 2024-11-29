import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("dataset_2.csv")
#Task 2: In ra index của 20 học sinh có điểm writing score cao nhất của mỗi
#group (race/ethnicity)
group = df.groupby("race/ethnicity")["writing score"].nlargest(n=20)
#print(group.index)
#Task 3: Thống kê số lượng học sinh của group A theo parental level of
#education
group_A = df[df["race/ethnicity"] == 'group A'].groupby("race/ethnicity")["parental level of education"]
group_A_stu = group_A.value_counts()/group_A.value_counts().sum()

labels = df["parental level of education"].unique()
#plt.pie(group_A_stu,labels = labels, colors = ["red","green","yellow","purple","blue","gray"],autopct = "%1.1f%%")
#plt.axis("equal")
#plt.show()
#Task 4: Có phải xu hướng chung, cha mẹ có học vấn càng cao thì điểm số
# trung bình 3 môn của con cái cũng càng cao ko
#df["mean_of_score"] = (df["writing score"] +df["math score"] +df["reading score"])/3

mean_of_score= df.groupby("parental level of education")[["writing score","math score","reading score"]].mean()

print(mean_of_score.sort_values(by=['writing score', 'math score', 'reading score'],axis = 0))

#Task 5: Chất lượng bữa ăn (lunch) có tương phản với điểm số trung bình 3
# môn của học sinh không
print(df.groupby("lunch")[["math score","reading score","writing score"]].mean())


#Task 6: Tìm ra Top 10 học sinh có điểm toán cao nhất của mỗi group

print(df.groupby("race/ethnicity")["math score"].nlargest(n =10).reset_index())


#Task 7: Với những học sinh ở cùng 1 group, cùng parental level of
#education, cùng loại bữa ăn (lunch), việc tham gia test preparation course
#có giúp học sinh đó có điểm trung bình 3 môn cao hơn những học sinh
#không tham gia ko
non_tpc = df[df["test preparation course"] == "none"].groupby(["race/ethnicity","parental level of education","lunch"])[["writing score","math score","reading score"]].mean()

com_tpc = df[df["test preparation course"] == "completed"].groupby(["race/ethnicity","parental level of education","lunch"])[["writing score","math score","reading score"]].mean()