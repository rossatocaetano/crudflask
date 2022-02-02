import MySQLdb
print('Conecting...')
conn = MySQLdb.connect(user='root', passwd='insert_password', host='127.0.0.1', port=3306) #criar conexão com o bd

# Descomente se quiser desfazer o banco...
# conn.cursor().execute("DROP DATABASE IF EXISTS `register_people`;")
# conn.commit()

# Cria a variável "criar_tabelas", que armazena os comandos SQL para criar o banco de dados do projeto
criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `register_people` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `register_people`;
    CREATE TABLE `people` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(50) COLLATE utf8_bin NOT NULL,
      `gender` varchar(40) COLLATE utf8_bin NOT NULL,
      `document` varchar(11) NOT NULL,
      `email` varchar(50) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `user` (
      `id` varchar(8) COLLATE utf8_bin NOT NULL,
      `name` varchar(20) COLLATE utf8_bin NOT NULL,
      `password` varchar(40) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

# executa os comandos armazenados na variável "criar_tabelas"
conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor() #o cursor que irá executar as querys
cursor.executemany(
      'INSERT INTO register_people.user (id, name, password) VALUES (%s, %s, %s)',
      [
            ('root', 'Root', 'admin'),
      ])

cursor.execute('select * from register_people.user')
print(' -------------  Users:  -------------')
for user in cursor.fetchall(): #fetchall recupera os dados do bd
    print(user[1])

# inserindo registros
cursor.executemany(
      'INSERT INTO register_people.people (name, gender, document, email) VALUES (%s, %s, %s, %s)',
      [
            ('Raphael', 'Masculino', '12345678910', 'raphael@raphael.com.br'),
            ('Luisa', 'Feminino', '12345678910', 'luisa@luisa.com.br'),
            ('Maria', 'Não binário', '12345678910', 'maria@maria.com.br'),
      ])

cursor.execute('select * from register_people.people')
print(' -------------  People:  -------------')
for person in cursor.fetchall():
    print(person[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()