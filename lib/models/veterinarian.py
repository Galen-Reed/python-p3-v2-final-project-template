from models.__init__ import CURSOR, CONN

class Veterinarian:

    all = {}

    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty

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
    def create_table(cls):
        """ Create a new table to persist the atributes of Veterinarian instances """
        sql = """
            CREATE TABLE IF NOT EXISTS veterinarians (
            id INTEGER PRIMARY KEY,
            name TEXT,
            specialty TEXT)
        """

        CURSOR.exectute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Veterinarian instances """
        sql = """
            DROP TABLE IF EXISTS veterinarians; 
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def save(self):
        """ Insert a new row with the name and specialty values of the current Veterinarian instance. 
        Update object id attribute using the primary key value of new row. 
        Save the object in local dictionary using table row's PK as dictionary key """
        sql = """
            INSERT INTO veterinarian (name, specialty)
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

        CURSOR.execute(sql, (self.id))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    