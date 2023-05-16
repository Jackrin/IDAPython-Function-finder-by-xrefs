import idaapi
import idautils

adrs = [0xA0B340]
callsNum = [2]
strict = True
temp = []
adrsXrefs = []
result = []

def getXrefs(adrs):
    global temp
    for i, adr in enumerate(adrs):
        temp = []
        temp.clear()
        for ref in idautils.XrefsTo(adr, 1):
            f = ida_funcs.get_func(ref.frm)
            if f:
                temp.append(hex(f.start_ea))
        temp = remove_repeated(temp, callsNum[i])
        if strict:
            temp = remove_repeated2(temp, callsNum[i])
        temp = list(set(temp))
        adrsXrefs.append(temp)
        
def remove_repeated(temp, k):
    temp = [i for i in temp if temp.count(i) >= k]
    return temp

def remove_repeated2(temp, k):
    temp = [i for i in temp if temp.count(i) == k]
    return temp
   
def xrefComp():
    global result
    if len(adrsXrefs) == 1:
        result = adrsXrefs[0]
    for i, xrefList in enumerate(adrsXrefs):
        try:
            if not adrsXrefs[i+1]:
                break;
        except IndexError:
            break;
        if i == 0:
            result = [x for x in xrefList if x in adrsXrefs[i+1]]
        result = [x for x in result if x in adrsXrefs[i+1]]
                         
getXrefs(adrs)
xrefComp()
print("\nResults:\n------------")
for match in result:
    print(match)
print("------------")