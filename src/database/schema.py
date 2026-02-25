import sqlite3
from pathlib import Path


def create_tables(conn: sqlite3.Connection):
    cursor = conn.cursor()

    # The NPC is missing details and items
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS savegame (
            id_savegame     INTEGER PRIMARY KEY AUTOINCREMENT,
            save_file_name  TEXT NOT NULL,
            player_name     TEXT NOT NULL,
            gender          TEXT NOT NULL,
            name_farm       TEXT NOT NULL,
            type_farm       TEXT
        );         

        CREATE TABLE IF NOT EXISTS snapshots (
            id_snapshot     INTEGER PRIMARY KEY AUTOINCREMENT,
            id_savegame     INTEGER NOT NULL REFERENCES savegame(id_savegame),
            date            TEXT,
            year            INTEGER NOT NULL,
            season          TEXT NOT NULL,
            day             INTEGER NOT NULL
            day_absolute    INTEGER,
            dinero_actual   INTEGER NOT NULL,                              
            delta_dinero    INTEGER,                              
            stamina_actual  INTEGER NOT NULL,                     
            stamina_max     INTEGER NOT NULL,             
            salud_actual    INTEGER NOT NULL,                              
            salud_max       INTEGER NOT NULL,                              
            nivel_mina      INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS skills_snapshots (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            snapshot_id     INTEGER NOT NULL REFERENCES snapshots(id_snapshot),
            name            TEXT NOT NULL,
            exp             INTEGER NOT NULL,
            lvl             INTEGER NOT NULL,
            delta_exp       INTEGER NOT NULL             
        );

        CREATE TABLE IF NOT EXISTS earnings_snapshots (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            snapshot_id     INTEGER NOT NULL REFERENCES snapshots(id_snapshot),
            delta_farming   INTEGER NOT NULL,
            delta_fishing   INTEGER NOT NULL,
            delta_forage    INTEGER NOT NULL,
            delta_mining    INTEGER NOT NULL,        
            delta_crafting  INTEGER
        );
                         
        CREATE TABLE IF NOT EXISTS friendship_snapshots (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            snapshot_id     INTEGER NOT NULL REFERENCES snapshots(id_snapshot),
            npc_id     INTEGER NOT NULL REFERENCES npc(id),
            points   INTEGER NOT NULL,
            hearts   INTEGER NOT NULL,
            delta_pts    INTEGER NOT NULL
        );
                        
        CREATE TABLE IF NOT EXISTS npc (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            name            TEXT NOT NULL,
            type            TEXT NOT NULL
        );
                         
        
    """)

    conn.commit()


def get_connection(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


if __name__ == "__main__":
    db_path = Path(__file__).parent.parent / "data" / "stardew.db"
    db_path.parent.mkdir(exist_ok=True)

    conn = get_connection(db_path)
    create_tables(conn)
    conn.close()

    print(f"Base de datos creada en: {db_path}")