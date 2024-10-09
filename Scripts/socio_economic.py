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

# Function to generate socio-emotional and behavioral data
def generate_socio_emotional_data(student_performance_summary):
    socio_emotional_data = []

    for student_id, performance_category in student_performance_summary.items():
        # Counseling Sessions and Emotional Well-being based on performance
        if performance_category == 'High Performer':
            counseling_sessions = np.random.randint(1, 3)  # Few sessions
            emotional_wellbeing = np.random.randint(7, 11)  # High well-being
            behavioral_issues = np.random.choice(['Yes', 'No'], p=[0.05, 0.95])  # Less likely to have behavioral issues
            peer_relationships = np.random.randint(8, 11)  # Good peer relationships
        elif performance_category == 'Medium Performer':
            counseling_sessions = np.random.randint(3, 6)  # Moderate sessions
            emotional_wellbeing = np.random.randint(5, 8)  # Moderate well-being
            behavioral_issues = np.random.choice(['Yes', 'No'], p=[0.1, 0.9])  # Moderate likelihood of issues
            peer_relationships = np.random.randint(5, 8)  # Average peer relationships
        else:  # Low Performer
            counseling_sessions = np.random.randint(4, 7)  # More sessions
            emotional_wellbeing = np.random.randint(3, 6)  # Low well-being
            behavioral_issues = np.random.choice(['Yes', 'No'], p=[0.2, 0.8])  # More likely to have behavioral issues
            peer_relationships = np.random.randint(3, 6)  # Struggles with peer relationships

        # Append the generated data
        socio_emotional_data.append({
            'Student ID': student_id,
            'Counseling Sessions Attended': counseling_sessions,
            'Emotional Well-being (1-10)': emotional_wellbeing,
            'Behavioral Issues (Yes/No)': behavioral_issues,
            'Peer Relationships (1-10)': peer_relationships
        })

    return pd.DataFrame(socio_emotional_data)

# Generate the socio-emotional and behavioral data
socio_emotional_df = generate_socio_emotional_data(student_performance_summary)

# Save the socio-emotional data to a CSV file
socio_emotional_df.to_csv('socio_emotional_data.csv', index=False)

