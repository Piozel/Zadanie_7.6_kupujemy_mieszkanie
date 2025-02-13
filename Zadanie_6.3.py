import os
import csv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Ścieżka do plików CSV
stations_csv_path = r'E:\Kodilla\Projekt_1\Pliki CSV\clean_stations.csv'
measure_csv_path = r'E:\Kodilla\Projekt_1\Pliki CSV\clean_measure.csv'

# Ścieżka do pliku bazy danych
DATABASE_URL = "sqlite:///stations.db"



# Funkcja importująca dane ze stacji
def import_stations(stations_csv_path):
    with engine.connect() as conn:
        # Otwieramy plik CSV
        with open(stations_csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            stations_data = []
            
            # Przygotowujemy dane do wstawienia
            for row in reader:
                stations_data.append({
                    'station': row['station'],
                    'latitude': row['latitude'],
                    'longitude': row['longitude'],
                    'elevation': row['elevation'],
                    'name': row['name'],
                    'country': row['country'],
                    'state': row['state']
                })
            
            # Wstawiamy dane do tabeli
            conn.execute(text("""
                INSERT INTO stations (station, latitude, longitude, elevation, name, country, state)
                VALUES (:station, :latitude, :longitude, :elevation, :name, :country, :state)
            """), stations_data)

# Funkcja importująca dane z pomiarów
def import_measurements(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file) 
        measurements = []
        
        for row in reader:
            # Przygotowanie danych do wstawienia
            measurements.append({
                'station': row['station'],
                'date': row['date'],
                'precip': float(row['precip']),
                'tobs': float(row['tobs'])
            })
        
        # Wstawiamy dane do bazy danych
        with engine.connect() as conn:
            conn.execute(text("""
                INSERT INTO measurements (station, date, precip, tobs)
                VALUES (:station, :date, :precip, :tobs)
            """), measurements)
        print(f"Zaimportowano {len(measurements)} pomiarów.")


if __name__== "__main__":
    # Sprawdzamy czy baza danych istnieje, jeżeli tak to ja usuwamy
    if os.path.exists("stations.db"):
        os.remove("stations.db")

    # Tworzymy połączenie z bazą danych
    engine = create_engine(DATABASE_URL, echo=True)


    
    with engine.connect() as conn:       # with działą podobnie jak w przypadku Open że po zakończeniu operacji otwierania zamyka połączenie
        # Tworzymy tabelę dla stacji
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS stations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                station TEXT,
                latitude REAL,
                longitude REAL,
                elevation REAL,
                name TEXT,
                country TEXT,
                state TEXT
            );
        """))

        # Tworzymy tabelę dla pomiarów
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS measurements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                station TEXT,
                date TEXT,
                precip REAL,
                tobs REAL
            );
        """))

    # Importowanie danych
    import_stations(stations_csv_path)
    import_measurements(measure_csv_path)

    # Sprawdzanie wyników za pomocą czystych zapytań SQL
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM stations LIMIT 5")).fetchall()
        for row in result:
            print(row)
