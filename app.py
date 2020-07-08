from flask import Flask,jsonify,request

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
@app.route("/tarefa/<int:id>/",methods=['GET'])
def tarefa(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            response = {'status':'Erro','msg':'registro nao encontrado'}
        except Exception as ex:
            response = {'status':'Erro','msg': ex}
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)