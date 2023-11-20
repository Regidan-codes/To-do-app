import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state['new-todo'] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("To-Do App")
st.subheader("This is my To-Do App")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a new to-do...",
              on_change=add_todo, key="new-todo")