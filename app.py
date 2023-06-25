from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':"Data Analyst I",
    'location':"Bengaluru,India",
    'salary':"Rs. 15,00,000"
  },
  {
    'id':2,
    'title':"Data Engineer ",
    'location':"Pune,India",
    'salary':"Rs. 13,00,000"
  },
  {
    'id':3,
    'title':"Business Analyst",
    'location':"Hyderabad,India",
    'salary':"Rs. 20,00,000"
  },
  {
    'id':4,
    'title':"Data Scientist",
    'location':"Bengaluru,India",
    'salary':"Rs. 25,00,000"
  }
]

@app.route("/")
def index():
  return render_template('home.html',jobs=JOBS,company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)