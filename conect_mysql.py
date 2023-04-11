from pymysql import connect
def obtener_conexion():
    host = 'localhost'
    user = 'root'
    password = ''
    database = 'formularios'
    try:
        conn= connect(host=host, user=user, password=password, database=database)
        return conn
    except Exception as e:
        print(e)
        return None