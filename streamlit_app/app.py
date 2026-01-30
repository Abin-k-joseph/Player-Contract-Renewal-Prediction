
import pandas as pd
import streamlit as st
import joblib


def model_creation():

    model = joblib.load('contract_model.jb')

    st.title("⚖️Player Renewal Decision Engine")
    st.caption("     Built for Scouting Teams & Sporting Directors")


    input_data={}

        
    st.subheader("Profile")

    position_map = {
        'Forward': 1,
        'Midfielder': 3,
        'Defender': 0,
        'GoalKeeper': 2
    }

    continent_map = {
        'Asia': 1,
        'Europe': 2,
        'Africa': 0,
        'South America': 3
    }

    required_field=['Age','Position','Continent','Defensive_Impact','Market_Value_M']


    player_name = st.text_input("Player Name")
    input_data['Age'] = st.number_input('Age', min_value=18, step=1)

    selected_postion=st.selectbox('Position',list(position_map.keys()))

    input_data['Position'] = position_map[selected_postion]

    selected_continent = st.selectbox('Continent',list(continent_map.keys()))

    input_data['Continent'] = continent_map[selected_continent]



    st.sidebar.header("🔍Scouting Performance Data")



    input_data['Minutes_Played'] = st.sidebar.number_input('Minutes Played', max_value=4000)
    input_data['Goals'] = st.sidebar.number_input('Goals', max_value=100)
    input_data['Assists'] = st.sidebar.number_input('Assists', max_value=100)
    input_data['Defensive_Impact'] = st.sidebar.slider('Defensive Impact', 0, 100, 50)
    input_data['Injury_Days'] = st.sidebar.number_input('Injury Days', max_value=365)
    input_data['Market_Value_M'] = st.sidebar.number_input('Market Value (€M)', step=0.1)
    input_data['Contract_Years_Left'] = st.sidebar.number_input('Contract Years Left', min_value=0, max_value=5)
    input_data['Coach_Trust_Score'] = st.sidebar.slider('Coach Trust Score', 0, 100, 50)
    if selected_postion == 'GoalKeeper':
        input_data['Saves'] = st.sidebar.number_input('GK Saves', max_value=4000)
    else:
        input_data['Saves'] = 0

    input_data['Attack_Contribution'] = input_data['Goals'] + input_data['Assists']

    input_data['Trust_Adjusted_Usage'] = (
        input_data['Minutes_Played'] * (input_data['Coach_Trust_Score'])
    )

    input_data['Injury_Risk_Index'] = (
        input_data['Injury_Days'] / input_data['Age']
        if input_data['Age'] > 0 else 0
    )

    input_data['GK_Effectiveness'] = (
        input_data['Saves'] / input_data['Minutes_Played']
        if input_data['Minutes_Played'] > 0 else 0
    )

    if st.button('Predict'):

        missing_fields = [i for i in required_field if input_data.get(i) in [None,0]]

        if missing_fields:
            st.warning(f"⚠️ Please fill in the following fields before predicting: {', '.join(missing_fields)}")
        else:
            input_df = pd.DataFrame([input_data])

            prediction = model.predict(input_df)[0]
            probability = model.predict_proba(input_df)[0][1]

            st.subheader("Prediction Result")

            if prediction == 1:
                st.success(f"✅ Contract should be RENEWED for {player_name}")
            else:
                st.error(f"❌ Contract should NOT be renewed for {player_name}")

            if probability > 0.75:
                st.success(f"🟢 HIGH CONFIDENCE RENEW : {probability:.2%}")
            elif probability > 0.5:
                st.warning(f"🟡 BORDERLINE DECISION : {probability:.2%}")
            else:
                st.error(f"🔴 DO NOT RENEW : {probability:.2%}")

def main():
    st.set_page_config(page_title='Contract Renewal Predictor',
                       page_icon='assets/shoot.png',
                       initial_sidebar_state='expanded'
                       )
    model_creation()

if __name__ == '__main__':
    main()