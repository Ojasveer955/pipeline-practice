from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "The CI/CD Pipeline worked! V1 is live."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)