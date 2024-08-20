import sqlite3

def user():
    con = sqlite3.connect("tutorial.db")

    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS user_information(id INTEGER PRIMARY KEY AUTOINCREMENT, name NOT NULL, email TEXT UNIQUE)")

    con.commit()

    cur.close()
    con.close()

# cur.execute("INSERT  INTO user_information(name, email) VALUES(?,?)", name, email)

con = sqlite3.connect("tutorial.db")

cur = con.cursor()

res = cur.execute("SELECT email FROM user_information")
#res.fetchall()
ab = res.fetchall()
for a in ab:
    c = ''.join(map(str,a))

    print(c)