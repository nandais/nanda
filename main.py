import os

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_folder='src/static', template_folder='src/templates')

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota genérica para a calculadora
@app.route('/<int:a>/<int:b>')
def oper(a: int, b: int):

    result = 0
    try:
            if b == 0:
                return render_template('error.html', error_message="Não é possível dividir por zero.",
                                       status_code=400), 400
            result = a / ((b/100) ** 2)
    except Exception as e:
        return redirect(url_for('index'))

    return render_template('math.html',name = f"resultado de {a} / {b}",result=f"{result:.2f}")




if __name__ == '__main__':
    # Define a porta a partir da variável de ambiente PORT, ou usa 5000 como padrão
    # A porta 80 geralmente requer privilégios de administrador, então 5000 é mais comum para desenvolvimento.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
