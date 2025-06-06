import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from PIL import Image

logo ="Windrush logo clipped1_redrawn BLUEE_v2 3.png"
logo_path = Image.open(logo) 
# Title
#st.title("Windrush Heritage Quiz")
col1,col2,col3 =st.columns(3)
with col2:
    st.write(logo_path)
st.markdown(
    "<h2 style='color: blue; text-align: center;'>My Evaluation Form</h1>",
    unsafe_allow_html=True
)

#st.title("Windrush Foundation 30")
st.subheader("**.**")
st.markdown(
    "<p style='color: blue; font-size: 20px;'>Evaluation Form</p>",
    unsafe_allow_html=True)

# Current date
now = datetime.now()
mydate = now.strftime("%Y-%m-%d")

# Form for user input
with st.form("questionnaire"):
    name = st.text_input("Name")
    gender = st.selectbox("Gender:", ["Male", "Female"])
    age = st.number_input("Age", min_value=0, step=1)
    feedback = st.text_area("Feedback")
    q1 = st.selectbox("How did you find the presentation", ["Very Interesting", "Okay", "Boring"])
    q2 = st.selectbox("How did you find the venue", ["Very Comfortable", "Uncomfortable", "Couldn't wait to leave"])
    q3 = st.selectbox("Will you be attending more Windrush events?", ["Absolutely Yes", "Maybe", "No"])
    submitted = st.form_submit_button("Submit")

    if submitted:
        new_data = pd.DataFrame([[name, gender, age, feedback, q1, q2, q3, mydate]],
                                columns=["Name", "Gender", "Age", "Feedback", "Question 1", "Question 2", "Question 3", "Date"])
        
        # Load existing data or create a new file if it doesn't exist
        try:
            file = r"C:\Users\Michael\Downloads\data.csv"
            df = pd.read_csv(file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Name", "Gender", "Age", "Feedback", "Question 1", "Question 2", "Question 3", "Date"])
        
        updated_df = pd.concat([df, new_data], ignore_index=True)
        updated_df.to_csv(file, index=False)

        st.success("Your response has been recorded!")
        st.dataframe(new_data)  # Display submitted data

file = r"C:\Users\Michael\Downloads\data.csv"


if st.button("Show Charts"):
    col1,col2,col3 = st.columns([1,3,1])
    with col2:
        st.subheader("Evaluation Chart Dashboard")
        st.header(" ")
    try:
        col1,col2,col3=st.columns([1,1,1])
        # Show charts if the button is clicked
        df = pd.read_csv(file)

        # Chart 1: Age Distribution Histogram
        with col1:
            #st.write("**Age Distribution of Attendees**")
            st.markdown("**<span style='color: red;'>Age Distribution of Attendees</span>**", unsafe_allow_html=True)
            fig, ax = plt.subplots()
            ax.hist(df["Age"], bins=10, color='skyblue', edgecolor='black')
            ax.set_xlabel("Age")
            ax.set_ylabel("Number of Attendees")
            ax.set_title("Distribution of Attendees by Age")
            st.pyplot(fig)

        with col2:
            # Chart 2: Presentation Feedback Pie Chart
            #st.write("**Presentation Feedback Summary**")
            st.markdown("**<span style='color: red;'>Presentation Feedback Summary</span>**", unsafe_allow_html=True)

            feedback_counts = df["Question 1"].value_counts()
            fig, ax = plt.subplots()
            ax.pie(feedback_counts, labels=feedback_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'gold', 'red'])
            ax.set_title("How Attendees Found the Presentation")
            st.pyplot(fig)

        with col3:
            # Chart 3: Attendance Intent Bar Chart
            st.markdown("**<span style='color: red;'>Future Attendance Intent</span>**", unsafe_allow_html=True)
            intent_counts = df["Question 3"].value_counts()
            fig, ax = plt.subplots()
            ax.bar(intent_counts.index, intent_counts, color=['green', 'orange', 'red'])
            ax.set_xlabel("Response")
            ax.set_ylabel("Number of Attendees")
            ax.set_title("Will Attendees Come to Future Windrush Events?")
            st.pyplot(fig)

    except FileNotFoundError:
        st.error("No data available yet. Please submit responses first.")

if st.button("Show Evaluation Database", key="Eval"):
    try:
        df = pd.read_csv(file)
        st.dataframe(df)

        

    except FileNotFoundError:
        st.error("No data available yet. Please submit responses first.")
