import streamlit as st
from ai71 import AI71
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve API key from environment variables
AI71_API_KEY = os.getenv("AI71_API_KEY")

# Set up the AI71 client
client = AI71(AI71_API_KEY)

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title(":grey[Dr.] :blue[*AI*] 🩺")
st.subheader(":grey[General Physician] 👨‍⚕️")

# Collect user inputs
symptoms = st.text_input("Please describe your symptoms:")
duration = st.number_input("How long have you been experiencing these symptoms? (in days)", min_value=0, step=1)
medications = st.text_input("Are you currently taking any medications?")
medical_history = st.text_input("Please provide any relevant medical history:")

# Initialize session state for messages and chat started flag
if "general_messages" not in st.session_state:
    st.session_state.general_messages = []
if "chat_started" not in st.session_state:
    st.session_state.chat_started = False

# Function to get AI response
def get_response(user_input):
    response_content = ""
    for chunk in client.chat.completions.create(
        messages=st.session_state.general_messages + [{"role": "user", "content": user_input}],
        model="tiiuae/falcon-180B-chat",
        stream=True,
    ):
        delta_content = chunk.choices[0].delta.content
        if delta_content:
            response_content += delta_content
    return response_content

# Display chat messages (excluding system messages)
for message in st.session_state.general_messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Chat input for user questions
user_input = st.chat_input("Ask a question about your health concern")

if user_input:
    if not st.session_state.chat_started:
        # Initialize the chat with user's information
        system_message = f"""You are an expert General Physician. 
        Your role is to provide a medical consultation based on the 
        following patient information: Symptoms - {symptoms}, Duration - {duration} days, Medications - {medications}, 
        Medical History - {medical_history}. Please provide a detailed medical consultation and possible treatment options.
        your response should follow this sequence.
        -. Provide possible medical issues as per the provided symptoms and other detail.
        -. how to cure this medical problem, this should include some tips regarding diet and exercise.
        -. now mention which medicines can be taken to cure this medical issue.
        -. provide some web links that support your response.
        """
        
        st.session_state.general_messages.append({"role": "system", "content": system_message})
        st.session_state.chat_started = True
    
    # Add user message to chat history and display it
    st.session_state.general_messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    
    # Get and display AI response
    response = get_response(user_input)
    st.session_state.general_messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
    
    # Rerun the app to update the chat history display
    st.rerun()