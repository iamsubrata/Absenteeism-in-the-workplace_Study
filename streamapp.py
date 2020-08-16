## Created by Subrata Paul , 15th Aug,2020 

import streamlit as st
import joblib
import numpy as np


#st.title("Predicting Absent Hours for Employees")
#header
#st.header("Header is head")
#success
#st.success("success will come")
#help in python 
#st.subheader('Input Parameters for Absent Hours Prediction')

#Converting the data to the codes

def get_value(r,data_label):
    print(data_label[r])
    return data_label[r]

# Reason names with thier codes
reason_label={'Certain infectious and parasitic diseases' : 1 , 
'Neoplasms' : 2 , 
'Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism' : 3 , 
'Endocrine, nutritional and metabolic diseases' : 4 , 
'Mental and behavioural disorders' : 5 , 
'Diseases of the nervous system' : 6 , 
'Diseases of the eye and adnexa' : 7 , 
'Diseases of the ear and mastoid process' : 8 , 
'Diseases of the circulatory system' : 9 , 
'Diseases of the respiratory system' : 10 , 
'Diseases of the digestive system' : 11 , 
'Diseases of the skin and subcutaneous tissue' : 12 , 
'Diseases of the musculoskeletal system and connective tissue' : 13 , 
'Diseases of the genitourinary system' : 14 , 
'Pregnancy, childbirth and the puerperium' : 15 , 
'Certain conditions originating in the perinatal period' : 16 , 
'Congenital malformations, deformations and chromosomal abnormalities' : 17 , 
'Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified' : 18 , 
'Injury, poisoning and certain other consequences of external causes' : 19 , 
'External causes of morbidity and mortality' : 20 , 
'Factors influencing health status and contact with health services.' : 21 , 
'Patient follow-up' : 22 , 
'Medical Consultation' : 23 , 
'Blood donation' : 24 , 
'Laboratory Examination' : 25 , 
'Unjustified Absence' : 26 , 
'Physiotherapy' : 27 , 
'Dental Consultation' : 28 , 
'No Reason' : 0 }

#Predict function

def predict(v_reason,Distance,BMI):
    
    #Loading the model dump to predict
    model=joblib.load('Absent_Hour_Predictor_model.ml')
    predicted_hours=model.predict([[v_reason,Distance,BMI]])
    return predicted_hours
    
    
def main():
    
    
    html_temp = """
    <div style="background-color:yellow;padding:10px">
    <h2 style="color:green;text-align:center;">Predicting Absent Hours for Employees </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.subheader('Input Parameters')
    

    #Input for Reason for Absence of the Employee

    #reason_default=tuple(reason_label.keys())+('Select an option',)
    reason=st.selectbox("Select Reason for Absense ", tuple(reason_label.keys()))
    #reason=st.selectbox("Select Reason for Absense ", reason_default,format_func=lambda x:'Select an option' if x =='Select an option' else      x)
    st.write('You selected the reason as :',reason)
    ##if reason !='Select an option':
    v_reason=get_value(reason,reason_label)
    st.write('Reason Code : ',v_reason)

    #Input for Employees Distance from Office
    Distance=st.number_input('Distance from Residence to Work',1.0,100.0)
    st.write('You Selected Distance as :',Distance)

    #Input for Employess Body Mass Index
    BMI=st.number_input('Enter a BMI index',0.0,100000.0)
    st.write('You selected Body Mass Index as :',BMI)
    pred_hours=''
    
    if st.button('Predict Absent Hours'):
        
        pred_hours=predict(v_reason,Distance,BMI)
        st.success('Prediction {}'.format(pred_hours[0]))




    
   
    
    
if __name__=='__main__':
    main()





