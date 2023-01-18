from app import app

@app.route('/')
def homePage():
    return {
        'test':'hi'
    }

@app.route('/favorite_five')
def favoritePage():
    return {
        'test':'hello'
    }