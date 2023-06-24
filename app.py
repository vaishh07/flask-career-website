from flask import Flask, render_template,json

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':"Data Analyst I",
    'location':"Bengaluru,India",
  },
  {
    'id':2,
    'title':"Data Analyst II",
    'location':"Bengaluru,India",
  },
  {
    'id':3,
    'title':"Data Analyst III",
    'location':"Bengaluru,India",
  },
  {
    'id':4,
    'title':"Data Scientist",
    'location':"Bengaluru,India",
  }
]

@app.route("/")
def index():
  return render_template('home.html',jobs=JOBS)
  

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)