import sqlite3
from pathlib import Path


def create_tables(conn: sqlite3.Connection):
    cursor = conn.cursor()

    # The NPC is missing details and items
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS snapshots (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            save_file_name  TEXT NOT NULL,
            parsed_at       TEXT NOT NULL,
            in_game_year    INTEGER,
            in_game_season  TEXT,
            in_game_day     INTEGER
        );

        CREATE TABLE IF NOT EXISTS player_economy (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            snapshot_id     INTEGER NOT NULL REFERENCES snapshots(id),
            money           INTEGER,
            total_money_earned INTEGER
        );

        CREATE TABLE IF NOT EXISTS player_skills (
            snapshot_id     INTEGER NOT NULL REFERENCES snapshots(id),
            farming_xp      INTEGER,
            mining_xp       INTEGER,  
            foraging_xp     INTEGER,
            fishing_xp      INTEGER,
            combat_xp       INTEGER,
            deepest_mine_level INTEGER
        ); 
                         
        CREATE TABLE IF NOT EXISTS player_activity (
            snapshot_id     INTEGER NOT NULL REFERENCES snapshots(id),
            days_played     INTEGER,
            fish_caught       INTEGER,  
            monsters_killed     INTEGER,
            quests_completed     INTEGER,
            steps_taken       INTEGER
        ); 
                         
        CREATE TABLE IF NOT EXISTS npc (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            gender       TEXT NOT NULL

        );
                         
        CREATE TABLE IF NOT EXISTS friendships_snapshot (
            snapshot_id     INTEGER NOT NULL REFERENCES snapshots(id),
            npc_id     INTEGER NOT NULL REFERENCES npc(id),
            friendship_points       INTEGER
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