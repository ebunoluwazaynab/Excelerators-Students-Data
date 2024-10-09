import pandas as pd
import numpy as np

np.random.seed(42)

# Define extracurricular activities with Activity IDs and Types
activities = {
    1: {'activity_name': 'Football', 'activity_type': 'Sports'},
    2: {'activity_name': 'Basketball', 'activity_type': 'Sports'},
    3: {'activity_name': 'Chess', 'activity_type': 'Academic'},
    4: {'activity_name': 'Robotics', 'activity_type': 'Academic'},
    5: {'activity_name': 'Athletics', 'activity_type': 'Sports'},
    6: {'activity_name': 'Dance', 'activity_type': 'Arts'},
    7: {'activity_name': 'Debate', 'activity_type': 'Academic'},
    8: {'activity_name': 'Drama', 'activity_type': 'Arts'},
    9: {'activity_name': 'Volleyball', 'activity_type': 'Sports'},
    10: {'activity_name': 'Arts & Crafts', 'activity_type': 'Arts'},
    11: {'activity_name': 'Math Club', 'activity_type': 'Academic'},  # Additional academic activities
    12: {'activity_name': 'Science Club', 'activity_type': 'Academic'},
    13: {'activity_name': 'Debate Club', 'activity_type': 'Academic'},
    14: {'activity_name': 'Literary Society', 'activity_type': 'Academic'}
}

# Assuming teacher IDs are available (you can modify this based on your existing teacher table)
teacher_ids = np.arange(1, len(activities) + 1)  # Assuming one teacher per activity

# Generate the Activity Table with the teacher ID
def create_activity_table_with_teachers():
    activity_table = []
    for activity_id, activity_info in activities.items():
        teacher_id = np.random.choice(teacher_ids)  # Assign a random teacher ID to each activity

        activity_table.append({
            'activity_id': activity_id,
            'activity_name': activity_info['activity_name'],
            'teacher_id': teacher_id,  # Foreign key for teacher responsible
            'activity_type': activity_info['activity_type']
        })

    return pd.DataFrame(activity_table)

# Create the activity table
activity_table_df = create_activity_table_with_teachers()

# Save the activity table to CSV file if needed
activity_table_df.to_csv('activity_table.csv', index=False)
