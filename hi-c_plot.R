#R script to plot the interactions heatmaps given a matrix as input
#the program automaticly fills the information needed for the plot
#the output is a plot in svg

args=commandArgs(trailingOnly = TRUE)
library(Sushi)
a<-read.table(args[1], check.names = FALSE)
b<-as.matrix(a)

#chromosome field
chrom=args[2]
#interval start field
chromstart=as.integer(args[3])
#interval end field
chromend=as.integer(args[4])
ma=(chromend-chromstart)/25000

#if a png output file is wanted
#png(filename=args[5], height=1654, width=1654)

svg(filename=args[5], height=1654, width=1654)

phic = plotHic(b,chrom,chromstart,chromend,palette = colorRampPalette(c("white","red")),flip=FALSE, max_y = ma, zrange=c(0,4))

labelgenome(chrom,chromstart,chromend,side=1,scipen=20,n=20,scale="bp",edgeblankfraction=0.20,line=.18,chromline=.5,scaleline=0.5)

addlegend(c(0.28,2),palette=phic[[2]],side="right",bottominset=0.4,topinset=0,xoffset=-.035,labelside="left",width=0.025,title.offset=0.035)

dev.off()