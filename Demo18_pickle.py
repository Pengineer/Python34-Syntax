# pickle 将较长序列存储到磁盘

import pickle

my_list = [1, 'a', ['赵','钱']]
pickle_file = open('D:\\my_list.pkl', 'wb')
pickle.dump(my_list, pickle_file)
pickle_file.close()

pickle_file = open('D:\\my_list.pkl', 'rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)
