import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve API key from environment variables
AI71_API_KEY = os.getenv("AI71_API_KEY")

st.set_page_config(page_title="Dr. AI", page_icon="🩺")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.title(":grey[Dr.] :blue[*AI*] 🩺")    
    
    st.write("""Hi there! <br>I'm **Dr. AI**, a virtual healthcare assistant.<br>
    I'm here to help you with various aspects of your health and wellness journey.<br> 
    Whether you're looking for help with planning a balanced diet, creating a 
    personalized exercise routine, or addressing any general health concerns, 
    I'm here to provide guidance and assistance every step of the way.<br><br>
    Please select the service you are looking assistance with:
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Diet Planner 🍎", use_container_width=True):
            st.switch_page("pages/Diet_Planner.py")

    with col2:
        if st.button("Exercise Planner 🏋️", use_container_width=True):
            st.switch_page("pages/Excercise_Planner.py")

    with col3:
        if st.button("General Physician 👨‍⚕️", use_container_width=True):
            st.switch_page("pages/General_Physician.py")

if __name__ == "__main__":
    main()
