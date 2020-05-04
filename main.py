import eel
from sympy import *
#from sympy.plotting import plot

eel.init('UI')
'''
@eel.expose
def test(l,f,u):
    x=symbols('x')
    ans=''
    if u=='' and l=='':
        #indefinite
        
        integrated=integrate(f,x)
        p1=plot(f, (x,-20,20),show=False)
        p1.save('output_graph.jpg')
        ans=integrated
        
        

    elif u!='' and l!='':
        #definite
        if u.isdigit() and l.isdigit():
            #ok
            l=eval(l)
            u=eval(u)
            definite=integrate(f,(x,l,u))
            p1=plot(f, (x,l,u),show=False)
            p1.save('output_graph.jpg')
            
            ans=definite
            

        else:
            #error
            ans='Invalid Input'

            pass
    a=open('file.txt','w')
    a.write(str(ans))
    a.close()
'''
@eel.expose
def factorise(exp):
    try:
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z=symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
        exp=exp.strip(' ').lower()
        exp=eval(exp)
        factorise=str(factor(exp))
        return factorise
    except:
        return "Sorry something went wrong on your side. We will try to figure out soon."


eel.start('index.html',size=(1216,650))
