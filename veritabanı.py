import sqlite3
import datetime

con = sqlite3.connect(r"C:\Users\arifseyda\Desktop\rezervasyon_sistemi\db.sqlite3")
cursor = con.cursor()

def verileri_al():
    cursor.execute('Select id, username,password from auth_user')
    liste = cursor.fetchall()
    return liste

def verileri_al2():
    cursor.execute('Select reserved_start_date,user_id,username,lastname,reserved_start_time,reserved_end_time,status,status2 from rezervasyon_reservation')
    liste = cursor.fetchall()
    return liste

def verileri_al3():
    cursor.execute(
        'Select status3 from rezervasyon_reservation')
    liste = cursor.fetchall()
    return liste

def tupple_to_array(tupple,number):
    result = []

    for s in tupple:
        for x in s:
            result.append(x)
            array = [result[i * number:(i+1) * number] for i in range((len(result)+ number -1) // number)]
    return array

liste_auth_user = verileri_al()
liste_reservasyon = verileri_al2()
liste_esxi = verileri_al3()


array_auth_user = tupple_to_array(liste_auth_user,3)
array_resrvasyon = tupple_to_array(liste_reservasyon,8)
array_esxi = tupple_to_array(liste_esxi,1)

array_year = []
array_month = []
array_day = []
array_day_name = []
array_date_islemleri = []
for i in array_resrvasyon:
    year, month, day = i[0].split('-')
    array_year.append(year)
    array_month.append(month)
    array_day.append(day)
    day_name = datetime.date(int(year), int(month), int(day))
    day_name2 = day_name.strftime("%A")
    array_day_name.append(day_name2)

    date_islem = datetime.datetime(int(year), int(month), int(day))
    array_date_islemleri.append(date_islem)

gun = []

for j in array_day_name:
    if j == "Monday":
        gun.append("M")
    if j == "Tuesday":
        gun.append("T")
    if j == "Wednesday":
        gun.append("W")
    if j == "Thursday":
        gun.append("Th")
    if j == "Friday":
        gun.append("F")
    if j == "Saturday":
        gun.append("Sa")
    if j == "Sunday":
        gun.append("Su")

print(len(array_resrvasyon))
print(len(array_auth_user))

if len(array_resrvasyon) < len(array_auth_user):
    for j in range(0,len(array_auth_user)):
        if j >= len(array_resrvasyon):
            continue
        for k in array_auth_user:
            if k[0] == array_resrvasyon[j][1]:
                array_resrvasyon[j][1] = k[1]
                array_resrvasyon[j].append(k[2])
else:
    for k in range(0, len(array_resrvasyon)):
        for n in range(0, len(array_auth_user)):
            if array_auth_user[n][0] == array_resrvasyon[k][1]:
                array_resrvasyon[k][1] = array_auth_user[n][1]
                array_resrvasyon[k].append(array_auth_user[n][2])

#Şifrenin baştan bir kısmını kırpıyoruz.
for k in array_resrvasyon:
    k[8] = k[8].split("pbkdf2_sha256$")[1]


for j in array_resrvasyon:
    if j[6] == 0 and j[7] == 0:
        j[1] = j[1] + "_power"
    if j[6] == 1 and j[7] == 0:
        j[1] = j[1] + "_water"

# gun isminin ilk harfinin eklenimi
for m in range(0,len(array_resrvasyon)):
    array_resrvasyon[m].append(gun[m])

baslangic_zamani = ""
bitis_zamani = ""
for n in range(0,len(array_resrvasyon)):
    baslangic_zamani = array_resrvasyon[n][4]
    bitis_zamani = array_resrvasyon[n][5]

    hours,minutes,saniye = baslangic_zamani.split(":")
    start_time = hours + ":" + minutes
    array_resrvasyon[n][4] = start_time

    hours2, minutes2, saniye2 = bitis_zamani.split(":")
    end_time = hours2 + ":" + minutes2
    array_resrvasyon[n][5] = end_time

for q in range(0,len(array_resrvasyon)):
    array_resrvasyon[q].append(array_date_islemleri[q])

for x in range(0,len(array_resrvasyon)):
    array_resrvasyon[x].append(array_esxi[0])

# isim soyisim birleştirme
isim = ""
soyad = ""

for l in array_resrvasyon:
    isim = l[2]
    soyad = l[3]
    l[2] = isim + " " + soyad
    isim = ""
    soyad = ""

print(array_resrvasyon)
print(gun)

date = datetime.datetime.now().date()

yil,ay,gun = str(date).split("-")
tarih = datetime.datetime(int(yil), int(ay), int(gun))
print(tarih)
print(type(array_resrvasyon[0][0]))
con.close()
'''
user_array = []
for i in array_resrvasyon:
    if i[6] == 2:
        user_array.append(i[1])

print(user_array)
user_array = list(dict.fromkeys((user_array)))
print(user_array)
'''

