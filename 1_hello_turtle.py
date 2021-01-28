# Az importálás mások által (vagy akár a mi régi kódunk is lehet) készített programokra való hivatkozás
# Legalább ezeket nem nekünk kellett megírni:)
# A Turtle osztály a teknőc nyomóformája, a Screen pedig a képernyőé.
from turtle import Turtle
from turtle import Screen


# Létrehozzuk a képernyőt, ahol a teknőc szaladgálhat.
akvarium = Screen()
# Létrhozunk egy teknőcöt. Ez a sor ismételhető lenne többször, akkor több teknőcünk lenne, de a neveik nem egyezhetnek.
ametiszt = Turtle()
# A shape metódussal meg tudjuk változtatni a megjelenő képet.
ametiszt.shape("turtle")

# Ismételld 100-szor
for i in range(100):
    # Menj előre 20 pixelt
    ametiszt.forward(20)
    # fordulj balra 57 fokot
    ametiszt.left(57)
    # Menj előre 40 pixelt
    ametiszt.forward(40)
    # fordulj balra 57 fokot
    ametiszt.right(19)
    # Menj az ismétlés elejére, és néz meg, hogy kell-e még ismételni

# válts színt pirosra
ametiszt.color('red')
# rajzolj egy kört, aminek a sugara 100
ametiszt.circle(100)

# válts színt zöldre
ametiszt.color('green')
# Ismételd 180-szor (hogy kör legyen a végén, mert ugye 2 fokonként fordul és 180-szor ismétel, az 360 fok összesen)
for i in range(180):
    ametiszt.forward(2)
    ametiszt.left(2)

# Az ablak vezérlőelemeinek futtatása, hogy be tudjuk zárni majd:)
akvarium.mainloop()

# UI: legközelebb objektum lesz a teknőc viselkedése is:)