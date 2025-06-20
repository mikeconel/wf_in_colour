import streamlit as st
import pandas as pd
from datetime import datetime
import time
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import sqlite3
from textblob import TextBlob

st.set_page_config(
    page_title="Windrush In Colour Evaluation Form",
    layout="wide",
    #page_icon="📊"
    #page_icon="images/Windrush logo clipped1_redrawn BLUEE_v2 3_R1.png"
    page_icon="images/Windrush In Colour Exhibition_LOGO.png"
)

# Database connection function
def exhibition_database():
    conn = sqlite3.connect("wf.db")
    return conn

def handle_dates():
    """Central date range handler with persistent state"""
    # Store absolute min/max dates separately
    if 'absolute_dates' not in st.session_state:
        #current_date=datetime.now().strftime("%y:%m:%d")
        try:
            conn = exhibition_database()
            cur=conn.cursor()
            cur.execute("SELECT MIN(mydate) FROM windrushincolour_2")
            min_date_result = cur.fetchone()[0]

            cur.execute("SELECT MAX(mydate) FROM windrushincolour_2")
            max_date_result = cur.fetchone()[0]

            conn.close()

            # Convert to datetime.date if strings
            min_date = pd.to_datetime(min_date_result).date()
            max_date = pd.to_datetime(max_date_result).date()

            st.session_state.absolute_dates = (min_date, max_date)      
            conn.close()
            st.session_state.absolute_dates = (min_date, max_date)
        except Exception as e:
            st.error(f"Data for this date does not exists {str(e)}")
            return
        
     # Initialize with absolute dates if not set
    if 'date_range' not in st.session_state:
        st.session_state.date_range = list(st.session_state.absolute_dates)

    # Show date picker with boundaries
    new_dates = st.date_input(
        "Select Date Range",
        value=st.session_state.date_range,
        min_value=st.session_state.absolute_dates[0],
        max_value=st.session_state.absolute_dates[1],
        key="global_date_picker"
    )

    if isinstance(new_dates, (list, tuple)) and len(new_dates) == 2:
        st.session_state.date_range = new_dates



salutation=(f"**:red[Thank you for taking the time out to complete this form.]**")
def stream_data():
    for word in salutation.split(" "):
        yield word + " "
        time.sleep(0.5)


def evaluation_form():
    custom_css = """
        <style>
         
       /*Dynamically keeping page max width to 700px*/ 
          .block-container {
            max-width: 70%;
            margin: auto;
        }
        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    
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

    
    .stForm {
        background-color: #E2E8F0  !important; /* Windrush white */
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
.stSelectbox-container-form {
    border: 1px solid #1E3A8A !important;
    border-radius: 8px;
}

[data-testid="stSelectbox"] label {
        color: black !important;
        }

.stSelectbox-container-form button {
    background-color: #C4A747 !important;
}

.stSelectbox-container button:hover {
    background-color: #6495ED;
}

.stSelectbox-container button:active {
    background-color: #6495ED;
}

        [data-testid="stTextArea"] label {
        color: black !important;
        }

        [data-testid="stNumberInput"] label {
        color: black !important;
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
            background-color:  #F8FAFC !important;
            border: 1px solid #1E3A8A !important;
            border-color:black !important;
            border-radius: 8px !important;
        }

       hr {
            border: 1px solid #C4A747 !important;
        }


        </style>
        """
    #Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
   
    # Current date
    now = datetime.now()
    mydate = now.strftime("%Y-%m-%d")
    mytime = now.strftime("%H:%M:%S")
    # Logo
    logo = "images/Windrush In Colour Exhibition_LOGO 3.png"
    logo_path = Image.open(logo)
   
    with st.expander(" ", expanded=True):
        with st.container():
            st.image(logo_path)
            col1,col2,col3 = st.columns([1,1,1])     
            
            col1,col2,col3 = st.columns([1,8,1])
           
            with col2:
                st.markdown(
            "<h2 style='color: #C4A747; text-align:center; text-shadow: 1px 1px 2px black, 0 0 25px blue, 0 0 5px darkblue;'>Evaluation Form & Dashboard</h2>",
            unsafe_allow_html=True
        )
            with col2:
                st.markdown(
                "<p style='color: blue; text-align: justify;'>Windrush Foundation values the support we receive from the community, we want to hear your feedback of our in-person or online events. We are committed to giving you, our supporters the highest quality products and service. Your feedback will help us to ensure that both our in-person and online events are excelling in quality and variety. Click on the button below to take part. It usually takes between 4 to 6 minutes to complete. Thank you in advance.</p>",
                unsafe_allow_html=True
            )
        tab1, tab2 = st.tabs(["**Evaluation Form**", "**Windrush in Colour Dashboard**"])

        with tab1:
            with st.form("questionnaire"):
                with st.container():
                    a,col_b,c = st.columns([1,3,1])
                
                    with col_b:
                        name = st.text_input("**Name**")
                        gender = st.selectbox("**Gender:**", ["Male", "Female","Not specified"])
                        age = st.number_input("**Age**", min_value=15, step=1)
                        ethnicity = st.selectbox("**Ethnicity**", ["None",
                        "African", "Asian", "Asian British", "Black British", "Black mixed", "Caribbean",
                        "European", "White British", "White Mixed", "Other"
                        ])
                    #if ethnicity == "Other":
                        #ethnicity = st.text_input("Please enter your ethnicity:")
                        q6 = st.text_input("**If you are visiting as a school, please enter name of school**")
                        location = st.text_input("**Postcode**")

                with st.container():
                    a,col_b,c = st.columns([1,3,1])
                    with col_b:
                        marketing = st.selectbox("**How did you hear about this exhibition:**", [
                        " ", "Radio", "TV", "Email", "Word of Mouth", "Social Media"
                        ])
                   
                        social_media = st.selectbox("**If via Social Media, select the social media platform:**", [
                            "Don't us social media", "YouTube", "Facebook", "Instagram", "WhatsApp", "Messenger", "LinkedIn",
                            "Telegram", "Signal", "Snapchat", "TikTok"
                            ])

                with st.container():
                    a,col_b,c = st.columns([1,3,1])
                    with col_b:
                        q1 = st.selectbox("**How did you find the exhibition story?**",
                            [0, 5, 4, 3, 2, 1],
                            format_func=lambda x: {
                            0:  " ",
                            5: "5. Very Interesting",
                            4: "4. Interesting",
                            3: "3. Okay",
                            2: "2. Boring",
                            1: "1. Did not like it at all"
                            }[x])
                        q2 = st.text_area("**How did the story make you feel?**",max_chars=300)
                        q3 = st.selectbox("**How did you find the venue?**",
                        [" ", "Very Comfortable", "Uncomfortable", "Couldn't wait to leave"])
                        q4 = st.selectbox("**Will you attend Windrush Foundation events/exhibitions in the future?**",
                        [" ", "Absolutely Yes", "Maybe", "No"])
                        feedback = st.text_area("**Please use this space to add further comments about this exhibition.**",max_chars=800)
                        q5 = st.text_input("**If you would like to keep informed about future Windrush Foundation events, please leave a valid e-mail address.**",max_chars=80)
                    a,col_b,c = st.columns([1,3,2])
                    with c:
                        submitted = st.form_submit_button("**Submit**")
                #submitted = st.form_submit_button("Submit")

                if submitted:
                    try:
                        conn = exhibition_database()
                        cur = conn.cursor()
                        cur.execute('''
                            CREATE TABLE IF NOT EXISTS windrushincolour_2 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT, gender TEXT, age INTEGER, ethnicity TEXT, location TEXT,
                                feedback TEXT, marketing TEXT, social_media TEXT,
                                q1 INTEGER, q2 TEXT, q3 TEXT, q4 TEXT, q5 TEXT, q6 TEXT, mydate TEXT, mytime TEXT
                            )
                        ''')

                        cur.execute('''
                            INSERT INTO windrushincolour_2
                            (name, gender, age, ethnicity, location, feedback, marketing, social_media,
                            q1, q2, q3, q4, q5, q6, mydate,mytime)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
                        ''', (
                            name, gender, age, ethnicity, location, feedback, marketing,
                            social_media if marketing == "Social Media" else None,
                            q1, q2, q3, q4, q5, q6, mydate, mytime
                        ))
                        

                        conn.commit()
                        time.sleep(0.5)
                        st.success("**✅ Your response has been recorded!**")
                        st.write_stream(stream_data)
                        time.sleep(0.5)
                        
                        # Redirect to Windrush Foundation website
                        st.write("**🌐:red[Redirecting...]**")
                        time.sleep(1)
                       
                        st.markdown("""
                            <meta http-equiv="refresh" content="3;url=https://www.windrushfoundation.com">
                                <p>You will be redirected to the Windrush Foundation website in 3 seconds...</p>
                                """, unsafe_allow_html=True)

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
            cola,colb,colc,=st.columns([1,8,1])
            with colb:
                st.subheader("📊:rainbow[Windrush In Colour Dashboard]")
                #st.write("**Login below to see :rainbow['Windrush In Colour'] exhibition insights.**")
            handle_dates()
            st.markdown("""<hr style='border: 2px solid #C4A747;'>""", unsafe_allow_html=True)


            try:
                conn = exhibition_database()
                df = pd.read_sql_query("SELECT * FROM windrushincolour_2", conn)
                conn.close()

              ###  df = df.fillna(0)  # Replace NaN values with 0
              ###  df.replace([np.inf, -np.inf], np.nan, inplace=True)  # Handle infinite values
              ###  df.dropna(inplace=True)  # Remove rows with NaN if necessary

                with st.container():  # Replaces problematic expander
                    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Participant Count", "Gender Distribution", "Age Distribution", "Ethnicity Distribution","Future Attendance Intent","Marketing","Exhibition Ratings"])

                    with tab1:
                        col1, col2, col3 = st.columns([1, 1, 1])
                        with col2:
                            df["mydate"] = pd.to_datetime(df["mydate"], format="%Y-%m-%d", errors="coerce")
                            df["mytime"] = pd.to_datetime(df["mytime"], format="%H:%M:%S", errors="coerce")
                                                        # Filter based on selected date range
                            filtered_df = df[
                                (df["mydate"].dt.date >= st.session_state.date_range[0]) &
                                (df["mydate"].dt.date <= st.session_state.date_range[1])
                                ]
                            
                            # Count participants by name (or any unique identifier)
                            participant_counts = filtered_df["id"].nunique()  # or len(filtered_df) if names can repeat

                            st.metric(
                                label="Participant Count",
                                value=participant_counts,
                                delta=0.5,
                                delta_color="inverse"
                                )

                    with tab2:
                        col1, col2, col3 = st.columns([1, 3, 1])
                        with col2:
                            # Filter based on selected date range
                            filtered_df = df[
                                (df["mydate"].dt.date >= st.session_state.date_range[0]) &
                                (df["mydate"].dt.date <= st.session_state.date_range[1])
                                ]

                            # Count participants by name (or any unique identifier)
                            #participant_counts = filtered_df["name"].nunique()  # or len(filtered_df) if names can repeat

                            
                            gender_count = filtered_df["gender"].value_counts().sort_values(ascending=False)
                            #gender_count = df["gender"].value_counts().sort_values(ascending=False)
                            fig, ax = plt.subplots()
                            ax.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%')
                            st.pyplot(fig)
                            st.table(gender_count)

                    with tab3:
                        col1, col2, col3 = st.columns([1, 8, 1])
                        with col2:
                            #st.markdown("**<span style='color: red;'>Age Distribution</span>**", unsafe_allow_html=True)
                            fig, ax = plt.subplots()
                            ax.hist(filtered_df["age"], bins=10, color='blue', edgecolor='gold')
                            ax.set_xlabel("Age")
                            ax.set_ylabel("Number of Attendees")
                            st.pyplot(fig)

                            cola,colb,colc =st.columns(3)
                            min_age = filtered_df["age"].min()
                            metric_label = "Minimum Age"
                            metric_value = f":blue[{min_age}]"

                            mean_age = filtered_df["age"].mean()
                            metric_label_2 = "Average Age"
                            metric_value_2 = f":red[{mean_age}]"

                            max_age = filtered_df["age"].max()
                            metric_label_3 = "Maximum Age"
                            metric_value_3 = f":blue[{max_age}]"

                            col1, col2, col3= st.columns(3)
                            with col1:
                                st.markdown(f"**{metric_label}: {metric_value}**")
                                min_age_count = (filtered_df["age"] == min_age).sum()
                                st.metric('Total Min Age People',min_age_count)
                            with col2:
                                st.markdown(f"**{metric_label_2}: {metric_value_2}**")  # styled
                                median_age = filtered_df["age"].median()
                                median_age_count = (filtered_df["age"] == median_age).sum()
                                st.metric('Total Median Age People',median_age_count)
                            with col3:
                                st.markdown(f"**{metric_label_3}: {metric_value_3}**")  # styled
                                max_age_count = (filtered_df["age"] == max_age).sum()
                                st.metric('Total Max Age People',max_age_count)
                    with tab4:
                        col1, col2, col3 = st.columns([1, 3, 1])
                        with col2:
                            #st.markdown("**<span style='color: red;'>Ethnicity Distribution</span>**", unsafe_allow_html=True)
                            ethnicity_count = filtered_df["ethnicity"].value_counts().sort_values(ascending=False)
                            fig, ax = plt.subplots(figsize=(6,6))
                            myexplosion = [0.2 if i % 3 == 0 else 0 for i in range(len(ethnicity_count))]

                            ax.pie(ethnicity_count, labels=ethnicity_count.index, 
                                   autopct='%1.1f%%',explode=myexplosion)
                            ax.set_title("Ethnicity Distribution")
                            ax.legend(ethnicity_count.index, loc="best")

                            st.pyplot(fig)
                    
                    with tab5:
                        col1, col2, col3 = st.columns([1, 3, 1])
                        with col2:
                            #st.markdown("**<span style='color: red;'>Future Attendance Intent</span>**", unsafe_allow_html=True)
                            intent_counts = filtered_df["q4"].value_counts()
                            fig, ax = plt.subplots()
                            ax.bar(intent_counts.index, intent_counts, color=['green', 'orange', 'red'])
                            ax.set_xlabel("Response")
                            ax.set_ylabel("Number of Attendees")
                            st.pyplot(fig)
                    with tab6:
                        col1, col2 = st.columns(2)
                        with col1:
                            marketing_counts = filtered_df["marketing"].value_counts().sort_values(ascending=False)
                            fig, ax = plt.subplots(figsize=(6,6))
                            myexplosion = [0.2 if i % 3 == 0 else 0 for i in range(len(marketing_counts))]
                            ax.pie(marketing_counts, labels=marketing_counts.index,
                                   autopct='%1.1f%%',explode=myexplosion,startangle=90)
                            ax.set_title("Marketing Pipelines")
                            ax.legend(marketing_counts.index, loc="best")
                            st.pyplot(fig)
                        with col2:
                            social_media_counts = filtered_df["social_media"].value_counts().sort_values(ascending=False)
                            fig, ax = plt.subplots(figsize=(6,6))
                            myexplosion = [0.2 if i % 3 == 0 else 0 for i in range(len(social_media_counts))]
                            ax.pie(social_media_counts, labels=social_media_counts.index,
                                   autopct='%1.1f%%',explode=myexplosion,startangle=90)
                            ax.set_title("Preferred Social Media")
                            ax.legend(social_media_counts.index, loc="best")
                            st.pyplot(fig)
                    
                    with tab7:
                        cola, col2, colc = st.columns([1,2,1])
                        with col2:
                            #st.markdown("**<span style='color: red;'>Future Attendance Intent</span>**", unsafe_allow_html=True)
                            ex_ratings_counts = filtered_df["q1"].value_counts().sort_values(ascending=False)
                            fig, ax = plt.subplots()
                            ax.bar(ex_ratings_counts,ex_ratings_counts.index, color=["gold", "green", "brown", "blue", "red"])
                            ax.set_xlabel("How did you find the exhibition story?")#,"green","blue","gold","grey"
                            ax.set_ylabel("Rating Score")
                            st.pyplot(fig)

                with st.container():
               
                    st.markdown("""<hr style='border: 2px; solid #C4A747;'>""", unsafe_allow_html=True)
                    tab1, tab2, tab3 = st.tabs(["Time Series Data","Sentiment Analysis","Show Evaluation Database"])
                    with tab1:
                        import matplotlib.dates as mdates
                        col_1,col_2= st.columns(2)
                        st.write("**:red[Frequency of participants throughout the day!!!]**")
                        with col_1:
                            start_time = datetime.strptime("00:01:00", "%H:%M:%S").time()
                            end_time = datetime.strptime("23:59:59", "%H:%M:%S").time()

                            participant_time = df[(df["mytime"].dt.time >= start_time) & (df["mytime"].dt.time <= end_time)]
                            fig, ax = plt.subplots()
                            # Histogram
                            ax.hist(participant_time["mytime"], bins=10, color='blue', edgecolor='gold')

                            # X-axis labels and formatting
                            ax.set_xlabel("Time")
                            ax.set_ylabel("Number of Participants")

                            # Convert x-axis to display proper time format
                            ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

                            # Set x-axis limits manually
                            ax.set_xlim(pd.to_datetime("00:01:00", format="%H:%M:%S"), pd.to_datetime("23:59:59", format="%H:%M:%S"))

                            st.pyplot(fig)

                        with col_2:
                            fig, ax = plt.subplots()
                            
                            ax.scatter(participant_time["mytime"], participant_time["id"], color='red', alpha=0.7)
                            # Formatting X-axis
                            ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
                            ax.set_xlabel("Time")
                            ax.set_ylabel("Participant ID")
                            st.pyplot(fig)
                           
                       
                    with tab2:
                        ans=filtered_df['feedback']
                        ans2=filtered_df['q2']
                        ans_total=ans+ans2
                        #st.write(type(ans2))
                        total_sentiments = sentiment_analysis(ans_total)
                        
                         # Create a dictionary to store the sentiment analysis results
                        sentiment_results = {
                            "Positive": total_sentiments["positive"],
                            "Neutral": total_sentiments["neutral"],
                            "Negative": total_sentiments["negative"]
                            }
                        
                        # Create a DataFrame from the sentiment analysis results
                        df_sentiments = pd.DataFrame([sentiment_results])
    
                        # Display the sentiment analysis results in a table
                        #st.write("Sentiment Analysis Results:")
                        #st.table(df_sentiments)
                        df_sentiments_1=df_sentiments

                        #social_media_counts = df["social_media"].value_counts().sort_values(ascending=False)
                        l1=df_sentiments['Positive'].iloc[0]
                        l2=df_sentiments['Neutral'].iloc[0]
                        l3=df_sentiments['Negative'].iloc[0]
                        sentiments_count=[l1,l2,l3]
                      
                        sentiments_count_x=['Positive','Neutral','Negative']
                        mycolours=["gold","blue","red"]
                        myexplode= [0.2 if i % 3 == 0 else 0 for i in range(len(sentiments_count))]
                        fig, ax = plt.subplots(figsize=(6,6))
                        ax.pie(sentiments_count,labels=sentiments_count_x, autopct='%1.1f%%', 
                               colors=mycolours, explode=myexplode,textprops={'fontsize': 10},startangle=90)
                        
                        ax.legend(sentiments_count_x, loc="best")
                        ax.set_title("Sentiment Analysis Results:")
                        col1,col2,col3 = st.columns([1,4,1])
                        with col2:
                            st.pyplot(fig)
                        with col2:
                            st.dataframe(df_sentiments_1)



                    with tab3:
                        st.dataframe(filtered_df)

                    # if st.button("Show Evaluation Database"):
                    #     st.dataframe(df)

                if st.button("🔒 Logout"):
                    st.session_state['authenticated'] = False
                    st.success("You have been logged out.")
                    st.rerun()
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
                    Designed by BIS Smart Digital Solutions
                    </p>
                    </div> """, unsafe_allow_html=True)

def sentiment_analysis(responses):
  
    analysis={
                'positive':0,
                'neutral':0,
                'negative':0,             
            }
    for text in responses:
        if isinstance(text,str):
            polarity = TextBlob(text).sentiment.polarity

            if polarity > 0.2:
                analysis["positive"] += 1
            elif polarity < -0.2:
                analysis["negative"] += 1
            else:
                analysis["neutral"] += 1
    total=sum(analysis.values()) or 1

    return {k:round((v/total)*100,1) for k,v in analysis.items()}


if __name__ == "__main__":
    evaluation_form()