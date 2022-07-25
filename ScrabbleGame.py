points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4,
          4, 8, 4, 10]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("Kurallar: 'Her iki oyuncu da aynı uzunlukta kelimeler girmelidir,"
      "kelimeler latin harflerle yazılmalıdır!'")

puan_1 = 0
puan_2 = 0
text_1_original = input("Birinci oyuncu lütfen kelimenizi girin: ")
# birinci oyuncu kelimesini girer

text_2_original = input("İkinci oyuncu lütfen kelimenizi girin: ")
# ikinci oyuncu kelimesini girer

text_1 = text_1_original.lower()
text_2 = text_2_original.lower()
# büyük harf girilme ihtimaline karşı text_1 ve text_2'deki bütün harfleri
# lowercase'e çevirdik
kelimeler = [text_1, text_2]
puanlar = [puan_1, puan_2]

for j in range(len(kelimeler)):               # kelimeler döngüye sokulur
    for i in range(len(kelimeler[j])):        # kelimeler[i] döngüye sokulur
        for e in range(len(letters)):         # harfler döngüye sokulur
            if kelimeler[j][i] == letters[e]:  # kelimeler[i] ?= harfler
                puanlar[j] += points[e]
                break

sonuçlar = str(puanlar[0])+"-"+str(puanlar[1])

if puanlar[0] > puanlar[1]:                          # puanlar kıyaslanır
    print(sonuçlar, "--> Birinci oyuncu kazandı!")   # sonuçlar yazdırılır
elif puanlar[0] < puanlar[1]:
    print(sonuçlar, "--> İkinci oyuncu kazandı!")
else:
    print(sonuçlar, "--> Sonuç berabere!")
