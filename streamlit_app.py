import streamlit as st

st.set_page_config(page_title="OlimpHub", page_icon="🔥")

st.title("🔥 OlimpHub")
st.subheader("Привет, Аружан! 👋")

# Стрики и прогресс
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Твой Стрик", value="4 дня", delta="🔥")
with col2:
    st.metric(label="Задач решено", value="12", delta="+2 сегодня")

st.markdown("---")

st.write("### 🎯 Задание на сегодня")
st.info("Решить 3 задачи по Математике (Тема: Квадратные уравнения)")

if st.button("🚀 Начать тренировку"):
    st.switch_page("pages/2_Practice.py")

st.write("### 📊 Твой прогресс на этой неделе")
st.progress(65)
