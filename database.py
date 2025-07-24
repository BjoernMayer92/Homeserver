import sqlite3
import sys, os


def create_database(path):
	try:
		with sqlite3.connect(path) as conn:
			print(f"Opened Sqlite database version {sqlite3.sqlite_version}")
	except sqlite3.Error as e:
		print(f"An Error occurred {e}")

	with open("setup_db.sql", "r") as f:
		setup_script = f.read()

	cursor = conn.cursor()
	cursor.executescript(setup_script)
	conn.commit()

if __name__ == "__main__":
	path = os.path.join(".","database.db")
	create_database(path)


