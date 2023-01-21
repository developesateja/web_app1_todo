import streamlit as st  # this package helps display code on a web-browser.
# Streamlit is also popular for displaying info in graphical format on a webpage
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["input_todo"] + "\n"    # session_state stores widget info displayed on window
    # It has structure similar to dictionary
    print(f"New todo to add is: {new_todo}")
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("To-Do app")
st.subheader("This is my todo app")
st.write("Use this app to add a ToDo and mark it complete")

for index, item_todo in enumerate(todos):
    is_checked = st.checkbox(item_todo, key=item_todo)
    # key is unique and is same as the todo name itself
    if is_checked:  # if the checkbox is checked
        print(f"todo to complete: {item_todo}")
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item_todo]     # delete checkbox item from session so that it wont be displayed next time
        st.experimental_rerun() # rerun the script from here onwards, to render the whole GUI again

st.text_input(label="todo", label_visibility='hidden', placeholder="Enter a todo",
              on_change=add_todo, key="input_todo")
# on_change acts like event and calls the callback function provided

st.session_state

print("Hello: "
      "This will be printed on cmd line whenever webpage loads/ reloads")


