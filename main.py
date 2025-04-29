import pandas as pd

file=pd.read_csv("db.csv")

menu='''
Choose an option:
      
a) Add to wallet
b) Withdraw from wallet
c) Add new wallet
d) Calculate sum f all wallets
e) Calculate mean of all wallets
f) Wipe a wallet
g) Calculate simple interest
h) Calculate compound interest
i) Wallet with highest balance
j) Wallet with lower balance
k) Exit
    '''

def add_wallet(name):
    print(file.head())
    pos=file["name"].count()
    print(file)
    file.loc[pos+1,"name"]=name
    file.loc[pos+1,"balance"]=0
    print(file)

def add_to_wallet():
    print("Select a wallet (Introduce a number):")
    print(file)
    add_wallet_selected=int(input())
    amount=int(input("Insert the ammount you wanna add: "))
    file.loc[add_wallet_selected,"balance"]+=amount
    print(file)

def withdraw():
    print("Select a wallet (Introduce a number):")
    print(file)
    withdraw_wallet_selected=int(input())
    amount=int(input("Insert the ammount you wanna withdraw: "))
    file.loc[withdraw_wallet_selected,"balance"]-=amount
    print(file)

def sum_of_wallets():
    values=file.loc[:,"balance"].sum()
    print(values)

def mean_of_wallets():
    values=file.loc[:,"balance"].mean()
    print(values)

def wipe_wallet():
    print("Select a wallet (Introduce a number):")
    print(file)
    wipe_wallet_selected=int(input())
    file.loc[wipe_wallet_selected,"balance"]=0
    print(file)

def simple_interest():
    print("Select a wallet (Introduce a number):")
    print(file)
    simple_wallet_selected=int(input())
    simp_int=float(input("Input the interess: "))
    file.loc[simple_wallet_selected,"balance"]=(1+simp_int)*file.loc[simple_wallet_selected,"balance"]
    print(file)

def compound_interest():
    print("Select a wallet (Introduce a number):")
    print(file)
    simple_wallet_selected=int(input())
    simp_int=float(input("Input the interess: "))
    years=int(input("Enter the years: "))
    file.loc[simple_wallet_selected,"balance"]=file.loc[simple_wallet_selected,"balance"]*(1+simp_int)**years
    print(file)

def highest_balance():
    values=file.loc[:,"balance"].max()
    print(values)

def lower_balance():
    values=file.loc[:,"balance"].min()
    print(values)

print(menu)

option=input(str("Select your choice: "))

while option:
    if option=="show":
        print(menu)
        option=input(str("Select your choice: "))

    elif option=="a":
        add_to_wallet()
        option="show"

    elif option=="b":
        withdraw()
        option="show"

    elif option=="c":
        name=input(str("Enter your new wallet name: "))
        add_wallet(name)
        option="show"

    elif option=="d":
        adder=sum_of_wallets()
        option="show"
    
    elif option=="e":
        adder=mean_of_wallets()
        option="show"
    
    elif option=="f":
        wipe_wallet()
        option="show"
    
    elif option=="g":
        simple_interest()
        option="show"
    
    elif option=="h":
        compound_interest()
        option="show"

    elif option=="i":
        highest_balance()
        option="show"

    elif option=="j":
        lower_balance()
        option="show"

    elif option=="k":
        break
        
    else:
        print("Invalid option")
        option="show"