import pymysql


class Database:
    def __init__(self):
        self.__connection = pymysql.connect(host='127.0.1.1',
                                            user='root',
                                            password='Joder99Contac',
                                            db='contactos',
                                            cursorclass=pymysql.cursors.DictCursor)
        self.__query_add = 'INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)'
        self.__query_list = 'SELECT id, fullname, phone, email FROM contacts'
        self.__query_delete = 'DELETE FROM contacts WHERE id = %s'
        self.__query_get = 'SELECT id, fullname, phone, email FROM contacts WHERE id = %s'
        self.__query_update = 'UPDATE contacts SET fullname = %s, phone = %s, email = %s WHERE id = %s'

    def add_contact(self, fullname, phone, email):
        with self.__connection.cursor() as cursor:
            cursor.execute(self.__query_add, (fullname, phone, email))
            cursor.close()
        self.__connection.commit()

    def list_contacts(self):
        with self.__connection.cursor() as cursor:
            cursor.execute(self.__query_list)
            contacts = cursor.fetchall()
            cursor.close()
            return contacts

    def delete_contact(self, id_contact):
        with self.__connection.cursor() as cursor:
            cursor.execute(self.__query_delete, id_contact)
            cursor.close()
        self.__connection.commit()

    def get_contact(self, id_contact):
        with self.__connection.cursor() as cursor:
            cursor.execute(self.__query_get, id_contact)
            contact = cursor.fetchone()
            cursor.close()
            return contact

    def update_contact(self, contact: tuple):
        with self.__connection.cursor() as cursor:
            cursor.execute(self.__query_update, contact)
            cursor.close()
        self.__connection.commit()
