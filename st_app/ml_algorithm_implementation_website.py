import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from PIL import Image
import joblib 


page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://www.wallpaperflare.com/static/853/1009/106/simple-simple-background-minimalism-black-background-wallpaper.jpg");
    }}
    background: rgba(0,0,0,0);
    </style>
    """
st.markdown(page_bg_img, unsafe_allow_html=True)



def display_underline(text, underline=False, color="white", size=14, bold=False):
    styles = f'color: {color}; text-decoration: {"underline" if underline else "none"};'
    styles += f'font-size: {size}px; font-weight: {"bold" if bold else "normal"};'
    styled_text = f'<span style="{styles}">{text}</span>'
    st.markdown(styled_text, unsafe_allow_html=True)


# Inject CSS to change label color to white
st.markdown(
    """
    <style>
    .stNumberInput label {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


display_underline('NASA SPACE APP CHALLENGE!', size = 20, bold = True)
display_underline('OBJECTS NEAR TO THE EARTH!', size = 25, underline = True, bold = True, color = 'yellow')

with open('home.txt', 'r') as f:
    text = f.read()
st.write('---')
display_underline(text, color = 'white', size = 13)



df = pd.read_csv('neo.csv')
# remove those two columns
df = df.drop(['orbiting_body','sentry_object'], axis=1)

x = df[['est_diameter_min', 'est_diameter_max', 'relative_velocity', 'est_diameter_min']]
y = df['hazardous'].astype("int")
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 0)



# Step 1: Load the saved Random Forest model
model = joblib.load('random_forest_model.pkl')


a, b, c, d, e, g = st.tabs(['WHY THIS', 'SAFETY', 'SOMETHING TOWARD EARTH', 'Precautions', 'Explore Data', 'Gallery'])

with a:
    st.write('---')
    with open('whythis/one.txt', 'r') as f:
        text = f.read()
    display_underline(text, size = 17, color = 'white', bold = True)

    image = Image.open('splash.jpg')

    # Display the image in the Streamlit app
    st.image(image, caption='Splash Image', use_column_width=True)
    

    with open('whythis/two.txt', 'r') as f:
        text = f.read()
    display_underline(text, size = 16, color = 'yellow', bold = True, underline = True)


with b:
    with open('safety/safety.txt', 'r') as f:
        text = f.read()
    display_underline(text, size = 13, color = 'white', bold= True, underline = True)

with c:
    st.write('---')
    st.write('---')
    display_underline('We can predict whether a object heading toward earth is hazardious for us or not.', size = 20, color = 'yellow', bold=True)

    with st.form(key='input_form'):
        est_diameter_min = st.number_input('Enter minimum estimated diameter (in km)', min_value=0.000, value=10.000, step=0.001)
        est_diameter_max = st.number_input('Enter maximum estimated diameter (in km)', min_value=0.000, value=50.000, step=0.001)
        relative_velocity = st.number_input('Enter Relative Velocity (m/h)', min_value=0.000, value=20000.000, step=0.001)
        
        # Add a submit button
        submit_button = st.form_submit_button(label='Predict')

    # When the form is submitted, display the values and handle the logic
    if submit_button:

        input_data = pd.DataFrame({
        'est_diameter_min': [est_diameter_min],
        'est_diameter_max': [est_diameter_max],
        'relative_velocity': [relative_velocity]})

        prediction = model.predict(input_data)
        
        if prediction[0] == 0:
            display_underline('CONGRATS, IT IS NOT TO WORRY ABOUT!!', size = 15, bold = True, color = 'white')
            st.balloons()
        if prediction[0] == 1:
            st.warning('We predict it is time of hurry for people of Earth.')

            display_underline('determining seriousness of coming object: ')
            logmodel = joblib.load('Logistic_regression.pkl')

            alpha = logmodel.predict_proba(input_data)
  
            if alpha[0][1] < 0.4:
                display_underline('Not very much hazardious but taking precautions is necessary', bold=True, color = 'yellow')
                display_underline('Precautions', color='white', size=15, underline = True)
                display_underline('Continous tracking and orbit recalculation.', color='white', size=15)
                
                display_underline("Observations to refine asteroid's trajectory.", color='white', size=15)
                
                display_underline('Early-stage discussion on possible deflection methods.', color='white', size=15)
                display_underline('Early informational public notifications, without creating panic.', color='white', size=15)

            
            elif alpha[0][1] < 0.6 and alpha[0][1] >= 0.4:
                
                display_underline('TAKE PRECAUTIONS, there are not good vibes', bold=True, color='yello', size=17)
                display_underline('Precautions', color='white', size=15, underline = True)
                display_underline('Inform government and key agencies. ', color='white', size=15)
                display_underline('Provide guidelines on assembling emergency kits.', color='white', size=15)
                display_underline('Organize regular drills to practice evacuation.', color='white', size=15)
                display_underline('Offer mental health to support to help community cope with anxiety.', color='white', size=15)
                
                


            
            else:
                display_underline('TAKE NECESSARY STEPS AS SOON AS POSSIBLE, its not a good object', bold=True, color='yellow', size=18)
                display_underline('Precautions', color='white', size=15, underline = True)
                display_underline('Identify safe locations that can withstand impacts.', color='white', size=15)
                display_underline('Stockpile essential supplies', color='white', size=15)
                display_underline('Develop evacuation plans', color='white', size=15)
                display_underline('Ensure accesibility to safe shelters. ', color='white', size=15)



with d:
    display_underline('What to do if something is approaching toward earth and is hazardious?', color = 'white', bold = True, size =17)
    display_underline('RELAX', color = 'white')
    display_underline('PRAY', color = 'white')
    display_underline('GET TO SAFE PLACE', color = 'white')
    display_underline('TRY NOT TO BE UNDER OPEN SKY', color = 'white')
    display_underline('DRINK PANELTY OF WATER', color = 'white')
    

with e:
    st.markdown(
    """
    <style>
    .stRadio label, .stSelectbox label, .stMultiselect label, .stCheckbox label, .stNumberInput label, .stSubheader, .stTextInput  label {
        color: white;
    }

    /* Change the color of radio button options */
    div[data-baseweb="radio"] > div {
        color: white;
    }

    /* Adjusting the background of select dropdowns if needed */
    .stSelectbox div[role="listbox"] > div {
        background-color: black;
        color: white;
    }
    
    /* For checkbox options */
    .stCheckbox > div {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True)
    
    display_underline("Select Columns to View", size = 15)
    columns = st.multiselect("", options=df.columns.tolist(), default=df.columns.tolist())
    st.write(df[columns])

    # Option to filter rows by 'hazardous' status
    display_underline("Filter by Hazardous Status", size = 15, bold=True)
    hazardous_filter = st.selectbox("Is the asteroid hazardous?", options=['All', 'Yes', 'No'])
    if hazardous_filter == 'Yes':
        st.write(df[df['hazardous'] == True])
    elif hazardous_filter == 'No':
        st.write(df[df['hazardous'] == False])
    else:
        st.write(df)

    # Option to view summary statistics
    display_underline("Summary Statistics", size = 15)
    if st.checkbox("Show Summary Statistics"):
        st.write(df.describe())

    # Option to sort data by a selected column
    display_underline("Sort Data", size=15)
    sort_by = st.selectbox("Choose a column to sort by", options=df.columns)
    sort_order = st.selectbox("Sort order", options=["Ascending", "Descending"])
    if sort_order == "Ascending":
        st.write(df.sort_values(by=sort_by, ascending=True))
    else:
        st.write(df.sort_values(by=sort_by, ascending=False))

with g:
    
    #imag = Image.open('image/chart1.jpg')

    # Display the image in the Streamlit app
    st.image('image/chart1.jpg')
    st.write('---')
    display_underline('Accuracy', color = 'white', size = 15, bold = True)
    st.image('image/chart2.jpg')
    
    

with st.sidebar:
    display_underline('NASA apps challenge', color = 'black', size = 17)
    st.write('---')
    display_underline('- Our challenge is to find the seriousness of objects heading to earth.', color = 'black')
    
    








    





