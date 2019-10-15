data=['AC=1;AF=0.167;AN=6;BaseQRankSum=;ClippingRankSum=0;']
keys=[]
values=[]
for ele in data:
    ele=ele.replace('\\x3b',',')
    ele=ele.replace('\\x3d','=')
    interim=ele.split(';')
    for items in interim:
        x=items.find('=')
        key_temp=items[:x]
        value_temp=items[x+1:]
        if len(key_temp)>0 and len(value_temp)>0:
            keys.append(key_temp)
            values.append(value_temp)
    info_dict=dict(zip(keys,values))

print(info_dict)
