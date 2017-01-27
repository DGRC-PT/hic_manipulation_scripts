#!/usr/bin/python
#transforms the input file with the format 
#chrA\tstart cordA\t end cordA\tchrB\tstart cordB\tend cordB\t number of interactions
#in an histogram type of track for histogram plot in circos
#this script can do two types of files
#one with the total interactions of the input file
#with the output as:
#chr\tstart bin\t end bin\t total interactions

#the input command is:
#python make_hist.py matrix outfile chrr binsize

#and another with the maintained and disrupted interactions
#created by a given breakpoint
#with the output as:
#chr\tstart bin\t end bin\t maintained interactions\t disrupted interactions

#the input command is:
#python make_hist.py "bp" matrix breakpoint outfile chromosome binsize

from sys import argv

def read_file(infile):
	"""read the infile with the format
	chrA\tstart cordA\t end cordA\tchrB\tstart cordB\tend cordB\t number of interactions
	and extract the counts of interactions per bin. It returns a dictionary as
	dic[startbin]=number of interactions that involve bin1"""
	f=open(infile)
	dic={}
	s=set()
	for i in f:
		line=i.split()
		if line[1] not in dic and line[4] not in dic:
			dic[line[1]]=float(line[-1])
			dic[line[4]]=float(line[-1])
			s.add(line[1]+"-"+line[4])
			s.add(line[4]+"-"+line[1])
		elif line[1] in dic and line[4] not in dic:
			dic[line[1]]+=float(line[-1])
			dic[line[4]]=float(line[-1])
			s.add(line[1]+"-"+line[4])
			s.add(line[4]+"-"+line[1])
		elif line[1] not in dic and line[4] in dic:
			dic[line[1]]=float(line[-1])
			dic[line[4]]+=float(line[-1])
			s.add(line[1]+"-"+line[4])
			s.add(line[4]+"-"+line[1])
		else:
			if line[1]+"-"+line[4] not in s or line[4]+"-"+line[1] not in s:
				dic[line[1]]+=float(line[-1])
				dic[line[4]]+=float(line[-1])
				s.add(line[1]+"-"+line[4])
				s.add(line[4]+"-"+line[1])
			
	f.close()
	return dic

def writte(dic, outfile1, chrr, binsize):
	"""writes the output of read_file with the format:
	chr\tstartbin\tendbin\tnumber of interactions"""
	out1=open(outfile1, "w")
	for key, value in dic.items():
		out1.write(str(chrr)+"\t"+str(key)+"\t"+str(int(key)+int(binsize))+"\t"+str(value)+"\n")
	out1.close()
	
	
###################################3

def read_file_sep(infile, bp):
	"""read the infile with the format
	chrA\tstart cordA\t end cordA\tchrB\tstart cordB\tend cordB\t number of interactions
	and extract the counts of interactions per bin separated by maintained and disrupted
	taking into account the breakpoint given. It returns a dictionary as
	dic[startbin]=[disrupted interactions, maintained interactions]"""
	f=open(infile)
	dic={}
	s=set()
	for i in f:
		line=i.split()
		if line[1] not in dic and line[4] not in dic:
			s.add(line[1]+"-"+line[4])
			s.add(line[4]+"-"+line[1])
			if (int(line[1])<int(bp) and int(line[4])>int(bp)) or (int(line[1])>int(bp) and int(line[4])<int(bp)):
				dic[line[1]]=[float(line[-1]),0.0]#[interrompidas, mantidas]
				dic[line[4]]=[float(line[-1]), 0.0]
			else:
				dic[line[1]]=[0.0, float(line[-1])]#[interrompidas, mantidas]
				dic[line[4]]=[0.0, float(line[-1])]				
		elif line[1] in dic and line[4] not in dic:
			s.add(line[1]+"-"+line[4])
			s.add(line[4]+"-"+line[1])
			if (int(line[1])<int(bp) and int(line[4])>int(bp)) or (int(line[1])>int(bp) and int(line[4])<int(bp)):
				dic[line[1]][0]+=float(line[-1])
				dic[line[4]]=[float(line[-1]),0.0]
			else:
				dic[line[1]][1]+=float(line[-1])
				dic[line[4]]=[0.0, float(line[-1])]			
		elif line[1] not in dic and line[4] in dic:
			s.add(line[1]+"-"+line[4])
			s.add(line[4]+"-"+line[1])
			if (int(line[1])<int(bp) and int(line[4])>int(bp)) or (int(line[1])>int(bp) and int(line[4])<int(bp)):
				dic[line[1]]=[float(line[-1]),0.0]
				dic[line[4]][0]+=float(line[-1])
			else:
				dic[line[4]][1]+=float(line[-1])
				dic[line[1]]=[0.0, float(line[-1])]					
		else:
			if line[1]+"-"+line[4] not in s or line[4]+"-"+line[1] not in s:
				s.add(line[1]+"-"+line[4])
				s.add(line[4]+"-"+line[1])
				if (int(line[1])<int(bp) and int(line[4])>int(bp)) or (int(line[1])>int(bp) and int(line[4])<int(bp)):
					dic[line[1]][0]+=float(line[-1])
					dic[line[4]][0]+=float(line[-1])
				else:
					dic[line[1]][1]+=float(line[-1])
					dic[line[4]][1]+=float(line[-1])			
	f.close()
	return dic

def writte_sep(dic, outfile1, chrr, binsize):
	"""writes the output of read_file with the format:
	chr\tstartbin\tendbin\tnumber of maintained interactions\t number of disrupted interactions"""
	out1=open(outfile1, "w")
	for key, value in dic.items():
		out1.write(str(chrr)+" "+str(key)+" "+str(key+int(binsize))+" "+str(value[1])+" "+str(value[0])+"\n")
	out1.close()
	

if argv[1]=="bp":
	writte_sep(read_file_sep(argv[2], argv[3]), argv[4], argv[5],argv[6])
else:
	writte(read_file(argv[1]), argv[2], argv[3], argv[4])
