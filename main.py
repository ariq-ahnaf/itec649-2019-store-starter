
import random
from bottle import Bottle, template, static_file, request, redirect, HTTPError

import model
import session

app = Bottle()


@app.route('/')
def index(db):
    data = model.product_list(db)
    info = {
        'title': "The WT Store",
        'message': data,
    }

    return template('index', info)

@app.route('/product/0')
def index(db):
    session.get_or_create_session(db)

    data = model.product_get(db, 0)
    info = {
        'data': data
    }
    return template('product_page', info)

@app.route('/product/1')
def index(db):
    session.get_or_create_session(db)
    data = model.product_get(db,1)
    info = {
        'data': data
    }
    return template('product_page',info)

@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='static')


if __name__ == '__main__':

    from bottle.ext import sqlite
    from dbschema import DATABASE_NAME
    # install the database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))
    app.run(debug=True, port=8010)
