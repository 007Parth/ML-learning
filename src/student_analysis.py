import pandas as pd
df = pd.read_csv("data/students.csv")
# Print dataframe:
print(df)
# Print only Math column
print(f'printng only the math column:\n{df["Math"]}')
# Find average Math marks
avg_math_score = df["Math"].mean()
print(f'avg math score: {avg_math_score}') 
# Find topper student
df["total_marks"] = pd.DataFrame(df["Math"]+
                           df["Science"]+
                           df["English"])
# print(df["total_marks"])
max_marks_scored =df["total_marks"].max()
topper  =  df[df["total_marks"]==max_marks_scored]

# print(topper)
print(f'Below is the topper of the class: \n{topper[["Name","total_marks"]]}')
# Below are my attempts in trying to find out the topper:
# print[df[topper]]
# for item in df["total_marks"]:
#     # print(item)
#     if df["total_marks"] == max_marks_scored:
#         print(f'Topper is: {df["Name"]}')
# print(f"Topper is: {df["name"]==df["total_marks"].max()}")
# Attempted to do it using the for loop
# for marks in total_marks:
#     if marks == total_marks.max(): 
#         print(f'Toppers marks: {marks} and topper is: {df.}')
    
# print(f'max : {}')
# for item in df:
#     total_marks = df["Math"]+df["Science"]+df["English"]

# next task adding the percentage column:
df["Percentage"] = (df["total_marks"] / 300) * 100
print(f'Below is the dataframe with percentage column in it:\n{df}')

