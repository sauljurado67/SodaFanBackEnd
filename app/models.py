from app.database import get_db


class SodaFan:

    # contructor
    def __init__(self, idtemas=None, nombre=None, albun=None, creditos=None):
        self.idtemas = idtemas
        self.nombre = nombre
        self.albun = albun
        self.creditos = creditos

    def serialize(self):
        return {
            'idtemas': self.idtemas,
            'nombre': self.nombre,
            'albun': self.albun,
            'creditos': self.creditos,
        }

    @staticmethod
    def get_all():
        # logica de buscar en la base todos los temas
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM temas"
        cursor.execute(query)
        # obtengo resultados
        rows = cursor.fetchall()
        temas = [SodaFan(idtemas=row[0], nombre=row[1], albun=row[2],
                         creditos=row[3]) for row in rows]
        # cerramos el cursor
        cursor.close()
        return temas

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.idtemas:
            cursor.execute("""
                UPDATE temas SET nombre = %s, albun = %s, creditos = %s
                WHERE idtemas = %s
            """, (self.nombre, self.albun, self.creditos, self.idtemas))
        else:
            cursor.execute("""
                INSERT INTO temas (nombre, albun, creditos) VALUES (%s, %s, %s)
            """, (self.nombre, self.albun, self.creditos))
            # voy a obtener el último id generado
            self.idtemas = cursor.lastrowid
        db.commit()  # confirmar la accion
        cursor.close()

    @staticmethod
    def get_by_id(idtemas):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM temas WHERE idtemas = %s", (idtemas,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return SodaFan(idtemas=row[0], nombre=row[1], albun=row[2], creditos=row[3])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM temas WHERE idtemas = %s", (self.idtemas,))
        db.commit()
        cursor.close()
