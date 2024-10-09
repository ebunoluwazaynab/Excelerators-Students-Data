import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Load the academic performance data (to get performance summary)
academic_performance_df = pd.read_csv('academic_performance.csv')

# Classify students by performance category
academic_performance_df['Performance Category'] = pd.cut(
    academic_performance_df['Average Grade (100%)'],
    bins=[0, 50, 70, 100],
    labels=['Low Performer', 'Medium Performer', 'High Performer']
)

# Group by Student ID to summarize performance category (most common performance category)
student_performance_summary = academic_performance_df.groupby('Student ID')['Performance Category'].apply(lambda x: x.mode()[0])

# Function to generate study habits and time management data
def generate_study_habits_data(student_performance_summary):
    study_habits_data = []

    for student_id, performance_category in student_performance_summary.items():
        # Study habits based on performance category
        if performance_category == 'High Performer':
            study_hours = np.random.randint(12, 16)  # More study hours per week
            adherence = np.random.randint(85, 100)  # High adherence to study schedule
            revision_frequency = np.random.randint(4, 7)  # Frequent revision (times/week)
            exam_confidence = np.random.randint(8, 11)  # High exam confidence
        elif performance_category == 'Medium Performer':
            study_hours = np.random.randint(6, 12)  # Moderate study hours
            adherence = np.random.randint(60, 85)  # Moderate adherence to study schedule
            revision_frequency = np.random.randint(2, 5)  # Moderate revision frequency
            exam_confidence = np.random.randint(5, 8)  # Medium exam confidence
        else:  # Low Performer
            study_hours = np.random.randint(2, 6)  # Fewer study hours
            adherence = np.random.randint(40, 60)  # Low adherence to study schedule
            revision_frequency = np.random.randint(0, 3)  # Infrequent revision
            exam_confidence = np.random.randint(1, 5)  # Low exam confidence

        # Append the generated data
        study_habits_data.append({
            'Student ID': student_id,
            'Study Hours per Week': study_hours,
            'Adherence to Study Schedule (%)': adherence,
            'Revision Frequency (Times/Week)': revision_frequency,
            'Exam Preparation Confidence (1-10)': exam_confidence
        })

    return pd.DataFrame(study_habits_data)

# Generate the study habits and time management data
study_habits_df = generate_study_habits_data(student_performance_summary)

# Save the study habits data to a CSV file
study_habits_df.to_csv('study_habits_data.csv', index=False)
