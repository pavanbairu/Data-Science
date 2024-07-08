# Import necessary modules from Flask
from flask import Flask, request, render_template, jsonify

# Initialize a Flask app
app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    # Render the home page template
    return render_template('index.html')

# Define the route to handle math operations from a web form
@app.route("/math", methods=['POST'])
def math_ops():
    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve the operation and numbers from the form data
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        # Perform the appropriate operation based on the 'ops' value
        # Check if the operation is addition
        if ops == 'add':
            result = "the sum of " + str(num1) + " and " + str(num2) + " is : " + str(num1 + num2)

        # Check if the operation is subtraction
        if ops == 'subtract':
            result = "the sum of " + str(num1) + " and " + str(num2) + " is : " + str(num1 - num2)

        # Check if the operation is multiplication
        if ops == 'multiply':
            result = "the sum of " + str(num1) + " and " + str(num2) + " is : " + str(num1 * num2)

        # Check if the operation is division
        if ops == 'divide':
            result = "the sum of " + str(num1) + " and " + str(num2) + " is : " + str(num1 / num2)

        # Render the results page with the result
        return render_template('results.html', result=result)

# Define the route to handle math operations from a JSON request
@app.route("/postman", methods=['POST'])
def math_ops_1():
    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve the operation and numbers from the JSON data
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        # Perform the appropriate operation based on the 'ops' value
        # Check if the operation is addition
        if ops == 'add':
            result = "the sum of " + str(num1) + " and " + str(num2) + " is : " + str(num1 + num2)

        # Check if the operation is subtraction
        if ops == 'subtract':
            result = "the sum of " + str(num1) + " and " + str(num2) + " is : " + str(num1 - num2)

        # Check if the operation is multiplication
        if ops == 'multiply':
            result = "the sum of " + str(num1) + " and " + str(num2) + " is : " + str(num1 * num2)

        # Check if the operation is division
        if ops == 'divide':
            result = "the sum of " + str(num1) + " and " + str(num2) + " is : " + str(num1 / num2)

        # Return the result as a JSON response
        return jsonify(result)

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0")