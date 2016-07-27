from stack import stack
import math
class calculator:
    def calculate(exp):
        value=''
        print("print expression")
        def prec(t,o):
            d={'(':10,'$':5,'i':5,'_':5,'!':5,'p':5,'s':5,'^':5,'t':5,'u':5,'v':5,'w':5,'x':5,'y':5,'z':5,'/':4,'*':4,'+':2,'-':2}
            if(d[t]>=d[o]):
                return True
            else:
                    return False
        try:
            var=exp
            f=var.find(" ")
            if(f!= -1):
                print("remove blank spaces ")
            s=stack()
            post=''
            for l in var:
                n=ord(l)
                if((n in range(48,58))or(l in ['.'])):
                    post=post+l;
                elif(l in ['+','-','*','/','(','_','!','i','p','$','s','t','u','v','^','w','x','y','z']):
                    post=post+' '
                    while( not s.isempty() and (not s.peek()=='(')and prec(s.peek(),l)):
                        post = post + s.peek()
                        post=post+' '
                        s.pop()
                    s.push(l)
                elif(l=='('):
                    s.push(l)
                elif(l==')'):
                    while(not s.isempty() and not s.peek()=='('):
                        post=post+' '
                        post=post+s.peek()
                        
                        s.pop()
                    s.pop()
            while(not s.isempty()):
                post=post+' '
                post=post+ s.pop()
            post=post+' '
            post=(post.split())
            print(post)
            
            l=stack()
            r=''
            for h in post:
                if(h not in ['+','-','/','*','p','_','!','i','$','s','t','u','v','^','w','x','y','z']):
                    l.push(h)
                if(h in ['+','-','/','*','$','s','!','_','p','i','t','u','v','^','w','x','y','z']):
                    if(h=='/'):
                        k=float(l.pop())
                        b=float(l.pop())
                        r=float(b/k)
                        l.push(r)
                    if(h=='*'):
                        k=float(l.pop())
                        b=float(l.pop())
                        r=float(k*b)
                        l.push(r)
                    if(h=='+'):
                        k=float(l.pop())
                        b=float(l.pop())
                        r=float(k+b)
                        l.push(r)
                    if(h=='-'):
                        k=float(l.pop())
                        b=float(l.pop())
                        r=float(b-k)    
                        l.push(r)
                    if(h=='s'):
                        k=float(l.pop())
                        r=float(math.sqrt(k))
                        l.push(r)
                    if(h=='t'):
                        k=float(l.pop())
                        r=float(math.sin(k))
                        l.push(r)
                    if(h=='u'):
                        k=float(l.pop())
                        r=float(math.cos(k))
                        l.push(r)
                    if(h=='v'):
                        k=float(l.pop())
                        r=float(math.tan(k))
                        l.push(r)
                    if(h=='^'):
                        k=float(l.pop())
                        b=float(l.pop())
                        r=float(math.pow(b,k))    
                        l.push(r)
                    if(h=='w'):
                        k=float(l.pop())
                        r=float(math.asin(k))
                        l.push(r)
                    if(h=='x'):
                        k=float(l.pop())
                        r=float(math.acos(k))
                        l.push(r)
                    if(h=='y'):
                        k=float(l.pop())
                        r=float(math.atan(k))
                        l.push(r)
                    if(h=='z'):
                        k=float(l.pop())
                        r=float(math.log(k))
                        l.push(r)
                    if(h=='$'):
                        k=float(l.pop())
                        r=float(math.log10(k))
                        l.push(r)
                    if(h=='p'):
                        k=float(l.pop())
                        r=float(math.factorial(k))
                        l.push(r)
                    if(h=='i'):
                        k=float(l.pop())
                        r=float(1/k)
                        l.push(r)
                    
                    if(h=='!'):
                        k=float(l.pop())
                        b=float(l.pop())
                        r=float(math.factorial(b)/math.factorial(b-k))
                        l.push(r)
                    if(h=='_'):
                        k=float(l.pop())
                        b=float(l.pop())
                        r=float(math.factorial(b)/(math.factorial(b-k)* math.factorial(k)))
                        l.push(r)
            l.printstk()
            value=l.pop()
            print(value)
            return str(value)
        

        except:print("SYNTAX ERROR")
        

             
                

