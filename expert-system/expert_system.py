import streamlit as st
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

import streamlit as st

cold = ['headache', 'runny nose', 'sneezing', 'sore throat']
influenza = ['sore throat', 'fever', 'headache', 'chills', 'body ache']
typhoid = ['headache', 'abdominal pain', 'poor appetite', 'fever']
chicken_pox = ['rash', 'body ache', 'fever']
measles = ['fever', 'runny nose', 'rash', 'conjunctivitis']
malaria = ['fever', 'sweating', 'headache', 'nausea', 'vomitting', 'diarrhea']

care_instructions = {
    'cold': 'Avoid going out in cold temperatures and rest well for the next 2-3 days. Try taking steam and drink plenty of water. Avoid having cold food or drinks.',
    'influenza': 'Get plenty of rest, drink fluids, and take antiviral medications as prescribed by your doctor.',
    'typhoid': 'Take antibiotics as prescribed by your doctor, get plenty of rest, and drink fluids.',
    'chicken_pox': 'Keep the rash clean and dry, take over-the-counter pain relievers, and use calamine lotion to reduce itching.',
    'measles': 'Get plenty of rest, drink fluids, and take over-the-counter pain relievers. Avoid contact with others to prevent spreading the disease.',
    'malaria': 'Take prescribed antimalarial medications, rest, drink fluids, and use mosquito repellent to prevent further mosquito bites.'
}

style = """
    <style>
        body {
            background-color: #282a36;
            color: #ebeb12;
        }
        .stButton button {
            background-color: #bd93f9;
            color: #f8f8f2;
            font-weight: bold;
            border-radius: 0.25rem;
            padding: 0.5rem 1rem;
            border: none;
            margin-top: 1rem;
        }
        .stButton button:hover {
            background-color: #6272a4;
            cursor: pointer;
        }
    </style>
"""

st.markdown(style, unsafe_allow_html=True)

st.title("Medical Expert System")

symptoms = list(set(cold + influenza + typhoid + chicken_pox + measles + malaria))
selected_symptoms = [symptom for symptom in symptoms if st.checkbox(symptom)]

if st.button("Submit"):
    disease_similarity = {'cold' : 0,
     'influenza' : 0 , 
     'typhoid':0 ,
     'chicken_pox' : 0, 
     'measles':0, 
     'malaria':0 }

    if selected_symptoms:
        all_symptoms_dict = {k:v for v,k in enumerate(symptoms)}

        selected_symptoms_vector = np.zeros(len(symptoms))

        for symptom in selected_symptoms:
            selected_symptoms_vector[all_symptoms_dict[symptom]] = 1
        
        vectors = [np.zeros(len(symptoms)) for i in range(6)]
        
        vectors[0][[all_symptoms_dict[x] for x in cold]] = 1
        vectors[1][[all_symptoms_dict[x] for x in influenza]] = 1
        vectors[2][[all_symptoms_dict[x] for x in typhoid]] = 1
        vectors[3][[all_symptoms_dict[x] for x in chicken_pox]] = 1
        vectors[4][[all_symptoms_dict[x] for x in measles]] = 1
        vectors[5][[all_symptoms_dict[x] for x in malaria]] = 1

        for i, disease in enumerate(disease_similarity.keys()):
            similarity_score = cosine_similarity([selected_symptoms_vector], [vectors[i]])[0][0]
            disease_similarity[disease] = similarity_score


        most_similar_disease = max(disease_similarity, key=disease_similarity.get)
        st.write(f"Your symptoms suggest that you might have {most_similar_disease}")
        st.write("")
        st.write("Care suggestions:")
        st.write(f"I suggest you to {care_instructions[most_similar_disease]}")

    else:
        st.error("Add atleast one symptom")