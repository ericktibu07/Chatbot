from flask import Flask, render_template, request, jsonify
from chatbot_logic import cargar_preguntas_respuestas, clasificar_pregunta, crear_base_vectorial, responder_pregunta

app = Flask(__name__)

# Inicializar el chatbot
csv_path = 'Preguntas.csv'
df = cargar_preguntas_respuestas(csv_path)
index, vectorizer = crear_base_vectorial(df)

# Ruta para la página principal (index.html)
@app.route("/")
def home():
    return render_template("index.html")

# Ruta para la página de contacto (contacto.html)
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

# Ruta para la página de cursos (cursos.html)
@app.route("/cursos")
def cursos():
    return render_template("cursos.html")

# Ruta para la página de historia (historia.html)
@app.route("/historia")
def historia():
    return render_template("historia.html")

# Ruta para la página de misión (mision.html)
@app.route("/mision")
def mision():
    return render_template("mision.html")

# Ruta para manejar las solicitudes al chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    pregunta = data.get('pregunta')
    
    # Clasificar la pregunta y generar la respuesta
    nivel, respuesta_predefinida = clasificar_pregunta(pregunta)
    
    if respuesta_predefinida:
        respuesta = respuesta_predefinida
    else:
        respuesta = responder_pregunta(pregunta, index, vectorizer, df)

    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(debug=True)
