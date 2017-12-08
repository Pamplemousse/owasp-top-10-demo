from flask import Flask
from flask import render_template, request, abort
from hashlib import sha256
from flask import make_response

# Broken authentication

def login():
    if request.method == 'POST':
        pass_hashed = "no hash"

        if request.form['login'] == 'toto' and request.form['password'] == 'aa':
            pass_hashed = sha256(str(request.form['password'])
                          .encode('utf-8')).hexdigest()

        resp = make_response(render_template('A2-login.html', title='Broken Authentication', login=request.form['login'], pass_hashed=pass_hashed))
        resp.set_cookie('pass_hashed', pass_hashed)
        return resp
        
    elif request.method == 'GET':
        return render_template('A2.html', title='Broken Authentication')

def render(page=None):
    if page is None:
        return render_template('A2.html', title='Broken Authentication')
    if page == 'login':
        return login()
    assert(404)
