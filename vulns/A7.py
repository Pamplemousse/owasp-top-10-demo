from flask import Flask
from flask import render_template, redirect, request, url_for

# Cross-Site scripting (XSS)

def render():
    return redirect(url_for("A7_with_id", id="identifiant-super-unique"))

def render_with_id(id):
    return render_template('A7.html',
                           title="Cross Site Scripting (XSS)",
                           id=id)
