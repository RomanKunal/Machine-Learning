from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World it is my youtube channel"

@app.route('/call')
def call():
   return "Hello World it is my youtube channel opened by three engineering friends"


if __name__ == '__main__':
   app.run(debug=True)