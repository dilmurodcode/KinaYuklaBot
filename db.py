import psycopg2

class PostgreSQL:
    def __init__(self):
        self.CreateDB()
        self.ConnectDB()
        self.CreateTable()

    def CreateDB(self):
        conn = psycopg2.connect(
            host="localhost",
            user="kino",
            password="kino",
            dbname="kino"
        )
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM pg_database WHERE datname='kino'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute("CREATE DATABASE kino;")

        cursor.close()
        conn.close()

    def ConnectDB(self):
        self.conn = psycopg2.connect(
            host="localhost",
            user="kino",
            password="kino",
            dbname="kino"
        )
        self.cursor = self.conn.cursor()

    def CreateTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS kino (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                file_id VARCHAR(200),
                file_size BIGINT,
                bot_username VARCHAR(200),
                movie_id INTEGER,
                file_type VARCHAR(200),
                created_at TIMESTAMP NUll,  
                updated_at TIMESTAMP NULL
            );
        """)
        self.conn.commit()

    def CreateDate(self):
        self.cursor.execute("INSERT INTO kino(name, file_id, file_size, bot_username, movie_id,file_type) VALUES('aa','22',345,'bb',34,'fff')")
        self.conn.commit()




kino = PostgreSQL()
kino.CreateDate()
