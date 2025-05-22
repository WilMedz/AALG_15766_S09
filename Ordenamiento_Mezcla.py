def merge_sort (arr):
    if len (arr) <=1:
        return arr
    
    mitad=len(arr)//2
    izq=merge_sort(arr[:mitad])
    der=merge_sort(arr[mitad:])
    
    return ord_mezcla(izq,der)
    
def ord_mezcla (izq,der):
    resultado=[]
    i=j=0
    
    while i<len (izq) and j< len(der):
        if izq[i]<der[j]:
            resultado.append(izq[i])
            i +=1
        else:
            resultado.append(der[j])
            j +=1
            
    resultado+= izq [i:]
    resultado+= der [j:]
    
    return resultado

lista=[6,2,8,4,10]
print("la lista de numeros es: ",lista)
lista_ordenada=merge_sort(lista)
print("la lista ordenada es: ",lista_ordenada)