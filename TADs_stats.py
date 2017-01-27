#this script uses a matrix with
#chrA\tstart cordA\t end cordA\tchrB\tstart cordB\tend cordB\t number of interactions
#and extract statistics of total, disrupted and mantained interactions
#taking into account the breakpoint given by the user
#command:
#python TADs_stats.py interaction_matrix chromosome(as named in the matrix) start_interval stop_interval breakpoint 
#the statistics are outputed to prompt

from sys import argv

def select_ints(infile,chrr, start, stop):
	"""from a interactions file with the fields
	chrA\tstart cordA\t end cordA\tchrB\tstart cordB\tend cordB\t number of interactions
	selects the interactions that one of the intervals is inside start and stop.
	retrives a dictionary with
	dic[start cordA-start cordB]=number of interactions"""
	f=open(infile)
	dic={}
	for i in f:
		line=i.split()
		if chrr==line[0] and chrr==line[3]:
			if line[1]+"-"+line[4] not in dic and line[4]+"-"+line[1] not in dic and line[1]!=line[4]:
				if (int(line[1])>=int(start) and int(line[2])<=int(stop)) or (int(line[4])>=int(start) and int(line[5])<=int(stop)):
					dic[line[1]+"-"+line[4]]=float(line[-1])
	f.close()
	return dic


def stats(dic, bp):
	"""uses the dictionary created by select_ints to calculate the total
	maintained and disrupted interactions taking into account the breakpoint#####"""
	tot=0.0
	man=0.0
	intt=0.0
	for key, value in dic.items():
		i=key.split("-")
		if int(i[0])<=int(bp) and int(i[1])>=int(bp) : 
			intt+=value
		elif int(i[1])<=int(bp) and int(i[0])>=int(bp) : 
			intt+=value
		else:
			man+=value
		tot+=value
	print("totais: "+str(tot))
	print("interrompidas: "+str(intt))
	print("mantidas: "+str(man))

	

stats(select_ints(argv[1], argv[2], argv[3], argv[4]), argv[5])
