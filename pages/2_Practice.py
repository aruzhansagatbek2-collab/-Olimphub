import streamlit as st

st.title("✍️ Practice: Math")
st.write("### Задача №1")
st.latex(r"n^2 - 5n + 6 = 0")
st.write("Найдите все целые значения $n$.")

answer = st.text_input("Твой ответ (через запятую):")

if st.button("Check answer"):
    if "2" in answer and "3" in answer:
        st.success("✅ Правильно! Ты получил +10 очков.")
        st.balloons()
    else:
        st.error("❌ Попробуй еще раз. Подсказка: используй теорему Виета.")
