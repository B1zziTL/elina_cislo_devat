#naimportovanie modulu tkinter
import tkinter

#nastavenie platna
canvas = tkinter.Canvas(width=500, height=100, background="black")
canvas.pack()

#otvorenie suboru
subor = open("zastavky.txt","r")

#zadefinovanie premennej a zoznamu
cislo = 0
zastavky = []

def nacitanie(): #funkcia na nacitanie info zo suboru
    for riadok in subor: #cyklus na prechadzanie riadkov v subore
        #vymazanie prazdnych znakov
        riadocek = riadok.strip()

        #vlozenie upraveneho riadku do zoznamu
        zastavky.append(riadocek)

#zadefinovanie povodnych suradnic textu
x = -150
y = 50       

def indexovanie(event): #funkcia na zmenu cisla zobrazovanej zastavky
    #zadefinovanie globalnych premennych
    global x,y,cislo

    cislo += 1

def vykreslenie(): #funkcia na vykreslenie zastavky
    #zadefinovanie globalnych premennych
    global x,y,cislo

    #vymazanie vsetkeho na platne
    canvas.delete("all")

    #podmienka na vypisanie konecnej zastavky
    if cislo == len(zastavky) - 1:
        canvas.create_text(x,y,text=zastavky[cislo]+" KONEČNÁ",font="Arial 30",fill="red")
    else:
        canvas.create_text(x,y,text=zastavky[cislo],font="Arial 30",fill="red")

    #podmienka na vykreslovanie od zaciatku
    if x < 654:
        x += 10
    else:
        x = -150

    #vykreslenie funkcie za cas 50 ms
    canvas.after(50,vykreslenie)

#zavolanie funkcii
nacitanie()
vykreslenie()

#nabindovanie vsetkych tlacidiel na funkciu indexovanie
canvas.bind_all("<Key>",indexovanie)

#zatvorenie suboru
subor.close()
