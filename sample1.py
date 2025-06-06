import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  # Corrected import
import time
from PIL import Image

logo ="Windrush logo clipped1_redrawn BLUEE_v2 3.jpg"
logo_path = Image.open(logo) 
# Title
#st.title("Windrush Heritage Quiz")
col1,col2,col3 =st.columns(3)
with col2:
    st.write(logo_path)
st.markdown(
    "<h2 style='color: blue; text-align: center;'>Heritage Quiz</h1>",
    unsafe_allow_html=True
)

# Initialize session state for points and leaderboard
if "points" not in st.session_state:
    st.session_state.points = 0
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = [("Nick", 9, 2), ("Sarah", 7, 1), ("Jane", 12, 3)]

col1, col2 = st.columns(2)

with col1:
    # User input
    name = st.text_input("What is your name?")
    year = st.number_input("What year class are you in?", min_value=5, max_value=15, step=1)

with col2:
    # Always Display Leaderboard (Sorted)
    #st.write("### Current Leaderboard")
    st.markdown(
    "<h5 style='color: black; text-align: center;'>Current Leaders' board Quiz</h5>",
    unsafe_allow_html=True
)

    updated_df = pd.DataFrame(st.session_state.leaderboard, columns=['Name', 'Age', 'Points'])
    updated_df = updated_df.sort_values(by="Points", ascending=False)
    st.dataframe(updated_df)

# Quiz Questions
st.write("### Quiz Questions")

# Question 1
st.write("Who were the primary passengers aboard the Empire Windrush?")
options = [
    "Caribbean immigrants", 
    "British sailors", 
    "Both Caribbean immigrants and British sailors", 
    "None of the above"
]
selected_option = st.radio("Select the correct answer:", options, key="Windrush")

# Question 2
st.write("Name the two founders of the Windrush Foundation.")
options_2 = [
    "Mary Seacole and Lennox Lewis", 
    "Doreen Lawrence and Diane Abbott", 
    "Boris Johnson and Theresa May", 
    "Samuel B. King and Arthur Torrington"
]
selected_option_2 = st.radio("Select the correct answer:", options_2, key="Founders")

# Question 3
st.write("What was the name of the British Guyanese soldier who became an actor and singer, fought for Britain in WWII, and was captured by the Nazis?")
options_3 = [
    "Cy Grant", 
    "Winston Churchill", 
    "Private Ryan", 
    "None of the above"
]
selected_option_3 = st.radio("Select the correct answer:", options_3, key="CyGrant")

# Process quiz submission
if st.button("Submit Answer"):
    points = 0  # Reset points

    if selected_option == "Caribbean immigrants":
        st.success("Correct! Caribbean immigrants played a key role.")
        points += 1
    else:
        st.error("Incorrect.")

    if selected_option_2 == "Samuel B. King and Arthur Torrington":
        st.success("Correct! Samuel B. King & Arthur Torrington founded the Windrush Foundation.")
        points += 1
    else:
        st.error("Incorrect.")

    if selected_option_3 == "Cy Grant":
        st.success("Correct! Cy Grant was a WWII veteran and later became an actor and singer.")
        points += 1
    else:
        st.error("Incorrect.")

    st.session_state.points = points  # Store points in session state

    if name:  # Ensure name is entered
        st.session_state.leaderboard.append((name, year, points))

    # Display updated leaderboard
    st.write("### Updated Leaderboard")
    updated_df = pd.DataFrame(st.session_state.leaderboard, columns=['Name', 'Age', 'Points'])
    updated_df = updated_df.sort_values(by="Points", ascending=False)
    #st.dataframe(updated_df)

# Show Score Button
if name and st.session_state.points >= 0:
    if st.button("Show my score"):
        if st.session_state.points > 0:
            st.success(f"Great job, {name}! You scored **{st.session_state.points} points.**")
        
        if st.session_state.points == 3:
            time.sleep(1)
            st.balloons()
        elif 0 < st.session_state.points < 3:
            st.write(f"**...but try again!**")
        else:
            st.markdown(f"<p style='color: blue; text-align: center; font-size: 20px;'>{name} you scored {st.session_state.points} points. Please re-read Windrush 75.</p>", unsafe_allow_html=True
                        )
            #st.write(f"{name}, You scored **{st.session_state.points} points.** Please re-read Windrush 75.")
        st.dataframe(updated_df)


# Show Bar Graph Button
if st.button("Show Bar Graph", key="bChart"):
    updated_df = pd.DataFrame(st.session_state.leaderboard, columns=['Name', 'Age', 'Points'])
    updated_df = updated_df.sort_values(by="Points", ascending=False)

    fig, ax = plt.subplots()
    colours = ["red", "gold", "green", "black"]
    ax.bar(updated_df['Name'], updated_df['Points'], color=colours[:len(updated_df)])
    ax.set_xlabel("Players", color='blue')
    ax.set_ylabel("Points",color='blue')
    ax.set_title("Quiz Leaders' board", color='red')

    st.pyplot(fig)  # Display the bar chart in Streamlit
