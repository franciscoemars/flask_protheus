"""
Exemplo simples de como usar Flask para TOTVS PROTHEUS.

- Conexão via lib da Oracle, cx_Oracle.
- Utilizando sqlalchemy como possibilidade de abstração, mas
executando uma querry pura.
- Utilizando as tabelas SA1010 (Clientes) e SF2010 (Notas)

by femars@icloud.com
"""

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
    sql = engine.execute("SELECT TRIM(SF2.F2_CLIENTE||SF2.F2_LOJA) AS CLIENTE, TRIM(SA1.A1_NREDUZ) AS NOME, COUNT(SF2.F2_CLIENTE||SF2.F2_LOJA) AS TOTAL, to_char( SUM(SF2.F2_VALBRUT), 'L999G999G999D99', 'nls_currency = R$ nls_numeric_Characters= ,.' ) FATURADO FROM SF2010 SF2 INNER JOIN SA1010 SA1 ON SF2.F2_CLIENTE||SF2.F2_LOJA = SA1.A1_COD||SA1.A1_LOJA AND SA1.D_E_L_E_T_ <> '*' WHERE SF2.F2_CLIENTE <> '009366' AND SF2.F2_EMISSAO = '20141015' GROUP BY SF2.F2_CLIENTE||SF2.F2_LOJA, SA1.A1_NREDUZ ORDER BY TOTAL DESC")
    # Fechando conexão
    conn.close()
    # Jinja2 utilizado para renderizar o template
    return render_template('index.html', sql=sql)

if __name__ == "__main__":
    app.run()