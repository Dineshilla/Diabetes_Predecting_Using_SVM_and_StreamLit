
import numpy as np
import pickle
import streamlit as st



def predict(input_data):
    load_clf = pickle.load(open("C:/Users/DINESH/trained_model.sav","rb"))

    pred_test = load_clf.predict(input_data)
    
    if pred_test == 1:
        return "Diabetes"
    elif pred_test == 0:
        return "Not Diabetes"
    

def main():
    st.title("Diabetes Predicting Model")
    
    						
    Age = st.text_input("Enter your Age")
    Pregnancies = st.text_input("Enter Pregnancies ")
    Glucose = st.text_input("Enter Glucose Level")
    BloodPressure = st.text_input("Enter BloodPressure ")
    SkinThickness = st.text_input("Enter SkinThickness ")
    Insulin = st.text_input("Enter Insulin Level ")
    BMI = st.text_input("Enter BMI ")
    DiabetesPedigreeFunction = st.text_input("Enter DiabetesPedigreeFunction ")
    
    
    predicted_ans = ""
    
    if st.button("Diabetes Test Results"):
        predicted_ans = predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
    st.success(predicted_ans)
    
if __name__ == '__main__' :
    main()