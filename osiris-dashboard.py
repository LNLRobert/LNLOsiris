import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

# Load printers from configuration
with open('config/printers.json') as f:
    printers = json.load(f)

# Moonraker API polling
def get_printer_data(printer):
    try:
        response = requests.get(f"http://{printer['ip']}:{printer['port']}/printer/info")
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        return {"status": "Down", "reason": str(e)}

@app.route('/')
def dashboard():
    printer_status = []
    for printer in printers:
        printer_status.append(get_printer_data(printer))
    return render_template('index.html', printers=printer_status)