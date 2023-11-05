from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    nombre = ''
    comision = 0
    if request.method == 'POST':
        nombre = request.form['nombre']
        ventas = int(request.form['ventas'])
        comision = round(ventas * 13 / 100,2)
    return render_template('index.html', nombre=nombre, comision=comision)

if __name__ == '__main__':
    app.run(debug=True)




