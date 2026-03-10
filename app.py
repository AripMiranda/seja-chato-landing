from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Isso procura o index.html dentro da pasta templates [cite: 1, 15]
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)