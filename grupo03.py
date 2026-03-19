def _0xF4A2(O00,l11,I11,o00O,_l1l,ll11,lI11,l0l0):
 _00=0
 if O00!=None:
  if len(O00)==11:
   _I1=0;_ll1=0
   while _I1<9:_ll1+=int(O00[_I1])*(10-_I1);_I1+=1
   _0l1=(_ll1*10)%11
   if _0l1==10:_0l1=0
   if _0l1==int(O00[9]):
    _I1=0;_ll1=0
    while _I1<10:_ll1+=int(O00[_I1])*(11-_I1);_I1+=1
    _0l1=(_ll1*10)%11
    if _0l1==10:_0l1=0
    if _0l1==int(O00[10]):_00=1
    else:_00=2
   else:_00=3
  else:_00=4
 else:_00=5
 _0x1=lambda:["Positivo","Revisar","Negativo","Baixo","Menor","Erro desconhecido","Item inválido 2","Item inválido 1","Tamanho inválido","Item nulo","Erro"]
 return _0x1()[0]if _00==1and l11>18and I11>500and o00O and _l1l<1000else(_0x1()[1]if _00==1and l11>18and I11>500and o00O and _l1l>=1000else(_0x1()[2]if _00==1and l11>18and I11>500and not o00O else(_0x1()[3]if _00==1and l11>18and I11<=500else(_0x1()[4]if _00==1and l11<=18else(_0x1()[5]if _00==0else(_0x1()[6]if _00==2else(_0x1()[7]if _00==3else(_0x1()[8]if _00==4else(_0x1()[9]if _00==5else _0x1()[10])))))))))
print(_0xF4A2("12345678909",19,600,True,500,None,None,None))
