from flask import Flask, render_template, request
import yfinance as yf
from database import add_actiune, init_db, get_actiuni



init_db()  
app = Flask(__name__)

def get_price(symbol):
    actiune = yf.Ticker(symbol)
    pret = actiune.info.get('currentPrice') or actiune.info.get('regularMarketPrice') or 0
    return pret
  
  
  
actiuni = get_actiuni()



# total = sum(actiune['cantitate'] * actiune['pret'] for actiune in actiuni)

@app.route('/', methods=['GET', 'POST'])
def hello_trader():
    if request.method == 'POST':
        simbol = request.form['simbol']
        cantitate = int(request.form['cantitate'])
        add_actiune(simbol, cantitate)
    
    actiuni_raw = get_actiuni()
    actiuni = []
    total = 0
    
    for row in actiuni_raw:
        simbol = row[1]
        cantitate = row[2]
        pret = get_price(simbol)
        valoare = cantitate * pret
        total += valoare
        actiuni.append({
            "simbol": simbol,
            "cantitate": cantitate,
            "pret": round(pret,2),
            "valoare": valoare
        })
        
    simboluri = [a["simbol"] for a in actiuni]
    valori = [a["valoare"] for a in actiuni]
    return render_template('index.html', name='Trader', actiuni=actiuni, total=round(total,2), simboluri=simboluri, valori=valori)
    



app.run(debug=True)