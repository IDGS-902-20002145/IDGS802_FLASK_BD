from db import get_connection

try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call insertar_alumno(%s,%s,%s)', ('Adriana','Barron','adri@hmail.com'))
    connection.commit()
    connection.close()

except Exception as ex:
    print('ERROR {}'.format(ex))