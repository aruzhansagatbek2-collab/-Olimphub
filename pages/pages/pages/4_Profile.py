import streamlit as st

st.title("👤 Личный кабинет")

st.write("**Имя:** Аружан")
st.write("**Предметы:** Математика, Химия")
st.write("**Уровень:** Intermediate")

st.divider()

st.write("### Статистика")
chart_data = {"Math": 45, "Chemistry": 15, "Physics": 5}
st.bar_chart(chart_data)

if st.button("Выйти из аккаунта"):
    st.warning("Сессия завершена")
