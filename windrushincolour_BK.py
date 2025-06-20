import streamlit as st
import pandas as pd
from datetime import datetime
import time
import matplotlib.pyplot as plt
from PIL import Image
import sqlite3

st.set_page_config(
    page_title="Windrush In Colour Evaluation Form",
    layout="wide",
    #page_icon="📊"
    page_icon="images/Windrush logo clipped1_redrawn BLUEE_v2 3_R1.png"
)

# Database connection function
def exhibition_database():
    conn = sqlite3.connect("wf.db")
    return conn

salutation=("Thank you for taking the time out to complete this form.")
def stream_data():
    for word in salutation.split(" "):
        yield word + " "
        time.sleep(0.5)

# # Logo
# logo = "images/Windrush Foundation 30th Anniversary 2025_R4.png"
# logo_path = Image.open(logo)
# col1, col2, col3 = st.columns([2,1,2])
# with col2:
#     st.image(logo_path, width=180)

def evaluation_form():
    custom_css = """
        <style>
       /* Main page text color */
        [data-testid="stAppViewContainer"] > .main * {
        color: #FFF; /* Change text color to white */
        }

        /* Remove padding/margin from header */
        header, .stApp header {
        padding-top: 0px;
        margin-top: 0px;
        background-color:  #1E3A8A; /* Ensure header background is windrush blue */
        }
    /* Change background color of the main content area */
    /* Custom CSS for full-screen mode */
    .stApp {
        background-color: #1E3A8A; /* Windrush blue */
        color: #2D3748 !important; /* Change text color to white */
    }

    .stExpander {
        background-color: #FFF !important; /* Windrush white */
        color: #2D3748; !important; /* Change text color to white */
        border: 1px solid #1E3A8A !important;
        border-color:black !important;
        border-radius: 8px !important;
    }

    .stForm {
        background-color: #F8FAFC !important; /* Windrush white */
        color: #2D3748; !important; /* Change text color to white */
    }

    /* Button styling */
    .stButton > button {
        background-color: #C4A747 !important;
        color: #1E3A8A !important;
        border: 2px solid #1E3A8A !important;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    /* Hover effect */
    .stButton > button:hover {
        background-color: #1E3A8A !important;
        color: #C4A747 !important;
        border-color: #C4A747 !important;
    }

    /* Button styling */
    .stForm button {
        background-color: #C4A747 !important;
        color: #1E3A8A !important;
        border: 2px solid #1E3A8A !important;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    /* Hover effect */
    .stForm button:hover {
        background-color: #1E3A8A !important;
        color: #C4A747 !important;
        border-color: #C4A747 !important;
    }

        /* Text input styling */
        [data-testid="stTextInput"] input {
            background-color: #F8FAFC !important;
            color: black !important;
            border: 2px solid #1E3A8A !important;
            border-radius: 8px;
            padding: 12px !important;
        }

        [data-testid="stTextInput"] input:focus {
            border-color: #C4A747 !important;
            color: black !important;
            box-shadow: 0 0 0 2px rgba(30, 58, 138, 0.2);
        }

        /* Placeholder text styling */
        [data-testid="stTextInput"] input::placeholder {
            color: #94A3B8 !important;
            opacity: 1;
        }

        /* Dropdown/select styling */
        [data-testid="stSelectbox"] div {
            border: 1px solid #1E3A8A !important;
            border-radius: 8px !important;
        }

        /* Text area styling */
        [data-testid="stTextArea"] textarea {
            background-color: #F8FAFC !important;
            border: 2px solid #1E3A8A !important;
            border-radius: 8px !important;
            color: #1E3A8A !important;
        }

        /* Target password input label specifically */
        [data-testid="stTextInput"] label {
        color: black !important;
        }

        stAlert {
            color: white !important;
            font-weight: bold !important;
            background-color: white !important;
            border-radius: 5px;
            padding: 10px;
        }

       
           /* Selected tab styling */
        div[data-testid="stTabs"] button[aria-selected="true"] {
            color: #C4A747 !important; /* Gold */
            border-bottom: 3px solid #C4A747 !important;
        }

       div[data-testid="stExpander"] {
            width: 80% !important; /* Adjust width */
            margin: auto !important; /* Centers horizontally */
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        </style>
        """
    #Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
   
    # Current date
    now = datetime.now()
    mydate = now.strftime("%Y-%m-%d")
    # Logo
    logo = "images/Windrush Foundation 30th Anniversary 2025_R4.png"
    logo_path = Image.open(logo)
    col1, col2, col3 = st.columns([2,1,2])
    #with col2:
        #st.image(logo_path, width=180)
    with st.expander(" ", expanded=True):
        col1,col2,col3 = st.columns([1,5,1])
        with col2:
            a,b =st.columns([1,10])
            with b:
                st.header(":rainbow[Windrush in Colour Exhibition]")
            #st.markdown("<div style='margin-bottom: -350px; padding-bottom: 0px'></div>", unsafe_allow_html=True)  # Adjust space here
        with col2:
            a2,b2,c2 =st.columns(3)
            with b2:
                st.image(logo_path, width=150)
        with col2:
            st.markdown(
        "<h2 style='color: #C4A747; text-align:center; text-shadow: 1px 1px 2px black, 0 0 25px blue, 0 0 5px darkblue;'>Evaluation Form & Dashboard</h2>",
        unsafe_allow_html=True
    )
        with col2:
            st.markdown(
            "<p style='color: blue; text-align: justify;'>Windrush Foundation values the support we receive from the community, we want to hear your feedback of our in-person or online events. We are committed to giving you, our supporters the highest quality products and service. Your anonymous feedback will help us to ensure that both our in-person and online events are excelling in quality and variety. Click on the button below to take part. It usually takes between 4 to 6 minutes to complete. Thank you in advance.</p>",
            unsafe_allow_html=True
        )
        tab1, tab2 = st.tabs(["Evaluation Form", "Windrush in Colour Dashboard"])

        with tab1:
            with st.form("questionnaire"):
                with st.container():
                    name = st.text_input("Name")
                    gender = st.selectbox("Gender:", ["Male", "Female"])
                    age = st.number_input("Age", min_value=15, step=1)
                    ethnicity = st.selectbox("Ethnicity", ["None",
                        "African", "Asian", "Asian British", "Black British", "Black mixed", "Caribbean",
                        "European", "White British", "White Mixed", "Other"
                    ])
                    #if ethnicity == "Other":
                        #ethnicity = st.text_input("Please enter your ethnicity:")
                    q6 = st.text_input("If you are visiting as a school, please enter name of school")
                    location = st.text_input("Postcode")

                with st.container():
                    marketing = st.selectbox("How did you hear about this exhibition:", [
                        "None", "Radio", "TV", "Email", "Word of Mouth", "Social Media"
                    ])
                   
                    social_media = st.selectbox("If via Social Media, select the social media platform:", [
                            "None", "YouTube", "Facebook", "Instagram", "WhatsApp", "Messenger", "LinkedIn",
                            "Telegram", "Signal", "Snapchat", "TikTok"
                        ])

                with st.container():
                    q1 = st.selectbox("How did you find the exhibition story?",
                        [5, 4, 3, 2, 1],
                        format_func=lambda x: {
                            5: "5. Very Interesting",
                            4: "4. Interesting",
                            3: "3. Okay",
                            2: "2. Boring",
                            1: "1. Did not like it at all"
                        }[x])
                    q2 = st.text_input("How did the story make you feel?")
                    q3 = st.selectbox("How did you find the venue?",
                        ["None ", "Very Comfortable", "Uncomfortable", "Couldn't wait to leave"])
                    q4 = st.selectbox("Will you attend more Windrush events/exhibitions?",
                        [" ", "Absolutely Yes", "Maybe", "No"])
                    feedback = st.text_area("Please use this space to add further comments about this exhibition")
                    q5 = st.text_input("If you would like to keep informed about future Windrush Foundation events, please leave a valid e-mail address.")

                submitted = st.form_submit_button("Submit")

                if submitted:
                    try:
                        conn = exhibition_database()
                        cur = conn.cursor()
                        cur.execute('''
                            CREATE TABLE IF NOT EXISTS windrushincolour (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT, gender TEXT, age INTEGER, ethnicity TEXT, location TEXT,
                                feedback TEXT, marketing TEXT, social_media TEXT,
                                q1 INTEGER, q2 TEXT, q3 TEXT, q4 TEXT, q5 TEXT, q6 TEXT, mydate TEXT
                            )
                        ''')

                        cur.execute('''
                            INSERT INTO windrushincolour
                            (name, gender, age, ethnicity, location, feedback, marketing, social_media,
                            q1, q2, q3, q4, q5, q6, mydate)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (
                            name, gender, age, ethnicity, location, feedback, marketing,
                            social_media if marketing == "Social Media" else None,
                            q1, q2, q3, q4, q5, q6, mydate
                        ))

                        conn.commit()
                        st.success("✅ Your response has been recorded!")
                        st.write_stream(stream_data)
                        st.markdown("<p style=font-style:'Arial;color:red'>Why not head over to our website? www.windrushfoundation.com</p>",
                                    unsafe_allow_html=True)
                        conn.close()
                    except Exception as e:
                        st.error(f"❌ Could not insert data: {str(e)}")
    # Admin login and dashboard
        if 'authenticated' not in st.session_state:
            st.session_state['authenticated'] = False

    with tab2:
      
        if not st.session_state['authenticated']:
            a,b,c = st.columns(3)
            with a:
                password = st.text_input("Enter admin password", type="password")
            if st.button("Click to login"):
                if password == st.secrets["ADMIN_PW"]:
                    st.session_state['authenticated'] = True
                    st.success("✅ Logged in successfully")
                else:
                    st.error("❌ Incorrect password")

        if st.session_state['authenticated']:
            cola,colb,colc,=st.columns([1,3,1])
            with colb:
                st.subheader("")
                st.subheader("📊 Windrush In Colour Dashboard")
            st.markdown("""<hr style='border: 2px; solid #C4A747;'>""", unsafe_allow_html=True)
            try:
                conn = exhibition_database()
                df = pd.read_sql_query("SELECT * FROM windrushincolour", conn)
                conn.close()

                with st.container():  # Replaces problematic expander
                    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Participant Count", "Gender Distribution", "Age Distribution", "Ethnicity Distribution","Future Attendance Intent","Marketing","Exhibition Ratings"])

                    with tab1:
                        col1, col2, col3 = st.columns([1, 1, 1])
                        with col2:
                            #st.markdown("**<span style='color: red;'>Participant Count</span>**", unsafe_allow_html=True)
                            participant_counts = df["name"]
                            participant_counts=len(participant_counts)
                            st.metric(label="**Participant Count**",value=participant_counts,delta=0.5, delta_color="inverse")

                    with tab2:
                        col1, col2, col3 = st.columns([1, 3, 1])
                        with col2:
                            #st.markdown("**<span style='color: red;'>Gender Distribution</span>**", unsafe_allow_html=True)
                            gender_count = df["gender"].value_counts().sort_values(ascending=False)
                            fig, ax = plt.subplots()
                            ax.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%')
                            st.pyplot(fig)

                    with tab3:
                        col1, col2, col3 = st.columns([1, 3, 1])
                        with col2:
                            #st.markdown("**<span style='color: red;'>Age Distribution</span>**", unsafe_allow_html=True)
                            fig, ax = plt.subplots()
                            ax.hist(df["age"], bins=10, color='skyblue', edgecolor='black')
                            ax.set_xlabel("Age")
                            ax.set_ylabel("Number of Attendees")
                            st.pyplot(fig)

                    with tab4:
                        col1, col2, col3 = st.columns([1, 3, 1])
                        with col2:
                            #st.markdown("**<span style='color: red;'>Ethnicity Distribution</span>**", unsafe_allow_html=True)
                            ethnicity_count = df["ethnicity"].value_counts().sort_values(ascending=False)
                            fig, ax = plt.subplots()
                            ax.pie(ethnicity_count, labels=ethnicity_count.index, autopct='%1.1f%%')
                            st.pyplot(fig)
                    
                    with tab5:
                        col1, col2, col3 = st.columns([1, 3, 1])
                        with col2:
                            #st.markdown("**<span style='color: red;'>Future Attendance Intent</span>**", unsafe_allow_html=True)
                            intent_counts = df["q4"].value_counts()
                            fig, ax = plt.subplots()
                            ax.bar(intent_counts.index, intent_counts, color=['green', 'orange', 'red'])
                            ax.set_xlabel("Response")
                            ax.set_ylabel("Number of Attendees")
                            st.pyplot(fig)
                    with tab6:
                        col1, col2 = st.columns(2)
                        with col1:
                            marketing_counts = df["marketing"].value_counts().sort_values(ascending=False)
                            fig, ax = plt.subplots()
                            ax.pie(marketing_counts, labels=marketing_counts.index, autopct='%1.1f%%')
                            st.pyplot(fig)
                        with col2:
                            social_media_counts = df["social_media"].value_counts().sort_values(ascending=False)
                            fig, ax = plt.subplots()
                            ax.pie(social_media_counts, labels=social_media_counts.index, autopct='%1.1f%%')
                            st.pyplot(fig)
                    
                    with tab7:
                        cola, col2, colc = st.columns([1,2,1])
                        with col2:
                            #st.markdown("**<span style='color: red;'>Future Attendance Intent</span>**", unsafe_allow_html=True)
                            ex_ratings_counts = df["q1"].value_counts().sort_values(ascending=False)
                            fig, ax = plt.subplots()
                            ax.barh(ex_ratings_counts.index, ex_ratings_counts, color=["gold", "silver", "brown", "blue", "red"])
                            ax.set_xlabel("Ratings Score")#,"green","blue","gold","grey"
                            ax.set_ylabel("Exhibition Ratings")
                            st.pyplot(fig)

                with st.container():
               
                    st.markdown("""<hr style='border: 2px; solid #C4A747;'>""", unsafe_allow_html=True)

                            
                    if st.button("Show Evaluation Database"):
                        st.dataframe(df)


                if st.button("🔒 Logout"):
                    st.session_state['authenticated'] = False
                    st.success("You have been logged out.")
                return df
            except Exception as e:
                st.error(f"Dashboard Error: {str(e)}")
        else:
            st.info("🔐 Admin authentication required for insights")
    
    col1,col2,col3 = st.columns(3)  
    with col2:
        st.markdown("""
                    <div style="background-color: rgba(255, 255, 255, 0.4); 
                    padding: 10px; 
                    border-radius: 10px; 
                    display: flex; 
                    align-items: center; 
                    justify-content: center; 
                    height: 50px;">
                    <p style="color: white; font-size: 15px; 
                    font-weight: bold; font-variant: small-caps; text-align: center; margin: 0;">
                    Designed by BIS Digital Solutions
                    </p>
                    </div> """, unsafe_allow_html=True)



if __name__ == "__main__":
    evaluation_form()