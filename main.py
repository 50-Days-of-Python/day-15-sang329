num_list = eval(input())
format_list = []
for i in num_list:
  format_list.append("{:,}".format(i))
  
print(format_list)
