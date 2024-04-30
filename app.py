from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ticker = request.form.get('ticker')
        stock = yf.Ticker(ticker)
        hist_data = stock.history(period="1y")
        return render_template('index.html', tables=[hist_data.to_html(classes='data')], titles=hist_data.columns.values, ticker=ticker)
    return render_template('index.html', tables=[], titles=[], ticker=None)

if __name__ == '__main__':
    app.run(debug=True)
        