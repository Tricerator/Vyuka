import random

class Gladiator:

   def __init__(self,jmeno,  zbran, zbroj, cena,
                zivoty, sila = 3, obrana = 3,
                rychlost = 0.2, stesti = 0.2):
       self.zkusenost = 0
       self.zbran = zbran
       self.zbroj = zbroj
       self.zivoty = zivoty
       self.stesti = stesti
       self.sila = sila
       self.obrana = obrana
       self.jmeno = jmeno
       self.rychlost = rychlost
       self.cena = cena

   def __str__(self): return self.jmeno

   def predstav_se(self):
       return f"Ave Caesar! Morituri Te salutant, ego sum {self.jmeno}"
  

   def utoc(self, souper = None):
       weight = random.random()
       utok = (self.zbran + self.sila)*(1 + self.stesti)
       return int(utok*weight)

   def bran_se(self, souper  = None):
       obrana = (self.obrana + self.zbroj)* (1 + self.rychlost + self.stesti)
       weight = random.random()
       return int(obrana*weight)

   def ziskejSkill(self, XP):
       self.zkusenost += XP

   
       
   

    
       
       
       
       
