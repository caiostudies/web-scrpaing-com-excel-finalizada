import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='banquinho',
    user='root',
    password=''
)

cursor = conexao.cursor()
cursor.execute('select database();')
cursor.fetchone()


def produtos_banco():
    comando = f'SELECT * FROM notes'
    cursor.execute(comando)
    return cursor.fetchall()


def pesquisaBanco(marca):
    if marca == '':
        cmd = f" SELECT * FROM notes "
    else:
        cmd = f" SELECT * FROM notes WHERE Marca = '{marca}' "
    cursor.execute(cmd)
    a = cursor.fetchall()
    return a

