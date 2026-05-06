import pandas as pd

df = {
    "Name" : ["Rahul","Amit","Sneha","Pooja","karan","Neha"],
    "Age" : [20,30,45,58,25,47],
    "Salary":[2555,88888,77777,66666,48956,254156],
    "Department": ["IT","Mechanical","Development","Medical","Business","Farma"],
    "Experince":[2,8,4,3,9,6]
}

data = pd.DataFrame(df)
# print(data)

# # show the first 3 rows
# d1=data.head(3)
# print(d1)

# # Shows last 3 rows
# d2=data.tail(3)
# print(d2)

# # get column name
# print(data.columns)

# # find the shape of data frame
# print(data.shape)

# # select bonly name and salary columns
# d3 =print(data["Name"],["Salary"])
# print(d3)

# result= data[data["Age"] >25]
# print(result)

# result1 = data[(data["Salary"] >= 66666) & (data["Salary"] <=70000)]
# print(result1)

# result3 = data["Salary"].mean()
# print(result3)

# result4= data[data["Department"]=="IT"]
# print(result4)

# result5= data[data["Department"]=="Development"]
# print(result5)

# result6= data.sort_values(by="Salary", ascending=True)
# print(result6)

n = len(data)

for i in range(n):
    for j in range(0,n-i-1):
        if data.iloc[j]["Salary"] < data.iloc[j+1]["Salary"]:
            temp = data.iloc[j].copy()
            data.iloc[j] = data.iloc[j+1]
            data.iloc[j+1] = temp
print("Manual sorted list:")
print(data)









