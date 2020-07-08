from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET'])
def tarefa():
    return 'Olá mundo'

if __name__ == '__main__':
    app.run(debug=True)