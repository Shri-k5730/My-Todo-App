import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo list")
st.subheader("This is my todo list app")
st.text_input(label="Enter the to-do in the box below:", placeholder="Add a todo here!",
              on_change=add_todo, key="new_todo")

st.write("<i><font color = 'Red'>Pressing enter with no text in the box enters a blank todo!</i>"
         "<br><i><font color = 'Red'>Selecting the checkbox completes the to-do and removes it from the list!</i>",
         unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()