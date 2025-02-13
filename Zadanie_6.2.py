import sqlite3
from sqlite3 import Error
import random

db_file = "pilkarze.db"

def create_connection(db_file):
    """Tworzy połączenie z bazą danych SQLite."""
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(f"Błąd podczas łączenia z bazą danych: {e}")
    return connection

def execute_sql(connection, sql):
    """Wykonuje zapytanie SQL."""
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except Error as e:
        print(f"Błąd SQL: {e}")

def add_pilkarz(conn, pilkarz):
    """Dodaje nowego piłkarza do tabeli pilkarze."""
    if conn is None:
        print("Brak połączenia z bazą danych.")
        return None

    sql = """INSERT INTO pilkarze (imie, nazwisko, id_zespolu)
             VALUES (?, ?, ?)"""
    
    cursor = conn.cursor()
    cursor.execute(sql, pilkarz)
    conn.commit()
    return cursor.lastrowid

def add_liga(conn, zespol):
    """Dodaje nowy zespół do tabeli liga."""
    if conn is None:
        print("Brak połączenia z bazą danych.")
        return None

    sql = """INSERT INTO liga (id_zespolu, nazwa_zespolu, liga)
             VALUES (?, ?, ?)"""
    cursor = conn.cursor()
    cursor.execute(sql, zespol)
    conn.commit()
    return cursor.lastrowid

def select_all(conn, table):
   """
   Query all rows in the table
   :param conn: the Connection object
   :return:
   """
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()

   return rows

def select_where(conn, table, **query):
   """
   Query tasks from table with data from **query dict
   :param conn: the Connection object
   :param table: table name
   :param query: dict of attributes and values
   :return:
   """
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
   rows = cur.fetchall()
   return rows

def delete_where(conn, table, **kwargs):
   """
   Delete from table where attributes from
   :param conn:  Connection to the SQLite database
   :param table: table name
   :param kwargs: dict of attributes and values
   :return:
   """
   qs = []
   values = tuple()
   for k, v in kwargs.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)

   sql = f'DELETE FROM {table} WHERE {q}'
   cur = conn.cursor()
   cur.execute(sql, values)
   conn.commit()

   if cur.rowcount > 0:
       print(f"Usunięto {cur.rowcount} rekord(ów) z tabeli {table}.")
   else:
       print("Nie znaleziono pasujących rekordów do usunięcia.")

def update_(conn, table, id, **kwargs):
   """
   update status, begin_date, and end date of a task
   :param conn:
   :param table: table name
   :param id: row id
   :return:
   """
   parameters = [f"{k} = ?" for k in kwargs]
   parameters = ", ".join(parameters)
   values = tuple(v for v in kwargs.values())
   values += (id, )

   sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
   try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
       print("OK")
   except sqlite3.OperationalError as e:
       print(e)
    

if __name__ == "__main__":
    create_pilkarze_sql = """
    CREATE TABLE IF NOT EXISTS pilkarze (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        imie TEXT NOT NULL,
        nazwisko TEXT NOT NULL,
        id_zespolu INTEGER,
        FOREIGN KEY (id_zespolu) REFERENCES liga (id)
    );
    """

    create_liga_sql = """
    CREATE TABLE IF NOT EXISTS liga (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_zespolu INTEGER NOT NULL,
        nazwa_zespolu TEXT NOT NULL,
        liga TEXT NOT NULL
    );
    """

    # Tworzenie połączenia
    conn = create_connection(db_file)

    if conn is not None:
        execute_sql(conn, create_liga_sql)
        execute_sql(conn, create_pilkarze_sql)

        zespoly = [
            (1, "Liverpool", "Premier League"),
            (2, "Real Madrid", "La Liga"),
            (3, "Bayern Monachium", "Bundesliga"),
            (4, "Juventus", "Serie A"),
            (5, "PSG", "Ligue 1")
        ]

        # Dodanie 5 zespołów
        for zespol in zespoly:
            add_liga(conn, zespol)
        print("Dodano 5 zespołów.")

        pilkarze = [
            ("Robert", "Lewandowski", random.randint(1, 5)),
            ("Karim", "Benzema", random.randint(1, 5)),
            ("Leo", "Messi", random.randint(1, 5)),
            ("Cristiano", "Ronaldo", random.randint(1, 5)),
            ("Kylian", "Mbappe", random.randint(1, 5)),
            ("Neymar", "Junior", random.randint(1, 5)),
            ("Mohamed", "Salah", random.randint(1, 5)),
            ("Kevin", "De Bruyne", random.randint(1, 5)),
            ("Erling", "Haaland", random.randint(1, 5)),
            ("Vinicius", "Junior", random.randint(1, 5)),
            ("Sergio", "Ramos", random.randint(1, 5)),
            ("Luka", "Modric", random.randint(1, 5)),
            ("Toni", "Kroos", random.randint(1, 5)),
            ("Harry", "Kane", random.randint(1, 5)),
            ("Romelu", "Lukaku", random.randint(1, 5)),
            ("Antoine", "Griezmann", random.randint(1, 5)),
            ("Raheem", "Sterling", random.randint(1, 5)),
            ("Jadon", "Sancho", random.randint(1, 5)),
            ("Marcus", "Rashford", random.randint(1, 5)),
            ("Paulo", "Dybala", random.randint(1, 5)),
            ("Joshua", "Kimmich", random.randint(1, 5)),
            ("Andrew", "Robertson", random.randint(1, 5)),
            ("Trent", "Alexander-Arnold", random.randint(1, 5)),
            ("Bruno", "Fernandes", random.randint(1, 5)),
            ("Virgil", "van Dijk", random.randint(1, 5)),
            ("Ederson", "Moraes", random.randint(1, 5)),
            ("Alisson", "Becker", random.randint(1, 5)),
            ("Gianluigi", "Donnarumma", random.randint(1, 5)),
            ("Zlatan", "Ibrahimovic", random.randint(1, 5)),
            ("Phil", "Foden", random.randint(1, 5))
        ]

        # Dodanie 30 piłkarzy
        for pilkarz in pilkarze:
            add_pilkarz(conn, pilkarz)
        print("Dodano 30 piłkarzy.")

        pilkarze_ = select_all(conn, "pilkarze")
        print(pilkarze_)

        zespoly = select_all(conn, "liga")
        print(zespoly)

        print("**********************************")
        where = select_where(conn, "pilkarze", id_zespolu=1)
        print(where)

        transfer = update_(conn, "pilkarze", 2, id_zespolu = 4)

        delete = delete_where(conn, "pilkarze", imie="Erling") 
      
        # Zamknięcie połączenia
        conn.close()
    else:
        print("Nie udało się połączyć z bazą danych.")