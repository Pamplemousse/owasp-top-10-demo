from flask import Flask
from flask import render_template

# Sensitive Data Exposure

def render():
    return render_template('sensitive-data-exposure.html')
