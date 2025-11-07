from flask import Flask, render_template, request

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        peso = float(request.form['peso'])
        altura_cm = float(request.form['altura'])
        altura = altura_cm / 100

        imc = peso / (altura ** 2)
        peso_ideal = 22 * (altura ** 2)

        # Classificação
        if imc < 18.5:
            classificacao = "Magreza"
        elif imc < 24.9:
            classificacao = "Normal"
        elif imc < 29.9:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        return render_template(
            'resultado.html',
            peso=round(peso, 2),
            altura=round(altura_cm, 2),
            imc=round(imc, 2),
            classificacao=classificacao,
            peso_ideal=round(peso_ideal, 2)
        )

    except Exception as e:
        return f"Erro ao calcular IMC: {e}"

if __name__ == '__main__':
    app.run(debug=True)

