#import pyodbc
#server = 'seventhson.database.windows.net'
#database = 'seventhson'
#username = 'seventhson'
#password = 'treehacks2017'
#driver= '{ODBC Driver 13 for SQL Server}'
#cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
#cursor = cnxn.cursor()
#cursor.execute("select @@VERSION")
#row = cursor.fetchone()
#if row:
#    print row