#trabajo sistematico S4
#NOMBRES 
#Nahomy Bonilla
#Isamar Espinoza
#Ernesto Gámez

class rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        
    def result (self):
        print(f"el resultado es{self.base * self.altura}")
        
ejercicio1 = rectangulo(10,2)
ejercicio1.result()


class figura_geometrica (rectangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)
        
    def resultado2(self):
        print(f"el resultado es {self.base * self.altura / 2}")

ejercicio1 = figura_geometrica(20,4)
ejercicio1.result()
ejercicio1.resultado2()

class cuenta_Bancaria:
    def __init__(self,saldo_inicial):
        self.__saldo = saldo_inicial
        
    def depositar(self,cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print (f'se han depositado {cantidad}unidades.')
        else:
            print('La cantidad a ser depositada tiene que tener un valor mayor a 0.')
            
    def retirar (self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print('f 0se han retirado {cantidad}unidades.')
        else:
            print('el saldo no es permitido.')
            
    def consultaSaldo (self):
        print(f'el saldo actual es: {self.__saldo}')
        
        
        #Creacion de cuenta
miCuenta= cuenta_Bancaria(2000)
        
        #ACCEDER
miCuenta.consultaSaldo()
        
miCuenta.depositar (-200)
        
miCuenta.depositar (300)