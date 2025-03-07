import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero"

@app.route("/")
def home():
    return "Welcome to the Calculator API!"

@app.route("/calculate", methods=["GET"])
def calculate():
    try:
        x = float(request.args.get("x"))
        y = float(request.args.get("y"))
        op = request.args.get("op")
        
        if op == "+":
            result = add(x, y)
        elif op == "-":
            result = subtract(x, y)
        elif op == "*":
            result = multiply(x, y)
        elif op == "/":
            result = divide(x, y)
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

