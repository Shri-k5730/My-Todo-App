import streamlit as st
import functions
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%d-%m-%Y %H:%M:%S")

todos = functions.get_todos()

st.write(st.experimental_user.email)

with open('web_app1/userlog.txt', 'r') as file_local:
    user_local = file_local.readlines()
    user_local.append(st.experimental_user.email)


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
        st.rerun()


# Check historical user log


# for index, user in enumerate(user_local):
#     with open('web_app1/userlog.txt', 'w') as file:
#         file.writelines(user_local[-200:])
#
# st.write(user_local[-5:])

