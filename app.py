from flask import Flask, render_template

app = Flask(__name__)
JOBS =[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
     'salary' : 'Rs. 1,00,000'
  },
  {
    'id':2,
    'title':'python Developer',
    'location':'Mumbai, India',
     'salary' : 'Rs. 2,00,000'
  },
  {
    'id':3,
    'title':'Web developer',
    'location':'Pune, India',
     'salary' : 'Rs. 3,00,000'
  },
  {
    'id':4,
    'title':'java developer',
    'location':'Mumbai, India'
    
  }, {
    'id':5,
    'title':'game developer',
    'location':'Noida, India',
     'salary' : 'Rs. 5,00,000'
  },
]

@app.route("/")
def hello_world():
  return render_template('index.html',
                        jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
