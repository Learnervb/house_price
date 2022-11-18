import numpy as np
import pandas as pd
import pickle
import streamlit as st

pickle_in = open("reg_model.pkl", "rb")
regressor = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT):
    
    """Let's calculate the price of the house
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: CRIM
        in: query
        type: number
        required: true
      - name: ZN
        in: query
        type: number
        required: true
      - name: INDUS
        in: query
        type: number
        required: true
      - name: CHAS
        in: query
        type: number
        required: true
      - name: NOX
        in: query
        type: number
        required: true
      - name: RM
        in: query
        type: number
        required: true
      - name: AGE
        in: query
        type: number
        required: true
      - name: DIS
        in: query
        type: number
        required: true
      - name: RAD
        in: query
        type: number
        required: true
      - name: TAX
        in: query
        type: number
        required: true
      - name: PTRATIO
        in: query
        type: number
        required: true
      - name: B
        in: query
        type: number
        required: true
      - name: LSTAT
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=regressor.predict([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])
    return prediction

def main():
    st.title("Happy Home")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> House Price Prediction </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    CRIM = st.number_input("CRIM",format="%.5f")
    ZN = st.number_input("ZN",format="%.5f")
    INDUS = st.number_input("INDUS",format="%.5f")
    CHAS = st.number_input("CHAS",format="%.5f")
    NOX = st.number_input("NOX",format="%.5f")
    RM = st.number_input("RM",format="%.5f")
    AGE = st.number_input("AGE",format="%.5f")
    DIS = st.number_input("DIS",format="%.5f")
    RAD = st.number_input("RAD",format="%.5f")
    TAX = st.number_input("TAX",format="%.5f")
    PTRATIO = st.number_input("PTRATIO",format="%.5f")
    B = st.number_input("B",format="%.5f")
    LSTAT = st.number_input("LSTAT",format="%.5f")
    result=0
    if st.button("Predict"):
        result=predict_note_authentication(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
    st.success('The Price of the House is {} lakhs'.format(result))
    if st.button("About"):
        st.text("Lets have your own house")
        st.text("Built your dreams")
    

if __name__=='__main__':
    main()