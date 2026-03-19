import math
import random

def x(a,b,c,d=None,e=None,f=None):
    z=0
    print("...")
    if a>0:
        print("a="+str(a))
        if b=='sim':
            print("b ok")
            if c>=100:
                print("c>=100")
                if c<200:
                    z=c*0.05
                    print("z1="+str(z))
                else:
                    if c>=200:
                        print("c>=200")
                        if c<500:
                            z=c*0.10
                            print("z2="+str(z))
                        else:
                            print("c>=500?")
                            if c>=500:
                                if c<1000:
                                    z=c*0.15
                                    print("z3="+str(z))
                                else:
                                    print("c>=1000!")
                                    if c>=1000:
                                        z=c*0.20
                                        print("z4="+str(z))
            temp=c-z
            print("temp: "+str(temp))
            if d:
                print("d: "+str(d))
                if d=='ouro':
                    temp2=temp*0.95
                    print("temp2: "+str(temp2))
                    temp=temp2
                elif d=='prata':
                    temp3=temp*0.97
                    print("temp3: "+str(temp3))
                    temp=temp3
                elif d=='bronze':
                    temp4=temp*0.98
                    print("temp4: "+str(temp4))
                    temp=temp4
            print("temp d: "+str(temp))
            if e:
                print("e: "+str(e))
                if e>0:
                    temp5=temp-(e*10)
                    print("temp5: "+str(temp5))
                    if temp5<0:
                        print("temp5 < 0")
                        temp5=0
                    temp=temp5
                    print("temp e: "+str(temp))
            if f:
                print("f: "+str(f))
                if f==True:
                    temp6=temp*0.98
                    print("temp6: "+str(temp6))
                    temp=temp6
            print("temp x: "+str(temp))
            resultado=c-temp
            valor_final=temp
            print("R$"+str(c))
            print("R$"+str(round(resultado,2)))
            print("R$"+str(round(valor_final,2)))
            return valor_final
        else:
            print("nao")
            return c
    else:
        print("erro")
        return -1

print("="*50)
resultado1=x(1,'sim',750,'ouro',2,True)
print("\n")

print("="*50)
resultado2=x(1,'sim',1500,'prata',0,False)
print("\n")

print("="*50)
resultado3=x(1,'sim',150,None,None,None)
