from database.db import get_connection
from .entities.Usuario import Usuario


class UsuarioModel():

    @classmethod
    def get_usuarios(self):
        try:
            connection = get_connection()
            usuarios = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre FROM usuarios ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    usuario = Usuario(row[0], row[1])
                    usuarios.append(usuario.to_JSON())

            connection.close()
            return usuarios

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_usuario(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre FROM usuarios WHERE id = %s", (id,))
                row = cursor.fetchone()

                usuario = None
                if row != None:
                    usuario = Usuario(row[0], row[1])
                    usuario = usuario.to_JSON()

            connection.close()
            return usuario

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def add_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuarios (id, nombre) 
                                VALUES(%s, %s)""", (usuario.id, usuario.nombre))
                affected_rows=cursor.rowcount
                connection.commit()
            connection.close()

            return affected_rows

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE usuarios SET nombre = %s
                                WHERE id = %s""", (usuario.nombre, usuario.id))
                affected_rows=cursor.rowcount
                connection.commit()
            connection.close()

            return affected_rows

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario.id,))
                affected_rows=cursor.rowcount
                connection.commit()
            connection.close()

            return affected_rows

        except Exception as ex:
            raise Exception(ex)
 
