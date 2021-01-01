#!/usr/bin/env python

data = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"""


def apply_all_replacements(molecules, replacements):
	new_molecules = set()
	# loop the input molecules
	for molecule in molecules:
		# loop the available replacements
		for to_replace, replacement in replacements:
			# loop over the characters of this input molecule
			for i in range(len(molecule) + 1 - len(to_replace)):
				# check if the current character(s) match the bit to replace
				a, b, c = molecule[0:i], molecule[i:i+len(to_replace)], molecule[i+len(to_replace):]
				if b == to_replace:
					# build a new molecule
					new_molecule = a + replacement + c
					# add the new molecule to the set
					new_molecules.add(new_molecule)
	return new_molecules

lines = data.split('\n')
medicine_molecule = lines[-1]
replacements = []
for line in lines:
	if len(line.strip()) == 0:
		break
	replacements.append(line.split(' => '))

molecules = apply_all_replacements([medicine_molecule], replacements)
print(len(molecules))

#reductions = [[re.compile(big), small] for small, big in replacements]
reductions = [[big, small] for small, big in replacements]

print(reductions)

# def apply_all_reductions(molecules, reductions):
# 	new_molecules = set()
# 	for molecule in molecules:
# 		for big, small in reductions:
# 			find_start = 0
# 			while find_start >= 0:
# 				found_start = molecule.find(big, find_start)
# 				if found_start >= 0:
# 					find_start = found_start + 1
# 					new_molecule = molecule[0:found_start] + small + molecule[found_start+len(big):]
# 					new_molecules.add(new_molecule)
# 				else:
# 					find_start = found_start
# 	return new_molecules

def apply_all_reductions(molecules, reductions):
	new_molecules = set()
	for molecule in molecules:
		for big, small in reductions:
			molecule.replace(big, small)
	return new_molecules


molecules = [medicine_molecule]

i = 0
while 'e' not in molecules:
	molecules = apply_all_reductions(molecules, reductions)
	i += 1
	if len(molecules) > 0:
		shortest = min([len(x) for x in molecules])
		print('After {0} rounds, {1} molecules, shortest is {2}'.format(i, len(molecules), shortest))
	else:
		print('After {0} rounds, 0 molecules?!'.format(i))


