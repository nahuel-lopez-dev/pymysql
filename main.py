import pymysql

if __name__ == '__main__':
    
    try:
    
        connect = pymysql.Connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = '',
            db = 'pythondb'
        )

        print('Conexión realizada de forma exitosa')
        
    except pymysql.err.OperationalError as err:
        print('No fue posible realizar la conexión')
        print(err)
        