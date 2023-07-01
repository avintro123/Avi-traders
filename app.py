from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Web designer',
    'location': 'Shimla, India',
    'salary': 'Rs. 1,00,000',
  },
  {
    'id': 2,
    'title': 'Programmer',
    'location': 'Delhi, India',
    'salary': 'Rs. 14,00,000',
  },
  {
    'id': 3,
    'title': 'Front/Backend developer',
    'location': 'Chandigarh, India',
    'salary': 'Rs. 9,00,000',
  },
  {
    'id': 4,
    'title': 'Graphics',
    'location': 'Kolkata, India',
    'salary': 'Rs. 19,00,000',
  },
]


@app.route("/")
def hello_avitraders():
  return render_template('home.html', jobs=JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
