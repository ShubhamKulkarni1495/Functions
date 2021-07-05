color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
sort=sorted(color_dict.keys())
dic={}
for i in sort:
    for j in color_dict.values():
        if color_dict[i]==j:
            dic[i]=color_dict[i]
            break
print(dic)