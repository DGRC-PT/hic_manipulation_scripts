# Interactions manipulation scripts

Small scripts developed for the manipulation, plot and extraction of metrics from hi-c interaction matrixes

##sam2readtable.py
Transforms a SAM file into a read table to be inputed to juicebox:

In the command line:
<pre><code>python sam2readtable.py
</code></pre>

##dump2matrix.py
Transforms the output of juicebox dump into a table-style interaction list
With the following elements:
ChromosomeA start_coordinate_A end_coordinate_A chromosomeB start_coordinate_B end_coordinate_B number of interactions

In the command line:
<pre><code>python dump2matrix.py chromosome binnsize infile > outfile
</code></pre>

+ The chromosome must be inputed as the user wants it to appear in the output file
+ binnsize is the bin size used in the matrix, in bp

##select_interactions_interval.py
Uses a input file as outputed by dump2matrix.py, and selects the interactions inside
the interval defined by the user. The output as the same format as the input.

In the command line:
<pre><code>python select_interactions_interval.py infile start_interval end_interval > outfile
</code></pre>

##TADs_stats.py
Retrives metrics of total, maintained and disrupted interactions from an input file similar
to the output of dump2matrix.py, using a breakpoint defined by the user

In the command line:
<pre><code>python TADs_stats.py infile chromosome start_interval stop_interval breakpoint 
</code></pre>

+ The chromosome must be inputed as the user wants it to appear in the output file
+ start and stop interval defines the interval to be analysed
+ breakpoint is the breakpoint coordinate in bp


##make_hist.py
Retrives a histogram-type of input file for circos, using as input file a file similar to the dum2matrix.py output file.
This script output two types of file:
+ one with the information of the total interactions by bin
#another with the information of the maintained and disrupted interactions by bin

In the command line (for the total interactions):
<pre><code>python make_hist.py infile outfile chromosome binsize 
</code></pre>

In the command line (for the maintained and disrupted interactions):
<pre><code>python make_hist.py "bp" infile breakpoint outfile chromosome binsize
</code></pre>


##hic2heatmap
Wrapper of a python script and an R script to plot hic heatmaps.
The Wraper as a graphic interface that can be called using:

<pre><code>python make_TADs_Heatmaps.py
</code></pre>

![Input interface]https://github.com/DGRC-PT/hic_manipulation_scripts/blob/master/heatmap_input.png

###Dependencies:
+ Python
+ R
+ Python OS
+ R sushi package 
+ Gooey

##License:

GPLv2


##Found a bug?

Or maybe just wanto to drop some feedback? Just open an issue on github!
   
