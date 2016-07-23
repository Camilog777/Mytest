#!flask/bin/python
# -*- coding: iso-8859-15 -*-
# Librerias requeridas para correr aplicaciones basadas en Flask
from flask import Flask, jsonify, make_response, request
import subprocess

app = Flask(__name__)

# Web service que se invoca al momento de ejecutar el comando
# curl http://localhost:5000
@app.route('/',methods = ['GET'])
def index():
	return "Bienvenido al manejador de MV"

# Este metodo retorna la lista de sistemas operativos soportados por VirtualBox
# Los tipos de sistemas operativos soportados deben ser mostrados al ejecutar 
# el comando
# curl http://localhost:5000/vms/ostypes
# Este es el codigo del item 1
@app.route('/vms/ostypes',methods = ['GET'])
def ostypes():
	output = subprocess.check_output(['VBoxManage','list','ostypes'])
	return output

# Este metodo retorna la lista de maquinas asociadas con un usuario al ejecutar
# el comando
# curl http://localhost:5000/vms
# Este es el codigo del item 2a
@app.route('/vms',methods = ['GET'])
def listvms():
	output = subprocess.check_output(['VBoxManage','list','vms'])
	return output

# Este metodo retorna aquellas maquinas que se encuentran en ejecucion al 
# ejecutar el comando
# curl http://localhost:5000/vms/running
# Este es el codigo del item 2b
@app.route('/vms/running',methods = ['GET'])
def runninglistvms():
	output = subprocess.check_output(['VBoxManage','list','runningvms'])
	return output

# Este metodo retorna las caracteristicas de una maquina virtual cuyo nombre es
# vmname .
@app.route('/vms/info/<vmname>', methods = ['GET'])
def vminfo(vmname):
	output = subprocess.check_output(["./SearchMV.sh",vmname])
	return output

# Usted deberá realizar además los items 4 y 5 del enunciado del proyecto 
# considerando que:
# - El item 4 deberá usar el método POST del protocolo HTT
#curl -i -H "Content-Type: application/json" -X POST -d '{"name":"os-web","memory":"580","cores":"4"}' http://localhost:5000/vms
@app.route('/vms',methods = ['POST'])
def createvm():
	VM = request.json['name']
	Mem = request.json['memory']
	Core = request.json['cores']
	Cre=subprocess.check_output(["./CreateMV.sh",VM,Mem,Core])
	return Cre

# - El item 5 deberá usar el método DELETE del protocolo HTTP
#Borra una tarea(curl -i -X DELETE http://localhost:5000/vms/os-web)
@app.route('/vms/<vmname>',methods = ['DELETE'])
def deletemv(vmname):
	VM=vmname
	Del=subprocess.check_output(["./DeleteMV.sh",VM])
	return Del

if __name__ == '__main__':
        app.run(debug = True, host='0.0.0.0')
