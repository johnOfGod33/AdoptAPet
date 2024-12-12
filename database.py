import sqlite3

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
    
    def get_all_animals(self):
        cursor = self.get_connection().cursor()
        query = ('SELECT id, nom, espece, race, age FROM animaux ORDER BY RANDOM() LIMIT 5')

        cursor.execute(query)

        random_animals = cursor.fetchall()

        return random_animals
