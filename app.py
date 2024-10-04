import streamlit as st

# Set page configuration
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="centered")

# CSS styling with responsive design
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
        margin: 1em auto;
        width: 100%;
        padding: 0 10px;
    }
    
    .title {
        font-family: 'Pacifico', cursive;
        font-size: calc(2em + 2vw); /* Responsive font size */
        text-align: center;
        background: linear-gradient(45deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 2px 4px rgba(255, 215, 0, 0.5));
        margin-bottom: 0.2em;
        width: 100%;
        overflow-wrap: break-word;
        word-wrap: break-word;
        hyphens: auto;
    }
    
    /* Title wrapper for better mobile display */
    .title-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }
    
    .title-text {
        display: inline-block;
    }
    
    .title-emoji {
        font-size: 0.8em;
        margin: 0 5px;
        display: inline-block;
    }
    
    .subtitle {
        font-family: 'Arial', sans-serif;
        font-size: calc(1em + 0.5vw);
        color: #FFA500;
        text-align: center;
        margin-top: 10px;
        padding: 0 10px;
    }
    
    .message {
        color: #FFD700;
        font-family: 'Arial', sans-serif;
        font-size: calc(1.2em + 0.5vw);
        text-align: center;
        margin: 1.5em auto;
        padding: 15px;
        max-width: 90%;
        background: rgba(255, 215, 0, 0.1);
        border-radius: 20px;
        border: 2px solid rgba(255, 215, 0, 0.3);
    }
    
    .stVideo {
        margin: 1.5em auto;
        border-radius: 15px;
        border: 2px solid #FFD700;
    }

    /* Media queries for better responsiveness */
    @media screen and (max-width: 480px) {
        .title {
            font-size: calc(1.8em + 2vw);
        }
        .title-emoji {
            font-size: 0.7em;
        }
        .message {
            padding: 10px;
        }
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Responsive title
st.markdown("""
    <div class="title-container">
        <div class="title-wrapper">
            <div class="title">
                <span class="title-emoji">🌟</span>
                <span class="title-text">Happy Birthday, Anvi!</span>
                <span class="title-emoji">🌟</span>
            </div>
        </div>
        <div class="subtitle">✨ May your day be magical! ✨</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="message">Here\'s to a beautiful day filled with love and joy! 🎉🎂</div>', unsafe_allow_html=True)

# Video player
try:
    with open("birthday_video.mp4", 'rb') as video_file:
        video_bytes = video_file.read()
    st.video(video_bytes)
except FileNotFoundError:
    st.error("Video file not found. Please ensure 'birthday_video.mp4' exists in the same directory.")

# Celebrate with balloons
st.balloons()