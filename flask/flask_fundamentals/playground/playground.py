from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
  return render_template("index.html", num = int(3))

@app.route('/play/<int:n>')
def index2(n):
  return render_template("index.html", num = n)

@app.route('/play/<int:n>/<color>')
def index3(n, color):
  return render_template("index.html", num = n, color = color)

if __name__=="__main__":
  app.run(debug=True)
