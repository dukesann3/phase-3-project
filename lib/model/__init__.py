import sqlite3

CONN = sqlite3.connect("schedule_database.db")
CURSOR = CONN.cursor()