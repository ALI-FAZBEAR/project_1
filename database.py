import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute( """
                            CREATE TABLE IF NOT EXISTS Contacts (id INTEGER PRIMARY KEY,
                            name text, family text, address text, phone text)
                            """)
        self.con.commit()
        
    def insert(self, name, family, address, phone):
        self.cur.execute("""
                            INSERT INTO Contacts VALUES( NULL, ?, ?, ?, ?)
                            """, (name, family, address, phone))
        self.con.commit()
        
    def select(self):
           # self.cur.execute('SELECT * FROM Contacts WHERE address = "arak" ')
           
          # self.cur.execute('SELECT * FROM Contacts WHERE not address = "arak" ')
          
          # self.cur.execute('SELECT * FROM Contacts WHERE address in ("arak","tehran") ')
          # where address="arak" or address="tehran"   
          
          # self.cur.execute('SELECT * FROM Contacts WHERE address not in ("arak","tehran") ')
          
          # ... where like pattern(wildcard _ or %)
          
        #   self.cur.execute('SELECT * FROM Contacts WHERE address like "ta%" ')  #tehran , tabriz
          # self.cur.execute('SELECT * FROM Contacts WHERE address not like "t%" ')
          # self.cur.execute('SELECT * FROM Contacts WHERE address like "_a%" ')   # tabriz
          # self.cur.execute('SELECT * FROM Contacts WHERE address like "t%" or address like "a%"')
          self.cur.execute('SELECT * FROM Contacts')
          return self.cur.fetchall()
    def delete(self,id):
        self.cur.execute('DELETE  FROM Contacts WHERE id =?',(id,))

    def update(self,id,name,family,address,phone):
        self.cur.execute('UPDATE Contacts SET name =?, family=?, address=?, phone=? WHERE id = ?',
        (name,family,address,phone,id))
        self.con.commit()

    def search(self,input_search):
            self.cur.execute('SELECT * FROM Contacts WHERE name=? or family=? or address=? or phone=?',
            (input_search,input_search,input_search,input_search))
            return self.cur.fetchall()

      



     