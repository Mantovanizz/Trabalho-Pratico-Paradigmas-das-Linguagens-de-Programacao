import subprocess
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_url_path="/static")

KB_PATH = "kb.pl"

def consultar_prolog(aluno):
    try:
        query = f"recomenda_lista({aluno}, L), write(L), halt."

        result = subprocess.run(
            ["swipl", "-s", KB_PATH, "-g", query],
            capture_output=True,
            text=True
        )

        saida = result.stdout.strip()

        print("SAÍDA PROLOG:", saida)

        # Se vier vazio
        if not saida:
            return []

        # A saída deve ser tipo: [a,b,c]
        if not (saida.startswith("[") and saida.endswith("]")):
            return {"erro_parse": saida}

        # Remover colchetes
        conteudo = saida[1:-1].strip()

        if conteudo == "":
            return []

        # Quebrar por vírgula
        itens = [x.strip() for x in conteudo.split(",")]

        # Converter átomos Prolog em strings Python
        itens = [str(item) for item in itens]

        return itens

    except Exception as e:
        return {"erro": str(e)}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    aluno = data.get("aluno")

    resposta = consultar_prolog(aluno)

    if isinstance(resposta, dict) and "erro" in resposta:
        return jsonify({"erro": f"Falha ao consultar Prolog: {resposta['erro']}"}), 500

    if isinstance(resposta, dict) and "erro_parse" in resposta:
        return jsonify({"erro": f"Falha ao interpretar resposta do Prolog: {resposta['erro_parse']}"}), 500

    return jsonify({"cursos": resposta})


if __name__ == "__main__":
    print("=== Backend rodando em http://localhost:5000 ===")
    print(f"Usando KB: {KB_PATH}")
    app.run(debug=True)
