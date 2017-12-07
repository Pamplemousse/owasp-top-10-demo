from flask import Flask
from flask import render_template, abort, request
import pickle
import binascii

# Sensitive Data Exposure

def login():
    if request.method == 'POST':
        ID = request.form['ID']
        user = pickle.loads(binascii.unhexlify(ID))
        return "Bienvenu %s !" % (user)
    else:
        return render_template('A8.html',
                               title='Insecure Deserialization')

def genere_id(lastname, firstname):
    return "%s-%s" % (binascii.hexlify(str.encode(lastname)).decode('utf-8'),
                         binascii.hexlify(str.encode(firstname)).decode('utf-8'))


def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        ID = binascii.hexlify(pickle.dumps([firstname, lastname])).decode('utf-8')
        return "Your ID: " + ID
    elif request.method == 'GET':
        return render_template('A8.html',
                               title='Insecure Deserialization')

def render(page=None):
    if page is None:
        return render_template('A8.html',
                               title='Insecure Deserialization')
    if page == 'login':
        return login()
    if page == 'register':
        return register()
    assert(404)
