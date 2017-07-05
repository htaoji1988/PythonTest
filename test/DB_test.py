import pymysql.cursors

connection = pymysql.connect(host='172.16.107.136',
                             user='root',
                             password='Abcd@1234',
                             db='testdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
# cur = conn.cursor()
# cur.execute("SELECT * FROM user")
# for r in cur.fetchall():
#    print(r)
# cur.close()
# conn.close()
