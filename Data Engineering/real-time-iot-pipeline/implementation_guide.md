# **Implementation Guide: Real-Time IoT Data Processing Pipeline**

## **Step-by-Step Setup**

### **Step 1: Simulate IoT Data**
Refer to **`data-simulation-script/iot_data_simulation.py`** for the **Python script** to simulate IoT data and send it to **Azure IoT Hub**.

### **Step 2: Register an IoT Device**
1. In **Azure IoT Hub**, navigate to **IoT Devices**.
2. Click **+ New**, enter a **Device ID** (e.g., `sensor-device-001`), and click **Save**.
3. Copy the **Primary Connection String** for use in your data simulation script.

### **Step 3: Configure Access Policies**
1. Go to **Shared access policies** in your **IoT Hub**.
2. Ensure a policy with **`Registry Read/Write`** and **`Service Connect`** permissions exists.
3. Copy the **Primary key** if needed for other services.

### **Step 4: Verify Connectivity**
1. Use **Azure IoT Explorer** to test and monitor messages.
2. Confirm that the **IoT device** is sending messages and they are being received by the **IoT Hub**.

### **Step 5: Set Up Azure Stream Analytics**
Refer to **`azure-config/stream-analytics-query.sql`** for configuring the **job** and adding **inputs and outputs**.

### **Step 6: Configure Azure SQL Database**
Refer to **`azure-config/sql-table-schema.sql`** for creating the **table structure** to store processed data.

### **Step 7: Visualize in Power BI**
Refer to **`power-bi/dashboard_screenshot.png`** for an example of how to build **real-time dashboards** and display insights.
