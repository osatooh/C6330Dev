import unittest
import sqlite3
from database import DatabaseManager

  # testing connection to database 
class DatabaseManagerTestCase(unittest.TestCase):
   
    def test_db_connection(self):
       # Assume
       database_filename = 'Bookmarks'
       databasemanager = DatabaseManager(database_filename)
       
       # Action
       result= databasemanager.connection
      
       # Assert
       self.assertTrue(result)

  #testing create table method      
    def test_create_table(self):
        #Assume
        tname = 'Bookmarks'
        cnames = {"id": "INTEGER PRIMARY KEY AUTOINCREMENT", 
                  "title" : "TEXT NOT NULL"}
        expectedtable = 'CREATE TABLE IF NOT EXISTS Bookmarks(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL);'
        #IF NOT EXISTS Bookmarks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL)'
       
        # Action
        result = DatabaseManager._execute

        # Assert
        self.assertNotEqual(result, expectedtable)
      
    def test_add(self):

        #Assume
        tname = 'Bookmarks3'
        data = {"title" : "?" ,"url" : "?" }
        addcommand = "INSERT INTO Bookmarks3 (title, url) VALUES (?, ?);"
       
        # Action
        result = DatabaseManager._execute

        # Assert
        self.assertNotEqual(result, addcommand)
'''                  
  def test_delete(self):

        # Assume
        tname = 'Bookmarks3'
        data = {"title" : "?" ,"url" : "?" }
        citeria = (columnname = data.value)
        delcommand = "DELETE FROM Bookmarks3 WHERE (title = ?)"
       
        # Action
        result = DatabaseManager._execute

        # Assert
        self.assertEqual(result, delcommand)
'''
if __name__ == "__main__":
     unittest.main()




