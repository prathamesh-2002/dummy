def sort(array):
    n=len(array)
    for i in range(0,n-1):
        smallest=i
        for j in range(i+1,n):
            if(array[j]<array[smallest]):
                smallest=j
        array[i],array[smallest]=array[smallest],array[i]

def main():
    a=input("Enter array:").split()
    a=[int(x) for x in a]
    sort(a)
    print("Sorting:")
    
    print(a)

if __name__=="__main__":
    main()
