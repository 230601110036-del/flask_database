from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

import sqlite3
import os

application = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "database.db")


# ==========================
# KONEKSI DATABASE
# ==========================

def get_db():

    conn = sqlite3.connect(DB_NAME)

    conn.row_factory = sqlite3.Row

    return conn


# ==========================
# HOME
# ==========================

@application.route('/')
def home():

    return render_template(
        'home.html'
    )


# ==========================
# READ DATA
# ==========================

@application.route('/reservasi')
def index():

    conn = get_db()

    data = conn.execute(
        '''
        SELECT *
        FROM reservasi
        ORDER BY id DESC
        '''
    ).fetchall()

    conn.close()

    return render_template(
        'index.html',
        container=data
    )


# ==========================
# CREATE DATA
# ==========================

@application.route(
    '/tambah',
    methods=['GET', 'POST']
)
def tambah():

    if request.method == 'POST':

        nama = request.form['nama']
        telepon = request.form['telepon']
        paket = request.form['paket']
        tanggal = request.form['tanggal']
        jam = request.form['jam']

        conn = get_db()

        conn.execute(
            '''
            INSERT INTO reservasi
            (
                nama,
                telepon,
                paket,
                tanggal,
                jam
            )
            VALUES
            (
                ?,?,?,?,?
            )
            ''',
            (
                nama,
                telepon,
                paket,
                tanggal,
                jam
            )
        )

        conn.commit()
        conn.close()

        return redirect(
            url_for('index')
        )

    return render_template(
        'tambah_form.html'
    )


# ==========================
# UPDATE DATA
# ==========================

@application.route(
    '/ubah/<int:id>',
    methods=['GET', 'POST']
)
def ubah(id):

    conn = get_db()

    data = conn.execute(
        '''
        SELECT *
        FROM reservasi
        WHERE id=?
        ''',
        (id,)
    ).fetchone()

    if request.method == 'POST':

        nama = request.form['nama']
        telepon = request.form['telepon']
        paket = request.form['paket']
        tanggal = request.form['tanggal']
        jam = request.form['jam']

        conn.execute(
            '''
            UPDATE reservasi
            SET
                nama=?,
                telepon=?,
                paket=?,
                tanggal=?,
                jam=?
            WHERE id=?
            ''',
            (
                nama,
                telepon,
                paket,
                tanggal,
                jam,
                id
            )
        )

        conn.commit()
        conn.close()

        return redirect(
            url_for('index')
        )

    conn.close()

    return render_template(
        'ubah_form.html',
        data=data
    )


# ==========================
# DELETE DATA
# ==========================

@application.route('/hapus/<int:id>')
def hapus(id):

    conn = get_db()

    conn.execute(
        '''
        DELETE FROM reservasi
        WHERE id=?
        ''',
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(
        url_for('index')
    )

# ==========================
# MAIN PROGRAM
# ==========================

if __name__ == '__main__':

    application.run(
        debug=True
    )