from tkinter import*
from tkinter import messagebox
import math
import sys
#______________________________________________________________________________________________________________________________________________________________________
#Mano padaryta funkcija, kuri atskiria viską, kas yra prieš ir po kablelio. Nesvarbu ar tai bus raidės, ar po kablelio nieko nebus, ji visada suveiks.
def sveikoji(skaicus):
    F=[];F2=[];kableliai=0;sveikas="";nesveikas=""
    for x in skaicus:
        if x==".":
            kableliai+=1
        elif kableliai==0:
            F.append(x)
        elif kableliai>0:
            F2.append(x)
    for x in F:
        sveikas=sveikas+x
    for x in F2:
        nesveikas=nesveikas+x
    if sveikas=="":
        sveikas="0"
    if nesveikas=="":
        nesveikas="0"
    return sveikas,nesveikas

#______________________________________________________________________________________________________________________________________________________________________
#Pagrindinė funkcija, kurioje vyksta visi konvertavimai.
def konvertavimas(*args):
    global ats11
    ats11=""
#Gauname skaičius prieš ir po kablelio, tai pat skaičiavimo sistemą, į kurią norime konvertuoti.
    a,c=sveikoji(variable.get())
    b=int(variable2.get())
#Tikrinamos atitinkamos sistemos
#=======================================================================================================================================================================
#Tikrinama ar tai nėra 10.
    if int(variable3.get())==10:
#Jei tai yra 10, tai kreipiamės į funkcija kuri konvertuoja iš 10 į reikiamą.
        ats1=isdesimtaines(a,b)
        variable1.set(ats1)
#=======================================================================================================================================================================
#Tikrinama ar tai nėra 2.
    elif int(variable3.get())==2:
#Jei tai yra 2, tai kreipiamės į funkcija kuri konvertuoja iš 2 į reikiamą. Nurodome, kad tai ne trupmena su False.
        ats1=isdvejetaines(a,b,False)
        variable1.set(ats1)
#=======================================================================================================================================================================
#Tikrinama ar tai nėra 8.
    elif int(variable3.get())==8:
        if int(variable2.get())==2 or int(variable2.get())==16:
#Jeigu iš 8 konvertuojama į 2 arba 16 naudojama atitinkama funkcija, kuri yra paprastesnė.
            ats1=isastuntaines(a,b,False)
        else:
#Jeigu iš 8 konvertuojama į kitas sistemas, tai pirma susikonvertuojama į dešimtainę, tada iš dešimtainės į reikiamą sistemą. Naudojamasi funkcijomis.
            ats1=isdesimtaines(idesimtaine(a,8),b)  
        variable1.set(ats1)
#=======================================================================================================================================================================
#Tikrinama ar tai nėra 16.
    elif int(variable3.get())==16:
        if int(variable2.get())==2 or int(variable2.get())==8:
#Jeigu iš 16 konvertuojama į 8 arba 2 naudojama atitinkama funkcija, kuri yra paprastesnė.
            ats1=issesioliktines(a,b,False)
        else:
#Jeigu iš 16 konvertuojama į kitas sistemas, tai pirma susikonvertuojama į dešimtainę, tada iš dešimtainės į reikiamą sistemą. Naudojamasi funkcijomis.      
            ats1=isdesimtaines(idesimtaine(a,16),b)  
        variable1.set(ats1)
#=======================================================================================================================================================================
#Tikrinama ar nėra kitų sistemų.
    elif int(variable3.get())==3 or int(variable3.get())==4 or int(variable3.get())==5 or int(variable3.get())==6 or int(variable3.get())==7 or int(variable3.get())==9 or int(variable3.get())==10 or int(variable3.get())==11 or int(variable3.get())==12 or int(variable3.get())==13 or int(variable3.get())==14 or int(variable3.get())==15:
#Jeigu iš likusių konvertuojama į kitas sistemas, tai pirma susikonvertuojama į dešimtainę, tada iš dešimtainės į reikiamą sistemą. Naudojamasi funkcijomis.      
        ats1=isdesimtaines(idesimtaine(a,variable3.get()),b) 
        variable1.set(ats1)
#Jeigu niekas neįrašyta nustatome 0.
    if ats1=="":
        ats1="0"
#Pašaliname skalę, kuri bus dar pridedama jei yra bent koks skaičius po kablelio.
    oi.grid_remove()
    ik.grid_remove()

#=======================================================================================================================================================================
#Jeigu po kablelio yra skaičių...
    if c!="0" and variable.get()!=variable1.get():
#Pridedama "Kiek skaičių po kablelio nori" skalė.
        oi.grid(row=0,column=6,padx=10)
        ik.grid(row=0,column=5,padx=10)
#Tikrinamos trupmeninų skaičių sistemos.
#=======================================================================================================================================================================
#Jeigu iš 10 skaičiavimo sistemos trupmeninė dalis konvertuojama į kokią kitą, tai skaičius po kablelio paverčiame trupmenine dalimi ir tada kreipiames į funkcija kuri iš dešimtainės paverčia į reikiamą.
        if variable3.get()=="10":
            c=float(int(c)/10**len(c))
            ats11=isdesimtainetrupmena(c,b)
#Po funkcijos susidaro masyvas, kurį cikle sujungiame kaip vieną tekstinę eilutę.
#=======================================================================================================================================================================
#Jei konvertuojama iš 2 skaičiavimo sistemos.
        elif variable3.get()=="2":
#Jei konvertuojama į kitas skaičiavimo sistemas (be 8 ir 16), tai naudojama tipiška konvertavimo funkcija.
            if b!=8 and b!=16:
                POM=isdvejetaines(c,b,True)
                for x in POM:
                    ats11=ats11+str(x)
#Jei konvertuojama į 16 ar 8 skaičiavimo sistemą naudojami paprastesni konvertavimo metodai. Taipat pridedami 0, kur truksta skaičiu po kablelio.
            else:
                ats11=tikrinimas(isdvejetaines(c,b,True))

#=======================================================================================================================================================================
#Jei konvertuojama iš 8 skaičiavimo sistemos.
        elif variable3.get()=="8":
#Konvertuojant į 2 ar 16 skaičiavimo sistemą naudojami paprastesni konvertavimo metodai. Taipat pridedami 0, kur truksta skaičiu po kablelio.
            if int(variable2.get())==2 or int(variable2.get())==16:
                ats11=tikrinimas(isastuntaines(c,b,True))
#Konvertuojant į kitas skaičiavimo sistemas pirma pasiverčiama į dešimtinę, tada į reikiamą.
            else:
                ats11=isdesimtainetrupmena(idesimtainetrupmena(c,8),b)
#=======================================================================================================================================================================
#Jei konvertuojama iš 16 skaičiavimo sistemos.
        elif int(variable3.get())==16:
#Konvertuojant į 2 ar 8 skaičiavimo sistemą naudojami paprastesni konvertavimo metodai. Taipat pridedami 0, kur truksta skaičiu po kablelio.
            if int(variable2.get())==2 or int(variable2.get())==8:
                ats11=tikrinimas(issesioliktines(c,b,True))
            else:
#Konvertuojant į kitas skaičiavimo sistemas pirma pasiverčiama į dešimtinę, tada į reikiamą.
                ats11=isdesimtainetrupmena(idesimtainetrupmena(c,16),b)
#Jei reikia konvertuoti iš nepaminėtų skaičiavimo sistemų pirmą perkonvertuojama į dešimtainę, tada iš dešimtainės į reikiamą
        elif int(variable3.get())==3 or int(variable3.get())==4 or int(variable3.get())==5 or int(variable3.get())==6 or int(variable3.get())==7 or int(variable3.get())==9 or int(variable3.get())==10 or int(variable3.get())==11 or int(variable3.get())==12 or int(variable3.get())==13 or int(variable3.get())==14 or int(variable3.get())==15:
            ats11=isdesimtainetrupmena(idesimtainetrupmena(c,variable3.get()),b)
#=======================================================================================================================================================================
#Išvedame atsakymus
        variable1.set(str(ats1)+"."+str(ats11))
#Jei vienoje pusėje yra nulis, tai ir kitoje turi būti nulis
    if variable.get()=="0":
        variable1.set("0")
#______________________________________________________________________________________________________________________________________________________________________
#Funkcija, kurioje taisomos įvesties klaidos
def rasymas(*args):
#Visos gautos raidės paverčiamos į didžiasias/
    skaic=0
    opo=str(variable.get())
    opo=opo.upper()
    for x in opo:
        if x==".":
            skaic=skaic+1
    if skaic>1:
        opo=opo.replace(".","")
    variable.set(opo)
    rodiklis=int(variable3.get())
#Pagal funkciją gaunami skaičiai prieš ir po kablelio
    a,c=sveikoji(variable.get())
#Tikrinami skaičiai prieš ir po kablelio. Jeigu skaičiaus negalima paversti sveikuoju skaitmeniu tai tiktinama, ar simbolis yra žodyne. Jei jo žodyne nėra jis yra tiesiog pašalinamas
    for o in [str(a),str(c)]:
        for x in o:
            try:
                int(x)
            except:
                try:
                    list(skaiciaikaipraides.keys())[list(skaiciaikaipraides.values()).index(x)]
                except:
                    variable.set(opo.replace(x,""))
                    rasymas()
                x=list(skaiciaikaipraides.keys())[list(skaiciaikaipraides.values()).index(x)]
#Tikrinami ar įvesti skaičiai nėra didesni nei pradinė skaičiavimo sistema. Jeigu jie yra didesni, skaičiavimo sistema prisitaiko prie įvestų skaičių.
            if int(x)>=int(rodiklis):
                rodiklis=x
                variable3.set(str(int(rodiklis)+1))
#Ištaisius rašymo klaidas kreipiamasi į konvertavimo funkciją.
    konvertavimas()
faa=0
def keitimas1(*args):
    global variable,variable1,variable2,variable3,faa
    if faa>0:
        variable3,variable2=variable2,variable3
        variable,variable1=variable1,variable
    faa=0
    wg.config(textvariable=variable2)
    wgf.config(textvariable=variable3)
    e.config(textvariable=variable)
    e1.config(textvariable=variable1)
    rasymas()
def keitimas2(*args):
    global variable,variable1,variable2,variable3,faa
    if faa==0:
        variable2,variable3=variable3,variable2
        variable,variable1=variable1,variable
    wg.config(textvariable=variable3)
    wgf.config(textvariable=variable2)
    e.config(textvariable=variable1)
    e1.config(textvariable=variable)
    faa=faa+1
    rasymas()
#______________________________________________________________________________________________________________________________________________________________________
#Funkcija, į kurią kreipiamasi jei norima konvertuoti iš dešimtainės sistemos trupmenos.
def isdesimtainetrupmena(c,b):
            ats11=""
            POM=[]
#Ciklas eina tiek kartų kiek reikia skaitmenų po kablelio. Pradinis skaitmuo dauginamas iš reikiamos sistemos skaičiaus.
            for x in range (int(ik.get())):
                c=c*b
#Pradinis skaitmuo dauginamas iš reikiamos sistemos skaičiaus. Sveikoji dalis pridedama į masyvą, o trupemninė dlais dauginama toliau.
                if c>=10:
                    POM.append(skaiciaikaipraides.get(c//1))
                else:
                    POM.append(int(c//1))
                c=c%1
#Iš masyvo viskas sudedama į vieną tekstinę eilutę.
            for x in POM:
                ats11=ats11+str(x)
            return ats11
#______________________________________________________________________________________________________________________________________________________________________
#Funkcija, į kurią kreipiamasi jei norima konvertuoti į dešimtainės sistemos trupmeną.
def idesimtainetrupmena(c,b):
    skaic=1;suma=0
#Ciklas eina tiek kiek eilutėje yra simbolių/skaičių.
    for x in str(c):
#Jei neišeina paversti į sveikajį skaičių ieškoma masyve.
        try:
            int(x)
        except:
            x=list(skaiciaikaipraides.keys())[list(skaiciaikaipraides.values()).index(x)]
#Skaičius dauginamas iš reikiamos sistemos pakeltos minusiniu laipsniu ir sudedamas į sumą.
        suma+=int(x)*int(b)**-skaic
#Laipsniaus pakitimas
        skaic+=1
    return suma
#______________________________________________________________________________________________________________________________________________________________________
#Konvertavimas į dešimtainę skaičiavimo sistemą.
def idesimtaine(a,b):
    ats=0;laipsn=0
#Ciklas eina tiek kiek eilutėje yra simbolių/skaičių.
    for x in reversed(str(a)):
#Jei neišeina paversti į sveikajį skaičių ieškoma masyve.
            try:
              int(x)
            except:
                x=list(skaiciaikaipraides.keys())[list(skaiciaikaipraides.values()).index(x)]
#Skaičius dauginamas iš reikiamos sistemos pakeltos laipsniu ir sudedamas į sumą.
            ats=ats+int(x)*(int(b)**laipsn)
            laipsn=laipsn+1
    return ats
#______________________________________________________________________________________________________________________________________________________________________
#Konvertavimas iš dešimtainės skaičiavimo sistemos.
def isdesimtaines(a,b):
        ats=""
        A=[]
#Ciklas eis tol kol pradinis skaičius bus daugiau už 0.
        while int(a)>0:
#Dalinant iš norimos skaičiavimo sistemos liekana sudedama į masyvą.
                f=int(a)%b
                if f>9:
                    f=skaiciaikaipraides.get(f)
                A.append(f)
#O likusi dalis dalinama toliau.
                a=int(a)//b
#Gautas masyvas sudedamas į tekstinę eilutę/
        for x in reversed(A):
                ats=ats+str(x)
        return ats
#______________________________________________________________________________________________________________________________________________________________________
#Konvertavimas iš dvejetainės skaičiavimo sistemos.
def isdvejetaines(a,b,c):
    d=0;F=[];F1=[];ats=""
#Jeigu nekonvertuojama į 16 arba 8 skaičiavimo sistemą tai pirma persikonvertuojama į dešimtainę, o iš dišimtainės į norimą.
    if b!=8 and b!=16:
#Tikrinama ar ne trupmena.
        if c==True:
            d=isdesimtainetrupmena(idesimtainetrupmena(a,variable3.get()),int(variable2.get()))
        else:
            d=isdesimtaines(idesimtaine(a,2),int(variable2.get()))
#Jei yra 16 arba 8 skaičiavimo sistema.
    else:
#Visa eilutė sudedama į masyvą po vieną simbolį.
        for x in str(a):
            F.append(x)
#Jei skaičiavimos sistema yra aštuntainė viską skirstisime į triadas. Visa šios funkcijos dalis eina būtent šitaip:
        if b==8:
#Patikrinama, kiek skaičių trūksta iki dalaus iš 3 skaičiaus. Jei trūksta pridedama.
            if (len(F)%3)!=0:
                for u in range (3-len(F)%3):
                    if c==True:
                        F.append(0)
                    else:
                        F.insert(0,0)
            mo=0
#Suskirstoma į triadas ir sudedama į masyvą.
            for ma in range(len(F)//3):
                F1.append(str(F[ma*2+mo])+str(F[ma*2+1+mo])+str(F[ma*2+2+mo]))
                mo+=1
#Gautos triados sutikrinamos žodyne ir sudedamos į galutinį atsakymą.
            for ma in F1:
                ats=ats+str(dvejataineiastuntaine.get(ma))
                d=int(ats)
#Jei skaičiavimos sistema yra šešioliktainė viską skirstisime į teatradas. Visa šios funkcijos dalis eina būtent šitaip:
        elif b==16:
#Patikrinama, kiek skaičių trūksta iki dalaus iš 4 skaičiaus. Jei trūksta pridedama.
            if (len(F)%4)!=0:
                for u in range (4-len(F)%4):
                    if c==True:
                        F.append(0)
                    else:
                        F.insert(0,0)
#Suskirstoma į teatradas ir sudedama į masyvą.
            mo=0
            for ma in range(len(F)//4):
                F1.append(str(F[ma*2+mo])+str(F[ma*2+1+mo])+str(F[ma*2+2+mo])+str(F[ma*2+3+mo]))
                mo+=2
#Gautos teatrados sutikrinamos žodyne ir sudedamos į galutinį atsakymą.
            for ma in F1:
                ats=ats+str(dvejataineisesioliktaine.get(ma))
            d=ats
    return d
#______________________________________________________________________________________________________________________________________________________________________
#Konvertavimas iš aštuntainės skaičiavimo sistemos.
def isastuntaines(a,b,c):
#Jei yra į 16 arba 2 skaičiavimo sistemą naudojami paprasti metodai su triadomis ir teatradomis.
    if int(variable2.get())==16 or int(variable2.get())==2:  
        lol=""
#Sukonvertuojama į dvejetainę skaičiavimo sistemą su triadomis.
        for po in str(a):
            lol=lol+str(list(dvejataineiastuntaine.keys())[list(dvejataineiastuntaine.values()).index(int(po))])
        a=lol
#Jei reikia konvertuoti į šešioliktainę tai einam tiesiai į dvejetainę skaičiavimo sistemą ir iš ten konvertuojame į šešioliktainę.
        if int(variable2.get())==16 and c==True:
            a=isdvejetaines(lol,16,True)
        elif int(variable2.get())==16 and c==False:
            a=isdvejetaines(lol,16,False)
    return a
#______________________________________________________________________________________________________________________________________________________________________
#Konvertavimas iš šešioliktainės skaičiavimo sistemos.
def issesioliktines(a,b,c):
#Jei yra į 8 arba 2 skaičiavimo sistemą naudojami paprasti metodai su triadomis ir teatradomis.
    if int(variable2.get())==8 or int(variable2.get())==2:
        lol=""
#Sukonvertuojama į dvejetainę skaičiavimo sistemą su teatradomis.
        for po in str(a):
            lol=lol+str(list(dvejataineisesioliktaine.keys())[list(dvejataineisesioliktaine.values()).index(po)])
        a=lol
#Jei reikia konvertuoti į aštuntainę tai einam tiesiai į dvejetainę skaičiavimo sistemą ir iš ten konvertuojame į aštuntainę.
        if int(variable2.get())==8 and c==True:
            a=isdvejetaines(lol,8,True)
        elif int(variable2.get())==8 and c==False:
            a=isdvejetaines(lol,8,False)
        return a
#______________________________________________________________________________________________________________________________________________________________________
#Tikrinama, kiek skaičių yra po kablelio. Jei trūksta pridedama "0". Jei perdaug nuemami nuo galo skaitmenys.
def tikrinimas(ats11):
    if len(str(ats11))>int(ik.get()):
        ats11=str(ats11)[:-(len(str(ats11))-int(ik.get()))]
    elif len(str(ats11))<int(ik.get()):
        ats11=str(ats11)+"0"*(int(ik.get())-len(str(ats11)))
    return ats11   
#______________________________________________________________________________________________________________________________________________________________________
#Išėjimo iš programos funkcija.
def isejimas():
    ats=messagebox.askyesno("Išėjimas","Ar norite išeiti iš šios programos?")
    if ats==True:
        pg.destroy()
    else:
        None
#______________________________________________________________________________________________________________________________________________________________________
#Visi žodynai reikalingi šiai programai veikti optimaliausiu būdu.
skaiciaikaipraides={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
dvejataineiastuntaine={"000":0,"001":1,"010":2,"011":3,"100":4,"101":5,"110":6,"111":7}
dvejataineisesioliktaine={"0000":"0","0001":"1","0010":"2","0011":"3","0100":"4","0101":"5","0110":"6","0111":"7","1000":"8","1001":"9","1010":"A","1011":"B","1100":"C","1101":"D","1110":"E","1111":"F"}
#______________________________________________________________________________________________________________________________________________________________________
#Nustatomi lango parametrai. Padaroma, kad programa prisitaikytu prie esamos rezoliucijos.
pg=Tk();ilgis=pg.winfo_screenwidth();plotis=pg.winfo_screenheight();pg.geometry("%dx%d" % (ilgis,plotis));pg.config(background="#F6F6F6");pg.resizable(False,False);pg.attributes("-fullscreen", True)
if ilgis<=1200 or plotis <=700:
    k=0.55
elif ilgis>1200 and ilgis<1600 or plotis >700 and plotis <=900:
    k=0.6
elif ilgis>=1600 and plotis >900:#Panašiai su šia rezoliucija buvo daryta programa
    k=1
#______________________________________________________________________________________________________________________________________________________________________
#Antraštė.
Label(pg,text="Skaičiavimo sistemų konvertavimas",bg="#F6F6F6",font=("Times","36", "bold underline")).pack(pady=plotis/6)
#______________________________________________________________________________________________________________________________________________________________________
#Reikalingi kintamieji objektams.
variable=StringVar()#Pirmasis skaicius
variable1=StringVar()#Antrasis skaicius
variable2=StringVar()#Antroji sistema
variable3=StringVar()#Pirmoji sistema
#______________________________________________________________________________________________________________________________________________________________________
#Rėmelis
a=Frame(pg,bd=5,relief=RIDGE,bg="#F6F6F6");a.pack()
#______________________________________________________________________________________________________________________________________________________________________
#Sukuriami Spinbox'ai, kurie atstovauja skaičiavimo sistemas.
options=["2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
wg = OptionMenu(a,variable2,*options,command=keitimas1)
wg.config(justify=CENTER,width=6,font="10",bg="#F6F6F6")
wg.grid(row=0,column=4,padx=15)#Antroji sistema
wgf = OptionMenu(a,variable3,*options,command=keitimas1)
wgf.config(justify=CENTER,width=6,font="10",bg="#F6F6F6")
wgf.grid(row=0,column=1)#Pirmoji sistema
variable3.set("2")
variable2.set("2")
#______________________________________________________________________________________________________________________________________________________________________
#Įkeliama rodyklės nuotrauka.
photo=PhotoImage(file="output_Lvv92P.gif")
photo=photo.subsample(3)
nuotrauka=Label(a,image=photo,bd=0, highlightthickness=0)
nuotrauka.grid(row=0,column=2,padx=15,pady=15)
#______________________________________________________________________________________________________________________________________________________________________
#Sukuriamas išėjimo mygtukas.
d=Button(pg,text="X",font=("Arial","17","bold"),bg="red",command=isejimas)
d.place(x=ilgis-36,y=0)
#______________________________________________________________________________________________________________________________________________________________________
#Sukuriami laukai, į kuriuos būtų galima rašyti skaitmenis ir atvaizduoti gautus konvertavimo atsakymus
e=Entry(a,justify=CENTER,width=int(45*k),font="10",bg="#F6F6F6",textvariable=variable)
e.grid(row=0,column=0,padx=15)#Pirmasis skaicius
e1=Entry(a,justify=CENTER,width=int(45*k),font="10",bg="#F6F6F6",textvariable=variable1)
e1.grid(row=0,column=3)#Antrasis skaicius
#Nustatoma, kad kai įrašai skaičių (būtent atleidi klavišą) programa kreipiasi į funkciją.
e.bind("<KeyRelease>", keitimas1)
e1.bind("<KeyRelease>", keitimas2)

#______________________________________________________________________________________________________________________________________________________________________

#Sukuriama skalė po kablelio, bei ją paaiškinantis užrašas.
ik=Scale(a,from_=1,to=30,bg="#F6F6F6",command=konvertavimas);
oi=Label(a,bd=5,font=("Times","15"),text=" ←      Skaičiai\n ← po kablelio",bg="white")
#______________________________________________________________________________________________________________________________________________________________________
#Pradiniai skaičiai - 0
variable1.set("0")
variable.set("0")
#______________________________________________________________________________________________________________________________________________________________________
#Padaroma, kad nesimatytų klaidų. (Kartais išmeta, bet programai neigiamų efektų nepadaro)
class DevNull:
    def write(self, msg):
        pass
sys.stderr = DevNull()
mainloop()
#______________________________________________________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________________________________________________

