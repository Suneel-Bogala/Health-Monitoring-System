# Health Monitoring System Dashboard

## 📌 Project Overview
The **Health Monitoring System Dashboard** is a Big Data project designed to process and visualize patient health data. It uses **Apache Spark, Hadoop, Kafka, and NoSQL databases** for large-scale data processing. The dashboard, built with **Streamlit**, provides insights into key health parameters such as **Blood Pressure (BP), Sugar Levels, Cholesterol, and Haemoglobin**.

## 🛠️ Tech Stack
- **Python** (for data processing & visualization)
- **Apache Spark** (for big data processing)
- **Hadoop (HDFS)** (for distributed data storage)
- **Kafka** (for real-time streaming)
- **MongoDB/Cassandra** (for NoSQL storage)
- **Streamlit** (for interactive dashboard)
- **Matplotlib & Seaborn** (for data visualization)

## 📊 Features
✅ **Generate 10,000 Patient Records** (Synthetic Data)  
✅ **Process Patient Data with Spark**  
✅ **Display Interactive Data Visualizations**  
✅ **Filter Patients by Age & Gender**  
✅ **Real-time Data Streaming via Kafka**  
✅ **Patient Feedback Storage in NoSQL**  
✅ **Machine Learning-based Health Risk Analysis**  

## 📂 Project Structure
```
├── data/
│   ├── patient_data.csv  # Generated patient dataset
├── scripts/
│   ├── generate_data.py  # Data generation script
│   ├── spark_processing.py  # Spark data processing script
│   ├── kafka_producer.py  # Sends processed data to Kafka
│   ├── kafka_consumer.py  # Doctor's consumer application
├── dashboard/
│   ├── app.py  # Streamlit dashboard
├── README.md  # Project Documentation
```

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/health-monitoring-system.git
cd health-monitoring-system
```

### 2️⃣ Install Dependencies
```bash
pip install streamlit pandas numpy matplotlib seaborn pyspark kafka-python pymongo
```

### 3️⃣ Generate Patient Data
```bash
python scripts/generate_data.py
```

### 4️⃣ Start Kafka (If Real-time Processing is Enabled)
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```

### 5️⃣ Run Streamlit Dashboard
```bash
streamlit run dashboard/app.py
```

## 📌 Future Enhancements
🚀 **Risk Classification using Machine Learning**  
🚀 **Database Sharding for Scalable NoSQL Storage**  
🚀 **Doctor's Alert System for Critical Cases**  
🚀 **Mobile App for Patients**  

## 📝 Contributing
Contributions are welcome! Feel free to submit issues and pull requests.

## 📜 License
This project is licensed under the MIT License.

## 📧 Contact
For queries, reach out to **suneelreddy567700@gmail.com**.
