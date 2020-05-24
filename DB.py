import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
#создание таблицы бд
def create_table():
    sql_create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT,
        NICK TEXT
    )
    '''
    cursor.execute(sql_create_table)
    print('Таблица создана')

#чтение всей таблицы бд
def read_db():
    sql_read = '''
     SELECT * FROM users
    '''
    cursor.execute(sql_read)
    return cursor.fetchall()

def write_db(msg, clk):
    #Чтение имен из бд и запись в data
    sql_read = '''
        SELECT NAME FROM users
    '''
    cursor.execute(sql_read)
    data = cursor.fetchall()
    #запись в бд имен и никнеймов
    sql_write = '''
    INSERT INTO users (NAME, NICK)
    VALUES(?, ?)
    '''
    #получение id сервера и получение всех польщователей сервера
    id_guild = msg.guild.id
    guild = clk.get_guild(id_guild)
    #перебор всех пользователей
    for m in guild.members:
        name = str(m.name)
        if str(m.nick) == 'None':
            nick = name
        else:
            nick = str(m.nick)
        #проверка имен на совпадение в бд
        if (nick,) not in cursor.fetchall() and data != []:
            pass
        else:
            cursor.execute(sql_write, (name, nick))
    connection.commit()

#получение числа всех пользователей в бд(Число инкрементирования)
def get_numb_of_users():
    sql_read = '''
    SELECT SEQ FROM sqlite_sequence WHERE name="users"
    '''
    cursor.execute(sql_read)
    return cursor.fetchall()

