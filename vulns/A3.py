from flask import Flask
from flask import render_template, abort, request

# Sensitive Data Exposure

def login():
    return render_template('A3-login.html',
                           title='Sensitive Data Exposure')

def register():
    if request.method == 'POST':
        return request.form['firstname'] + ' ' + request.form['lastname']
    elif request.method == 'GET':
        return render_template('A3-register.html',
                               title='Sensitive Data Exposure')

def render(page=None):
    if page is None:
        return render_template('A3.html',
                               title='Sensitive Data Exposure')
    if page == 'login':
        return login()
    if page == 'register':
        return register()
    assert(404)
