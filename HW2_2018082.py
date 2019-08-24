# CSE 101 - IP HW2
# K-Map Minimization 
# Name: RHYTHM GUPTA
# Roll Number: 2018082
# Section: A
# Group: 2
# Date: 18 Oct, 2018

def minFunc(numVar, stringIn):
	import fns_hw2
    
	b = stringIn.index('d')    
	minterms = stringIn[1:b-2].split(',')  # minterms list containing values of type int
	for i in minterms:
		minterms[minterms.index(i)] = int(i)
	binminterms = [0]*len(minterms)
	for i in range(len(minterms)):
		binminterms[i] = fns_hw2.converter_4bit(bin(minterms[i])[2:])
		

	if stringIn[b+2] == '-':
		dcminterms = []
	else:
		k = stringIn.index(')', b)    
		dcminterms = stringIn[b+3:k].split(',')  # don't care minterms
	for i in dcminterms:
		dcminterms[dcminterms.index(i)] = int(i)
	bindcminterms = [0]*len(dcminterms)
	for i in range(len(dcminterms)):
		bindcminterms[i] = fns_hw2.converter_4bit(bin(dcminterms[i])[2:])


        
	two = []  # list collecting all those implicants which have been formed by joining two minterms

	allbinminterms = binminterms + bindcminterms  # all minterms  (in binary )containing don't care ones
 

	G = [] # list containing those elements of allbinminterms which have combined to form two
	for i in allbinminterms:
		for j in allbinminterms[(allbinminterms.index(i)):]:
			if i!=j:
				if i[1:] == j[1:]:                      # only first digit is different
					two.append('&'+i[1:])
					G.append(i)
					G.append(j)
				elif (i[0] + i[2:]) == (j[0] + j[2:]):  # only second digit is different
					two.append(i[0] + '&' + i[2:])
					G.append(i)
					G.append(j)
				elif (i[0:2] + i[3]) == (j[0:2] + j[3]): # only third digit is different
					two.append(i[0:2] + '&' + i[3])
					G.append(i)
					G.append(j)
				elif (i[0:3]) == (j[0:3]):            # only last digit is different
					two.append(i[0:3] + '&')
					G.append(i)
					G.append(j)

	G = fns_hw2.uniq(G)
	binminterms.sort()
	uniprime = []  # prime implicants containing only one minterm
	for i in binminterms:
		flag = 1
		for j in G:
			if i == j:
				flag = 0
		if flag == 1:
			uniprime.append(i)

    
    
	two = fns_hw2.uniq(two)

	
	quad = []  # list collecting all those implicants which have been formed by joining four minterms


	H = [] # list containing those elements of allbinminterms which have combined to form quad
	for i in two:
		for j in two[(two.index(i)):]:
			if i!=j:
				if i[1:] == j[1:]:
					quad.append('&'+i[1:])
					H.append(i)
					H.append(j)
				elif (i[0] + i[2:]) == (j[0] + j[2:]):
					quad.append(i[0] + '&' + i[2:])
					H.append(i)
					H.append(j)
				elif (i[0:2] + i[3]) == (j[0:2] + j[3]):
					quad.append(i[0:2] + '&' + i[3])
					H.append(i)
					H.append(j)
				elif (i[0:3]) == (j[0:3]):
					quad.append(i[0:3] + '&')
					H.append(i)
					H.append(j)

	H = fns_hw2.uniq(H)
	two.sort()
	duoprime = [] # list containing prime implicants containing two minterms each
	for i in two:
		flag = 1
		for j in H:
			if i == j:
				flag = 0
		if flag == 1:
			duoprime.append(i)
	quad = fns_hw2.uniq(quad)

	
    
	octa = []  # list collecting all those implicants which have been formed by joining four minterms


	I = [] # list containing those elements of allbinminterms which have combined to form octa
	for i in quad:
		for j in quad[(quad.index(i)):]:
			if i!=j:
				if i[1:] == j[1:]:
					octa.append('&'+i[1:])
					I.append(i)
					I.append(j)
				elif (i[0] + i[2:]) == (j[0] + j[2:]):
					octa.append(i[0] + '&' + i[2:])
					I.append(i)
					I.append(j)
				elif (i[0:2] + i[3]) == (j[0:2] + j[3]):
					octa.append(i[0:2] + '&' + i[3])
					I.append(i)
					I.append(j)
				elif (i[0:3]) == (j[0:3]):
					octa.append(i[0:3] + '&')
					I.append(i)
					I.append(j)
	I = fns_hw2.uniq(I)
	quad.sort()
	quadprime = [] # list containing prime implicants containing four minterms each
	for i in quad:
		flag = 1
		for j in I:
			if i == j:
				flag = 0
		if flag == 1:
			quadprime.append(i)

	octa = fns_hw2.uniq(octa)

	hexa = []
	for i in octa:
		for j in octa[octa.index(i):]:
			if i != j :
				if i[1:] == j[1:]:
					hexa.append('&' + i[1:])
				elif i[0] == j[0] and i[2:] == j[2:]:
					hexa.append(i[0] + '&' + i[2:])
				elif i[3] == j[3] and i[:2] == j[:2]:
					hexa.append(i[:2] + '&' + i[3])
				elif i[:3] == j[:3]:
					hexa.append(i[:3] + '&')
	hexa = fns_hw2.uniq(hexa)

	#map0
	primeimp = uniprime
	primeimp.extend(duoprime)
	primeimp.extend(quadprime)
	primeimp.extend(octa)
	map0 = {}

	primedecoded = {}
	for i in primeimp:
		primedecoded[i] = fns_hw2.decoder(i)

	for j in minterms:
		map0[j] = primedecoded
	epi = [] # list of essential prime implicants
	min_epi = [] # list of minterms which are included in essential prime implicants
	# finding epi
	for m in map0:  # m is input minterm 
		T = []       # local list 
		k = fns_hw2.converter_4bit(bin(m))[2:]   # binary value of input minterm
		for n in map0[m]:  # n is prime implicant
			for p in map0[m][n]:  # p is minterm corresponding to n
				if k == p:
					T.append(n)  # T collects prime implicants consisting of input minterm
		if len(T) == 1: # only 1 prime implicant contains input minterm
			epi.append(T[0])
			min_epi.append(m)

	epi = fns_hw2.uniq(epi)
	for i in epi:
		for j in fns_hw2.decoder(i):
			if min_epi.count(int(j,2)) == 0:
				min_epi.append(int(j,2))

	
	rempi = []  #list of prime implicants which are not epi
	for i in primeimp:
		if epi.count(i) == 0:
			rempi.append(i)

	remmin = []  # list of minterms which are not covered in epi
	for i in minterms:
		if min_epi.count(i) == 0:
			remmin.append(i)

	#map1

	map1 = {}
	rempi_decoded = {}
	for i in rempi:
		rempi_decoded[i] = fns_hw2.decoder(i)

	for j in remmin:
		map1[j] = rempi_decoded

	
	P = []  # a list containing dictionaries. Terms in these dictionaries are summed together and these dictionaries are multiplied together
	for m in map1:
		X = {}
		k = fns_hw2.converter_4bit(bin(m)[2:])
		for n in map1[m]:
			for p in map1[m][n]:
				if p==k:
					X[str(rempi.index(n))] = n
		P.append(X)	
	possible_ans = []         # a list containing those terms of possible_other_terms which have least number of prime implicants
	
	possible_other_terms = fns_hw2.sop(P)

	
	if len(possible_other_terms) > 0:                # finding terms with least number of terms among possible_other_terms
		min = len(possible_other_terms[0])

		for i in possible_other_terms:
			if len(i) < min:
				min = len(i)


		for i in possible_other_terms:
			if len(i) == min:
				possible_ans.append(i)
	
	list_possible_ans = []  # A list which contains sublists. Each of these sublists is a possible minimum solution of the problem
	epi_hr = []  # contains essential prime implicants in terms of w,x,y,z
	for i in range(len(epi)):
		epi_hr.append(fns_hw2.pi_hr(epi[i]))
	if len(possible_ans)==0:
		list_possible_ans.extend(epi_hr)
	else:
		for a in possible_ans :
			S = []
			for b in a:
				k = fns_hw2.pi_hr(rempi[int(b)])
				S.append(k)
			S.extend(epi_hr)
			list_possible_ans.append(S)
	
	output = ''
	
	for j in list_possible_ans:
		for i in j:
			output = output + i
			if i!=j[-1]:
				output = output + '+'
		if j != list_possible_ans[-1]:
			output = output + ' OR '
	if numVar == 4:
		if hexa == ['&&&&']:
			return('1')
		else:
			return(output)
	elif numVar == 3:
		if primeimp == ['0&&&']:
			return('1')
		else:
			output1 = output.replace("w'","")
			output2 = output1.replace('x','w')
			output3 = output2.replace('y','x')
			finaloutput = output3.replace('z','y')
			return(finaloutput)
	elif numVar == 2:
		if primeimp == ['00&&']:
			return('1')
		else:
			output1 = output.replace("w'","")
			output2 = output1.replace("x'","")
			output3 = output2.replace('y','w')
			finaloutput = output3.replace('z','x')
			return(finaloutput)






