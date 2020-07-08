from flask import Flask

app = Flask(__name__)

tarefas = [
    {
        'id':0,
        'tarefa':'Desenvolver uma API flask',
        'responsavel':'Dassaev',
        'status':False
    },
    {
        'id':1,
        'tarefa':'estudar elementor',
        'responsavel':'dev',
        'status':False
    }

]
@app.route("/",methods=['GET'])
def tarefa():
    return 'Olá mundo'

if __name__ == '__main__':
    app.run(debug=True)