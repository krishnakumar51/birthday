import streamlit as st

# Set page configuration
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="centered")

# CSS styling with lovely, attractive design
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1c1c1c;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    .title-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 2em auto;
        max-width: 100%;
    }
    
    .title {
        font-family: 'Pacifico', cursive;
        font-size: 4.2em;
        text-align: center;
        white-space: nowrap;
        background: linear-gradient(45deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 2px 4px rgba(255, 215, 0, 0.5));
        margin-bottom: 0.2em;
    }
    
    .title-emoji {
        font-size: 1.5em;
        margin: 0 10px;
    }
    
    .subtitle {
        font-family: 'Arial', sans-serif;
        font-size: 1.5em;
        color: #FFA500;
        text-align: center;
        margin-top: 10px;
    }
    
    .message {
        color: #FFD700;
        font-family: 'Arial', sans-serif;
        font-size: 1.8em;
        text-align: center;
        margin: 1.5em auto;
        padding: 20px;
        max-width: 800px;
        background: rgba(255, 215, 0, 0.1);
        border-radius: 20px;
        border: 2px solid rgba(255, 215, 0, 0.3);
    }
    
    .stVideo {
        margin: 2em auto;
        border-radius: 15px;
        border: 2px solid #FFD700;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Lovely, attractive title
st.markdown("""
    <div class="title-container">
        <div class="title">
            <span class="title-emoji">🌟</span>
            Happy Birthday, Anvi!
            <span class="title-emoji">🌟</span>
        </div>
        <div class="subtitle">✨ May your day be as special as you are! ✨</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="message">Here\'s to a beautiful day filled with love, laughter, and all the joy you deserve! 🎉🎂</div>', unsafe_allow_html=True)

# Video player
try:
    with open("birthday_video.mp4", 'rb') as video_file:
        video_bytes = video_file.read()
    st.video(video_bytes)
except FileNotFoundError:
    st.error("Video file not found. Please ensure 'birthday_video.mp4' exists in the same directory.")

# Celebrate with balloons
st.balloons()