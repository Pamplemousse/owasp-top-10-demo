from flask import Flask
from flask import render_template

import vulns.A1 as A1_vuln
import vulns.A2 as A2_vuln
import vulns.A3 as A3_vuln
import vulns.A7 as A7_vuln
import vulns.A8 as A8_vuln

app = Flask(__name__)

@app.route('/')
def main():
    routes = [
        { 'implemented': True,  'name': 'Injection'                                  , 'endpoint': 'A1'},
        { 'implemented': True,  'name': 'Broken Authentication'                      , 'endpoint': 'A2'},
        { 'implemented': True,  'name': 'Sensitive Data Exposure'                    , 'endpoint': 'A3'},
        { 'implemented': False, 'name': 'XML External Entities (XXE)'                , 'endpoint': 'A4'},
        { 'implemented': False, 'name': 'Broken Access Control'                      , 'endpoint': 'A5'},
        { 'implemented': False, 'name': 'Security Misconfiguration'                  , 'endpoint': 'A6'},
        { 'implemented': True,  'name': 'Cross-Site-Scripting (XSS)'                 , 'endpoint': 'A7'},
        { 'implemented': True,  'name': 'Insecure Deserialization'                   , 'endpoint': 'A8'},
        { 'implemented': False, 'name': 'Using Components with Known Vulnerabilities', 'endpoint': 'A9'},
        { 'implemented': False, 'name': 'Insufficient Logging and Monitoring'        , 'endpoint': 'A10'}
    ]

    return render_template('main.html',
                           title="Owasp Top Ten (2017)",
                           routes=routes)

# Injection
@app.route('/A1')
@app.route('/A1/<page>', methods=['POST'])
def A1(page='users'):
    return A1_vuln.render()

@app.route('/A1/users.json', methods=['GET', 'POST'])
def A1_api():
    return A1_vuln.users_as_json()

# Broken Authentication
@app.route('/A2/<page>', methods=['GET', 'POST'])
@app.route('/A2')
def A2(page=None):
    return A2_vuln.render(page)

# Sensitive Data Exposure
@app.route('/A3/<page>', methods=['GET', 'POST'])
@app.route('/A3')
def A3(page=None):
    return A3_vuln.render(page)

# XML External Entities (XEE)
@app.route('/A4')
def A4():
    return render_template('not_yet_implemented.html')

# Broken Access Control
@app.route('/A5')
def A5():
    return render_template('not_yet_implemented.html')

# Security Misconfiguration
@app.route('/A6')
def A6():
    return render_template('not_yet_implemented.html')

# Cross-Site Scripting (XSS)
@app.route('/A7')
@app.route('/A7/')
def A7():
    return A7_vuln.render()

@app.route('/A7/<id>')
def A7_with_id(id="identifiant-super-unique"):
    return A7_vuln.render_with_id(id)


# Insecure Deserialization
@app.route('/A8/<page>', methods=['POST', 'GET'])
@app.route('/A8')
def A8(page=None):
    return A8_vuln.render(page)

# Using Components With Known Vulnerabilities
@app.route('/A9')
def A9():
    return render_template('not_yet_implemented.html')

# Insufficient Logging and Monitoring
@app.route('/A10')
def A10():
    return render_template('not_yet_implemented.html')
