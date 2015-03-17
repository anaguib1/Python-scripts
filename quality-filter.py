#! /usr/bin/env python

"""
Eliminate reads with average quality scores lower than
a set threshold.  Output sequences will be placed in 'passquality.keep'.

% python scripts/quality-filter.py [ -Q <cutoff> ] <data1> <data2> ...

Use '-h' for parameter help.

fh.write(saved_lines + '\n')

"""
file = 'SRR492066.fastq'
fh = open("SRR492066_quality.fastq", "w")
#counter to track what line is being read
i = 1
saved_lines = []

#opens/closes the file
with open(file) as f:
    for line in f:
    
    	#store lines preemptively
    	saved_lines.append(line)
    
    	#if on the line with quality score
        if(i % 4 == 0):
			s = line
			sum1 = [ord(c) for c in s]
			#check that it passes quality threshold
			if( sum(sum1)/len(s) > 50 ):
				for item in saved_lines:
					fh.write("%s\n" % item)
        		del saved_lines[:]
        		#reset the list
        		
        #continue line counting
        i += 1        	
        
        

fh.close()