
fcomplete = open('todo/completed.txt','r')
ftodo = open('todo/calcHM.txt')

todo = ftodo.readlines()
complete = fcomplete.readlines()

print len(todo)
print len(complete)

for line in complete:
	todo.remove(line)
	print len(todo)

fcomplete.close()
ftodo.close()

print len(todo)
fnewTodo = open('todo/calcHM2.txt','w')

for line in todo:
	fnewTodo.write(line)

fnewTodo.close()