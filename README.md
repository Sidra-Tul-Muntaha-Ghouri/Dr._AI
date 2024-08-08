# Dr. AI 🩺

## About the Project

Dr. AI is an innovative virtual healthcare assistant developed for the Falcon Hackathon. This project aims to provide personalized health-related services using advanced AI technology, specifically leveraging the Falcon-180B-chat model.

## Features

Dr. AI offers three main services:

1. **Diet Planner** 🍎
   - Personalized diet plans based on user input
   - Consideration of dietary preferences and health conditions

2. **Exercise Planner** 🏋️
   - Customized exercise routines
   - Adaptable to different fitness levels and goals

3. **General Physician** 👨‍⚕️
   - Virtual medical consultations
   - Symptom analysis and preliminary advice

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Model**: Falcon-180B-chat (via AI71 API)
- **Environment Management**: dotenv

## Project Demo
[![Watch Demo](https://img.youtube.com/vi/4xdpSnlEjag/0.jpg)](https://www.youtube.com/watch?v=4xdpSnlEjag)

## Project Structure

```
Dr.AI/
│
├── .streamlit/                                  # Streamlit configuration files
├── pages/                                       # Additional pages for Streamlit app
│   ├── Diet_Planner.py
│   ├── Exercise_Planner.py
│   └── General_Physician.py
├── .env                                         # Environment configuration file
├── .gitignore                                   # Git ignore file
├── Home.py                                      # Home page of the Streamlit app
├── requirements.txt                             # Python dependencies
└── styles.css                                   # Custom styles for the app
```
## Setup and Installation

1. Clone the repository:
```
git clone https://github.com/your-username/Dr.AI.git
cd Dr.AI
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```
3. Install the required packages:
```
pip install -r requirements.txt
```
4. Set up your `.env` file with your AI71 API key:
```
AI71_API_KEY=your_api_key_here
```
5. Run the Streamlit app:
```
streamlit run Home.py
```
## Usage

1. Start the application and navigate to the provided local URL.
2. Choose the desired service from the sidebar (Diet Planner, Exercise Planner, or General Physician).
3. Input your personal information and health-related details as prompted.
4. Interact with the AI assistant through the chat interface to receive personalized advice and plans.

## Contributing

We welcome contributions to Dr. AI! Please feel free to submit issues, fork the repository and send pull requests!

## License

This project is licensed under the MIT License.

## Acknowledgments

- This project was created for the Falcon Hackathon
- Special thanks to AI71 for providing access to the Falcon-180B-chat model

## Contact

Sidra Tul Muntaha - sidratulmuntaha135@gmail.com

Project Link: [https://github.com/your-username/Dr.AI](https://github.com/Sidra-Tul-Muntaha-Ghouri/Dr._AI)



Try out @ https://doctorai135.streamlit.app/
