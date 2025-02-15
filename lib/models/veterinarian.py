from models.__init__ import CURSOR, CONN

class Veterinarian:

    all = {}

    def __init__(self, name, specialty, id=0):
        self.id = id
        self.name = name
        self.specialty = specialty

    def __repr__(self):
        return f"Veterinarian: {self.name}, specialty: {self.specialty}"

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
    def specialty(self):
        return self._specialty

    @specialty.setter
    def specialty(self, specialty):
        if isinstance(specialty, str) and len(specialty):
            self._specialty = specialty
        else:
            raise ValueError(
                "Specialty must be a non-empty string"
            )
        
    @classmethod
    def get_id_by_name(cls, vet_name):
        """ Find veterinarian by name and return their ID """
        veterinarian = cls.find_by_name(vet_name)
        if veterinarian:
            return veterinarian.id
        else:
            return None
        
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the atributes of Veterinarian instances """
        sql = """
            CREATE TABLE IF NOT EXISTS veterinarians (
            id INTEGER PRIMARY KEY,
            name TEXT,
            specialty TEXT)
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Veterinarian instances """
        sql = """
            DROP TABLE IF EXISTS veterinarians; 
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and specialty values of the current Veterinarian instance. 
        Update object id attribute using the primary key value of new row. 
        Save the object in local dictionary using table row's PK as dictionary key """
        sql = """
            INSERT INTO veterinarians (name, specialty)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.specialty))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, specialty):
        """ Initialize a new Veterinarian instance and save the object to the database """
        veterinarian = cls(name, specialty)
        veterinarian.save()
        return veterinarian
    
    def update(self):
        """ Update the table row corresponding to the current Veterinarian instance """
        sql = """ 
            UPDATE veterinarians
            SET name = ?, specialty = ?
            WHERE id = ? 
        """

        CURSOR.execute(sql, (self.name, self.specialty, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the table row corresponding to the current Veterinarian instance,
        delete the dictionary entry, and reassign id attribure"""

        sql = """
            DELETE FROM veterinarians
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """ Return a Veterinarian object having the attribute values from table row """

        veterinarian = cls.all.get(row[0])
        if veterinarian:
            veterinarian.name = row[1]
            veterinarian.specialty = row[2]
        else:
            veterinarian = cls(row[1], row[2], row[0])
            cls.all[veterinarian.id] = veterinarian
        return veterinarian
    
    @classmethod
    def get_all(cls):
        """ Return a list containing a Veterinarian object per row in table """
        sql = """
            SELECT *
            FROM veterinarians
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """ Return a Veterinarian object by their id """
        sql = """
            SELECT *
            FROM veterinarians
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """ Return Veterinarian object by their name """
        sql = """
            SELECT *
            FROM veterinarians
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_specialty(cls, specialty):
        """ Return  Veterinarian object by their specialty """
        sql = """
            SELECT *
            FROM veterinarians
            WHERE specialty = ?
        """
        rows = CURSOR.execute(sql, (specialty,)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else []

    def patients(self):
        """ Return list of patients that a veterinarian has """
        from models.patient import Patient
        sql = """
            SELECT * FROM patients
            WHERE veterinarian_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
        
        rows = CURSOR.fetchall()
        return [ 
            Patient.instance_from_db(row) for row in rows
        ]