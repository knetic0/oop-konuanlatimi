from service import Service

clients =[
    {
        "plate_no":"80EF9060",
        "name_surname":"Mustafa Yıldız",
        "work_list":["yag","yikama"]
    },
    {
        "plate_no":"80VV1234",
        "name_surname":"Hasan Tonton",
        "work_list":["yikama","motor_temizligi"]
    },
    {
        "plate_no":"06PP9658",
        "name_surname":"Hatice Kurtulan",
        "work_list":["disk","balata"]
    },
    {
        "plate_no":"34GG7766",
        "name_surname":"Elif Korkmaz",
        "work_list":["onbin"]
    },
    {
        "plate_no":"46TT2154",
        "name_surname":"Şevket Altuğ",
        "work_list":["yirmibin"]
    },
    {
        "plate_no":"01AA001",
        "name_surname":"Adana Valisi",
        "work_list":["otuzbin"]
    },
    {
        "plate_no":"31HH9988",
        "name_surname":"Sadi Payaslı",
        "work_list":["otuzbin"]
    }
]

Service.set_service_name("Hasan Usta")
Service.set_workmanship_rate(0.25)

for client in clients:
    if client["work_list"][0] == "onbin":
        cl = Service.onbin(
            plate_no = client["plate_no"], 
            name_surname= client["name_surname"]
        )
    elif client["work_list"][0] == "yirmibin":
        cl = Service.yirmibin(
            plate_no = client["plate_no"], 
            name_surname= client["name_surname"]
        )
    elif client["work_list"][0] == "otuzbin":
        cl = Service.otuzbin(
            plate_no = client["plate_no"], 
            name_surname= client["name_surname"]
        )
    else:
        cl = Service(
            plate_no = client["plate_no"], 
            name_surname= client["name_surname"],
            work_list= client["work_list"]
        )
    cl.do_worklist()
    cl.print()


"""
Örnek Çıktı
--------------------
80EF9060-Mus*** Yıl***-2022-11-03
*yag,400tl,100.0tl
*yikama,50tl,12.5tl
İşçilik Oranı:0.25
Toplam:562.5tl
Servis:Hasan Usta
--------------------
--------------------
80VV1234-Has*** Ton***-2022-11-03
*yikama,50tl,12.5tl
*motor_temizligi,100tl,25.0tl
İşçilik Oranı:0.25
Toplam:187.5tl
Servis:Hasan Usta
--------------------
--------------------
06PP9658-Hat*** Kur***-2022-11-03
*disk,1600tl,400.0tl
*balata,750tl,187.5tl
İşçilik Oranı:0.25
Toplam:2937.5tl
Servis:Hasan Usta
--------------------
--------------------
34GG7766-Eli*** Kor***-2022-11-03
*yag,400tl,100.0tl
*yag_filtresi,75tl,18.75tl
*hava_filtresi,110tl,27.5tl
*polen_filtresi,60tl,15.0tl
*yikama,50tl,12.5tl
İşçilik Oranı:0.25
Toplam:868.75tl
Servis:Hasan Usta
--------------------
--------------------
46TT2154-Şev*** Alt***-2022-11-03
*motor_temizligi,100tl,25.0tl
*balata,750tl,187.5tl
*disk,1600tl,400.0tl
*yag,400tl,100.0tl
*yag_filtresi,75tl,18.75tl
*hava_filtresi,110tl,27.5tl
*polen_filtresi,60tl,15.0tl
*yikama,50tl,12.5tl
İşçilik Oranı:0.25
Toplam:3931.25tl
Servis:Hasan Usta
--------------------
--------------------
01AA001-Ada*** Val***-2022-11-03
*motor_temizligi,100tl,25.0tl
*balata,750tl,187.5tl
*disk,1600tl,400.0tl
*yag,400tl,100.0tl
*yag_filtresi,75tl,18.75tl
*hava_filtresi,110tl,27.5tl
*polen_filtresi,60tl,15.0tl
*yikama,50tl,12.5tl
İşçilik Oranı:0.25
Toplam:3931.25tl
Servis:Hasan Usta
--------------------
--------------------
31HH9988-Sad*** Pay***-2022-11-03
*motor_temizligi,100tl,25.0tl
*balata,750tl,187.5tl
*disk,1600tl,400.0tl
*yag,400tl,100.0tl
*yag_filtresi,75tl,18.75tl
*hava_filtresi,110tl,27.5tl
*polen_filtresi,60tl,15.0tl
*yikama,50tl,12.5tl
İşçilik Oranı:0.25
Toplam:3931.25tl
Servis:Hasan Usta
--------------------
"""