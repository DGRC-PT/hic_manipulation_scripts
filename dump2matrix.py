#simple method that transforms the intrachromosomal matrix outputed
#by juicebox dump, into a file more easy to use by other tools
#the output is:
#chrA\tstart cordA\t end cordA\tchrB\tstart cordB\tend cordB\t number of interactions
#command:
#python dump2matrix.py chromosome(as we want to see in the output file) binnsize infile > outfile

from sys import argv

def read_file(chrr, binn, infile):
	f=open(infile)
	for i in f:
		line=i.split()
		print(chrr+"\t"+ line[0]+"\t"+ str(int(line[0])+int(binn))+"\t"+chrr+"\t"+line[1]+"\t"+str(int(line[1])+int(binn))+"\t"+line[-1].strip())
	f.close()

read_file(argv[1], argv[2], argv[3])
