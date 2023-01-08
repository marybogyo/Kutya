from Kutya import Kutya

kutya1 = Kutya("Kíra", "szuka", "yorkshire terrier", 25, 4 )
kutya2 = Kutya("Mexi", "kan", "németh juhász", 60, 50)
kutya3 = Kutya("Bodza", "szuka", "mopsz", 30, 6)
kutya = [kutya1, kutya2, kutya3]

i = 0
while i < len(kutya):
    actkutya = kutya[i]
    actkutya.tevekenyseg()
    i += 1

'''i = 0
while i < len(kutya):
    kutya[i].tevekenyseg()
    if kutya[i].tev == 1:
        print(f"{kutya[i].nev} harap")
    i += 1
'''


