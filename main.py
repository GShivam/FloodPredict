from flask import Flask,render_template, request
app = Flask(__name__)
import sub
import numpy



@app.route('/')
def hello_world():
  return  render_template("frontpage.html")

@app.route('/hello', methods = ['GET', 'POST'])
def hello_world1():
  f= = request.files['file']
  
  return  render_template("frontpage.html")



if __name__ == '__main__':
  app.run()
