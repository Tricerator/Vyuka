from Hrac import *
from TypyGladiatoru import *

def main():
   privitej()
   den = 1
   while True:
      arena(den)
      input()
      den +=1
def privitej():
    print(f"Zdravím tě, dobrodruhu." +
            "Pokusíš se nyní proslavit své jméno v aréně")
    jmeno = input("Jak se jmenuješ?  ")
    typ = ""
    while typ.lower() != "plebejec" and typ.lower() != "patricij":
       typ = input(f"Byl tvůj otec plebejec (těžké) či patricij? (lehké)\n")
    
    if typ.lower() == "plebejec":  penize = 3000
    else: penize = 12000
    global hrac
    hrac = Hrac(jmeno, penize)
    
    print(f"Najdeš pod jménem {jmeno} balíček s {penize} sestercií")
    

def arena(den):
    nakup()
    boj(generovaniProtivniku(den), den)


def nakup():
   
  vstup = input(f"Mas {hrac.penize}, chces nakupovat? [a/n]")
  while vstup.lower() != "n":
   if hrac.penize < 900:
      print("Jiz nemas penize, tak smele do areny!")
      return
   vstup = input("chces koupit Lucistnika - L (1000),"
         "Sermire - S (900) ci Jezdce - J(7000)")
   if vstup.upper() == "L":
         if hrac.penize >= 1000:
                     hrac.penize -= 1000
                     hrac.poleGladiatoru.append(Luk())
         else: print("Malo penez")
   elif vstup.upper() == "S":
         if hrac.penize >= 900:
                     hrac.penize -= 900
                     hrac.poleGladiatoru.append(MecAStit())
         else: print("Malo penez")
   elif vstup.upper() == "J":
         if hrac.penize >= 7000:
                     hrac.penize -= 7000
                     hrac.poleGladiatoru.append(Jezdec())
         else: print("Malo penez")
   else: print("Spatny typ jednotky")                   
   vstup = input(f"Mas {hrac.penize}, chces nakupovat? [a/n]")
  return 
    

def generovaniProtivniku(den):
   suma = den * 1 * 3000
   pole = []
   while suma >= 900:
      rand = random.randint(1,7)
      if rand in [1] :
         if suma >= 1000:
            pole.append(Luk())
            suma -=1000
      elif 2 == rand:
         if suma >= 900:
            pole.append(MecAStit())
            suma -= 900
      elif 3 == rand:
         if suma >= 7000:
            pole.append(Jezdec())
            suma -= 7000
   return pole

def boj(poleNepratel, den):
   while len(poleNepratel) > 0 and len(hrac.poleGladiatoru) > 0:
      nepritel = random.choice(poleNepratel)
      pritel = random.choice(hrac.poleGladiatoru)
      while pritel.zivoty > 0 and nepritel.zivoty > 0:
         utokP = pritel.utoc()
         obranaN = nepritel.bran_se()
         if utokP > obranaN:
            print(f"Tvuj {pritel.jmeno} zasahl za {utokP - obranaN} ")
            nepritel.zivoty -= (utokP - obranaN)
            zobraz2 = int((nepritel.zivoty/nepritel.maxHP)*50)
            print(f"\tNepratelsky {nepritel.jmeno} ma \n["  + nepritel.zivoty*"|" + (nepritel.maxHP -nepritel.zivoty)*" " +  "]")    

         utokN = nepritel.utoc()
         obranaP = pritel.bran_se()
         if utokN > obranaP:           
            print(f"Nepratelsky {nepritel.jmeno} zasahl za {utokN - obranaP} ")
            pritel.zivoty -= (utokN - obranaP)
            zobraz = int((pritel.zivoty/pritel.maxHP)*50)
            print(f"\tMuj {pritel.jmeno} ma \n["  + zobraz*"|" + (50 - zobraz)*" " +  "]")
     
            
      if pritel.zivoty <= 0:
         hrac.poleGladiatoru.remove(pritel)
         print(f"Prisel jsi o {pritel.jmeno}")
      else:
         poleNepratel.remove(nepritel)
         print(f"Zabil jsi {nepritel.jmeno}")
      input()   
   if len(hrac.poleGladiatoru) > 0:
      print("Zvitezil jsi!")
      hrac.penize += den * 3000
   else:
      print("Jsi loooooooser!")
      if(hrac.penize < 900):
         print("Jdi domu na Itaku!")
         exit()
         
   


if __name__ == "__main__":
   main()
