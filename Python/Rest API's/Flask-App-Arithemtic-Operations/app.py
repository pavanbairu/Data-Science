from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/math", methods = ['POST'])
def math_ops():

    if request.method == 'POST':

        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if ops == 'add':
            result = "the sum of " +str(num1) + " and " + str(num2) + " is : " + str(num1+num2)

        if ops == 'subtract':
            result = "the sum of " +str(num1) + " and " + str(num2) + " is : " + str(num1-num2)

        if ops == 'multiply':
            result = "the sum of " +str(num1) + " and " + str(num2) + " is : " + str(num1*num2)

        if ops == 'divide':
            result = "the sum of " +str(num1) + " and " + str(num2) + " is : " + str(num1/num2)

        return render_template('results.html', result = result)


@app.route("/postman", methods = ['POST'])
def math_ops_1():

    if request.method == 'POST':

        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if ops == 'add':
            result = "the sum of " +str(num1) + " and " + str(num2) + " is : " + str(num1+num2)

        if ops == 'subtract':
            result = "the sum of " +str(num1) + " and " + str(num2) + " is : " + str(num1-num2)

        if ops == 'multiply':
            result = "the sum of " +str(num1) + " and " + str(num2) + " is : " + str(num1*num2)

        if ops == 'divide':
            result = "the sum of " +str(num1) + " and " + str(num2) + " is : " + str(num1/num2)

        return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")