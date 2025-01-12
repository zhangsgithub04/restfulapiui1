import streamlit as st
import requests

# API endpoint URL
api_url = "https://en8mbz3dp3.execute-api.us-east-1.amazonaws.com/default/szrestful1"

# Streamlit app title
st.title("User Management App")

# Create a user
def create_user(name, age):
    payload = {"name": name, "age": age}
    response = requests.post(f"{api_url}", json=payload)
    if response.status_code == 201:
        st.success("User created successfully!")
        st.json(response.json())
    else:
        st.error("Error creating user")
        st.error(response.text)

# Read users
def read_users():
    response = requests.get(f"{api_url}")
    if response.status_code == 200:
        users = response.json()
        st.write(users)
    else:
        st.error("Error reading users")
        st.error(response.text)

# Read user by ID
def read_user_by_id(user_id):
    response = requests.get(f"{api_url}/{user_id}")
    if response.status_code == 200:
        user = response.json()
        st.write(user)
    else:
        st.error("Error reading user")
        st.error(response.text)

# Update a user
def update_user(user_id, name, age):
    payload = {"name": name, "age": age}
    response = requests.put(f"{api_url}/{user_id}", json=payload)
    if response.status_code == 200:
        st.success("User updated successfully!")
        st.json(response.json())
    else:
        st.error("Error updating user")
        st.error(response.text)

# Delete a user
def delete_user(user_id):
    response = requests.delete(f"{api_url}/{user_id}")
    if response.status_code == 204:
        st.success("User deleted successfully!")
    else:
        st.error("Error deleting user")
        st.error(response.text)

# App navigation
nav = st.sidebar.selectbox("Navigation", ["Create User", "Read Users", "Read User by ID", "Update User", "Delete User"])

if nav == "Create User":
    name = st.text_input("Enter user name")
    age = st.number_input("Enter user age", min_value=18)
    if st.button("Create User"):
        create_user(name, age)

elif nav == "Read Users":
    read_users()

elif nav == "Read User by ID":
    user_id = st.number_input("Enter user ID", min_value=1)
    if st.button("Read User"):
        read_user_by_id(user_id)

elif nav == "Update User":
    user_id = st.number_input("Enter user ID", min_value=1)
    name = st.text_input("Enter new user name")
    age = st.number_input("Enter new user age", min_value=18)
    if st.button("Update User"):
        update_user(user_id, name, age)

elif nav == "Delete User":
    user_id = st.number_input("Enter user ID", min_value=1)
    if st.button("Delete User"):
        delete_user(user_id)
