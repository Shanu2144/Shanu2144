import math

def countcustomer(bill):
    for i in bill:
        sqrt = math.sqrt(int(float(i)))
        if int(sqrt + 0.5) ** 2 == i:
            print(i)

    return

def main():
    bill=[]
    bill_size=int(input())
    bill=list(map(int(float(input())).split()))

    result= countcustomer(bill)
    print.result,

if__name__="__main__";
main()
