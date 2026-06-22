import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("employee_data.csv")

# -----------------------------
# 1. Basic Information
# -----------------------------
print("===== DATASET SHAPE =====")
print(df.shape)

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# -----------------------------
# 2. Missing Values
# -----------------------------
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# -----------------------------
# 3. Average Performance by Department
# -----------------------------
dept_performance = df.groupby("Department")["Performance_Score"].mean().sort_values(ascending=False)
print("\n===== AVERAGE PERFORMANCE BY DEPARTMENT =====")
print(dept_performance)

# -----------------------------
# 4. Correlation Analysis
# -----------------------------
numeric_df = df.select_dtypes(include=["number"])
correlation = numeric_df.corr()

print("\n===== CORRELATION MATRIX =====")
print(correlation)

# -----------------------------
# 5. Correlation Heatmap
# -----------------------------
plt.figure(figsize=(10, 7))
plt.imshow(correlation, cmap="coolwarm", aspect="auto")
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45, ha="right")
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# -----------------------------
# 6. Experience vs Performance Score
# -----------------------------
plt.figure(figsize=(7, 5))
plt.scatter(df["Experience_Years"], df["Performance_Score"])
plt.xlabel("Experience Years")
plt.ylabel("Performance Score")
plt.title("Experience vs Performance Score")
plt.tight_layout()
plt.savefig("experience_vs_performance.png")
plt.show()

# -----------------------------
# 7. Salary Distribution
# -----------------------------
plt.figure(figsize=(7, 5))
plt.hist(df["Monthly_Salary"], bins=6)
plt.xlabel("Monthly Salary")
plt.ylabel("Number of Employees")
plt.title("Salary Distribution")
plt.tight_layout()
plt.savefig("salary_distribution.png")
plt.show()

# -----------------------------
# 8. Attendance vs Performance
# -----------------------------
plt.figure(figsize=(7, 5))
plt.scatter(df["Attendance_Percentage"], df["Performance_Score"])
plt.xlabel("Attendance Percentage")
plt.ylabel("Performance Score")
plt.title("Attendance vs Performance Score")
plt.tight_layout()
plt.savefig("attendance_vs_performance.png")
plt.show()

# -----------------------------
# 9. Department-wise Average Performance (Bar Chart)
# -----------------------------
plt.figure(figsize=(7, 5))
dept_performance.plot(kind="bar")
plt.xlabel("Department")
plt.ylabel("Average Performance Score")
plt.title("Department-wise Average Performance")
plt.tight_layout()
plt.savefig("department_performance.png")
plt.show()

# -----------------------------
# 10. Projects Completed vs Performance
# -----------------------------
plt.figure(figsize=(7, 5))
plt.scatter(df["Projects_Completed"], df["Performance_Score"])
plt.xlabel("Projects Completed")
plt.ylabel("Performance Score")
plt.title("Projects Completed vs Performance Score")
plt.tight_layout()
plt.savefig("projects_vs_performance.png")
plt.show()

print("\nEDA completed successfully. Graphs saved as PNG files.")