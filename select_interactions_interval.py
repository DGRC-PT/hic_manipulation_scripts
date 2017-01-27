#uses a input file as:
#chrA\tstart cordA\t end cordA\tchrB\tstart cordB\tend cordB\t number of interactions
#and retrive the interactions from this file that are inside the interval given by the user
#the output has the same format as the input file
#command:
#python select_interactions_interval.py infile start_interval end_interval > outfile

from sys import argv

def select(infile, s, e):
	f=open(infile)
	start=int(s)
	end=int(e)
	for i in f:
		line=i.split("\t")
		if (int(line[1])>=start and int(line[1])<=end) or (int(line[2])>=start and int(line[2])<=end):
				print(i.strip())
		elif (int(line[5])>=start and int(line[5])<=end) or (int(line[4])>=start and int(line[4])<=end):
				print(i.strip())
	f.close()


select(argv[1], argv[2], argv[3])
