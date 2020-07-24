import sqlite3

def createTables():
    conn = sqlite3.connect('shareCodeBdd.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS code (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT DEFAULT 'Insert your code here ...',
            lang VARCHAR(50) DEFAULT 'py',
            createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updatedAt TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def createCode():
    conn = sqlite3.connect('shareCodeBdd.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO code DEFAULT VALUES
    ''')

    uid = c.lastrowid

    conn.commit()
    conn.close()

    return uid

def getCode(uid):
    conn = sqlite3.connect('shareCodeBdd.db')
    c = conn.cursor()

    c.execute('''
        SELECT
            code,
            lang
        FROM code
        WHERE uid = ?
    ''', uid)

    result = c.fetchone()

    conn.commit()
    conn.close()

    return result

def getAllCode():
    conn = sqlite3.connect('shareCodeBdd.db')
    c = conn.cursor()

    c.execute('''
        SELECT
            uid,
            code,
            lang
        FROM code
        ORDER BY
            updatedAt DESC,
            createdAt DESC
    ''')

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result

def updateCode(uid, code, lang):
    conn = sqlite3.connect('shareCodeBdd.db')
    c = conn.cursor()

    result = c.execute('''
        UPDATE code
        SET
            code= ?,
            lang = ?,
            updatedAt = CURRENT_TIMESTAMP
        WHERE uid = ?
    ''', (code, lang, uid))

    conn.commit()
    conn.close()

    return result