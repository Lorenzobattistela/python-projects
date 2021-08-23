from flask import Flask, render_template, request
import requests
app = Flask(__name__)

url = 'https://api.exchangerate-api.com/v4/latest/BRL'
rates = requests.get(url).json()

@app.route("/", methods = ["GET", "POST"])
def homepage():
    abbreviations = list(rates['rates'])
    if request.method == 'POST':
        brl_amount = request.form.get('brl_amount')
        abbreviation = request.form.get('abbreviation')
        if not brl_amount or not abbreviation:
            message = 'Missing amount / Initials'
            return render_template("fail.html", message=message)

        total = float(brl_amount) * float(rates['rates'][abbreviation])
        
        

        return render_template("sucess.html", total=total, abbreviation=abbreviation, amount=brl_amount)
    else:
        return render_template("index.html", abbreviations=abbreviations)


