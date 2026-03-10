import streamlit as st

st.title("📅 Предстоящие Олимпиады в КЗ")

olimps = [
    {"name": "Республиканская олимпиада", "date": "Март 2024", "subj": "Все предметы"},
    {"name": "IZhO (Жаутыковская)", "date": "Январь 2024", "subj": "Математика, Физика, Информатика"},
    {"name": "IQanat", "date": "Июнь 2024", "subj": "Отбор для сельских школ"},
]

for o in olimps:
    with st.expander(f"📌 {o['name']}"):
        st.write(f"**Дата:** {o['date']}")
        st.write(f"**Предметы:** {o['subj']}")
        if st.button("Записаться", key=o['name']):
            st.info("Вы добавлены в список участников!")
