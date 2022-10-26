import pymysql

connection = pymysql.connect(
    host="5.183.188.132",
    # port=8888,
    user="db_vgu_student",
    password="thasrCt3pKYWAYcK",
    database="db_vgu_test",
    charset='utf8'
)

while 1:
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM coupon;")
            for i in cursor.fetchall():
                print(i)
            break
    except pymysql.err.OperationalError:
        connection.ping(True)



connection.close()