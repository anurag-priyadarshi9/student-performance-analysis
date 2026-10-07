
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("student_performance_dataset.csv")

# 2. Calculate total marks and percentage
df["Total_Marks"] = (
    df["Assignment_Marks"]
    + df["Midterm_Marks"]
    + df["Final_Exam_Marks"]
)
df["Percentage"] = (df["Total_Marks"] / 150 * 100).round(2)

# 3. Determine result
df["Result"] = np.where(df["Percentage"] >= 40, "Pass", "Fail")

# 4. Display basic information
print("===== STUDENT PERFORMANCE ANALYSIS =====")
print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df[["Attendance", "Assignment_Marks", "Midterm_Marks",
          "Final_Exam_Marks", "Total_Marks", "Percentage"]].describe())

# 5. Performance analysis
print("\nAverage Percentage:", round(df["Percentage"].mean(), 2))
print("Highest Percentage:", df["Percentage"].max())
print("Lowest Percentage:", df["Percentage"].min())

top_student = df.loc[df["Percentage"].idxmax()]
print("\nTop Performer:", top_student["Name"])
print("Top Percentage:", top_student["Percentage"])

print("\nPass Students:", (df["Result"] == "Pass").sum())
print("Fail Students:", (df["Result"] == "Fail").sum())

# 6. Students with attendance below 75%
low_attendance = df[df["Attendance"] < 75]
print("\nStudents with attendance below 75%:")
print(low_attendance[["Name", "Attendance", "Percentage"]])

# 7. Graph 1 - Percentage comparison
plt.figure(figsize=(10, 5))
plt.bar(df["Name"], df["Percentage"])
plt.xticks(rotation=60, ha="right")
plt.xlabel("Student")
plt.ylabel("Percentage (%)")
plt.title("Student Percentage Comparison")
plt.tight_layout()
plt.show()

# 8. Graph 2 - Pass/Fail distribution
counts = df["Result"].value_counts()
plt.figure(figsize=(6, 5))
plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%")
plt.title("Pass and Fail Distribution")
plt.show()

# 9. Graph 3 - Attendance vs Percentage
plt.figure(figsize=(7, 5))
plt.scatter(df["Attendance"], df["Percentage"])
plt.xlabel("Attendance (%)")
plt.ylabel("Percentage (%)")
plt.title("Attendance vs Percentage")
plt.grid(True)
plt.show()

# 10. Save final processed data
df.to_csv("final_student_performance_analysis.csv", index=False)

print("\nAnalysis completed successfully.")
