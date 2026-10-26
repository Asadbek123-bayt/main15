parol = "  "
urinish = 0

while urinish < 5:
    kiritilgan = input("Parolni kiriting: ")

    if kiritilgan == parol:
        print("Xush kelibsiz!")
        break
    else:
        urinish = urinish + 1
        qolgan = 5 - urinish

        if qolgan > 0:
            print("Parol xato!")
            print("Qolgan urinishlar:", qolgan)
        else:
            print("Hisob bloklandi!")

print("Dastur tugadi.")

son = int(input("Musbat son kiriting: "))

if son > 0:
    vaqtincha = son
    yigindi = 0
    raqamlar = 0

    while vaqtincha > 0:
        raqam = vaqtincha % 10
        yigindi = yigindi + raqam
        raqamlar = raqamlar + 1
        vaqtincha = vaqtincha // 10

    print("Raqamlar yig'indisi:", yigindi)
    print("Raqamlar soni:", raqamlar)

    if son % 2 == 0:
        print("Son juft.")
    else:
        print("Son toq.")

    if yigindi > 20:
        print("Raqamlar yig'indisi 20 dan katta.")
    elif yigindi == 20:
        print("Raqamlar yig'indisi 20 ga teng.")
    else:
        print("Raqamlar yig'indisi 20 dan kichik.")
else:
    print("Xato! Musbat son kiriting.")

jami = 0
soni = 0
a = 0
b = 0
c = 0

while True:
    baho = int(input("Baho kiriting (1-5), tugatish uchun 0: "))

    if baho == 0:
        break
    elif baho >= 1 and baho <= 5:
        jami = jami + baho
        soni = soni + 1

        if baho == 5:
            a = a + 1
        elif baho == 4:
            b = b + 1
        else:
            c = c + 1

        print("Baho qabul qilindi.")
    else:
        print("Noto'g'ri baho! Qayta kiriting.")

if soni > 0:
    ortacha = jami / soni

    print("Baholar soni:", soni)
    print("O'rtacha baho:", ortacha)
    print("5 baholar:", a)
    print("4 baholar:", b)
    print("1-3 baholar:", c)

    if ortacha >= 4.5:
        print("Natija: A'lo!")
    elif ortacha >= 3.5:
        print("Natija: Yaxshi!")
    elif ortacha >= 3:
        print("Natija: Qoniqarli!")
    else:
        print("Natija: Qo'shimcha tayyorgarlik kerak.")
else:
    print("Hech qanday baho kiritilmadi.")

balans = 500000

while True:
    print("\n===== BANKOMAT =====")
    print("1. Balansni ko'rish")
    print("2. Pul yechish")
    print("3. Pul qo'shish")
    print("4. Chiqish")

    tanlov = input("Tanlovingizni kiriting: ")

    if tanlov == "1":
        print("Joriy balans:", balans, "so'm")

    elif tanlov == "2":
        pul = int(input("Yechiladigan pul: "))

        if pul <= 0:
            print("Summa musbat bo'lishi kerak!")
        elif pul > balans:
            print("Mablag' yetarli emas!")
        else:
            balans = balans - pul
            print("Pul yechildi.")
            print("Qolgan balans:", balans)

    elif tanlov == "3":
        pul = int(input("Qo'shiladigan pul: "))

        if pul <= 0:
            print("Noto'g'ri summa!")
        else:
            balans = balans + pul
            print("Pul qo'shildi.")
            print("Yangi balans:", balans)

    elif tanlov == "4":
        print("Bankomatdan foydalanganingiz uchun rahmat!")
        break

    else:
        print("Noto'g'ri tanlov! 1 dan 4 gacha tanlang.")

sirli_son = 37
urinishlar = 0
topildi = False

print("Son topish o'yiniga xush kelibsiz!")
print("Men 1 dan 100 gacha son o'yladim.")
print("Sizda 7 ta urinish bor.")

while urinishlar < 7:
    taxmin = int(input("Taxminingizni kiriting: "))

    if taxmin < 1 or taxmin > 100:
        print("Faqat 1 dan 100 gacha son kiriting!")
        continue

    urinishlar = urinishlar + 1

    if taxmin == sirli_son:
        print("Tabriklayman! To'g'ri topdingiz!")
        topildi = True
        break
    elif taxmin < sirli_son:
        print("Men o'ylagan son kattaroq.")
    else:
        print("Men o'ylagan son kichikroq.")

    qolgan = 7 - urinishlar

    if qolgan > 0:
        print("Qolgan urinishlar:", qolgan)
    else:
        print("Urinishlar tugadi!")

if topildi:
    print("Urinishlar soni:", urinishlar)
else:
    print("Siz yutqazdingiz.")
    print("Sirli son:", sirli_son)