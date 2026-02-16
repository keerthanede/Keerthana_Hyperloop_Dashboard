# Hyperloop Control Dashboard

A streamlit app to monitor Hyperloop pods
This app provides a centralized dashboard for engineers and operators to track pod performance, monitor environmental conditions, compare pod parameters, and get energy optimization tips.

---
**Features:**  

### 1. Pod Status Dashboard
- Displays all pods with key parameters:
  - **Speed (km/h)**  
  - **Battery (%)**  
  - **Operational Status** (`Operational`, `Maintenance`, `Docked`)
- Automatically updates with randomly generated data (or can be extended to real-time pod data).

### 2. Weather Updates & Alerts
- Shows current **temperature, wind speed, and conditions** at a given location.  
- Provides **automated safety alerts** based on weather conditions, including:
  - High wind warnings
  - Rain or storm alerts
  - Recommended operational speeds

### 3. Energy Optimization Tips
- Fetches **random energy-saving tips** from a public API.  
- Refreshes and provides new tips on clicking the button

### 4. Pod Comparison Tool
- Select **any two pods** and compare them. 
- Includes a warning if the same pod is selected twice.

---

**How to run:**  
1. Install dependencies: `pip install -r requirements.txt`  
2. Run the app: `streamlit run dashboard.py`  


**Images & assets:**  
- `Avishkar_logo.png` included

**Project structure**
GUI APPLICATION/
│
├─ dashboard.py         # Main Streamlit app
├─ requirements.txt     # Python dependencies
├─ README.md            # This file

└─ Avishkar_logo.png    # Logo used in the sidebar
