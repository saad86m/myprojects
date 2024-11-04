# **Implementation Guide: Real-Time IoT Data Processing Pipeline**

## **Step-by-Step Setup**

### **Step 1: Simulate IoT Data**
Refer to `data-simulation-script/iot_data_simulation.py` for the **Python script** to simulate IoT data and send it to **Azure IoT Hub**.

### **Step 2: Configure Azure IoT Hub**
Refer to `azure-config/iot-hub-setup.md` for instructions on creating and configuring an **IoT Hub** and registering a device.

### **Step 3: Set Up Azure Stream Analytics**
Refer to `azure-config/stream-analytics-query.sql` for configuring the **job** and adding **inputs and outputs**.

### **Step 4: Configure Azure SQL Database**
Refer to `azure-config/sql-table-schema.sql` for creating the **table structure** to store processed data.

### **Step 5: Visualize in Power BI**
Refer to `power-bi/dashboard_screenshot.png` for an example of how to build **real-time dashboards** and display insights.
