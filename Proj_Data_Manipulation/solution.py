import pandas as pd
import matplotlib.pyplot as plt

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

# #plot histograms
# courses_to_plot = ["NL110", "SC111", "SM122"]
# for course in courses_to_plot:
#     grades = df[course].replace(["V", "W"], None).dropna()
#     grades = grades.map(grade_vals)

#     #11 bins for 11 different types of grades
#     plt.hist(grades, bins=11)
#     plt.title(course)

#     #label axes and plot
#     plt.xlabel("Grade Received")
#     plt.ylabel("Number of Students")
#     plt.show()


#calculate pearson's correlation coefficient between
#SC111 and every other class
sc111 = df["SC111"].map(grade_vals)
for col in df.columns:
    if col == "SC111":
        continue
    
    grades = df[col].map(grade_vals)
    correlation = sc111.corr(grades)
    print(col, correlation)


#calculate which 2 courses have the strongest correlation
# calculate correlation between every pair of courses
# calculate correlation between every pair of courses
correlations = {}

courses = list(df.columns)

for i in range(len(courses)):
    for j in range(i + 1, len(courses)):

        course1 = courses[i]
        course2 = courses[j]

        grades1 = df[course1].map(grade_vals)
        grades2 = df[course2].map(grade_vals)

        correlation = grades1.corr(grades2)

        if pd.notna(correlation):
            correlations[(course1, course2)] = correlation

# find the strongest correlation
strongest = max(correlations, key=correlations.get)

print("\nCourses with strongest correlation:")
print(strongest[0], strongest[1], correlations[strongest])