in_dic = [{'7': '2'}, {'13': '2'}, {'13': '8'}, {'15': '16'}, {'15': '14'}, {'17': '8'}, {'23': '8'}, {'23': '18'}, {'22': '20'}, {'7': '6'}, {'17': '16'}, {'22': '18'}]

results = {}
for dic in in_dic :
    for key in (dic.keys()) :
        #
        if key not in results :
            results[key] = []
        results[key].append(dic[key])
        #print(key, dic[key])


print("input:\n", in_dic)
print("\nresults:\n", results)
