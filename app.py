import os
from flask import Flask, render_template, request, redirect, url_for
import openai
import json
from decimal import Decimal
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

load_dotenv('.cred')

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

# openai.api_key = os.getenv('OPENAI_API_KEY')

# if not openai.api_key:
#     raise ValueError("A chave da API OpenAI não está definida. Defina a variável de ambiente 'OPENAI_API_KEY'.")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gerar_guia', methods=['POST'])
def gerar_guia():
    dados_formulario = {
        "nome": request.form.get("nome"),
        "orcamento": float(request.form.get("orcamento")),
        "clima": request.form.get("clima"),
        "interesses": [interesse.strip() for interesse in request.form.get("interesses").split(",")],
        "data_inicio": request.form.get("data_inicio") if request.form.get("data_inicio") else None,
        "data_fim": request.form.get("data_fim") if request.form.get("data_fim") else None,
        "acomodacao": request.form.get("acomodacao"),
        "transporte": request.form.get("transporte"),
        "dietas": request.form.get("dietas") if request.form.get("dietas") else None,
        "companhia": request.form.get("companhia"),
        "atividade_fisica": request.form.get("atividade_fisica"),
        "idiomas": request.form.get("idiomas") if request.form.get("idiomas") else None,
        "acessibilidade": request.form.get("acessibilidade") if request.form.get("acessibilidade") else None,
        "faixa_etaria": request.form.get("faixa_etaria") if request.form.get("faixa_etaria") else None,
        "experiencias": request.form.get("experiencias") if request.form.get("experiencias") else None
    }

    mongo.db.planos_de_viagem.insert_one(dados_formulario)

    return redirect(url_for('index'))


    

if __name__ == '__main__':
    app.run(debug=True)