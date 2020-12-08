import requests # python3 -m pip install requests
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
	
	data = requests.get(http)
	print(data.text)
	#ща
	
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






