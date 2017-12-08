import sqlite3

from flask import Flask, jsonify, redirect, render_template, request, url_for, g

# Injection

DATABASE = 'injection.db'

def users_as_json():
    year_filter = request.args.get('year')

    if (year_filter == ''):
        cur = get_db().execute("SELECT first_name, last_name, year_of_birth FROM users LIMIT 10")
        users = cur.fetchall()
    else:
        cur = get_db().execute("SELECT first_name, last_name, year_of_birth FROM users WHERE year_of_birth LIKE '%" + year_filter + "%' LIMIT 10")
        users = cur.fetchall()

    cur.close()
    close_connection(None)

    resp = jsonify(users)
    resp.status_code = 200

    return resp


def render():
    cur = get_db().execute("SELECT * FROM users LIMIT 10")
    users = cur.fetchall()

    cur.close()
    close_connection(None)

    return render_template('A1.html', users=users)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
      db.close()
