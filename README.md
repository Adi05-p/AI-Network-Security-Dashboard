# AI-Network-Security-Dashboard  
### Python + Power BI | Synthetic Log Analysis | Threat Intelligence Monitoring

This project presents an end-to-end **AI-driven network security analytics workflow**, combining **Python-based synthetic log generation** with a **Power BI dashboard** for threat detection, anomaly identification, and traffic behavior analysis.

Designed as part of my data analytics portfolio, the project demonstrates practical skills in **data engineering, cybersecurity analytics, dashboard design**, and **business intelligence**—aligned with the expectations of postgraduate programs in Business Analytics.

---

## 🧩 Executive Summary

Modern organizations face increasing cybersecurity threats and rely heavily on real-time log analytics to detect anomalies and prioritize potential risks.

This project simulates such an environment by:

- Generating synthetic network logs using Python  
- Creating threat indicators (packet size, protocol, risk score)  
- Modeling realistic traffic data  
- Designing an interactive monitoring dashboard in Power BI  

The result is a visual intelligence system that highlights:

- Threat score trends  
- Suspicious IP behavior  
- Traffic patterns  
- Potential anomalies  

---

## 📊 Dashboard Overview

### **1. Threat Score Over Time**
A time-series line chart showing fluctuations in network risk.  
Used to identify high-severity windows or unusual spikes.

### **2. Average Packet Size by Protocol (TCP vs UDP)**
Shows comparative traffic load between protocols.  
Useful for detecting abnormal packet behavior (e.g., large UDP packets during attacks).

### **3. Packet Size Distribution (Histogram)**
Visualizes how data packets are distributed.  
Helps reveal unusual clusters or irregular traffic flows.

### **4. Top Suspicious Source IPs**
Ranks IP addresses with the highest threat scores.  
Highlights the most probable sources of malicious activity.

---

## 🧪 Data Generation Methodology

Synthetic data was generated using a custom Python script (`generate_data.py`) to replicate key elements of security logs:

- **Timestamps** (hourly events)  
- **Source & destination IPs**  
- **Network protocols (TCP/UDP)**  
- **Packet sizes (100–1500 bytes)**  
- **Threat scores (0–100)**  

Python libraries used:

- `pandas`  
- `numpy`  
- `os`

The dataset is saved as:/data/network_security_data.csv

This structure mirrors real SIEM (Security Information and Event Management) log outputs.

---

## 📌 Project Structure

AI-Network-Security-Dashboard/
│
├── data/
│ └── network_security_data.csv
│
├── generate_data.py
├── dashboard.png
└── README.md


---

## 🛠️ Tools & Technologies
- **Python 3.12** — Synthetic log creation  
- **Pandas & NumPy** — Data generation & transformation  
- **Power BI Desktop** — Dashboard & analytics  
- **DAX & Power Query** — Measures and data modeling  
- **CSV Data Pipeline** — Storage and ingestion

---

## 🎯 Key Analytical Insights

- Significant variation in hourly threat levels indicates possible scanning or probing events.
- TCP shows higher packet size averages due to its reliability-focused nature.
- Histogram reveals normal vs abnormal packet size clusters.
- Suspicious IP ranking highlights potential internal/external threats, guiding immediate investigation.

---

## 🎓 Relevance to Business Analytics

This project demonstrates:

✔ Data preprocessing  
✔ Visualization and storytelling  
✔ Applying analytics to cybersecurity  
✔ Business-focused interpretation  
✔ Dashboard development for management decisions  
✔ Integrating Python with BI tools  

It reflects strong analytical thinking and practical hands-on ability—skills highly relevant to programs at **Imperial College London, Warwick, Manchester, and Edinburgh**.

---

## 📂 Dashboard Preview

![Dashboard Screenshot](dashboard.png)

---

## 🚀 How to Run This Project

**1. Clone the repository:**
git clone https://github.com/Adi05-p/AI-Network-Security-Dashboard.git


**2. Install required Python libraries:**
pip install pandas numpy

**3. Generate dataset:**
python generate_data.py


**4. Open the CSV file in Power BI**  
Load → Visualize → Explore Insights

---

## 📬 Contact  9881133901
**Adetee Paatil**  
GitHub: https://github.com/Adi05-p  

Feel free to ⭐ star the project if you find it useful!






