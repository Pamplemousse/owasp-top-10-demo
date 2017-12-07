from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    routes = [
        { 'name': 'Injection'                                  , 'endpoint': 'A1'},
        { 'name': 'Broken Authentication'                      , 'endpoint': 'A2'},
        { 'name': 'Sensitive Data Exposure'                    , 'endpoint': 'A3'},
        { 'name': 'XML External Entities (XXE)'                , 'endpoint': 'A4'},
        { 'name': 'Broken Access Control'                      , 'endpoint': 'A5'},
        { 'name': 'Security Misconfiguration'                  , 'endpoint': 'A6'},
        { 'name': 'Cross-Site-Scripting (XSS)'                 , 'endpoint': 'A7'},
        { 'name': 'Insecure Deserialization'                   , 'endpoint': 'A8'},
        { 'name': 'Using Components with Known Vulnerabilities', 'endpoint': 'A9'},
        { 'name': 'Insufficient Logging and Monitoring'        , 'endpoint': 'A10'}
    ]
    return render_template('main.html', routes=routes)

# Injection
@app.route('/A1')
def A1():
    return 'A1'

# Broken Authentication
@app.route('/A2')
def A2():
    return 'A2'

# Sensitive Data Exposure
@app.route('/A3')
def A3():
    return render_template('sensitive-data-exposure.html')

# XML External Entities (XEE)
@app.route('/A4')
def A4():
    return 'A4'

# Broken Access Control
@app.route('/A5')
def A5():
    return 'A5'

# Security Misconfiguration
@app.route('/A6')
def A6():
    return 'A6'

# Cross-Site Scripting (XSS)
@app.route('/A7')
def A7():
    return 'A7'

# Insecure Deserialization
@app.route('/A8')
def A8():
    return 'A8'

# Using Components With Known Vulnerabilities
@app.route('/A9')
def A9():
    return 'A9'

# Insufficient Logging and Monitoring
@app.route('/A10')
def A10():
    return 'A10'
