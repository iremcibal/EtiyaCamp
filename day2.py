girilecekNotSayisi = int(input("Kaç adet not gireceksiniz"))
gecilenDersSayisi = 0
notDizisi= []

for note in range(girilecekNotSayisi):
    vize = float(input("Vize Notunuz:"))
    final = float(input("Final Notunuz:"))
    girilenNot = (vize*0.4 + final*0.6)

    notDizisi.append(girilenNot) 
    if(girilenNot >= 50):
        gecilenDersSayisi +=1

print(f"{girilecekNotSayisi} dersten {gecilenDersSayisi} kadar dersi geçtiniz")

for note in notDizisi:
    print(note)


#program sonunda girdiği notları kaçıncı not olduğu bilgisi ile yazdıralım 
#kişi direkt ortalama not girmek yerine vize -final girecek biz o dersin ortalamına ı hesaplayıp 
#geçme geçmeme yazılcak

