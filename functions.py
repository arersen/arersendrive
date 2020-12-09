import requests # python3 -m pip install requests
import base64
def add():
	name = input("username: ")
	file = input("filename: ")
	http = "http://arersengit.7m.pl/add.php?username=" + name + "&file=" + file
	#print(http)
	data = requests.get(http)
	print(data.text)
	slash = "/"
	print("Your link: http://arersengit.7m.pl/files/" + name + slash + file)
def get():
	name = input("username: ")
	file = input("filename: ")
	http = "http://arersengit.7m.pl/get.php?username=" + name  + "&file=" + file
	data = requests.get(http)
	print(data.text)
	#get.php?username=test&file=new.txt

def mkdir():
	name = input("username: ")
	file = input("filename: ")
	dir = input("directory name: ")
	http = "http://arersengit.7m.pl/mkdir.php/?username=" + name +  "&file=" + file + "&dir=" + dir
	#print(http)
	data = requests.get(http)
	print(data.text)
	link = name + "/" + file
	print("Your link: http://arersengit.7m.pl/files/" + name + "/" + dir)
def ls():
	name = input("username: ")
	print("If the directory is / then you are in main")
	dir = input("directory: ")

	http = 	"http://arersengit.7m.pl/list.php?username=" + name + "&dir=" + dir
	data = requests.get(http)
	print("\n")
	print("Directory content:" + name + "/" + dir)
	print(data.text)
class acc:
	def base64str():


		#read = open('encode.txt' ,'w')
		#read.write(encoded)

		name = input("username: ")
		file_pr = input("filename: ")
		data_1 = input("BASE64 String: ")



			#typeb64 = base64.encode(bytes(type,'utf-8'))
			#http://arersengit.7m.pl/edit.php?username=arersen&file=lox.py&data=YXJlcnNlbmdpdC43bS5wbC8vYWRkLnBocD91c2VybmFtZT10ZXN0JmZpbGU9bmV3LnR4dA==
		http = "http://arersengit.7m.pl/edit.php?username=" + name + "&file=" + file_pr + "&data=" + data_1
		date = requests.get(http)
		print(date.text)
class delete:
	def rm():
		name = input("username: ")
		file = input("filename: ")
		http = "http://arersengit.7m.pl/del.php?username=" + name + "&file=" + file
		data = requests.get(http)
		print (data.text)
		print('File succefuly removed!')






