from flaskext.mysql import MySQL

def config(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'nomeesquema'

def get_db(mysql):
    conn = mysql.connect()
    cursor = conn.cursor()

    return conn, cursor