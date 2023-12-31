
palabra1= "amoR"
palabra2 = "amor"

def anagrama (a:str,b:str):
    a=a.lower()
    b=b.lower()

    if a==b:
        print ("No es un anagrama")
    elif a!=b: sorted(a)== sorted(b)

print(anagrama(palabra1,palabra2))
