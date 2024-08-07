import streamlit as st
from ai71 import AI71
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve API key from environment variables
AI71_API_KEY = os.getenv("AI71_API_KEY")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Set up the AI71 client
client = AI71(AI71_API_KEY)

st.title(":grey[Dr.] :blue[*AI*] 🩺")
st.subheader(":grey[Exercise Planner] 🏋️")

seq_of_response = ""
# Collect user inputs
gender = st.selectbox("Please enter your Gender", ["Male", "Female"])
age = st.number_input("Please enter your age", min_value=0, max_value=120, step=1)
weight = st.number_input("Please enter your Weight in Kg", min_value=0.0, max_value=300.0, step=0.1)
height = st.number_input("Please enter your Height in cm", min_value=0.0, max_value=300.0, step=0.1)
fitness_level = st.selectbox("What's your current fitness level?", ["Beginner", "Intermediate", "Advanced"])
fitness_goals = st.text_input("What are your fitness goals? (e.g., weight loss, muscle gain, improved endurance)")
med_conditions = st.text_input("Any medical conditions or injuries to consider?")

# Initialize session state for messages if not already initialized
if "exercise_messages" not in st.session_state:
    st.session_state.exercise_messages = []

# Function to get AI response
def get_response(user_input):
    st.session_state.exercise_messages.append({"role": "user", "content": user_input})
    response_content = ""
    for chunk in client.chat.completions.create(
        messages=st.session_state.exercise_messages,
        model="tiiuae/falcon-180B-chat",
        stream=True,
    ):
        delta_content = chunk.choices[0].delta.content
        if delta_content:
            response_content += delta_content
    st.session_state.exercise_messages.append({"role": "assistant", "content": response_content})
    return response_content

# Button to generate exercise plan
if st.button("Generate Exercise Plan"):
    system_message = (f"""
    You are an Expert Exercise Planner.
    Your role is to provide a personalized exercise plan for a {gender} 
    of age {age} years, weighing {weight} kg and {height} cm tall. 
    This person's current fitness level is {fitness_level}, 
    with fitness goals of {fitness_goals}. They have the following medical conditions or injuries to consider: {med_conditions}. 
    Now provide a precise and well-defined exercise plan for this person. Remember to consider their fitness level, goals, and any medical conditions.
    """)
    
    st.session_state.exercise_messages = [{"role": "system", "content": system_message}]

    seq_of_response = (f"""the sequence of response should be in this order:
                            1. provide him a brief introduction on what exercise can he consider doing depending on his age, weight and fitness goal, which he has just provided.
                            2. Provide him a detail exercise plan which should contain the type of exercise and the time to which he should do that exercise, 
                            also mention which time is suitable for doing this exercise.
                            3. you must also provide some general tips regarding the daily schedule for example you can mention him how much time should he sleep and how long should he walk or workout. and you can also suggest him the he should take walk or ride bicycles instead or motor vwhicles for commutation.
                            4. You can provide some web links which supports your response also.
                            5. make sure that the user is comfortable with your response, you are not too harsh or too stich while responding to his querries.""")
    
    response = get_response(f"""Please provide a personalized exercise plan based on the information given.
                            in this sequence {seq_of_response}
                            """)
    st.chat_message("assistant").write(response)



# Chat input for follow-up questions
user_query = st.chat_input("Ask a follow-up question about your exercise plan")
if user_query:
    st.chat_message("assistant").write(response)
    st.chat_message("user").write(user_query)
    user_input = f"""Following your response that you have already provided, the user has asked this: {user_query}.
                     Now be mindful and generate a response to their query, keeping in mind the flow of your response which is {seq_of_response}"""
    response = get_response(user_input)
    st.chat_message("assistant").write(response)