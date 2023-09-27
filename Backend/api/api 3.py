#http://localhost:5000/index
#used the above link to get the output
from flask import Flask, jsonify

app = Flask(__name__)

# Initialize a counter
count = 0

@app.route('/index')
def index():
    global count
    count += 1
    response_data = {
        "response": "Hello World!",
        "times-requested": count
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run()
