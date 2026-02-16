import streamlit as st
import pandas as pd
import random
import requests
import json
import time

st.set_page_config(layout="wide")

#main ui
st.markdown(
    "<h2 style='text-align: center;'>HYPERLOOP CONTROL MONITOR</h2>",
     unsafe_allow_html=True
    )
st.space (size="small")


#function to generate pod data (random)
def generate_pod_data(name):
    return {
        "Name": name,
        "📡Speed": random.randint(600, 900),
        "🔋Battery": random.randint(40, 100),
        "🚄Status": random.choice(["Operational", "Maintenance", "Docked"])
    }

#function to generate weather data for different locations using latitude and logitude coordinates
def get_weather(lat, lon):
     api="8d57ac8f60ad2b8295b60af59a1be051"
     URL= "https://api.openweathermap.org/data/2.5/weather"
   
     params={ 
      "lon":lon,
      "lat":lat,
      "appid": "8d57ac8f60ad2b8295b60af59a1be051",
      "units":"metric"
     }
     response = requests.get(URL,params=params)
   
     if response.status_code==200:
        data=response.json()
        return {
            "Temp" :data["main"]["temp"],
            "Wind_speed" :data["wind"]["speed"],
            "Location" :data["name"],
            "Description" : data["weather"][0]["description"], 
        }
     else:
       return None

#function to generate random energy facts from the json placeholder api
def get_facts():
      url= "https://jsonplaceholder.typicode.com/posts" 
      energy_facts= requests.get(url)

      if energy_facts.status_code==200:
        posts=energy_facts.json()
        tip = random.choice(posts)
        return tip["body"]
      else:
        return "No facts available"


     
#SIDEBAR
with st.sidebar:
  
  st.image("./Avishkar_logo.png")
  st.title(" 👋 Welcome Mr.John!")
  st.header("DASHBOARD")

  with st.container(border=True , width ="stretch"):
   Selected= st.radio (
      "Let's look what's in there",
      ["Pods","Comparison", "Live Tracker","Energy Facts" ],
    )

name = ["Avishkar 1", "Avishkar 2", "Avishkar 3", "Avishkar 4"]
pods = [generate_pod_data(n) for n in name]
data = pd.DataFrame(pods)
data.index = data.index + 1 
  
# Displaying weather conditions , pod details ,alerts on the screen on clicking pods option on the sidebar 

if Selected == "Pods":
    st.subheader("Pod Status")
    st.dataframe(data, use_container_width=True)



 #the weather updates container
    col1 , col2 = st.columns(2)

    with col1:
      c= st.container(border= True)
    with col2:
        alerts=st.container(border=True)
        alerts.subheader("Alerts⚠️")
    
    #display the weather updates on the screen
    c.subheader("Weather updates🌤️")   
    climate= get_weather(13.0674 ,80.2376 )
    if climate :
       with c.spinner("Please wait"):
         time.sleep(2)
       c.write (f"📍Location : {climate["Location"]} ")
       c.write(f"🌡️Temperature :{climate["Temp"]}°C")
       c.write(f"🌬️Wind Speed : {climate["Wind_speed"]}m/s")
       c.write(f"💧Conditions: {climate["Description"]}")   
    else:
       c.error("Request failed")

    
    #alerts based on weather
    if climate["Wind_speed"] >12:
      alerts.warning("It is dangerous, Please stop the operations")
    elif climate["Wind_speed"] >8:
      alerts.warning("The wind speed is High!- Reduce speed to 400 km/h.")
    elif climate["Wind_speed"] >5 :
      alerts.warning("Moderate wind - Reduce speed to 800 km/h.")
    elif "rain" in climate["Description"]:
      alerts.warning("Rainy conditions! Reduce speed to 700 km/h.")
    elif "storm" in climate["Description"]:
      alerts.warning("Stormy! Reduce speed to 300 km/h or stop operations.")
    else:
      alerts.success("Safe to operate at max speed")


# To display random energy facts for the 
elif Selected == "Energy Facts":

     st.subheader("ENERGY OPTIMISATION TIPS")
     Clicked= st.button("💡Tips")
      
     if Clicked:
        col1 , col2 = st.columns(2)

        with col1:
         Display_Facts = st.container(border= True)
         Facts= get_facts()
         Display_Facts.write(Facts)


 #to compare pods
elif Selected == "Comparison":  
     col1 , col2 , col3 = st.columns([1 ,0.2 ,1])
    
     with col1:
         pod1_name= st.selectbox(
                 "Select Pods to compare",
                 name,
                 key="pod1_",
                 )
     with col3:
         pod2_name= st.selectbox(
                 "Select Pods to compare",
                 name,
                 key="pod2_"
                 )
     with col2:
          st.markdown("**VS**")
     
     if pod1_name == pod2_name:
          st.warning("⚠️ Please select two different pods to compare!")
     
     






    

    
    








     

    




  






  




  

