import pandas as pandas

data1 = {
                'id': '2348208',
                'site': 'nordstromrack',
                'name': 'Floral Blouse',
            }

data2 = {
                'id': '2348209',
                'site': 'gap',
                'name': 'Pink Shirt',
            }

data3 = {
                'id': '2348210',
                'site': 'oldnavy',
                'name': 'Cargo Shorts',
            }

dictlist = [data1, data2, data3]

df = pandas.DataFrame(dictlist)
print (df)

df.to_csv('data.csv')