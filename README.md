# flask_protheus
Utilizando Flask com ERP Protheus

Exemplo simples de como usar Flask para TOTVS PROTHEUS.

Basicamente, acessamos a base de dados do Protheus, no exemplo utiliza as tabelas SA1 e SF2, que geralmente são tabelas
padrão da TOTVS e que todos usam.
Com flask tratamos as informacoes e eximos em forma de Web, ou seja, temos todo o poder do Python e Flask para trabalhar 
os dados de outra forma do Protheus.

- Conexão via lib da Oracle, cx_Oracle.

- Utilizando sqlalchemy como possibilidade de abstração, mas
executando uma querry pura, não é necessário utilizar sqlalchemy.

- Query utlizada traz como exemplo, o faturamento dentro de um período de um mês.

by femars@icloud.com
