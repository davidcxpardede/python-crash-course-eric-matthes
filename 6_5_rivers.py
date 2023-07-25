'''
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile':'egypt'.
- Use a loop to print a sentence about each river.
- Use a loop to print the name of each river included in the dictionary.
- Use a loop to print the name of each country included in the dictionary.
'''

sungai_indonesia = {'Batanghari':'Sumatra',
         'Bengawan Solo':'Jawa',
         'Kapuas':'Kalimantan',
         'Lariang':'Sulawesi',
         'Sepik':'Papua',}

for sungai, pulau in sungai_indonesia.items():
    print(f"Sungai {sungai} berada di Pulau {pulau}.")

print("\nNama-nama sungai terpanjang di tiap pulau di Indonesia adalah:")
for sungai in sungai_indonesia.keys():
    print(f"Sungai {sungai}")
    
print("\nNama lima pulau utama di Indonesia adalah:")
for pulau in sungai_indonesia.values():
    print(f"Pulau {pulau}")