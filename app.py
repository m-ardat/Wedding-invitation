# Импорт библиотек
import streamlit as st
from PIL import Image

# Название
st.title("Приглашение на свадьбу")
# Добавляем боковую панель слева
st.sidebar.title("Приглашение на свадьбу")
# Добавляем кнопку-переключатель в боковую панель слева
list_button_name = ["Нажми кнопку, если хочешь увидеть котика!",
                    "Регистрация",
                    "Запрещёнка",
                    "Банкет",
                    "Мы вас любим!"]
button = st.sidebar.radio(label="Выберите кнопку:",
                               options=list_button_name,
                               index=0
                               )
# Условие
if button == list_button_name[0]:
    # загружаем картинку
    img_cat = Image.open(f"cat.jpg")
    # Уменьшаем размер изображения
    img_cat.thumbnail((1920, 1080))
    # Отображаем картинку используя Streamlit
    st.image(img_cat, use_column_width=True, output_format="JPG")
    st.text("Мяу!")

if button == list_button_name[1]:
    # показываем текст если checkbox1 выбран
    st.text("Дорогие родные и близкие!")
    st.text("Приглашаем вас на торжественную регистрацию нашего брака!")
    # загружаем картинку
    img1 = Image.open(f"Роял.jpg")
    # Уменьшаем размер изображения
    img1.thumbnail((720, 690))
    # Отображаем картинку используя Streamlit
    st.image(img1, use_column_width=True, output_format="JPG")
    # Текст
    st.text("Регистрация брака состоится в Особняке Роял.")
    st.text("- Адрес: Малая Ордынка, д.14, с.1;")
    st.text("- Ближайшие станции метро - Третьяковская и Полянка;")
    st.text("- Дата: 12.07.2024")
    st.text("- Время: с 15:20 до 15:40.")
    st.text("Для удобства предлагаем приехать чуть раньше.")
    st.text("Если вы будете опаздывать, не волнуйтесь и позвоните нам!")

if button == list_button_name[2]:
    checkbox, checkbox1, checkbox3, checkbox4, checkbox5 = False, False, False, False, False
    st.text("На территории Особняка Роял запрещено использовать:")
    forbidden_words = "конфетти, салюты, монеты, рис, принимать пищу, распивать алкогольные напитки"
    # Отображаем каждое слово на отдельной строке
    for word in forbidden_words.split(", "):
        st.text(f"- {word}")

if button == list_button_name[3]:
    checkbox, checkbox1, checkbox2, checkbox4, checkbox5 = False, False, False, False, False
    # загружаем картинку
    img2 = Image.open(f"bonappcafe.jpeg")
    # Уменьшаем размер изображения
    img2.thumbnail((720, 690))
    # Отображаем картинку используя Streamlit
    st.image(img2, use_column_width=True, output_format="JPEG")
    # Текст
    st.text("Вкусно поесть и выпить прохладного вина можно будет в ресторане BON APP cafe.")
    st.text("- Адрес: Никольская, 25, этаж 1;")
    st.text("- Ближайшие станция метро - Лубянка;")
    st.text("- Время: в ресторане ждем вас к 16:30.")
    st.text("Наша свадебная фотосессия закончится к пяти вечера,")
    st.text("поэтому подойдем в ресторан чуть позже.")
    st.text("Не переживайте, комфортно размещайтесь за нашим столиком,")
    st.text("забронированным заблаговременно.")

if button == list_button_name[4]:
    checkbox, checkbox1, checkbox2, checkbox3, checkbox5 = False, False, False, False, False
    # загружаем картинку
    img3 = Image.open(f"we.jpg")
    # Уменьшаем размер изображения
    img3.thumbnail((1920, 1080))
    # Отображаем картинку используя Streamlit
    st.image(img3, use_column_width=True, output_format="JPG")
    # Текст
    st.text("Ждем вас!")
    st.text("Ваши Максим и Алина.")

