# I. IMPORTING LIBRARIES:

import pandas as pd
import streamlit as st
import random
import requests

# II. GLOBAL DESIGNS:
# One-time style for all buttons: 
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #ffffff;
        color: #31333F;
        border-radius: 12px;
        padding: 0.6em 1.2em;
        border: none;
        box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.08);
        transition: all 0.2s ease-in-out;
        font-size: 16px;
    }

    div.stButton > button:hover {
        box-shadow: 2px 6px 14px rgba(0, 0, 0, 0.15);
        transform: scale(1.03);
        background-color: #f9f9ff;
        color: #111111;
    }
    </style>
""", unsafe_allow_html=True)

# Text area for short entries:
# 💅 Style override for text input (city box)
st.markdown("""
<style>
/* Override the Streamlit error input style */
div[data-baseweb="input"] > div {
    border-radius: 10px !important;
    background-color: #f1efeb !important;
}

/* Focused style */
div[data-baseweb="input"]:focus-within {
    border: 1px solid #f1efeb !important;
    box-shadow: 0 0 0 2px rgba(216, 196, 230, 0.3) !important;
}

/* Optional: change actual text input inside */
input {
    background-color: transparent !important;
    color: #4b4b4b !important;
}
</style>
""", unsafe_allow_html=True)

# Text area for longer entries:
st.markdown("""
<style>
/* Match the journal box to your city input */
textarea {
    background-color: #f1efeb !important;
    color: #4b4b4b !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 1em !important;
    font-size: 15px !important;
    font-family: 'Segoe UI', sans-serif !important;
    resize: none !important;
}

/* Override pink focus from Streamlit wrapper */
div.stTextArea > div > div > textarea:focus {
    border: none !important;
    outline: none !important;
    box-shadow: none !important;
}

/* 🩷 Fix the outer border container that causes pink */
div.stTextArea > div {
    border: 1px solid #f1efeb !important;
    border-radius: 10px !important;
    box-shadow: none !important;
    transition: border 0.3s ease;
}

/* On focus: soft gray, no glow */
div.stTextArea > div:focus-within {
    border: 1px solid #e3e0dc !important;
    box-shadow: none !important;
}
</style>
""", unsafe_allow_html=True)

# III. CODING THE PAGES:

#  0. PAGE NAVIGATION:
 #---------------------

tab_name = ["Nugget notes", "To do", "Mood tracker", "Reminder", "Recommendations"]
if "selected_tab" not in st.session_state:
    st.session_state["selected_tab"] = "Nugget notes"

# 👩‍💻 Create navigation bar:
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    if st.button("🧸 Nugget notes"):
        st.session_state["selected_tab"] = "Nugget notes"
with c2:
    if st.button("🧃 Get things done"):
        st.session_state["selected_tab"] = "To do"
with c3:
    if st.button("🌦️ Your mood now?"):
        st.session_state["selected_tab"] = "Mood tracker"
with c4:
    if st.button("🍭 Don't forget to"):
        st.session_state["selected_tab"] = "Reminder"
with c5:
    if st.button("🐇 Bunny's top three"):
        st.session_state["selected_tab"] = "Recommendations"

# 1. NUGGET NOTES TAB:
# ----------------------

if st.session_state["selected_tab"] == "Nugget notes":
    # Cute cat header gif:
    st.markdown("""
        <div style="text-align: center;">
            <img src="https://cliply.co/wp-content/uploads/2021/09/142109670_SAD_CAT_400.gif" 
                 style="width:180px; margin-top: 0px; margin-bottom: -50px;" />
        </div>
    """, unsafe_allow_html=True)

    # 🌸 Page title:
    st.title("Get a taste of...")

    # 📖 Load quotes from Excel:
    quotes = pd.read_excel("GF App_Quotes.xlsx")
    reminder = pd.read_excel("GF App_Notes.xlsx")

    # ✨ Display quotes in soft pastel box:
    def show_quote(text):
        st.markdown(
            f"""
            <div style="
                background-color: #e1f6f2;
                padding: 1rem;
                border-radius: 10px;
                font-size: 17px;
                font-weight: 500;
                color: #333333;
                margin-top: 15px;">
                {text}
            </div>
            """,
            unsafe_allow_html=True
        )

    # 📚 Convert columns to lists:
    philosophy_quotes = quotes["Philosophy"].dropna().tolist()
    fortunecookies_quotes = quotes["FortuneCookies"].dropna().tolist()
    horoscope_quotes = quotes["Horoscopes"].dropna().tolist()

    # 🍪 Quote category buttons:
    col1, col2, col3 = st.columns(3)
    with col1:
        button_1 = st.button("🧠 brain crumbs")
    with col2:
        button_2 = st.button("🍪 fortune cookies")
    with col3:
        button_3 = st.button("🔮 foresnacks")

    # 🧁 Show selected quote:
    if button_1:
        show_quote(random.choice(philosophy_quotes))
    if button_2:
        show_quote(random.choice(fortunecookies_quotes))
    if button_3:
        show_quote(random.choice(horoscope_quotes))

    # 🌼 Load notes from Excel:
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    st.markdown("🌼 Dessert is a nugget note ~")

    reminder_note = reminder["Note"].dropna().tolist()
    note = random.choice(reminder_note)

    # 🍃 Display note in pastel box:
    st.markdown(f"""
        <div style="
            background-color: #e1f6f2;
            padding: 12px;
            border-radius: 10px;
            font-size: 16px;
            color: #333333;">
            {note}
        </div>
    """, unsafe_allow_html=True)


# 2. MOOD TRACKER TAB:
# ----------------------
elif st.session_state["selected_tab"] == "Mood tracker":
    st.markdown("""
        <div style="text-align: center; margin-top: 30px;">
            <img src="https://media4.giphy.com/media/STfyJRwrheKrftQweJ/200w.gif?cid=6c09b952r1wrcsujebaqkouzp8tqhx2fqgo0xma7p2m651fm&ep=v1_stickers_search&rid=200w.gif&ct=s"
                 style="width:140px; margin-bottom:-10px;" />
        </div>
    """, unsafe_allow_html=True)

    st.title("Checking in on you")

    city = st.text_input("*first, where are you today babe?*", placeholder="Enter your city...")

    # ✅ ONLY run if city is entered
    if city.strip():
        import requests

        def get_weather(city_name, api_key):
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": city_name,
                "appid": api_key,
                "units": "metric"
            }
            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                weather_main = data["weather"][0]["main"]
                temperature = data["main"]["temp"]
                return weather_main, temperature
            else:
                return "Unavailable", "N/A"

        weather, temp = get_weather(city, "58f8cc3790811291589070baa4a09dfe")

        if weather:
            # 🌤 Set icon and message
            weather_icons = {
                "Clear": "☀️", "Clouds": "☁️", "Rain": "🌧️", "Snow": "❄️",
                "Thunderstorm": "⛈️", "Drizzle": "🌦️", "Mist": "🌫️"
            }
            icon = weather_icons.get(weather, "🌡️")

            if "Rain" in weather:
                msg = "It’s rainy — stay cozy and bring an umbrella ☔"
            elif "Clear" in weather:
                msg = "Sunny day — perfect time for a walk 🌿"
            elif "Clouds" in weather:
                msg = "Cloudy skies call for journaling and coffee ☕"
            elif "Snow" in weather:
                msg = "Bundle up! It’s a snowy kind of softness ❄️"
            else:
                msg = "The sky is doing its thing — so should you 💪"

            # 📦 Display weather card
            st.markdown(f"""
            <div style="
                background-color: #fdfdfd;
                border: 1px solid #e6e6e6;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
                margin-top: 20px;
                font-family: 'Segoe UI', sans-serif;
            ">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <div style="font-size: 50px;">{icon}</div>
                    <div style="text-align: right;">
                        <div style="font-size: 28px; font-weight: 600;">{temp}°C</div>
                        <div style="font-size: 16px; color: #666;"><strong>{weather}</strong> in <strong>{city}</strong></div>
                    </div>
                </div>
                <div style="margin-top: 15px; font-size: 16px; color: #444;">
                    {msg}
                </div>
            </div>
            """, unsafe_allow_html=True)

        else: 
            st.error("I tried checking the sky, but something went poof 😔☁️ Maybe try another city? Or give the Wi-Fi a little hug 💗📶")
        
         # --- Spacer ---
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # Build a journaling box and mood detection system:

    # Hugging Face Emotion Detection
    def detect_emotion(text):
        api_token = st.secrets["huggingface"]["api_token"]
        API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
        headers = {"Authorization": f"Bearer {api_token}"}
        response = requests.post(API_URL, headers=headers, json={"inputs": text})

        if response.status_code == 200:
            data = response.json()
            return data[0][0]["label"]
        else:
            return "neutral"

# 📝 Mood Journal Box
    entry = st.text_area("*now, how are you feeling?*", placeholder="Journal down your thoughts...", height = 150)

# 🎯 Detect mood and give response
    if st.button("📡 Check your mood"):
        if entry.strip():
            emotion = detect_emotion(entry)

        #   🎀 Cute response bank:
        responses = {
            "joy": "You're glowing — spread that sunshine 🌞",
            "sadness": "Sending you my hugs and a soft blanket 🧣",
            "anger": "Deep breath. You’re allowed to feel this way 💢 ",
            "fear": "It’s okay to be anxious — you’re still brave 🌙",
            "surprise": "Something is shifting — lean into the magic ✨",
            "disgust": "Ooooh let's clean that bad vibes 🌊",
            "neutral": "A quiet mood has its kind of beauty ☁️"
        }

        st.markdown(f"###### Maybe it is *{emotion}* (・・？)")
        st.markdown(f"{responses.get(emotion, '💗 You’re doing great. Keep going.')}")

    else:
        st.warning("Tell me a little something 💬")

# 3. TO DO LIST TAB:
elif st.session_state["selected_tab"] == "To do":
    st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <img src="https://media2.giphy.com/media/ZuorNU99NFvIrh8V10/giphy.gif?cid=6c09b952o4jolpxpt6f3svt2ivjt1o8l0ionskldkjc5que6&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=s" 
                 style="width:155px; margin-bottom: 5px;" />
        </div>
    """, unsafe_allow_html=True)

    st.title("Daily dose of tasks")
    st.markdown("🍬 Finish all 5 to unlock a surprise ~")

    # 🛠️ Setup: Init session state
    if "tasks" not in st.session_state:
        st.session_state["tasks"] = [""] * 5
    if "completed" not in st.session_state:
        st.session_state["completed"] = [False] * 5

    # 🪄 Update task function
    def update_task(index):
        st.session_state["tasks"][index] = st.session_state.get(f"task_input_{index}", "")

    # 📝 Task loop
    for i in range(5):
        task = st.session_state["tasks"][i]
        completed = st.session_state["completed"][i]

        if task.strip():
            # ✅ Show checkbox if task exists
            cols = st.columns([0.1, 0.9])
            with cols[0]:
                st.session_state["completed"][i] = st.checkbox(
                    "", value=completed, key=f"checkbox_{i}"
                )
            with cols[1]:
                st.markdown(f"""
                    <div style='
                        background-color: #ffffff;
                        padding: 10px;
                        border-radius: 10px;
                        margin-bottom: 10px;
                        color: {"#aaa" if st.session_state["completed"][i] else "#333"};
                        text-decoration: {"line-through" if st.session_state["completed"][i] else "none"};
                        border: 1px solid #eee;
                    '>
                        {task}
                    </div>
                """, unsafe_allow_html=True)
        else:
            # 🖊️ Show text input until task is typed
            st.text_input(
                f"Task {i+1}",
                value=task,
                placeholder="Type something...",
                key=f"task_input_{i}",
                on_change=update_task,
                args=(i,)
            )

    # 🌿 Count how many are done
    completed_count = sum(st.session_state["completed"])
    progress_percent = int((completed_count / 5) * 100)

    # 🌼 Show progress tracker label
    st.markdown(f"**{completed_count}/5 tasks done 🐾**")

    # 🌈 Custom pastel progress bar
    st.markdown(f"""
    <div style='
        width: 100%;
        background-color: #fff;
        border: 2px solid #f9c4d2;
        border-radius: 12px;
        padding: 4px;
        margin-top: 8px;
        margin-bottom: 20px;
        position: relative;
    '>
        <div style='
            height: 20px;
            width: {progress_percent}%;
            background: linear-gradient(90deg, #fcbad3, #f8c3e0, #c6d9f1, #d4f1f4);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            font-size: 13px;
        '>{progress_percent}%</div>
    </div>
    """, unsafe_allow_html=True)

    # 💌 Encouraging messages
    if completed_count == 0:
        st.info("Let’s start with something tiny 🎀")
    elif completed_count == 1:
        st.success("One bunny hop! Keep going 🐇")
    elif completed_count == 2:
        st.success("Two tasks done — you’re halfway to cuteness overload 🍓")
    elif completed_count == 3:
        st.warning("Three down! You’re doing this like a pro 🌈")
    elif completed_count == 4:
        st.warning("Almost there... One last push to unlock my gift 🌷")
    elif completed_count == 5:
        st.success("OMG you did it all 🎉")
        st.balloons()
    
        # Load the rewards now:
        rewards = pd.read_excel("GF App_Rewards.xlsx")
        reward_links = rewards["Link"].dropna().tolist()
        chosen_gift = random.choice(reward_links)

        # Show gift if all tasks are done:
        st.markdown(f"""
            <div style='text-align: center;'>
                <img src="{chosen_gift}" width="400">
                <div style='font-size: 16px; margin-top: 8px;'></div>
            </div>
            """, unsafe_allow_html=True)
        
    
    # 4. REMINDER PAGE:
# ---------------------
elif st.session_state["selected_tab"] == "Reminder":
    st.markdown("""
        <div style="text-align: center; margin-top: 10px;">
            <img src="https://media0.giphy.com/media/Odusl2RwScRtFvIYJB/giphy.gif?cid=6c09b952bbi9ams8veqjnrxczvvj9wjl5nsj4x97gyq1toui&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=ts" 
                 style="width:270px; margin-bottom: -20px;" />
        </div>
    """, unsafe_allow_html=True)
    
    import random

    st.title("Have you...")

    reminders = [
        {"text": "drank enough water 💧?", "gif": "https://img.clipart-library.com/2/clip-transparent-water-gif/clip-transparent-water-gif-34.gif"},
        {"text": "eaten a proper meal 🍽️?", "gif": "https://media4.giphy.com/media/xTiTnssXv8JwMawAX6/giphy.gif?cid=6c09b952vewcgbarnclhzf508bl3zimu2qnlboakifhdf1va&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=g"},
        {"text": "done your daily stretch 🧘?", "gif": "https://media3.giphy.com/media/CaiMaSrBdRAK37R2wF/giphy.gif?cid=6c09b952psasszeafwle63agik9f244u5evr1kwcnbwbck4f&ep=v1_stickers_search&rid=giphy.gif&ct=s"},
        {"text": "told me that you love me 💌?", "gif": "https://media.tenor.com/CH-pU6ldmjcAAAAM/sending-love.gif"},
        {"text": "taken a deep breath 🌬️?", "gif": "https://art.ngfiles.com/images/939000/939910_clockwork787_eskimo-breathing-gif.gif?f1561273910"},
        {"text": "slept for 8 hours 🌙?", "gif": "https://i.pinimg.com/originals/f4/a8/8d/f4a88d30e04e9c4eb7618028cf7bd26a.gif"},
        {"text": "eaten a good fruit 🍎", "gif": "https://i.pinimg.com/originals/a9/7d/bf/a97dbf78f7e1e46bead0df6944b5652d.gif"},
        {"text": "done your skincare routine 🧴?", "gif": "https://i.pinimg.com/originals/8d/28/21/8d2821c77a4594dd2b38a012a0482cf1.gif"},
        {"text": "gone out and touched some grass 🌱?", "gif": "https://custom-doodle.com/wp-content/uploads/doodle/auto-draft/cute-frog-hiking-doodle.gif"},
        {"text": "cleaned your space and mind 🧺?", "gif": "https://i.pinimg.com/originals/40/99/46/40994625020097e170dfabc716f22f6e.gif"},

    ]

    chosen = random.choice(reminders)

    st.image(chosen["gif"], width=200)
    st.subheader(chosen["text"])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ I did!"):
            st.success("💖 Bunny is proud of you!")
    with col2:
        if st.button("❌ Not yet..."):
            st.warning("😤 Bunny is judging you... go do it.")
            
# FINAL PAGE:
elif st.session_state["selected_tab"] == "Recommendations":
    import pandas as pd
    import random

    # 🐇 Header gif
    st.markdown("""
        <div style="text-align: center;">
            <img src="https://i.pinimg.com/originals/55/9f/77/559f77e1ec311c55c9086f8f06b0e588.gif" 
                 style="width:160px; margin-top: -19px; margin-bottom: -10px;" />
        </div>
    """, unsafe_allow_html=True)

    # 🌸 Page title
    st.title("Mr. Bunny’s basket has...")

    # 📖 Load recs from Excel
    df = pd.read_excel("GF App_Recs.xlsx")
    book_recs = df["Book"].dropna().tolist()
    movie_recs = df["Movie"].dropna().tolist()
    song_recs = df["Song"].dropna().tolist()

    # ✨ Display recommendation in pastel box
    def show_recs(title, items):
        st.markdown(
            f"""
            <div style="
                background-color: #fef6f9;
                padding: 1rem;
                border-radius: 10px;
                font-size: 16px;
                font-weight: 500;
                color: #333333;
                margin-top: 15px;
                border: 1px solid #f8c3d2;">
                <b>{title}</b><br><br>
                1. {items[0]}<br>
                2. {items[1]}<br>
                3. {items[2]}
            </div>
            """,
            unsafe_allow_html=True
        )

    # 🍪 Buttons for 3 categories
    col1, col2, col3 = st.columns(3)
    with col1:
        button_books = st.button("📚 some books")
    with col2:
        button_movies = st.button("🎬 some movies")
    with col3:
        button_songs = st.button("🎧 some songs")

    # ✨ Show selected category
    if button_books:
        show_recs("Today’s bunny book stack 📚", random.sample(book_recs, 3))
    elif button_movies:
        show_recs("It's time for a movie night 🎬", random.sample(movie_recs, 3))
    elif button_songs:
        show_recs("Vibe check: enjoy a cool playlist 🎧", random.sample(song_recs, 3))


