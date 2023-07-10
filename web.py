import streamlit as st
from modules.files import get_todos, write_todos

st.title('My Todo App')
st.subheader('This is my todo app.')
st.write('This app is to increase your productivity.')


todos = get_todos()

for todo in todos:
    st.checkbox(todo)


def add_todo():
    todo_local = st.session_state['new_todo']
    todos.append(todo_local + '\n')
    write_todos(todos)
    st.session_state['new_todo'] = ''


st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")