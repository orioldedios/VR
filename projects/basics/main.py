if __name__ == '__main__':
    print("hello world")

    #comment
    print(5)
    print(0.223)
    print(3.2E-12 * 100)
    print(format(211))
    number = 9
    name = "patata"

    number = int(input("Dame un numero: ")) #input (lo guarda como una string a menos que castees)
    print(number)                           #output

    var1 = 9
    var2 = 6
    var1 = var1 * var2
    print("var1 * var2 = {}".format(var1))

    #if
    if number > 0:
        print("number > 0")
    elif number < 0:
        print("number < 0")
    else:
        print("number = 0")

    #while
    while number < 100:
        number += 1
        print(number)

    #for
    for i in range(1, number):
        number -= 1
        print(number)

    #function
    def printMult(a, b=10):
        print(a, "*", b, "=", a*b)

    def orderMinMax(a, b):
        if a < b:
            return a, b
        else:
            return b, a

    printMult(number)
    x, y = orderMinMax(2, number)

    print("Min = " +str(x)) #+str = crea string de lo que le metes
    print("Max = " +str(y))

    #List
    myList = ["patata","mumu","chuchu"]
    myList.append("pol")
    print(myList)
    myList.insert(2, "ondestoy")
    print(myList)
    print("first item = ", myList[0])
    del myList[0]
    print(myList)

    #Tuple
    zoo = ("bear","snake","lion")
    print(zoo)
    print("num animals = " +str(len(zoo)))
    print(zoo[0:]) #print all
    print(zoo[0:2])#print between index 0 to 2

    #Dictionary
    myDict = \
    {
        "oriol": "ori",
        "jonathan": "jonny",
    }
    del myDict["oriol"]
    myDict["oscar"] = "oskitar"
    print("oscar = ", myDict["oscar"])

    #set
    mySet = set(["carrot","polos"])
    mySet1 = set(["carrot","osos"])

    print("patata" in mySet) #patata esta en myset?
    print(mySet1.intersection(mySet)) #que tienene en comun myset1 y myset?

    #Classes
    class Yo:
        def __init__(self,name,age): #constructor
            self.name = name
            self.age = age

        def quienSoy(self):
            print("y dise y dise, pos no, eres tu")
            print("soy", self.name)

    class Emociones(Yo):
        def __init__(self,name,age,happy):
            Yo.__init__(self,name,age)
            self.happy = happy

        def tell(self):
            print(("Teacher: {}").format(self.name))

    p = Yo("uri",98)
    p.quienSoy()

    po = Emociones(p.name, p.age,"true")
    print('name: {} Age: {} Feliz?: {}' .format(po.name, po.age, po.happy))

    #librerías
    import numpy as np #importa libreria

