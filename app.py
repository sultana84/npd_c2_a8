from flask import Flask
import datetime

now = datetime.datetime.now()

app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/helloworld')
def helloworld():
    return 'Hello, World'

@app.route('/NigharSultana')
def NigharSultana():
    return 'Nighar Sultana'

@app.route('/currentservertime')
def currentservertime():
    return now.strftime("%Y%m%dT%H%M%S")
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)


