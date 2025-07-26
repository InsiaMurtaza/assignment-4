import streamlit as st

st.markdown(
    """
    <style>
    /* Set default font color for the entire app */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #1E90FF;
        color: white!important;
    }

     /* Optional: Label text for input fields */
    label, .stTextInput > div > label {
        color: white!important;
    }

    div.stButton > button {
        background-color: #FFD700;
        color: black!important;
        font-weight: bold;
    }
    div.stButton > button:hover {
    background-color: #FFB800; /* Darker gold or orange shade */
    color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True)

def styled_message(message, type="success", font_color="#FFFFFF"):
    if type == "success":
        bg_color = "green"  
        # icon = "✅"
    elif type == "error":
        bg_color = "white"
        # icon = "❌"

    st.markdown(f"""
            <div style="background-color: {bg_color}; 
                padding: 10px; 
                border-radius: 6px;
                color: {font_color}; 
                font-size: 16px;">
                {message}
            </div>
            """, unsafe_allow_html=True)



st.title("BMI Calculator ⚖")
st.markdown("### An amazing app to calculate your Body Mass Index")


unit_height = st.selectbox("Choose unit for height",["Meters","Centimeters","Feet","Inches"])

height = st.number_input("Enter your height: ")

unit_weight = st.selectbox("Choose unit for wright",["Kilograms","Pounds"])

weight = st.number_input("Enter your weight: ")

def calc_bmi(height:float,weight:float,unit_height:float,unit_weight:float):

    height_conversion = {
        "Meters": 1,
        "Centimeters": 0.01,
        "Feet": 1 / 3.281,
        "Inches": 1 / 39.372
    }

    weight_coversion = {
      "Kilograms": 1,
      "Pounds" : 1/2.20462
    }
    
    height_in_m = height * height_conversion[unit_height]
    weight_in_kg = weight * weight_coversion[unit_weight]
    
    bmi:float = weight_in_kg/(height_in_m**2)
    return round(bmi,2)
    

st.button("Calculate BMI")
if st.button:
    if weight == 0.00 or height == 0.00:
        styled_message("Please enter both height and weight before clicking the button","error","black")
    else:
        result = calc_bmi(height,weight,unit_height,unit_weight)
        styled_message(f"Your BMI is {result}","success","white")

