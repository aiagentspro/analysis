from flask import Flask, jsonify
import yfinance as yf
import pandas as pd

app = Flask(__name__)

@app.route('/predict/<symbol>', methods=['GET'])
def predict_price(symbol):
    df = yf.download(symbol, period="1y")
    df["Close_shift"] = df["Close"].shift(-1)
    df.dropna(inplace=True)

    last_close = df["Close"].iloc[-1]
    predicted_price = df["Close_shift"].iloc[-1]

    return jsonify({
        "symbol": symbol,
        "current_price": round(last_close, 2),
        "predicted_price": round(predicted_price, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
