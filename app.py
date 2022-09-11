from crypt import methods
from flask import Flask, render_template, request, flash
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal
from curr import type_of_curr

app = Flask(__name__)
app.config["SECRET KEY"]="asldkntlkjhng"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/conversion", methods=["POST"])
def convert():
    """
    rates.convert("USD", "USD", 10)
    10.00
    """
    starting_currency = request.form.get("start").upper()
    ending_currency = request.form.get("end").upper()
    amount = request.form.get("amount")
    rates = CurrencyRates()
    
    if starting_currency not in type_of_curr:
        return render_template("home.html", error_msg="Invalid Starting Currency")
    elif ending_currency not in type_of_curr:
        return render_template("home.html", error_msg="Invalid Ending Currency")
    else:
        converted_amount = rates.convert(starting_currency, ending_currency, Decimal(amount))
        rounded_curr = round(converted_amount, 2)
        final = str(rounded_curr)
        curr_code = CurrencyCodes()
        symbol = curr_code.get_symbol(ending_currency)
        return render_template("result.html", symbol=symbol, amount=final)