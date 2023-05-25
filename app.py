from flask import Flask
FAI=Flask(__name__)

@FAI.route('/wish')
def wish():
    return 'Hello World'   
@FAI.route('/hello')
def hello():
    return 'WelCome to web page'

if __name__=='__main__':
    FAI.run(debug=True)