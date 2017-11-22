import json 
jsonInput = '' #Place JSON here 

jsonForFile = json.dumps(jsonInput, sort_keys=True,
                  indent=4, separators=(',', ': '))

f = open('jsonData.txt','w')
f.write(jsonForFile)
f.close()
