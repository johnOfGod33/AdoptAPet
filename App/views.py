from flask import Flask, render_template, g, abort, request, redirect, url_for

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


@app.route('/formulaire', methods=['GET', 'POST'])
def formulaire():
    if request.method == 'POST':
        nom = request.form.get('nom')
        age = request.form.get('age')
        espece = request.form.get('espece')
        race = request.form.get('race')
        description = request.form.get('description')
        courriel = request.form.get('courriel')
        adresse = request.form.get('adresse')
        ville = request.form.get('ville')
        cp = request.form.get('cp')

        db = get_db()
        animal_id = db.add_animal(nom, age, espece, race, description, courriel, adresse, ville, cp)
        
        return redirect(url_for('animal_detail', animal_id=animal_id))
    
    return render_template('form.html')

if __name__=="__main__":
    app.run()