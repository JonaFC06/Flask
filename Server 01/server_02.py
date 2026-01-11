from flask import Flask 

# Create an instance of the Flask Class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Create a dictionary to return as a response
    return {"message": "Hello World!"}