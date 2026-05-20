from flask import Flask, render_template


app = Flask(__name__)
actiuni = [
    {"simbol": "AAPL", "cantitate": 10, "pret": 180},
    {"simbol": "TSLA", "cantitate": 5, "pret": 245},
    {"simbol": "GOOGL", "cantitate": 3, "pret": 140},
]

@app.route('/')
def hello_trader():
  return render_template('index.html', name='Trader', actiuni=actiuni)

app.run(debug=True)