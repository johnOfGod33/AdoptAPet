from flask import Flask, render_template, g, abort, request, redirect, url_for

from database import Animals_db

from .utils import validate_input

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Animals_db()

    return g._database




@app.route('/', methods=['GET'])
def index():
    query = request.args.get('q', '').strip()
    db = get_db()

    if query:  
        animals = db.search_animals(query)
        is_search = True
    else: 
        animals = db.get_random_animals()
        is_search = False

    return render_template('home.html', animals=animals, query=query, is_search=is_search)




@app.route('/animal/<int:animal_id>')
def animal_detail(animal_id):
    db = get_db()
    animal = db.get_animal_by_id(animal_id)
    if not animal:
        abort(404, description='Animal not found')
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

        if (validate_input(nom, age, espece, race, courriel, cp)) : 
            db = get_db()
            animal_id = db.add_animal(nom, age, espece, race, description, courriel, adresse, ville, cp)
        
            return redirect(url_for('animal_detail', animal_id=animal_id))
        else:
            error_message = "Il y a des erreurs dans le formulaire. Veuillez vérifier les champs et réessayer."
            
            return render_template('form.html', error_message=error_message, 
                                   nom=nom, age=age, espece=espece, race=race, 
                                   description=description, courriel=courriel, 
                                   adresse=adresse, ville=ville, cp=cp)
    
    return render_template('form.html')

if __name__=="__main__":
    app.run()