import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)

rows = 5000
data = {
    "timestamp": pd.date_range(start="2024-01-01", periods=rows, freq="H"),
    "source_ip": np.random.choice(["192.168.1.1", "10.0.0.5", "172.16.0.2"], rows),
    "destination_ip": np.random.choice(["8.8.8.8", "3.3.3.3", "9.9.9.9"], rows),
    "protocol": np.random.choice(["TCP", "UDP"], rows),
    "packet_size": np.random.randint(100, 1500, rows),
    "threat_score": np.random.randint(0, 100, rows),
}

df = pd.DataFrame(data)
df.to_csv("data/network_security_data.csv", index=False)

print("Dataset created successfully!")
print("Rows:", len(df))
