from app.database import get_db


class UserFan:

    # Constructor
    def __init__(self, id=None, nombre=None, email=None, password=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'password': self.password,
        }

    @staticmethod
    def get_all_user():
        # Logica de buscar en la base de datos los usuarios
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM user"
        cursor.execute(query)
        # Obtengo resultados
        rows = cursor.fetchall()
        users = [UserFan(id=row[0], nombre=row[1], email=row[2],
                         password=row[3]) for row in rows]
        # Cerramos el cursor
        cursor.close()
        return users

    def saveUser(self):
        db = get_db()
        cursor = db.cursor()
        if self.id:
            cursor.execute("""
                    UPDATE user set nombre = %s, email = %s, assword = %s
                    WHERE id = %s
                """, (self.nombre, self.email, self.password, self.id))
        else:
            cursor.execute("""
                    INSERT INTO user (nombre, email, password) VALUES(%s, %s, %s)
                """, (self.nombre, self.email, self.password))
            # voy a obtener el último id generado
            self.id = cursor.lastrowid
        db.commit()  # confirmar la accion
        cursor.close()

    @staticmethod
    def get_by_idUser(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return UserFan(id=row[0], nombre=row[1], email=row[2], password=row[3])
        return None

    def deleteUser(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM user WHERE id = %s", (self.id,))
        db.commit()
        cursor.close()
