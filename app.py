from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

JSON_FILE = 'professores.json'

# ====================== FUNÇÕES AUXILIARES ======================
def load_data():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ====================== ROTAS CRUD ======================

@app.route('/professores', methods=['GET'])
def listar_professores():
    """Read - Listar todos os professores"""
    data = load_data()
    return jsonify(data)

@app.route('/professores/<int:prof_id>', methods=['GET'])
def consultar_professor(prof_id):
    """Read - Consultar professor por ID"""
    data = load_data()
    for prof in data:
        if prof['id'] == prof_id:
            return jsonify(prof)
    return jsonify({"erro": "Professor não encontrado"}), 404

@app.route('/professores', methods=['POST'])
def cadastrar_professor():
    """Create - Cadastrar novo professor"""
    data = load_data()
    novo = request.get_json()

    if not novo or not all(k in novo for k in ['nome', 'email', 'disciplina']):
        return jsonify({"erro": "Campos obrigatórios: nome, email e disciplina"}), 400

    # Gera ID automático
    max_id = max([p['id'] for p in data] + [0])
    novo['id'] = max_id + 1

    data.append(novo)
    save_data(data)
    return jsonify(novo), 201

@app.route('/professores/<int:prof_id>', methods=['PUT'])
def atualizar_professor(prof_id):
    """Update - Atualizar professor"""
    data = load_data()
    novo_dado = request.get_json()

    for prof in data:
        if prof['id'] == prof_id:
            if 'nome' in novo_dado:
                prof['nome'] = novo_dado['nome']
            if 'email' in novo_dado:
                prof['email'] = novo_dado['email']
            if 'disciplina' in novo_dado:
                prof['disciplina'] = novo_dado['disciplina']
            
            save_data(data)
            return jsonify(prof)
    return jsonify({"erro": "Professor não encontrado"}), 404

@app.route('/professores/<int:prof_id>', methods=['DELETE'])
def excluir_professor(prof_id):
    """Delete - Excluir professor"""
    data = load_data()
    for i, prof in enumerate(data):
        if prof['id'] == prof_id:
            excluido = data.pop(i)
            save_data(data)
            return jsonify(excluido)
    return jsonify({"erro": "Professor não encontrado"}), 404

# ====================== EXECUÇÃO ======================
if __name__ == '__main__':
    # Cria o arquivo JSON caso não exista
    if not os.path.exists(JSON_FILE):
        save_data([])
    app.run(debug=True)
