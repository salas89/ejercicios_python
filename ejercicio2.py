
palabra1= "amor"
palabra2 = "amor"

def anagrama (a:str,b:str):
    a=a.lower()
    b=b.lower()
    c=sorted(a)== sorted(b)

    if a==b:
        return ("No es un anagrama, son la misma palabra")
    elif c==True:
        return ("Es un anagrama") #sorted ordena los elementos de la variable, lista, etc.
    else: return("No es un anagrama")

print(anagrama(palabra1,palabra2))
