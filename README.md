# Employee-Performance-EDA-Analysis
Employee Performance EDA project using Python, Pandas, and Matplotlib to analyze salary, attendance, experience, project completion, and performance trends.
# Employee Performance Analysis using Exploratory Data Analysis (EDA)

## Project Overview
This project performs Exploratory Data Analysis (EDA) on an employee dataset to uncover patterns, trends, and relationships between employee attributes such as experience, salary, attendance, projects completed, and performance score.
The objective of this project is to analyze employee-related data, identify key factors affecting performance, and present insights using statistical summaries and visualizations.

## Technologies Used
* Python
* Pandas
* Matplotlib

## Dataset Features

The dataset contains the following employee attributes:
* **Employee_ID** – Unique ID of employee
* **Age** – Age of employee
* **Department** – Department of employee
* **Experience_Years** – Total years of experience
* **Monthly_Salary** – Monthly salary of employee
* **Attendance_Percentage** – Attendance percentage
* **Projects_Completed** – Number of projects completed
* **Performance_Score** – Performance score of employee
* **Overtime_Hours** – Overtime hours worked
* **Promotion** – Promotion status (Yes/No)

## Objectives
The main objectives of this EDA project are:
* To understand the structure of employee data
* To identify relationships between experience, salary, attendance, and performance
* To compare employee performance across different departments
* To find the factors that influence employee performance the most
* To visualize employee trends using charts and plots

## Analysis Performed
### 1. Data Inspection
* Dataset shape
* Dataset information
* First 5 rows
* Statistical summary

### 2. Missing Value Analysis
* Checked for missing values in the dataset

### 3. Correlation Analysis
* Generated a correlation matrix for numeric features
* Identified relationships among salary, experience, projects, attendance, and performance score

### 4. Data Visualization
The following visualizations were created:
* Correlation Heatmap
* Experience vs Performance Score
* Salary Distribution
* Attendance vs Performance Score
* Department-wise Average Performance
* Projects Completed vs Performance Score

## Key Insights
* Employees with more experience generally tend to have better performance scores.
* Higher attendance percentage is associated with improved employee performance.
* Employees who complete more projects usually have higher performance scores.
* Salary tends to increase with experience and performance.
* Some departments show stronger average performance compared to others.

## Project Structure
Employee-Performance-EDA-Analysis/
├── employee_data.csv
├── employee_eda_analysis.py
├── correlation_heatmap.png
├── experience_vs_performance.png
├── salary_distribution.png
├── attendance_vs_performance.png
├── department_performance.png
├── projects_vs_performance.png
├── README.md
└── .gitignore


## Output Files
After running the project, the following output graphs will be generated:
* correlation_heatmap.png
* experience_vs_performance.png
* salary_distribution.png
* attendance_vs_performance.png
* department_performance.png
* projects_vs_performance.png

## Conclusion
This EDA project helps in understanding employee behavior and performance patterns using data analysis and visualization. It highlights how factors such as experience, attendance, and project completion contribute to overall employee performance.
