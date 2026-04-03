import sqlite3

def init_db():

# Connect (creates the file if it doesn't exist)
    conn = sqlite3.connect('oracle_brain.db')
    cursor = conn.cursor()

    # 1. Clear the old tables (so we can fix any structure errors)
    cursor.execute("DROP TABLE IF EXISTS players")
    cursor.execute("DROP TABLE IF EXISTS teams")

    # Create Teams Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            stadium TEXT,
            home_form_coeff REAL DEFAULT 1.0,
            away_form_coeff REAL DEFAULT 1.0
        )
    ''')

    # 3. CREATE Players Table (This was the missing piece!)
    cursor.execute('''
        CREATE TABLE players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            team_id INTEGER,
            base_rating INTEGER,
            last_played_date TEXT,
            FOREIGN KEY (team_id) REFERENCES teams (id)
        )
    ''')

    # Seed Initial Data (2026 Sample)
    teams = [
        (1, 'Manchester City', 'Etihad Stadium'),
        (2, 'Arsenal', 'Emirates Stadium'),
        (3, 'Bolton Wanderers', 'Toughsheet Community Stadium')
    ]
    cursor.executemany('INSERT OR IGNORE INTO teams (id, name, stadium) VALUES (?,?,?)', teams)

    # 5. Seed Player
    cursor.execute("INSERT INTO players (name, team_id, base_rating, last_played_date) VALUES (?,?,?,?)", 
                   ('Erling Haaland', 1, 90, '2026-04-01'))

    conn.commit()

    # 6. VERIFICATION (Now correctly indented inside the function)
    print("Database Initialized & Seeded Successfully.")
    
    cursor.execute("SELECT name FROM teams")
    team_rows = cursor.fetchall()
    print(f"Verified Teams: {team_rows}")

    cursor.execute("SELECT name FROM players")
    player_rows = cursor.fetchall()
    print(f"Verified Players: {player_rows}")

    conn.close()

if __name__ == "__main__":
    init_db()

