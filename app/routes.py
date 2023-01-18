from app import app
from flask import render_template



@app.route('/')
def homePage():
    text = "Click the link to see the greatest to ever do it!"
    return render_template('index.html', my_text = text )




@app.route('/favorite_five')
def favoritePage():
    people = ['Derek Jeter', 'Neymar', 'Biggie Smalls', 'Lil Wayne', 'Carmelo Anthony']
    return render_template('favorite_five.html', people = people)