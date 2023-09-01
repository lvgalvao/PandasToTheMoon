from flask import render_template, request
from app import app
from .pandas_code import calculate_statistics

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Tente transformar os dados do formulário em inteiros
            data = request.form.get('data')
            data_list = list(map(int, data.split(',')))
            mean, median, mode, std = calculate_statistics(data_list)            
            return render_template('index.html', mean=mean, median=median, mode=mode, std=std)
        except ValueError:
            # Em caso de erro, exiba uma mensagem de erro
            return render_template('index.html', error="Valores invalidos. Coloque somente inteiros separados por virgula.")
    return render_template('index.html')