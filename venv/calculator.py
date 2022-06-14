import operator
class Calculator:

    def Number1IsPressed(self):
        getNumber1 = input()
        global Zahl1
        Zahl1 = Zahl1 + getNumber1
        print(Zahl1)
        return Zahl1

    def Number2IsPressed(self):
        getNumber2 = input()
        global Zahl2
        Zahl2 = Zahl2 + getNumber2
        print(Zahl2)
        return Zahl2

    def OperatorIsPressed(self):
        op = input()
        #op = '+'
        return op

    def Calculate(self):
        Ergebnis = operations[char](Zahl1, Zahl2)
        print(Ergebnis)
        return  Ergebnis

c = Calculator()



Zahl1 = ""
Zahl2 = ""

he = int(c.Number1IsPressed())
op = c.OperatorIsPressed()
ha = int(c.Number2IsPressed())


result = eval('{}{}{}'.format(he, op, ha))
print(result)
