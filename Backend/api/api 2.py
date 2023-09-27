#API Q2
#used the above link to get the output
from flask import Flask

app = Flask(__name__)

# Initialize a counter
counter = 0

@app.route('/index')
def index():
    global counter
    counter += 1
    return f'Hello World! You have requested this endpoint {counter} times!'

if __name__ == '__main__':
    app.run()