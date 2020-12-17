#written by @hakancangunerli ~ don't erase this unless you are a dick
#10
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
prGreen('Hello! This is a simple tax calculator for taxes due april 2020')


def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 

prRed('im not your accountant... go make them calculate it')
x= int(input('how much did you earn? '))

if (0< x <= 9700):
    print(' you are subjected to first tax bracket, which is 10 percent.')
    amount= float(x)
    print(amount * 0.1)
#12
if (9701<=x <= 39475):
    print(' you are subjected to second tax bracket, which is 12 percent.')
    amount= (float(x) - 9700)
    print((amount * .12) + 970) 
#22
if (39476<=x <= 84200):
    print(' you are subjected to third tax bracket, which is 22 percent.')
    amount= float(x) - 39475
    print((amount * 0.22) + 4543 )
#24
if (84201<=x <= 160725):
    print(' you are subjected to fourth tax bracket, which is 24 percent.')
    amount= float(x) -84200
    print((amount * 0.24) + 14382.50)
#32
if (160726<=x <= 204100):
    print(' you are subjected to fifth tax bracket, which is 32 percent.')
    amount= float(x)-  160725
    print((amount * 0.32) +32748.50)
#35
if (204101<=x <= 510300): 
    print(' you are subjected to sixth tax bracket, which is 35 percent.')
    amount= float(x) - 204100 
    print((amount * 0.35)+46628.50)
#37
if (x>= 510301):
    print(' you are subjected to seventh tax bracket, which is 37 percent.')
    amount= float(x) - 510300 
    print((amount * 0.37)+ 153798.50)

#aww, thanks for checking it out
