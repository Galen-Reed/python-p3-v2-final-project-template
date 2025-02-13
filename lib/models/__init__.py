import sqlite3

CONN = sqlite3.connect('vet_clinic.db')
CURSOR = CONN.cursor()
