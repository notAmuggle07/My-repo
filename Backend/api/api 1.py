#http://localhost:5000/index
#used the above link to get the output
# API Q1
from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
    return 'Hello World'

# Run the Flask app when the script is executed directly
app.run()