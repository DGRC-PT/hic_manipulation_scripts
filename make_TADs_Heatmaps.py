#transforms a matrix with the format:
#chrA\tstart cordA\t end cordA\tchrB\tstart cordB\tend cordB\t number of interactions
#into a simetric matrix and then plots it into an interaction heatmap

import argparse
from gooey import Gooey,GooeyParser
#from multiprocessing import Process, freeze_support
import os

@Gooey
def main():
	"""gives a graphic input form to the progran"""
	parser=GooeyParser(description="Matrix to	heatmap")

	parser.add_argument(
	'ch',
	metavar='Chromosome',
	help='insert the reference chromosome. Ex: chr2, chrX...')
	
	parser.add_argument(
	'start',
	metavar='Interval start',
	help='insert the start coordinate of the interval to plot')

	parser.add_argument(
	'stop',
	metavar='Interval end',
	help='insert the end coordinate of the interval to plot')
	
	parser.add_argument(
	'infile',
	metavar='Input file',
	help='chose the interactions file of interest (chromosome and cell line)', widget='FileChooser')
	
	parser.add_argument(
	'outfile',
	metavar='Output matrix file',
	help='insert the output matrix file name', widget="FileSaver")

	parser.add_argument(
	'outplot',
	metavar='Output plot file',
	help='insert the output plot file name (*.png)', widget="FileSaver")
	
	args= parser.parse_args()
	aa=str(args)
	#transforms the input matrix into a simetric matrix as required by R
	dic,names=read_ints(args.infile, args.start, args.stop)
	write_file(dic,names, args.outfile)
	#Runs the R script to output the plot
	os.system("Rscript hi-c_plot.R "+args.outfile+" "+args.ch+ " "+str(args.start)+" "+str(args.stop)+" "+str(args.outplot))
	

def read_ints(infile, start, stop):
	"""Reads the interactions matrix, taking into account
	the start and end of the region to plot"""
	f=open(infile)
	dic={}
	names=set()
	for i in f:
		line=i.split("\t")
		if int(line[1])>=int(start) and int(line[1])<=int(stop) and int(line[4])>=int(start) and int(line[4])<=int(stop) :
			if line[1]+"-"+line[4] not in dic:
				dic[line[1]+"-"+line[4]]=line[-1].strip()
				names.add(int(line[1]))
				names.add(int(line[4]))
	f.close()
	return dic, sorted(names)

def header(names):
	"""makes the header of the simetric matrix"""
	a="\t"
	for el in names:
		a+=str(el)+"\t"
	return a

def write_file(dic, names, outfile):
	"""writes the simetric matrix to be used by R sushi plot hic"""
	second=names
	out=open(outfile, "w")
	out.write(header(names)+"\n")
	for col in names:
		a=str(col)+"\t"
		for row in second:
			if str(col)+"-"+str(row) in dic:
				a+=dic[str(col)+"-"+str(row)]+"\t"
			elif str(row)+"-"+str(col) in dic:
				a+=dic[str(row)+"-"+str(col)]+"\t"
			else:
				a+="0\t"
		out.write(a+"\n")
	out.close()
	
if __name__ =='__main__':
	#freeze_support()
	main()
	
	#Process(target=f).start()
