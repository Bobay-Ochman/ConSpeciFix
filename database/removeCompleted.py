
fcomplete = open('todo/completed_old.txt','r')
fcomplete2 = open('todo/completed_old2.txt','r')
ftodo = open('todo/calcHM_orig.txt')

todo = ftodo.readlines()
complete = fcomplete.readlines()
complete.extend(fcomplete2.readlines())


print len(todo)
print len(complete)

for line in complete:
	try:
		todo.remove(line)
	except:
		pass
	print len(todo)

fcomplete.close()
ftodo.close()

print len(todo)
fnewTodo = open('todo/calcHM2.txt','w')

for line in todo:
	fnewTodo.write(line)

fnewTodo.close()