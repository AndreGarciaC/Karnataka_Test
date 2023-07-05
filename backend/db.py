import mysql.connector

class Db_manager():

    def db_connect(self):
        self.cnx = mysql.connector.connect(host='localhost',user='root',password='mariadblenovo',database='ktk_db')
        if self.cnx.is_connected():
            print("Connected to the MySQL database.")
    
    def db_disconnect(self):
        self.cnx.close()
    
    def db_query(self, _query):

        # Create a cursor
        self.cursor = self.cnx.cursor()
        
        # Execute a query
        self.cursor.execute(_query)

        # Fetch the results
        results = self.cursor.fetchall()

        # Close the cursor
        self.cursor.close()

        return results
    
    def db_val_query(self,_query,_val):
         # Create a cursor
        self.cursor = self.cnx.cursor()
        self.cursor.execute(_query, (_val,))
        # Fetch the results
        results = self.cursor.fetchall()
        # Close the cursor
        self.cursor.close()

        return results