from flask import Flask, render_template, g

from database import Animals_db

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Animals_db()

    return g._database




@app.route('/')
def index():
    db = get_db()
    animals = db.get_random_animals()
    return render_template('home.html', animals=animals)


if __name__=="__main__":
    app.run()