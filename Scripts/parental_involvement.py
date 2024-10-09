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

# Function to generate parental involvement data based on performance categories
def generate_parental_involvement_data(performance_summary):
    parental_data = []

    for student_id, performance_category in performance_summary.items():
        # Parent-Teacher Meetings: more meetings for high performers, fewer for low performers
        if performance_category == 'High Performer':
            parent_meetings = np.random.randint(3, 6)  # High involvement
            homework_help = np.random.randint(3, 5)  # More homework help
            access_to_resources = 'Yes'
        elif performance_category == 'Medium Performer':
            parent_meetings = np.random.randint(2, 4)  # Moderate involvement
            homework_help = np.random.randint(2, 4)  # Moderate homework help
            access_to_resources = np.random.choice(['Yes', 'No'])  # Could go either way
        else:  # Low Performer
            parent_meetings = np.random.randint(0, 3)  # Low involvement
            homework_help = np.random.randint(0, 2)  # Less homework help
            access_to_resources = 'No'

        # Append the generated data
        parental_data.append({
            'Student ID': student_id,
            'Parent-Teacher Meetings Attended': parent_meetings,
            'Homework Help (hours/week)': homework_help,
            'Access to Learning Resources (Yes/No)': access_to_resources
        })

    return pd.DataFrame(parental_data)

# Generate the parental involvement data
parental_involvement_df = generate_parental_involvement_data(student_performance_summary)

# Save the parental involvement dataset to a CSV file
parental_involvement_df.to_csv('parental_involvement.csv', index=False)
