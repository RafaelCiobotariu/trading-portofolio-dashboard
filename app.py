from flask import Flask, render_template, request
import yfinance as yf


app = Flask(__name__)

def get_price(symbol):
    actiune = yf.Ticker(symbol)
    pret = actiune.info['currentPrice']
    return pret
  
  
  
actiuni = [
    {"simbol": "AAPL", "cantitate": 10, "pret": get_price("AAPL")},
    {"simbol": "TSLA", "cantitate": 5, "pret": get_price("TSLA")},
    {"simbol": "GOOGL", "cantitate": 3, "pret": get_price("GOOGL")},
]

total = sum(actiune['cantitate'] * actiune['pret'] for actiune in actiuni)

@app.route('/', methods=['GET', 'POST'])
def hello_trader():
    if request.method == 'POST':
        simbol = request.form['simbol']
        cantitate = int(request.form['cantitate'])
        print(simbol, cantitate)
    return render_template('index.html', name='Trader', actiuni=actiuni, total=round(total,2))
    


  
print(get_price("AAPL"))
app.run(debug=True)