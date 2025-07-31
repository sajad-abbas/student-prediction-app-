
import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open("model.pkl", "rb"))

st.title("نموذج تنبؤ نجاح الطالب")

study_hours = st.number_input("عدد ساعات الدراسة", min_value=0.0, max_value=24.0, step=0.5)
attendance = st.number_input("نسبة الحضور", min_value=0, max_value=100, step=1)

if st.button("تنبأ"):
    data = np.array([[study_hours, attendance]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ الطالب متوقع أن ينجح")
    else:
        st.error("❌ الطالب متوقع أن يرسب")
