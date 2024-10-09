import pandas as pd
import numpy as np

# Assuming academic_performance_fixed_df is already available (from the previous script)
# Otherwise, load it from the saved CSV
academic_performance_fixed_df = pd.read_csv('academic_performance.csv')

# Classify students by performance category
academic_performance_fixed_df['Performance Category'] = pd.cut(
    academic_performance_fixed_df['Average Grade (100%)'],
    bins=[0, 50, 70, 100],
    labels=['Low Performer', 'Medium Performer', 'High Performer']
)

# Group by Student ID to summarize performance category (most common performance category)
student_performance_summary = academic_performance_fixed_df.groupby('Student ID')['Performance Category'].apply(lambda x: x.mode()[0])

# Function to generate learning behavior and engagement data
def generate_learning_behavior_data(student_performance_summary):
    learning_data = []

    for student_id, performance_category in student_performance_summary.items():
        # Generate data based on the performance category
        if performance_category == 'High Performer':
            login_frequency = np.random.randint(5, 7)  # High login activity
            homework_completion = np.random.randint(80, 100)  # High homework completion rate
            time_spent = np.random.randint(10, 13)  # High time spent on platform (hours)
        elif performance_category == 'Medium Performer':
            login_frequency = np.random.randint(3, 5)  # Moderate login activity
            homework_completion = np.random.randint(50, 80)  # Medium homework completion rate
            time_spent = np.random.randint(5, 9)  # Medium time spent on platform
        else:  # Low Performer
            login_frequency = np.random.randint(1, 3)  # Low login activity
            homework_completion = np.random.randint(20, 50)  # Low homework completion rate
            time_spent = np.random.randint(1, 5)  # Low time spent on platform

        # Append the generated data
        learning_data.append({
            'Student ID': student_id,
            'LMS Login Frequency (per week)': login_frequency,
            'Homework Completion Rate (%)': homework_completion,
            'Time Spent on Platform (hours)': time_spent
        })

    return pd.DataFrame(learning_data)

# Generate the learning behavior data
learning_behavior_df = generate_learning_behavior_data(student_performance_summary)

# Save the learning behavior dataset to a CSV file
learning_behavior_df.to_csv('learning_behavior.csv', index=False)

