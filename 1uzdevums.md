Artjoms Balaboskins, Arturs Sidorovs, Maksims Solovjovs, Anastasija Karpova 10a
# 1. Nē, jo specifikācijā trūkst daudz nepieciešamo detaļu.
# 2. Lai varētu to atrisināt, būtu jānoskaidro daudz dažādas detaļas, piemēram: kādas receptes vecvecāki lietos - kādā proporcijā tiek lietoti augļi un cukurs, kāds ir galarezultāts, kādas mērvienības ir minētas receptē, kā tas pārvērst SI mērvienībās, piemēram, ja minēti 6 vidēja izmēra āboli uz 100g cukura, kā to pārvērst gramos, ko tieši ome grib zināt, piemēram, kuru recepti ņemt, cik izmaksās cukurs noteiktam augļu daudzumam, cik ievārījuma iznāks izmantojot noteiktu daudzumu cukura
3.1. def ievarijums(aboli_svars, cukurs_uz_kg):
    izmaksa_kg = 0.75 * cukurs_uz_kg
    izmaksas = izmaksa_kg * aboli_svars
    print(izmaksas)
3.2. def izmaksas_receptei(recepte, cena):
    summa = 0
    for sastavdala, daudzums in recepte:
        summa += daudzums * cena[sastavdala]
    return summa

def izmaksas_kopa(abolu_svars):
    recepte1 = {“cukurs”: 0.6, “kanelis”: 0.08, “aboli”: 2.0, “udens”: 0.2}
    cenas = {“cukurs”: 0.75, “kanelis”: 30.0, “aboli”: 0.0, “udens”: 0.0}
    izmaksas_kg = izmaksas_receptei(recepte1, cenas) / recepte[“aboli”]
    ievarijuma_izmaksas = svars * izmaksas_kg

    print(“Uz {} kg ābolu izmaksas būs {}”.format(abolu_svars, ievarijuma_izmaksas))
