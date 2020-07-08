from flask import Flask,jsonify,request
import json
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
@app.route("/tarefas/",methods=['GET'])
def lista_tarefas():
    return jsonify(tarefas)

@app.route("/tarefa/<int:id>/",methods=['GET','PUT','DELETE'])
def tarefa(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            response = {'status':'Erro','msg':'registro nao encontrado'}
        except Exception as ex:
            response = {'status':'Erro','msg': ex}
        return jsonify(response)

    elif request.method == 'PUT':
        status = json.loads(request.data)
        if tarefas[id]['status'] != status:
            tarefas[id]['status'] = status
            response = {'msg':'status do registro alterado'}
        else:
            response = {'msg':'Erro: o registro já encontra-se no estado atual'}
        return jsonify(response)

    elif request.method == 'DELETE':
        try:
            tarefas.pop(id)
            response = {'status':'sucesso','msg':'registro deletado'}
        except IndexError:
            response = {'status':'Erro','msg':'Registro nao encontrado'}
        except Exception:
            response = {'status':'Erro','msg':'Desconhecido'}
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)