# E-Library API

This is an **E-Library API** built with **FastAPI** in Python. The API allows users to manage a library system, including features for adding, updating, retrieving books and user information and borrowing and returning books.

---

## Features

- Add new books and users
- Update book/user details
- Retrieve book/user details
- Delete books
- Deavtivate user accounts
- Borrowing and Returning books

---

## Setting Up the Project

### Step 1: Clone the Repository

To start, open CMD and locate a directory to clone into, preferably your downloads folder using the code:

cd Downloads

then clone the repository to your local machine:

git clone https://github.com/AmusanAyodeji/E-Library-API-Made-With-FastAPI.git

---

### Step 2: Open the project

Open your code editor from the folder where main.py is. If your using VS Code, right click then click "open with code"

---

### Step 3: Creating a virtual environment and Installing requirements

Run the following code in your code editor terminal:

python -m venv venv

For Windows:

.\venv\Scripts\activate

For Mac:

source venv/bin/activate

You'll know you've done it right if your terminal prompt starts with (venv)

Then run this code:

pip install -r requirements.txt

and wait for the requirements to finish downloading

---

## Running the API

### Step 1: Running the server

In your code editor terminal, Run:

uvicorn main:app --reload

### Step 2: Access the API Documentation

Once the server is running, open your web browser and navigate to:

http://127.0.0.1:8000/docs

You are free to test operations in the E-Library API

## Stopping the Server

In your code editor terminal, Press Ctrl + C

To deactivate the virtual environment, type deactivate then hit Enter
