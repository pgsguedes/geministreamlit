import streamlit as st
import os
#from dotenv import load_dotenv
import google.generativeai as genai

# Carregar variáveis
# load_dotenv(dotenv_path='/Users/pgsgu/GeminiAPI/.env.py')
# API_KEY = os.getenv("api_key")
API_KEY ="AIzaSyBVp4Db6wkvep6M98sSk9-fxhzVakHopsE"
genai.configure(api_key=API_KEY)

# Carregar Função gemini-pro model
def gemini_pro():
    model = genai.GenerativeModel('gemma-3n-e4b-it')
    return model
# Colocar Titulo e icone
st.set_page_config(
    page_title="Chat Bot Gemini",
    page_icon='icon.ico',
    layout='centered',
    initial_sidebar_state='expanded'
)
def roleForStreamlit(user_role):
    if user_role == 'model':
        return 'assistant'
    else:
        return user_role

model = gemini_pro()
if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = model.start_chat(history=[])
st.title('TalkBot - Paulo Guedes')
    # DISPLAY DO CHAT HISTORY
for message in st.session_state.chat_history.history:
        with st.chat_message(roleForStreamlit(message.role)):
            st.markdown(message.parts[0].text)
    # Pegar user input
user_input = st.chat_input('Informe o assunto :')

if user_input:
        st.chat_message('user').markdown(user_input)
        response= st.session_state.chat_history.send_message(user_input)
        with st.chat_message('assistant'):
            st.markdown(response.text)
