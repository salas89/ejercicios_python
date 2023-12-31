"""/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */"""


palabra1= "Roma"
palabra2 = "amor"

def anagrama (a:str,b:str):
    a=a.lower()
    b=b.lower()
    c=sorted(a)== sorted(b) #sorted ordena los elementos de la variable, lista, etc.

    if a==b:
        return ("No es un anagrama, son la misma palabra")
    elif c==True:
        return ("Es un anagrama") 
    else: return("No es un anagrama")

print(anagrama(palabra1,palabra2))
