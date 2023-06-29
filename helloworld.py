from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   speech = 'Welcome to my page.\nHow are you?'
   return speech

if __name__ == '__main__':
   app.run(post = 7980)