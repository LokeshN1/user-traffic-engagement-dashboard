from datetime import datetime, timedelta
import pandas as pd
import random

# Generate dummy data for the last 30 days
num_days = 30
end_date = datetime.today()
start_date = end_date - timedelta(days=num_days-1)

# Create date range
date_range = [start_date + timedelta(days=x) for x in range(num_days)]

# Sample data lists
traffic_sources = ['Organic', 'Social', 'Referral', 'Direct']
device_types = ['Desktop', 'Mobile', 'Tablet']

# Generate data
rows = []
for date in date_range:
    users = random.randint(100, 250)
    sessions = random.randint(users, users + 50)
    page_views = random.randint(sessions * 2, sessions * 4)
    avg_session_duration = round(random.uniform(1.0, 3.0), 2)  # in minutes
    bounce_rate = round(random.uniform(20.0, 50.0), 2)  # in percentage
    traffic_source = random.choice(traffic_sources)
    device_type = random.choice(device_types)
    rows.append({
        'Date': date.strftime('%Y-%m-%d'),
        'Users': users,
        'Sessions': sessions,
        'Page Views': page_views,
        'Avg. Session Duration (min)': avg_session_duration,
        'Bounce Rate (%)': bounce_rate,
        'Traffic Source': traffic_source,
        'Device Type': device_type
    })

# Create DataFrame and save to CSV
dummy_data_df = pd.DataFrame(rows)
dummy_data_df.to_csv('user_traffic_engagement_last_30_days.csv', index=False)
