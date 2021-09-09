import matplotlib.pyplot as plt
𥫖=range
𐫟=len
牜=True
㤑=False
𐢓=float
𬨍=input
import numpy as np
𨃪=np.linspace
ﻏ=np.sqrt
𪓀=np.tan
ﲩ=np.cos
𘡜=np.radians
def 𥐾(𐢍):
 ڻ=𘡜(𐢍)
 𞡁=ﲩ(ڻ)
 ٷ=𪓀(ڻ)
 return 𞡁,ٷ
def 恕(jrt,rjk,viosduh,xs):
 퍈=-0.5*jrt*((𣒤**2)/((rjk**2)*(viosduh**2)))+xs*𣒤
 return 퍈
def 𐰽(): 
 for i in 𥫖(𐫟(𫿶)):
  𠭸=ﻏ(((𫿶[i]-ګ[0])**2)+((𣣫[i]-𐳏[0])**2))
  𩸱=ﻏ(((𫿶[i]-ګ[1])**2)+((𣣫[i]-𐳏[1])**2))
  if 𠭸<ﱑ:
   ࡎ=牜
   break
  elif 𩸱<ﱑ:
   ࡎ=牜
   break
  else:
   ࡎ=㤑
 return ࡎ
def ࡗ():
 pass
𡮷=𐢓(𬨍("Quelle est la vitesse initiale de lancer en mètres par seconde ?"))
ﳷ=𐢓(𬨍("Quelle est la hauteur à laquelle le ballon est lancé ?"))
𐢍=𐢓(𬨍("Quel est l'angle de lancer en degrés ?"))
𞡁,ٷ=𥐾(𐢍)
ﱑ=0.24 
葬=6.75 
贐=0.45 
ګ=[6.15,6.6]
𐳏=[3.05-ﳷ,3.05-ﳷ]
𘟤=9.8 
𣒤=𨃪(0,10,60)
𣣫=恕(𘟤,𡮷,𞡁,ٷ)
𣣫=[item for item in 𣣫 if item>=0]
𫿶=𨃪(0,𣒤[𐫟(𣣫)],𐫟(𣣫))
if 𐰽()==牜:
 哬="Le ballon touche l'arceau"
else:
 哬="Le ballon ne touche pas l'arceau"
plt.plot(𫿶,𣣫,color='red',linewidth=4,linestyle=':',label='Trajectoire du ballon')
plt.plot(ګ,𐳏,marker="x",color="blue",linestyle=":",label='Limites du panier')
plt.ylim(0,4)
plt.xlim(0,10)
plt.title(哬)
plt.legend()
plt.show()