'''
    regex check for names
'''
import re

group_exp = re.compile(r'^(LG){0,1}([YnNnTtLl]||YP)(\d{1,})$')

item_exp = re.compile(r'^(LG){0,1}([YnNnTtLl]||YP)(\d{1,})\S{0,}_(\d{1,})$')


ies_exp = re.compile(r'[^\\]{1,}\.(ies|IES)$')

#ies_exp = re.compile(r'[^\\]{1,}\.(ies|IES)')


def matchGroup(gname):
	m = re.match(group_exp,gname)
	if m:
		typeheader = m.group(2)
		groupID = int(m.group(3))
		return typeheader,groupID
	else:
		return false

def matchItem(gname):
	m = re.match(item_exp,gname)
	if m:
		typeheader = m.group(2)
		groupID = int(m.group(3))
		itemID = int(m.group(4))
		return typeheader,groupID,itemID
	else:
		return False

def matchIES(iespath):

    m = re.search(ies_exp,iespath)

    result = ""
    if m:
        print "matched"
        result = m.group(0)
    return str(result)



if __name__ == "__main__":
	a = matchIES(str('ccc\\asdfaa.ies'))#Green accent G2 4000lm 3000K NB.ies#F:\GUCCI\IES\IES files\GreenAccent Power\NB.ies

	print a