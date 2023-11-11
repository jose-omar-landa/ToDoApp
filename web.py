import streamlit as st
from modules import functions


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is a todo list app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new item...", on_change=add_todo, key="new_todo")

st.session_state
