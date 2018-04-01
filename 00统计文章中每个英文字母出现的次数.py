#!/usr/bin/env python3
#encoding:utf-8

article = 'I was not delivered unto this world in defeat, nor does failure course in my veins. I am not a sheep waiting to be prodded by my shepherd. I am a lion and I refuse to talk, to walk, to sleep with the sheep. I will hear not those who weep and complain, for their disease is contagious. Let them join the sheep. The slaughterhouse of failure is not my destiny.'

new={}

for i in article:
   # if (i > 'a' and i < 'z') or (i > 'A' and i < 'Z'):
    if i.isalpha():
        if i not in new:
            new[i]=1
        else:
            new[i]+=1

print(new)
