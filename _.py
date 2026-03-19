__v = 0
_a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
__ = [_a[18]+_a[15],_a[17]+_a[9],_a[12]+_a[6],_a[17]+_a[18],_a[15]+_a[17],_a[18]+_a[2],_a[1]+_a[0],_a[15]+_a[4],_a[2]+_a[4],_a[6]+_a[14]]
_l = lambda x,y: x if x>y else y
_c = [_a[5]+_a[19], _a[5]+'5']

def _(a1,a2,a3,a4=[],**kw):
    global __v
    try:
     z1=None;z2=0;zzz=False;Z=0;zz=0;ZZ=0
     if not a1==None:
      if not not a1>0:
       if a3 in __:
        if a3==__[0]: z2=15
        else:
         if a3==__[1] or a3==__[2]: z2=20
         else:
          if a3 in __[3:6]: z2=25
          else:
           if not a3 in __[0:6]: z2=40
        if a1>50:
         if a1>50 and not a1>100: z2=z2-5
         if a1>100: z2=z2-5;z2=z2-5
         if a1>200: z2=z2-5
        if a2==_a[4]+_a[23]+_a[15]:
         z2=z2*2;print(_a[14]+_a[10]+'1')
        elif a2==_a[13]+_a[17]+_a[12]: z2=z2+0
        else:
         if not a2==None: z2=z2+10;print(_a[14]+_a[10]+'2')
        if len(a4)>0:
         c=a4[0]
         if c==_c[0]: __v=10;z2=z2-10;print(_a[14]+_a[10]+'3')
         else:
          if c==_c[1] and a1>150: __v=50;z2=z2-50
          else: print(_a[14]+_a[10]+'4')
        if z2<0: z2=_l(0,0)
        print(_a[17]+':',z2);return z2
       else: print(_a[4]+'1');return -1
      else: print(_a[4]+'2');return None
     else: return None
    except: print(_a[4]+'3');return 0

print(_(120,_a[4]+_a[23]+_a[15],__[6],a4=[_c[0]]))
print(_(80,_a[13]+_a[17]+_a[12],__[0]))
print(_(None,_a[13]+_a[17]+_a[12],__[0]))
print(_(50,_a[12]+_a[19]+_a[1],__[8],a4=[_c[1]]))
