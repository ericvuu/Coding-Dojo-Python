from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World!"

@app.route('/dojo')
def printDojo():
  return "Dojo"

@app.route('/say/<name>')
def greetPerson(name):
  return "Hi " + name + "!"

@app.route('/repeat/<int:num>/<string>')
def repeatStr(num, string):
  return string * int(num)

@app.errorhandler(404)
def not_found(error):
    return "Sorry! No response. Try again.", 404

# if __name__=="__main__":
app.run()
# debug=True
