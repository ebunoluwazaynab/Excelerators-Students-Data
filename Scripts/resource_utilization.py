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

# Function to generate resource utilization data with probabilities for all performance categories
def generate_resource_utilization_data(student_performance_summary):
    resource_utilization_data = []

    for student_id, performance_category in student_performance_summary.items():
        # Adjust probabilities based on performance category
        if performance_category == 'High Performer':
            tutoring_sessions = np.random.randint(3, 6)  # More tutoring sessions
            accessed_extra_materials = np.random.choice(['Yes', 'No'], p=[0.8, 0.2])  # 80% chance of Yes
            study_group_participation = np.random.choice(['Yes', 'No'], p=[0.8, 0.2])  # 80% chance of Yes
        elif performance_category == 'Medium Performer':
            tutoring_sessions = np.random.randint(1, 4)  # Moderate tutoring sessions
            accessed_extra_materials = np.random.choice(['Yes', 'No'], p=[0.4, 0.6])  # 40% chance of Yes
            study_group_participation = np.random.choice(['Yes', 'No'], p=[0.4, 0.6])  # 40% chance of Yes
        else:  # Low Performer
            tutoring_sessions = np.random.randint(0, 2)  # Fewer tutoring sessions
            accessed_extra_materials = np.random.choice(['Yes', 'No'], p=[0.1, 0.9])  # 10% chance of Yes
            study_group_participation = np.random.choice(['Yes', 'No'], p=[0.1, 0.9])  # 10% chance of Yes

        # Append the generated data
        resource_utilization_data.append({
            'Student ID': student_id,
            'Tutoring Sessions Attended': tutoring_sessions,
            'Accessed Extra Study Materials (Yes/No)': accessed_extra_materials,
            'Study Group Participation (Yes/No)': study_group_participation
        })

    return pd.DataFrame(resource_utilization_data)

# Generate the resource utilization data
resource_utilization_df = generate_resource_utilization_data(student_performance_summary)

# Save the resource utilization data to a CSV file
resource_utilization_df.to_csv('resource_utilization_data.csv', index=False)

