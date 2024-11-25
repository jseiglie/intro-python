print('hola mundo!')

#vars
#
# var, let, const
#

number = 5
VERSION = 1

# tipos de datos

#primitivos
name = 'Pepe'
#age = 55 
altura = 1.75 
alive = True 
pareja = None

## obj
## arr --> listas
arr = [1,2,4,5,6]
arr[0] # --> 1
print(arr[0])
# obj ---> dict
obj = {
    "nombre": "Pepe",
    "edad": 55
}
obj['nombre'] #--> Pepe 

print(obj['nombre'])


# funciones

# function suma () {
#
#}
# const sum = () => {
#
#}

def nombreFuncion():
    #codigo
    return (
        #lo que retorna
    )

def otraFuncion():
    #codigo
    return (
        #lo que retorna
    )

def sum(a,b):
    return a+b

print(sum(5,5))
print(sum)
def sayHi(name):
    #return 'hi ' + name
    return f"hi {name}"

print(sayHi('pepe'))

#Lambda

# variable = lambda param, ...n: return

salut = lambda x: f"hola {x}"
sumador = lambda a,b: a+b
print(salut('lola'))
print(sumador(3,3))

print('-----------------------------Loops---------------------------------')
#loops

lista = [5,7,8,9,6,5,4,2,1]
total = 0
for num in lista:
    total+=num
    print(num)
print('total----> ', total)
# for(let i = 0; i< lista.length; i++)

for index in range(len(lista)):
    print(lista[index])   

#lista.map()

def printIt(x):
    return 'funcion--- ' + str(x)

#map(funcion, iterable)

test = map(lambda x: printIt(x), lista)
print(list(test))

happy_people = ['Bob', 'Greg', 'Kyle']

result = list(map(lambda name: name + " is happy!", happy_people))

print(result)


#trabajando con listas
# lista[2] = 'pepe'

# print(lista[2]) #--> valor en la posicion 2
# # lista.append('lola')
# # lista.insert(5, 'matia')
# # lista.insert(8, 'matia')
# print(lista)
# # lista.remove('matia')
# print(lista)
# lista.sort()
# print(lista)


# # Operadores logicos

# print(5 in lista) # true

# # || --> or
# # && --> and
# print( 5==4 or 5==5) # true

# print( 5==4 and 5==5) # false
# print( 4==4 and 5==5) # true


# # condicionales

# age = None

# # if (age>16) {
# #     console.log('puede manejar')
# # }
# # else if (): {

# # } else {

# # }

# # if age>20:
# #     print('puede manejar y beber')
# # elif age>16:
# #     print('puede manejar')
# # else: 
# #     print('no puede')

# if age is None:
#     print('no tiene valor')