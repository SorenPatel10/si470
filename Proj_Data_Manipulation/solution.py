import pandas as pd
df = pd.read_csv("grades.csv")


grade_vals = {
    "F": 0, "RF": 0,
    "D": 1, "RD": 1, "D+": 2, "RD+": 2,
    "C-": 3, "C": 4, "C+": 5,
    "B-": 6, "B": 7, "B+": 8,
    "A-": 9, "A": 10
}
grade_letters = {
    0: "F", 1: "D", 2: "D+",
    3: "C-", 4: "C", 5: "C+",
    6: "B-", 7: "B", 8: "B+",
    9: "A-", 10: "A"
}

df_total = {}
a_total = {}

for col in df.columns:
    grades = df[col].replace(["V", "W"], None).dropna()
    
    #turn grades to their values
    grades = grades.map(grade_vals)
    
    #calculate and print median
    median = grades.median()
    print(col, grade_letters[round(median)])

    #count D+F's
    df_total[col] = grades.isin([0,1,2]).sum()
    #count A's
    a_total[col] = grades.isin([10]).sum()

print("\nCourses with most D's and F's: ")
print(pd.Series(df_total).nlargest(3))
print("\nCourses with most A's: ")
print(pd.Series(a_total).nlargest(3))

