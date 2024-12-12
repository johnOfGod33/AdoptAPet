import sqlite3

class Animal:
    def __init__(self, id, nom=None, espece=None, race=None, age=None, description=None, courriel=None, adresse=None, ville=None, cp=None):
        self.id = id
        self.nom = nom
        self.espece = espece
        self.race = race
        self.age = age
        self.description = description
        self.courriel = courriel
        self.adresse = adresse
        self.ville = ville
        self.cp = cp

class Animals_db :
    def __init__(self):
        self.connection = None 
    
    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/animaux.db')
        
        return self.connection

    def disconnect(self):
        if self.connection is not None: 
            self.connection.close()
    
    def get_random_animals(self):
        cursor = self.get_connection().cursor()
        query = ('SELECT id, nom, espece, race, age FROM animaux ORDER BY RANDOM() LIMIT 5')

        cursor.execute(query)

        animals_data = cursor.fetchall()
        animals = [Animal(*animal) for animal in animals_data]

        return animals
