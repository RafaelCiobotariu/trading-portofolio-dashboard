from flask import Flask, render_template, request, redirect, url_for
import yfinance as yf
from database import add_actiune, init_db, get_actiuni, delete_actiune



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
        return redirect(url_for('hello_trader'))
    
    actiuni_raw = get_actiuni()
    actiuni = []
    total = 0
    
    for row in actiuni_raw:
        simbol = row[1]
        cantitate = row[2]
        id = row[0]
        pret = get_price(simbol)
        valoare = cantitate * pret
        total += valoare
        actiuni.append({
            "id": id,
            "simbol": simbol,
            "cantitate": cantitate,
            "pret": round(pret,2),
            "valoare": valoare
        })
        
    simboluri = [a["simbol"] for a in actiuni]
    valori = [a["valoare"] for a in actiuni]
    return render_template('index.html', name='Trader', actiuni=actiuni, total=round(total,2), simboluri=simboluri, valori=valori)
    

@app.route('/delete/<int:id>')
def sterge(id):
    delete_actiune(id)
    return redirect(url_for('hello_trader'))
    


app.run(debug=True)