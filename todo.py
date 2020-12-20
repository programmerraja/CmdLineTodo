import sys,os,datetime	
class Todo:
	def __init__(self):

		# constant value
		self.CURRENTDIR=os.getcwd()
		self.TODOFILEPATH=os.path.join(self.CURRENTDIR,"todo.txt")
		self.DONEFILEPATH=os.path.join(self.CURRENTDIR,"done.txt")
		self.TODAYDATE=str(datetime.date.today())
		
		# calling main function
		self.main()

	def main(self):
		# getting the cmd line argv
		if(len(sys.argv)==3):
			option=sys.argv[1]
			argv=sys.argv[2]
		elif(len(sys.argv)==2):
			option=sys.argv[1]
			argv=False
		else:
			self.showHelp()
			return
		
		# call function to open file 
		self.openFile()
		
		# reading todo file content and store it on the var
		self.todo_file_content=self.readFile(self.TODOFILEPATH)
		
		# reading done file content and store it on the var
		self.done_file_content=self.readFile(self.DONEFILEPATH)
		
		# checking for the cmd line 
		if(option=="add"):
			self.addTodo(argv)
		elif(option=="ls"):
			self.listTodo()
		elif(option=="del"):
			if(argv):
				self.deleteTodo(int(argv))
			#if not agrv given
			else:
				print("Error: Missing NUMBER for deleting todo.")
		elif(option=="done"):
			if(argv):
				self.doneTodo(int(argv))
			#if not argv given
			else:
				print("Error: Missing NUMBER for marking todo as done.")
		elif(option=="help"):
			self.showHelp()
		elif(option=="report"):
			self.reportTodo()
		elif(option=="ls"):
			self.listTodo()
		else:
			print("Error: Invalid option")
			self.showHelp()

	def openFile(self):
		
		# if file exit we want to create file in append mode else create in write mode
		if(os.path.exists(self.DONEFILEPATH)):
			mode="a"
		else:
			mode="w"
		#openning file 
		self.todo_file=open(self.TODOFILEPATH,mode)
		self.done_file=open(self.DONEFILEPATH,mode)

	def readFile(self,filename):
		
		#returning the file content 
		file_ptr=open(filename,"r")
		file_content=file_ptr.readlines()
		return file_content

	def writeFileTodo(self,file_content):
		
		#write the todo in todo.txt file 
		file_ptr=open(self.TODOFILEPATH,"w")
		for i in range(0,len(file_content)):
			file_ptr.write(file_content[i])
			
			
	def writeFileDone(self,file_content):
		
		#write the todo in done.txt file 
		content="x "+self.TODAYDATE+" "+file_content
		self.done_file.write(content)

	def addTodo(self,todo):
		if(todo):
			#adding the todo in file 
			self.todo_file.write(todo+"\n")
			print("Added todo: \""+todo+"\"")
		else:
			print("Error: Missing todo string. Nothing added!")


	def listTodo(self):
		
		#list the todo
		if(self.todo_file_content):
			for i in range(len(self.todo_file_content)-1,-1,-1):		
					print("["+str(i+1)+"] "+self.todo_file_content[i],end='')
		else:
			print("There are no pending todos!")

	def deleteTodo(self,index):
		
		# delet the todo
		if(self.todo_file_content and index<=len(self.todo_file_content) and index>0):
			self.todo_file_content.pop(index-1)
			self.writeFileTodo(self.todo_file_content)
			print("Deleted todo #"+str(index))
		else:
			print("Error: todo #"+str(index)+" does not exist. Nothing deleted.")

	def doneTodo(self,index):
		
		# move the todo form todo.txt to done.txt
		if(self.todo_file_content and index<=len(self.todo_file_content) and index>0):
			compeleted_todo=self.todo_file_content[index-1]
			self.todo_file_content.pop(index-1)
			self.writeFileTodo(self.todo_file_content)
			self.writeFileDone(compeleted_todo)	
			print("Marked todo #"+str(index)+" as done.")
		else:
			print("Error: todo #"+str(index)+" does not exist.")



	def showHelp(self):
		
		# showing help
			print("""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics""")
	def reportTodo(self):
		
		# showing report
		Pending=len(self.todo_file_content)
		compeleted=len(self.done_file_content)
		print(self.TODAYDATE +" Pending : "+ str(Pending) +" Completed : "+ str(compeleted))
	

todoapp=Todo()