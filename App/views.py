from flask import Flask, render_template, g, abort

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



@app.route('/animal/<int:animal_id>')
def animal_detail(animal_id):
    db = get_db()
    animal = db.get_animal_by_id(animal_id)
    if not animal:
        abort(404)
    return render_template('animal_details.html', animal=animal)



if __name__=="__main__":
    app.run()