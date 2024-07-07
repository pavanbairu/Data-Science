# Import necessary modules from Flask
from flask import Flask
from flask import request

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the base URL /welcome
@app.route("/welcome")
def hello():
    # Function to handle requests to /welcome
    return "welcome to flask API Pavan Bairu"

# Define a route for the URL /welcome1
@app.route("/welcome1")
def project():
    # Function to handle requests to /welcome1
    return "welcome to new project"

# Define a route for the URL /addition
@app.route("/addition")
def addition():
    try:
        # Retrieve query parameters x and y, defaulting to 0 if not provided
        a = int(request.args.get("x", 0))
        b = int(request.args.get("y", 0))
        # Calculate the sum of a and b
        result = a + b
        # Return the result as a formatted string
        return "Addition for the user inputs {} + {} = {}".format(a, b, result)
    except ValueError:
        # Handle the case where the input values are not valid integers
        return "Invalid input. Please provide valid integers for x and y."

# Define a route for the URL /input_url
@app.route("/input_url")
def url_input():
    # Retrieve the query parameter x
    data = request.args.get('x')
    # Return the input data as a formatted string
    return "the input from user {}".format(data)

# Define another route for the URL /addition
# Note: This will override the previous /addition route
@app.route("/addition")
def add():
    # Return a fixed addition result
    return "addition {}".format(10 + 5)

# Check if the script is run directly
if __name__ == "__main__":
    # Run the Flask app on all available IP addresses
    app.run(host="0.0.0.0")
