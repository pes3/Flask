from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Open the URL in another tab, and then go to /hello/yourname'

@app.route('/hello/<name>') # name in the route url is a placeholder, any name you put in there will be passed into "hell_name" function

def hello_name(name):
    return 'Hello '+ name + '!'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
