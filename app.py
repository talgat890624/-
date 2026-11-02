import streamlit as st
import random
st.set_page_config(page_title="Словарь 50 слов", page_icon="🎮")

words = {"Кринж": "Чувство неловкости", "Краш": "Человек который нравится", "Вайб": "Атмосфера", "Имба": "Очень круто", "Рофл": "Шутка", "Сигма": "Независимый", "Ризз": "Очарование", "Скуф": "Не следит за собой", "Тильт": "Раздражение", "Делулу": "Живет иллюзиями", "Слей": "Потрясающе", "База": "Мнение", "Флексить": "Хвастаться", "Хайп": "Популярность", "Чиллить": "Отдыхать", "Токсик": "Негативный", "Гостинг": "Игнор", "Пруф": "Доказательство", "Фейк": "Подделка", "Спойлер": "Раскрытие сюжета", "Лойс": "Лайк", "Муд": "Настроение", "Шеймить": "Стыдить", "Буллинг": "Травля", "Хейт": "Ненависть", "Хейтер": "Критик", "Лейм": "Скучно", "Топчик": "Отлично", "Лакшери": "Роскошь", "Факап": "Провал", "Апгрейд": "Улучшение", "Крашиться": "Быть влюбленным", "Стенить": "Быть фанатом", "Шипперить": "Сводить парой", "Фандом": "Сообщество фанатов", "Эстетика": "Красота стиля", "Рандом": "Случайно", "Войбить": "Кайфовать", "Саспенс": "Напряжение", "Лютый": "Очень сильный", "Душнила": "Придира", "Инсайт": "Понимание", "Релейт": "Узнавать себя", "Софт": "Мягкий", "Кэнселинг": "Осуждение", "Пикми": "Выделяется", "Нормис": "Обычный", "Аура": "Впечатление", "Делулу-из-солулу": "Вера в мечту", "NPC": "Живет шаблонно"}

st.title("📚 50 СЛОВ МОДА И ТРЕНД 2026")
st.caption("Сделано в Актау | Проект Талгата")
tab1, tab2 = st.tabs(["📖 Словарь", "🎮 Игра"])
with tab1:
    search = st.text_input("🔍 Поиск:", placeholder="Напиши Кринж, Сигма...")
    count = 0
    for w,m in words.items():
        if search.lower() in w.lower() or search.lower() in m.lower() or search == "":
            with st.expander(f"🔹 {w}"):
                st.write(m)
            count += 1
    st.info(f"Найдено: {count} слов")
with tab2:
    st.subheader("Угадай что значит слово!")
    if 'q' not in st.session_state:
        st.session_state.q = random.choice(list(words.items()))
        st.session_state.score = 0
    q_word, q_true = st.session_state.q
    st.markdown(f"### Что значит: **{q_word}** ?")
    options = [q_true] + random.sample([v for k,v in words.items() if v != q_true], 3)
    random.shuffle(options)
    choice = st.radio("Выбери ответ:", options, key=str(random.random()))
    if st.button("Ответить ✅"):
        if choice == q_true:
            st.success("Правильно! +1 балл 🎉")
            st.session_state.score += 1
        else:
            st.error(f"Неа! Правильно: {q_true}")
        st.session_state.q = random.choice(list(words.items()))
        st.rerun()
    st.metric("Твои баллы", st.session_state.score)
    if st.button("Новая игра 🔄"):
        st.session_state.score = 0
        st.session_state.q = random.choice(list(words.items()))
        st.rerun()
