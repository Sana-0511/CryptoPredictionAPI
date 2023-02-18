from flask import Flask, request
from flask import Flask, render_template
from BTC_predictions import prenext
import datetime as dt

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def predict_price():
    predicted_price = prenext()
    prediction_date = dt.date.today() + dt.timedelta(days=1)
    
    return render_template('web.html', date = prediction_date , price = predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
