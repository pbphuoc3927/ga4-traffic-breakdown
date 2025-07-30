import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import uuid

# --- Config ---
NUM_USERS = 10000
MAX_SESSIONS_PER_USER = 10
START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 3, 31)

# --- Mock Pools ---
sources = ['google', 'direct', 'facebook', 'tiktok', 'youtube', 'zalo']
mediums = ['organic', 'cpc', 'referral', 'email', 'social']
devices = ['mobile', 'desktop', 'tablet']
countries = ['Vietnam', 'United States', 'Japan', 'Thailand', 'India']
events = ['page_view', 'add_to_cart', 'purchase', 'begin_checkout', 'scroll']

# --- Generate Data ---
def generate_ga4_data(num_users, max_sessions_per_user):
    data = []

    for user_id in range(1, num_users + 1):
        # Chọn ngày đầu tiên user xuất hiện (cohort)
        cohort_day = START_DATE + timedelta(days=random.randint(0, 30))  # trong 1 tháng đầu

        # Sinh số phiên cho user này
        num_sessions = random.randint(1, max_sessions_per_user)

        for i in range(num_sessions):
            session_date = cohort_day + timedelta(days=random.randint(0, 7 * (i + 1)))
            if session_date > END_DATE:
                continue

            session_id = f"sess_{uuid.uuid4().hex[:10]}"
            source = random.choice(sources)
            medium = random.choice(mediums)
            device = random.choice(devices)
            country = random.choice(countries)
            session_duration = np.random.exponential(scale=300)
            event_name = random.choice(events)
            conversion = int(event_name == 'purchase')

            data.append([
                session_id,
                user_id,
                session_date.strftime('%Y-%m-%d'),
                source,
                medium,
                device,
                country,
                round(session_duration, 2),
                event_name,
                conversion
            ])

    df = pd.DataFrame(data, columns=[
        'session_id', 'user_id', 'date', 'session_source', 'medium',
        'device_category', 'country', 'session_duration',
        'event_name', 'conversion'
    ])
    return df

# --- Save to CSV ---
if __name__ == "__main__":
    df = generate_ga4_data(NUM_USERS, MAX_SESSIONS_PER_USER)
    output_path = r"C:\Users\phuoc\ga4-traffic-breakdown\data\ga4_sample_data.csv"
    df.to_csv(output_path, index=False)
    print(f"✅ Generated {len(df)} rows of GA4 session-level data for {NUM_USERS} users → saved to ga4_sample_data.csv")
