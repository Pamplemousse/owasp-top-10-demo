from flask import Flask
from flask import render_template, abort, request

import binascii

Users = {'61646d696e-61646d696e': {'firstname': 'admin', 'lastname': 'admin'}}

# Sensitive Data Exposure

def login():
    if request.method == 'POST':
        ID = request.form['ID']
        if ID in Users:
            return "Bienvenu %s %s !" % (Users[ID]['firstname'], Users[ID]['lastname'])
        else:
            return "Cet ID ne correspond a aucun utilisateur dans notre base de donnees"
    else:
        return render_template('A3-login.html',
                               title='Sensitive Data Exposure')

def genere_id(lastname, firstname):
    return "%s-%s" % (binascii.hexlify(str.encode(lastname)).decode('utf-8'),
                         binascii.hexlify(str.encode(firstname)).decode('utf-8'))


def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        ID = genere_id(firstname, lastname)
        if ID in Users:
            return "L'utilisateur existe deja !"
        else:
            Users[ID] = {'firstname': firstname, 'lastname': lastname}
            return "Your ID: " + ID
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
