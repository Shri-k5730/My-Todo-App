import streamlit as st
import functions
from datetime import datetime
import pandas as pd

now = datetime.now()
current_time = now.strftime("%d-%m-%Y %H:%M:%S")

todos = functions.get_todos()
user_local = functions.get_user()


def add_user():
    user = st.session_state["new_user"] + " " + current_time + "\n"
    user_local.append(user)
    functions.write_user(user_local)


name = st.text_input(label="Enter your name/alias and press enter to continue:", on_change=add_user, key="new_user")

if len(name) != 0:

    def add_todo():
        todo = st.session_state["new_todo"] + "\n"
        todos.append(todo)
        functions.write_todos(todos)


    st.title("To-Do list")
    st.subheader("About app:")
    st.write("<font color = 'Green'>This is a basic todo app that let's users create tasks "
             "by entering in the text box"
             " and then mark it as complete by selecting the checkbox", unsafe_allow_html=True)
    st.text_input(label="Enter the to-do in the box below:", placeholder="Add a todo here!",
                  on_change=add_todo, key="new_todo")

    st.write("<i><font color = 'Red'>1. Pressing enter with no text in the box enters a blank todo!</i>"
             "<br><i><font color = 'Red'>2. Selecting the checkbox completes "
             "the to-do and removes it from the list!</i>",
             unsafe_allow_html=True)

    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.rerun()


st.write("<br><b><i>Last 5 users:</i></b><br>", unsafe_allow_html=True)
user_temp = pd.DataFrame(user_local)
user_temp.columns = ['Names']
st.dataframe(user_temp.tail(5), hide_index=True)


