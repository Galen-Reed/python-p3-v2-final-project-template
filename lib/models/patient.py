from models.__init__ import CURSOR, CONN
from models.veterinarian import Veterinarian

class Patient:

    all = {}

    def __init__(self, name, breed, age, veterinarian_id):
        self.id = None
        self.name = name
        self.breed = breed
        self.age = age
        self.veterinarian_id = veterinarian_id

    def __repr__(self):
        return f"Patient: {self.name}, {self.breed}, {self.age}yrs"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
    
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        if isinstance(breed, str) and len(breed):
            self._breed = breed
        else:
            raise ValueError(
                "Breed must be a non-empty string"
            )
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and int(age):
            self._age = age
        else:
            raise ValueError(
                "Age must be an integer"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Patient instances """
        sql = """
            CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            breed TEXT, 
            age INTEGER,
            veterinarian_id INTEGER,
            FOREIGN KEY (veterinarian_id) REFERENCES veterinarians(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop thje table that persists Patient instances """
        sql = """
            DROP TABLE IF EXISTS patients;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, breed, age, and veterinarian id values of the current Patient object. 
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO patients (name, breed, age, veterinarian_id)
            VALUES (?, ?, ?, ?)
        """
        print(self)
        CURSOR.execute(sql, (self.name, self.breed, self.age, self.veterinarian_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """ Update table row corresponding to current Patient instance."""
        sql = """
            UPDATE patients
            SET name = ?, breed = ?, age = ?, veterinarian_id =?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.breed, self.age, self.veterinarian_id, self.id))
        CONN.commit()

    def delete(self):
        """ Delete table row corresponding to Patient instance """
        sql = """
            DELETE FROM patients
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, name, breed, age, veterinarian_name):
        """ Initialize new Paitent instance and save to database """
        veterinarian_id = Veterinarian.get_id_by_name(veterinarian_name)

        if veterinarian_id is None:
            raise ValueError(f"Veterinarian: {veterinarian_name} not found. Please add them first")

        patient = cls(name, breed, age, veterinarian_id)
        patient.save()
        return patient
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a Patient object """
        patient = cls.all.get(row[0])
        if patient:
            patient.name = row[1]
            patient.breed = row[2]
            patient.age = row[3]
            patient.veterinarian_id = row[4]
        else:
            patient = cls(row[1], row[2], row[3], row[4])
            patient.id = row[0]
            cls.all[patient.id] = patient
        return patient
    
    @classmethod
    def get_all(cls):
        """ Return a list containing one Patient object """
        sql = """
            SELECT *
            FROM patients
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        """ Return Patient object corresponding to first table matching specified name """
        sql = """
            SELECT *
            FROM patients
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_breed(cls, breed):
        """ Return Patient object corresponding to the first table matching specified breed """
        sql = """
            SELECT *
            FROM patients
            WHERE breed is ?
        """
        rows = CURSOR.execute(sql, (breed,)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else []
    