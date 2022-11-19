'''
homerseklet = [0,12,13,9,2,7]

datum = ['okt.1','okt.2','okt.3','okt.4','okt.5','okt.6']

i=0

elso = homerseklet [0]

while elso = 0:
    pri'''
#feladt szövege:
#Adott egy lista, mely október havi napi középhőmérséklet értékeket tartalmazza. homerseklet= [0,12,13,9,2,7].
#Az első érték október 1.  A program írja ki, melyik napon csökkent az előző naphoz képest  a hőmérséklet több, mint 3 fokot?

'''ez a megoldás kiírja az összes olyan napot, ahol 3-al csökket a hőmérséklet'''
homerseklet = [0,12,13,9,2,7]

i = 0

while i < len(homerseklet) - 1:
    if (homerseklet(i)-homerseklet[i+1] > 3):
    print (f"{i+2}. napra")
    #leágazás vége
    i += 1
#ciklus vége

'''ez a megoldás az első olyan napot írja ki, amikor 3-mal csökkent a hőmérséklet'''
i = 0
while (i<len(homerseklet) - 1) and (homerseklet[i] - homerseklet[i+1] <= 3):
    i += 1
    #ciklus vége
if (i < len(homerseklet) - 1):
    print(f"{i+2}. napra ")
else:
    print(f"Nincs ilyen nap.")