from flask import Flask
aws_key = "AKIAIOSFODNN7EXAMPLE"
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! This is my secure app."

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0') # nosec
