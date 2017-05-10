import sys
import re
import argparse


parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()

with open(args.fname,newline='') as ifp:	
	for line in ifp:
		# convert everything to seconds 
		w=float(args.offset)
		mili=int(w*1000)
		sec=int(w)
		minutes=int((w%3600)//60)
		hrs=int(w//3600)

		#i am using the following regular expresion in order to 
		#find the time zones and i am separating every time 
		#zone in groups by () so i am making 8 different time slots in order to add or substract time
		# i am using + in order to find symbol : and .* to find multiple different symbols(-->)

		m=r'([0-9]{2}):+([0-9]{2}):+([0-9]{2}),+([0-9]{3}).*([0-9]{2}):+([0-9]{2}):+([0-9]{2}),+([0-9]{3})'
		rexp=re.compile(m)
		# i am serching every line of the text in order to find these ones with time
		k=rexp.search(line)
		if k:
		# i am using 8 variables to manage better the groups 
			a=int(k.group(1))
			b=int(k.group(2))
			c=int(k.group(3))
			d=int(k.group(4))
			e=int(k.group(5))
			f=int(k.group(6))
			g=int(k.group(7))
			h=int(k.group(8))
		# here i am doing the calculations in order to achieve the time we want
			if d<1000 and mili<1000 and d+mili<1000:
				d=d+mili
			else:
				d=1000-d


			if h<1000 and mili<1000 and h+mili<1000:
				h=h+mili
			else:
				h=1000-h

			if a<60 and hrs<60 and a+hrs<60:
				a=a+hrs
			else:
				a=60-a

			if b<60 and minutes<60 and b+minutes<60:
				b=b+minutes
			else:
				b=60-minutes

			if sec<60 and c<60 and sec+c<60:
				c=sec+c
			else:
				c=60-sec

			if e<60 and hrs<60 and e+hrs<60:
				e=e+hrs
			else:
				e=60-e

			if f<60 and minutes<60 and f+minutes<60:
				f=f+minutes
			else:
				f=60-minutes
				
			if sec<60 and g<60 and sec+g<60:
				g=sec+g
			else:
				g=60-sec

			# here i am using the format in order to print the time in the output tetx also i am making the old
			#line '' in order to put the new one at its possitions
			line=''
			form='{}:{}:{},{} --> {}:{}:{},{}'
			print(form.format(a,b,c,d,e,f,g,h))


			#print('wres',a,'minutes',b,'sec',c,'mili',d,'wres',e,'minutes',f,'sec',g,'mili',h)
			
		
		# -- αντικαταστήστε με τον δικό σας κώδικα (αρχή) --

		sys.stdout.write(line)

		# -- αντικαταστήστε με τον δικό σας κώδικα (τέλος) --