from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', rows=int(8), columns=int(8), color1 = "red", color2 = "black")

@app.route('/<int:x>')
def index2(x):
  return render_template('index.html', rows = int(x), columns=int(8), color1 = "red", color2 = "black")


@app.route('/<int:x>/<int:y>')
def index3(x, y):
  return render_template('index.html', rows = int(x), columns=int(y), color1 = "red", color2 = "black")


@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def index4(x,y,color1,color2):
  return render_template('index.html', rows = int(x), columns=int(y), color1 = color1, color2 = color2)

if __name__=="__main__":
  app.run(debug=True)
