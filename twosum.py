#Raget Homework

#Memasukkan Angka 
def aryinput():
    try:
        arrynt = list(map(int, input("Masukkan Angka2 ke Array. Pisahkan dengan Spasi : ").split(" ")))
        return arrynt
    except ValueError:
        return None
    
#Two Sum
def twosum(array, target):
    book = {}
    for i,x in enumerate(array):
        s = target - x
        if s in book:
            return [book[s],i]
        book[x] = i
    return "Tidak Ada Memenuhi Target"
            
# Menjalankan Program
masukkan_array = aryinput()
Target = int(input("Masukkan Target : "))
sumtwo = twosum(masukkan_array, Target)
print(sumtwo)
    