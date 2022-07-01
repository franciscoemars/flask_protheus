import cx_Oracle
import sqlalchemy
from sqlalchemy import create_engine, text
from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm

# Criando a conexão com o banco. Ex. cx_oracle://user:pass@192.168.0.1/protheusprod
engine = create_engine('oracle+cx_oracle:// ', pool_size=5, max_overflow=2)

app = Flask(__name__)
app.config['SECRET_KEY'] = '71a3a63114dSDFSDFSfd5bd64fafe77'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    # Conexão com o Banco de Dados
    conn = engine.connect() 
    # Executando a Querry
    sql = engine.execute("SELECT...")
    # Fechando conexão
    conn.close()
    # Jinja2 utilizado para renderizar o template
    return render_template('index.html', sql=sql)

if __name__ == "__main__":
    app.run()
