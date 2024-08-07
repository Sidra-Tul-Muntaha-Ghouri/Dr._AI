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
st.subheader(":grey[Diet Planner] 🍎")

# Collect user inputs
gender = st.selectbox("Please enter your Gender", ["Male", "Female"])
age = st.number_input("Please enter your age", min_value=0, max_value=120, step=1)
weight = st.number_input("Please enter your Weight in Kg", min_value=0.0, max_value=300.0, step=0.1)
height = st.number_input("Please enter your Height in feet", min_value=0.0, max_value=300.0, step=0.1)
dietary_pref = st.text_input("Your dietary preferences (e.g., vegetarian, non-vegetarian, vegan, etc.)")
Med_conditions = st.text_input("Any medical conditions or allergies")


# Function to get AI response
def get_response(messages):
    response_content = ""
    for chunk in client.chat.completions.create(
        messages=messages,
        model="tiiuae/falcon-180B-chat",
        stream=True,
    ):
        delta_content = chunk.choices[0].delta.content
        if delta_content:
            response_content += delta_content
    return response_content

# Button to generate diet plan
if st.button("Generate Diet Plan"):
    system_message = f"""You are an Expert Diet Planner. Your role is to provide a personalized diet plan for a {gender} 
    of age {age} years having weight of {weight} kg. This person prefers {dietary_pref} and has these medical issues: 
    {Med_conditions}. Now provide a detailed and well-defined diet plan for this person. Remember you have everything 
    you need to plan a balanced diet."""
    
    user_message = f"""
    Please provide a personalized diet plan based on the information given.
    The sequence of response should be like:
    - First of all, tell the user their BMI score as per their provided age: {age}, weight: {weight} and height: {height}
    - Second, mention what they should consider taking in their diet the most at their age, and what will be the advantages of taking these components in their diet.
    - Now provide a complete meal plan depending on what you have suggested earlier and on what they said they would prefer taking in meals.
    - You can also provide some delicious and healthy recipes.
    - You must also provide some web links regarding the recipes and about some healthy diet plans.
    """
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    
    response = get_response(messages)
    st.write(response)

# Initialize session state for chat messages if not already initialized
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# Display chat messages
for message in st.session_state.chat_messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input for follow-up questions
user_input = st.chat_input("Ask a follow-up question about your diet plan")

system_message = f"""You are an Expert Diet Planner. Your role is to provide a personalized diet plan for a {gender} 
    of age {age} years having weight of {weight} kg. This person prefers {dietary_pref} and has these medical issues: 
    {Med_conditions}. Now provide a detailed and well-defined diet plan for this person. Remember you have everything 
    you need to plan a balanced diet."""
seq = (f"""The sequence of response should be like:
    - First analze what the user is rying to ask.
    - Second, provide a detailed response, mention advantages and disadvantages also.
    - consider being as elpful as you can be
    - You must also provide some web links that supports your response.""")
prompt = f"""Following your response that you have already provided, the user has asked this: {user_input}.
                     Now be mindful and generate a response to their query, keeping in mind the flow of your response which is {seq}"""
    
if user_input:
    st.session_state.chat_messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(user_input)
    
    messages = [{"role": "system", "content": system_message}] + st.session_state.chat_messages
    response = get_response(messages)
    
    st.session_state.chat_messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)


