from PyQt4 import QtGui
from calculation import calculator as calcc
#calcc.calculate('25+25')
import sys
app = QtGui.QApplication(sys.argv)
l=''
p=''
w=QtGui.QMainWindow()
w.setWindowIcon(QtGui.QIcon('n.png'))
w.setGeometry(50,50,245,300)
w.setFixedSize(245,300)
w.setWindowTitle('calculator')

tbox=QtGui.QTextEdit(w)
tbox.setGeometry(5,5,235,50)
tbox.setReadOnly(True)
tbox.setText("0")
def b1():
    global tbox,l,p
    l=l+'1'
    p=p+'1'
    print("1")
    tbox.setText(l)
def b2():
    global tbox,l,p
    l=l+'2'
    p=p+'2'
    print("2")
    tbox.setText(l)
def b3():
    global tbox,l,p
    l=l+'3'
    p=p+'3'
    print("3")
    tbox.setText(l)
def b4():
    global tbox,l,p
    l=l+'4'
    p=p+'4'
    print("4")
    tbox.setText(l)
def b5():
    global tbox,l,p
    l=l+'5'
    p=p+'5'
    print("5")
    tbox.setText(l)
def b6():
    global tbox,l,p
    l=l+'6'
    p=p+'6'
    print("6")
    tbox.setText(l)
def b7():
    global tbox,l,p
    l=l+'7'
    p=p+'7'
    print("7")
    tbox.setText(l)
def b8():
    global tbox,l,p
    l=l+'8'
    p=p+'8'
    print("8")
    tbox.setText(l)
def b9():
    global tbox,l,p
    l=l+'9'
    p=p+'9'
    print("9")
    tbox.setText(l)
def b0():
    global tbox,l,p
    l=l+'0'
    p=p+'0'
    print("0")
    tbox.setText(l)
def bdeci():
    global tbox,l,p
    l=l+'.'
    p=p+'.'
    print(".")
    tbox.setText(l)

def bmul():
    global tbox,l,p
    l=l+'*'
    p=p+'*'
    print("*")
    tbox.setText(l)
def bdiv():
    global tbox,l,p
    l=l+'/'
    p=p+'/'
    print("/")
    tbox.setText(l)
def bs():
    global tbox,l,p
    l=l+'-'
    p=p+'-'
    print("-")
    tbox.setText(l)
def badd():
    global tbox,l,p
    l=l+'+'
    p=p+'+'
    print("+")
    tbox.setText(l)
def beq():
    global tbox,l,p
    
    print("=")
    p=calcc.calculate(p)
    l=p
    tbox.setText(l)
    l=(l)
    print(l)
def bAC():
    global tbox,l,p
    l=''
    p=''
    print("")
    tbox.setText(l)
def bdel():
    global tbox,l,p
    if(l[len(l)-1]=='('):
        l=l[0:len(l)-1]
        p=p[0:len(p)-1]
        if(len(l)>1):
            if(l[len(l)-1].isalpha()):
                
                print(l)
                while(l[len(l)-1].isalpha()):
                    l=l[0:len(l)-1]
                    print(l)
                p=p[0:len(p)-1]
        print(p,l)
    else:
        l=l[0:len(l)-1]
        p=p[0:len(p)-1]
        print(p,l)
    print("del")
    tbox.setText(l)
def obrac():
    global tbox,l,p
    l=l+'('
    p=p+'('
    print("(")
    tbox.setText(l)
def cbrac():
    global tbox,l,p
    l=l+')'
    p=p+')'
    print(")")
    tbox.setText(l)
def poww():
    global tbox,l,p
    l=l+'^'
    p=p+'^'
    print("^")
    tbox.setText(l)
def sqrtt():
    global tbox,l,p
    l=l+'sqrt('
    p=p+'s('
    print("sqrt")
    tbox.setText(l)
def sinn():
    global tbox,l,p
    l=l+'sin('
    p=p+'t('
    print("sin")
    tbox.setText(l)
def coss():
    global tbox,l,p
    l=l+'cos('
    p=p+'u('
    print("cos")
    tbox.setText(l)
def tann():
    global tbox,l,p
    l=l+'tan('
    p=p+'v('
    print("tan")
    tbox.setText(l)
def asin():
    global tbox,l,p
    l=l+'asin('
    p=p+'w('
    print("asin")
    tbox.setText(l)

def acos():
    global tbox,l,p
    l=l+'acos('
    p=p+'x('
    print("acos")
    tbox.setText(l)


def atan():
    global tbox,l,p
    l=l+'atan('
    p=p+'y('
    print("atan")
    tbox.setText(l)

def ln():
    global tbox,l,p
    l=l+'ln('
    p=p+'z('
    print("log")
    tbox.setText(l)
def logg():
    global tbox,l,p
    l=l+'log('
    p=p+'$('
    print("log")
    tbox.setText(l)
def fact():
    global tbox,l,p
    l=l+'fact('
    p=p+'p('
    print("fact")
    tbox.setText(l)
def inv():
    global tbox,l,p
    l=l+'inv('
    p=p+'i('
    print("inv")
    tbox.setText(l)
def P():
    global tbox,l,p
    l=l+'P'
    p=p+'!'
    print("P")
    tbox.setText(l)
def C():
    global tbox,l,p
    l=l+'C'
    p=p+'_'
    print("C")
    tbox.setText(l)
    
btn1 = QtGui.QPushButton("1",w)
btn1.clicked.connect(b1)
btn1.setGeometry(5,60,35,35)
btn2 = QtGui.QPushButton("2",w)
btn2.clicked.connect(b2)
btn2.setGeometry(45,60,35,35)
btn3 = QtGui.QPushButton("3",w)
btn3.clicked.connect(b3)
btn3.setGeometry(85,60,35,35)
btn4 = QtGui.QPushButton("4",w)
btn4.clicked.connect(b4)
btn4.setGeometry(5,100,35,35)
btn5 = QtGui.QPushButton("5",w)
btn5.clicked.connect(b5)
btn5.setGeometry(45,100,35,35)
btn6 = QtGui.QPushButton("6",w)
btn6.clicked.connect(b6)
btn6.setGeometry(85,100,35,35)

btn7 = QtGui.QPushButton("7",w)
btn7.clicked.connect(b7)
btn7.setGeometry(5,140,35,35)

btn8 = QtGui.QPushButton("8",w)
btn8.clicked.connect(b8)
btn8.setGeometry(45,140,35,35)

btn9 = QtGui.QPushButton("9",w)
btn9.clicked.connect(b9)
btn9.setGeometry(85,140,35,35)

btn0 = QtGui.QPushButton("0",w)
btn0.clicked.connect(b0)
btn0.setGeometry(5,180,75,35)

btnAC = QtGui.QPushButton("AC",w)
btnAC.clicked.connect(bAC)
btnAC.setGeometry(125,60,35,35)

btndeci = QtGui.QPushButton(".",w)
btndeci.clicked.connect(bdeci)
btndeci.setGeometry(85,180,35,35)
btndel = QtGui.QPushButton("DEL",w)
btndel.clicked.connect(bdel)
btndel.setGeometry(125,100,35,35)
btneq = QtGui.QPushButton("=",w)
btneq.clicked.connect(beq)
btneq.setGeometry(125,140,35,75)
btadd = QtGui.QPushButton("+",w)
btadd.clicked.connect(badd)
btadd.setGeometry(165,60,35,35)
bts = QtGui.QPushButton("-",w)
bts.clicked.connect(bs)
bts.setGeometry(165,100,35,35)
btmul = QtGui.QPushButton("*",w)
btmul.clicked.connect(bmul)
btmul.setGeometry(165,140,35,35)
btdiv = QtGui.QPushButton("/",w)
btdiv.clicked.connect(bdiv)
btdiv.setGeometry(165,180,35,35)
btobrac = QtGui.QPushButton("(",w)
btobrac.clicked.connect(obrac)
btobrac.setGeometry(205,60,35,35)
btcbrac = QtGui.QPushButton(")",w)
btcbrac.clicked.connect(cbrac)
btcbrac.setGeometry(205,100,35,35)
btpow = QtGui.QPushButton("^",w)
btpow.clicked.connect(poww)
btpow.setGeometry(205,140,35,35)
btsqrt = QtGui.QPushButton("sqrt",w)
btsqrt.clicked.connect(sqrtt)
btsqrt.setGeometry(205,180,35,35)
btnsin = QtGui.QPushButton("sin",w)
btnsin.clicked.connect(sinn)
btnsin.setGeometry(5,220,35,35)
btncos = QtGui.QPushButton("cos",w)
btncos.clicked.connect(coss)
btncos.setGeometry(45,220,35,35)
btntan = QtGui.QPushButton("tan",w)
btntan.clicked.connect(tann)
btntan.setGeometry(85,220,35,35)
btnasin = QtGui.QPushButton("asin",w)
btnasin.clicked.connect(asin)
btnasin.setGeometry(5,260,35,35)
btnacos = QtGui.QPushButton("acos",w)
btnacos.clicked.connect(acos)
btnacos.setGeometry(45,260,35,35)
btnatan = QtGui.QPushButton("atan",w)
btnatan.clicked.connect(atan)
btnatan.setGeometry(85,260,35,35)
btnln = QtGui.QPushButton("ln",w)
btnln.clicked.connect(ln)
btnln.setGeometry(125,260,35,35)
btnlog = QtGui.QPushButton("log",w)
btnlog.clicked.connect(logg)
btnlog.setGeometry(125,220,35,35)
btnfact = QtGui.QPushButton("fact",w)
btnfact.clicked.connect(fact)
btnfact.setGeometry(165,220,35,35)
btninv = QtGui.QPushButton("inv",w)
btninv.clicked.connect(inv)
btninv.setGeometry(165,260,35,35)
btnp = QtGui.QPushButton("nPr",w)
btnp.clicked.connect(P)
btnp.setGeometry(205,260,35,35)
btnc = QtGui.QPushButton("nCr",w)
btnc.clicked.connect(C)
btnc.setGeometry(205,220,35,35)

w.show()
    
sys.exit(app.exec_())
        
