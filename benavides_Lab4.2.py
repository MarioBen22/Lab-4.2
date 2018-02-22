# Mario Benavides
# Program Status - completed
# displays the number in mm the ocean will have risen over 25 years.


# header and new lines
print('Year\t', 'Sea Level Rise (mm)\n-----\t---------------------\n')


# range and calculations and print
mmrise = 1.8

for currentyear in range(1, 26):
	sealevelrise = currentyear * mmrise
	print(currentyear, '\t', format(sealevelrise, '.2f'))
