import streamlit as st

st.title("📝 Регистрация в OlimpHub")

with st.form("onboarding"):
    name = st.text_input("Как тебя зовут?")
    grade = st.select_slider("Выбери класс", options=list(range(5, 12)))
    
    st.write("Выбери свои предметы:")
    math = st.checkbox("Математика")
    phys = st.checkbox("Физика")
    chem = st.checkbox("Химия")
    bio = st.checkbox("Биология")
    
    submitted = st.form_submit_button("Start training")
    if submitted:
        st.success(f"Добро пожаловать, {name}! Твой план обучения готов.")
        st.balloons()
