from connection import Connection
from psycopg2.extras import RealDictCursor


def test_connection():
    db = Connection()
    with db._open_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM pokemon")
            result = cursor.fetchone()
            print("Conexión exitosa, resultado de la consulta de prueba:", result)


if __name__ == "__main__":
    test_connection()
