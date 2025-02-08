from models.__init__ import CURSOR, CONN

class Veterinarian:

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
    
    