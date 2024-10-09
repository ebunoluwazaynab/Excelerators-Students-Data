import pandas as pd
import numpy as np

# Load the academic performance data
academic_performance_df = pd.read_csv('academic_performance.csv')

# Classify students by performance category
academic_performance_df['Performance Category'] = pd.cut(
    academic_performance_df['Average Grade (100%)'],
    bins=[0, 50, 70, 100],
    labels=['Low Performer', 'Medium Performer', 'High Performer']
)

# Group by Student ID to summarize performance category (most common performance category)
student_performance_summary = academic_performance_df.groupby('Student ID')['Performance Category'].apply(lambda x: x.mode()[0])

# Function to generate attendance and participation data based on performance categories
def generate_attendance_data(performance_summary):
    attendance_data = []

    for student_id, performance_category in performance_summary.items():
        # Determine attendance percentage based on performance category
        if performance_category == 'High Performer':
            attendance = np.random.randint(80, 100)  # High performers tend to have high attendance
        elif performance_category == 'Medium Performer':
            attendance = np.random.randint(60, 80)  # Medium performers have moderate attendance
        else:
            attendance = np.random.randint(30, 60)  # Low performers have lower attendance

        # Participation score (out of 100) based on performance category
        if performance_category == 'High Performer':
            participation = np.random.randint(80, 100)  # High performers are more engaged
        elif performance_category == 'Medium Performer':
            participation = np.random.randint(40, 80)  # Medium engagement
        else:
            participation = np.random.randint(20, 60)  # Lower engagement for low performers

        # Append the generated data
        attendance_data.append({
            'Student ID': student_id,
            'Attendance Rate (%)': attendance,
            'Class Participation (%)': participation
        })

    return pd.DataFrame(attendance_data)

# Generate the attendance and participation data using the student performance summary
attendance_participation_df = generate_attendance_data(student_performance_summary)

# Save the attendance and participation dataset to a CSV file
attendance_participation_df.to_csv('attendance_participation.csv', index=False)

