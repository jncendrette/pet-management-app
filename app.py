from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar os dados dos pets temporariamente
pets = []

@app.route('/')
def index():
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        # Coletar as informações do formulário
        nome = request.form['nome']
        idade = request.form['idade']
        peso = request.form['peso']
        tipo = request.form['tipo']

        # Armazenar os dados do pet na lista
        pets.append({
            'nome': nome,
            'idade': idade,
            'peso': peso,
            'tipo': tipo
        })

        return redirect(url_for('index'))

    return render_template('add_pet.html')

if __name__ == '__main__':
    app.run(debug=True)
