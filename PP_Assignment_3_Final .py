import pandas as pd
import numpy as np
from tabulate import tabulate

# Step 1: Generate sample data
np.random.seed(42)
names = ['Karm', 'Geet', 'Richa', 'Harsh', 'Aditi', 'Nirdhar', 'Pushti', 'Krishna', 'Simran', 'Devansh']
num_students = len(names)

math_scores = np.random.randint(50, 100, size=num_students)
science_scores = np.random.randint(50, 100, size=num_students)
english_scores = np.random.randint(50, 100, size=num_students)

data = {
    'Name': names,
    'Math': math_scores,
    'Science': science_scores,
    'English': english_scores
}

df = pd.DataFrame(data)

# Step 2: Calculate average and grade
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Average'].apply(assign_grade)

# Step 3: Display table using tabulate
print("\n=== Student Performance Table ===\n")
print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))

# Step 4: Show summary statistics
print("\n=== Subject Averages ===")
subject_avgs = df[['Math', 'Science', 'English']].mean()
for subject, avg in subject_avgs.items():
    print(f"{subject}: {avg:.2f}")

top_student = df.loc[df['Average'].idxmax()]
print(f"\nTop Performer: {top_student['Name']} (Average: {top_student['Average']:.2f}, Grade: {top_student['Grade']})")

print("\n=== Grade Distribution ===")
grade_counts = df['Grade'].value_counts()
for grade, count in grade_counts.items():
    print(f"Grade {grade}: {count} student(s)")
