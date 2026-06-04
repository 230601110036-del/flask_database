from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

application = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
application.config['DB_NAME'] = os.path.join(BASE_DIR, 'database.db')

conn = None
cursor = None


def openDb():
    global conn, cursor
    conn = sqlite3.connect(application.config['DB_NAME'])
    cursor = conn.cursor()


def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()


@application.route('/')
def index():
    openDb()

    container = []

    for id, judul, penulis, penerbit in cursor.execute(
        'SELECT * FROM buku'
    ):
        container.append({
            'id': id,
            'judul': judul,
            'penulis': penulis,
            'penerbit': penerbit
        })

    closeDb()

    return render_template('index.html', container=container)


@application.route('/tambah', methods=['GET', 'POST'])
def tambah():

    if request.method == 'POST':

        id = request.form['id']
        judul = request.form['judul']
        penulis = request.form['penulis']
        penerbit = request.form['penerbit']

        openDb()

        cursor.execute(
            'INSERT INTO buku VALUES(?,?,?,?)',
            (id, judul, penulis, penerbit)
        )

        conn.commit()
        closeDb()

        return redirect(url_for('index'))

    return render_template('tambah_form.html')


@application.route('/ubah/<id>', methods=['GET', 'POST'])
def ubah(id):

    openDb()

    cursor.execute(
        'SELECT * FROM buku WHERE id=?',
        (id,)
    )

    row = cursor.fetchone()

    buku = {
        'id': row[0],
        'judul': row[1],
        'penulis': row[2],
        'penerbit': row[3]
    }

    if request.method == 'POST':

        judul = request.form['judul']
        penulis = request.form['penulis']
        penerbit = request.form['penerbit']

        cursor.execute(
            '''
            UPDATE buku
            SET judul=?, penulis=?, penerbit=?
            WHERE id=?
            ''',
            (judul, penulis, penerbit, id)
        )

        conn.commit()
        closeDb()

        return redirect(url_for('index'))

    closeDb()

    return render_template(
        'ubah_form.html',
        buku=buku
    )


@application.route('/hapus/<id>')
def hapus(id):

    openDb()

    cursor.execute(
        'DELETE FROM buku WHERE id=?',
        (id,)
    )

    conn.commit()
    closeDb()

    return redirect(url_for('index'))


if __name__ == '__main__':
    application.run(debug=True)