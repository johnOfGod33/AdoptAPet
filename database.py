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
    
    def get_animal_by_id(self, animal_id):
        cursor = self.get_connection().cursor()
        query = "SELECT * FROM animaux WHERE id = ?"
        cursor.execute(query, (animal_id,))
        animal_data = cursor.fetchone()

        if animal_data:
            return Animal(*animal_data) 
        return None
    
    def add_animal(self, nom, age, espece, race, description, courriel, adresse, ville, cp):
        connection = self.get_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO animaux (nom, age, espece, race, description, courriel, adresse, ville, cp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        cursor.execute(query, (nom, age, espece, race, description, courriel, adresse, ville, cp))
        connection.commit()

        return cursor.lastrowid


        
