from config import CONN, CURSOR

class Song:
    def __init__(self,name,album) -> None:
        self.name = name
        self.album = album
        self.id = None

@classmethod
def create_table(self):
  sql="""
         CREATE TABLE IF NOT EXISTS songs (
         id SERIAL PRIMARY KEY,
         name TEXT,
         album TEXT
        );
    """
  CONN.execute(sql)

def save(self):
 sql = """
          INSERT INTO songs (name, album)
          VALUES (?, ?)
        """

 CURSOR.execute(sql, (self.name, self.album))

 self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

@classmethod
def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

