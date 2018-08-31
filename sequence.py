
"""
pickle.dump(obj, file, protocol = None, fix_imports = True)
"""

import pickle
data = [1, 2, 3]
# 序列化数据并以字节对象返回
dumps_obj = pickle.dumps(data)
print('pickle.dumps():', dumps_obj)
# 从字节对象中反序列化数据
loads_data = pickle.loads(dumps_obj)
print('pickle.loads():', loads_data)

filename = 'data.log'

# 序列化数据到文件中
with open(filename, 'wb') as file:
        pickle.dump(data, file)

# 从文件中加载并反序列化
with open(filename, 'rb') as file:
    load_data = pickle.load(file)
    print('pickle.load():', load_data)
