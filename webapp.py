from flask import Flask #import the flask framework 
app = Flask(__name__) #create new Flask app

@app.route('/') # this is a decorator , adding on top of function to turn into route.
# if you go to your website with a slash at the end then nothing else, hell_world function will be run
#if we were to add the function below and go localhost:5000/test, we will see the word test
#@app.route('/test')
#def testing():
#return 'test'

def header():
    return 'Patrick & Python'


if __name__ == '__main__': # essentially just stating to run this code only if I ran it
# __name__ is a variable that python auto creates and is equal to __main__ when you run the code vs another script running the code
    app.run(host='0.0.0.0') # runs the app variable you created in line 2, the host we past in makes it run on localhost

    
