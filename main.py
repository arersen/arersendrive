import requests # python3 -m pip install requests
import functions as func
import base64
while True:
	typee = input(">")
	if typee == "add":
		func.add()
	if typee  == "get":
		func.get()
	if typee == "mkdir":
		func.mkdir()
	if typee == "ls":
		func.ls()
	if typee == "list":
		func.ls()
	if typee == "dir":
		func.ls()

	if typee == "put":
		func.acc.base64str()
	if typee == 'del':
		func.delete.rm()
