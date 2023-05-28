def checknumeric(n,d,l):
    while n.isnumeric() is False:
                print('Please give valid input\n')
                n=input(d)
                if l!=-1:
                    if n.isnumeric():
                        if int(n)>l or int(n)<1:
                            n='temp'
    return n

def add_coaches():
    n=input("Enter number of coaches to be added: ")
    n=int(checknumeric(n,"Enter number of coaches to be added: ",-1))
    out={}
    for i in range(n):
        desc=input('Enter coach description : ')
        seats=input('Enter number of seats : ')
        seats=checknumeric(seats,'Enter number of seats : ',-1)
        s=[x for x in range(1,int(seats)+1)]
        out[desc]=s
    return out


def view_coaches():
    global desc
    global coaches
    out={}
    for i in range(len(desc)):
        out[desc[i]]=coaches[i]
    print(out)

def remove_coaches():
    global desc
    global coaches
    print("Available Coaches")
    for i in range(0,len(desc)):
        print(f'{i+1}. {desc[i]}')
    n=input("Enter the coach number to delete : ")
    try:
        if int(n)>len(desc) or int(n)<1:
                    n='temp'
    except:
        while n.isnumeric() is False:
                print('Please give valid input\n')
                n=input("Enter the coach number to delete: ")
                if n.isnumeric():
                    if int(n)>len(desc) or int(n)<1:
                        n='temp'
    n=int(n)
    desc.pop(n-1)
    coaches.pop(n-1)
    print(desc)
    print(coaches)

def update_desc():
    global desc
    global coaches
    print("Available Coaches")
    for i in range(0,len(desc)):
        print(f'{i+1}. {desc[i]}')
    n=input("Enter the coach number to update : ")
    try:
        if int(n)>len(desc) or int(n)<1:
                    n='temp'
    except:
        n=checknumeric(n,"Enter the coach number to update: ",len(desc))
    n=int(n)
    d=input("Enter a value to update description(Press Enter if you don't want to update) : ")
    seats=input("Enter a value to update number of seats(Press Enter if you don't want to update) : ")
    s=[]
    if seats!='':
        seats=checknumeric(seats,"Enter a value to update number of seats(Press Enter if you don't want to update) : ",-1)
        s=[x for x in range(1,int(seats)+1)]
        coaches[n-1]=s
    if d!='':
        desc[n-1]=d
    print(desc)
    print(coaches)


def book_ticket():
    global desc
    global coaches
    global booked_tickets
    check=True
    while check is True:
        print("Available Coaches")
        for i in range(0,len(desc)):
            print(f'{i+1}. {desc[i]}')
        n=input("Enter the coach number to book : ")
        try:
            if int(n)>len(desc) or int(n)<1:
                        n='temp'
        except:
            n=checknumeric(n,"Enter the coach number to book: ",len(desc))
        n=int(n)
        print('\nSeats available : ')
        print(coaches[n-1])
        booked=list(input("Enter seat numbers to be booked for example '1,2,..'  : ").split(','))
        flag=True
        while flag is True:
            for i in range(len(booked)):
                if booked[i].isnumeric() is False:
                    print(booked[i])
                    break
                elif int(booked[i]) not in coaches[n-1]:
                    print(booked[i])
                    break
                elif i==(len(booked)-1):
                    flag=False
                else:
                    coaches[n-1].remove(int(booked[i]))
            if flag is not False:
                print('Please give valid input\n')
                print(coaches[n-1])
                booked=list(input("Enter seat numbers to be booked for example '1,2,..'  : ").split(','))
        print(f'Booked Tickets{booked}')
        for b in booked:
            booked_tickets[n-1].append(b)
        print('\n1. Book tickets')
        print('2. Exit')
        try:
            i=int(input())
            if i not in [1,2]:
                i='temp'
            i=int(i)
            if i==1:
                book_ticket()
            if i==2:
                return False
        except:
            print('Please give valid input')
            return False


def view_booked():
    global desc
    global booked_tickets
    out={}
    for i in range(len(desc)):
        out[desc[i]]=booked_tickets[i]
    print(out)





username=input("Enter Username : ")
ac_sleeper=[x for x in range(1,61)]
nonac_sleeper=[x for x in range(1,61)]
seater=[x for x in range(1,121)]
coaches=[ac_sleeper,nonac_sleeper,seater]
desc=['A/C Sleeper','Non A/C Sleeper','Seater']
booked_tickets=[[],[],[]]
check=True
if username=='admin':
    while check is True:
        print('\n1. Add additional coaches')
        print('2. View all seats in a coach / train')
        print('3. Remove the coaches')
        print('4. Update the details of the coaches of the train')
        print('5. To view booked tickets')
        print('6. Exit\n')
        try:
            i=int(input())
            if i>5 and i<1:
                i='temp'
            i=int(i)
            if i==1:
                msg=add_coaches()
                for i,j in msg.items():
                    desc.append(i)
                    coaches.append(j)
                    booked_tickets.append([])
            if i==2:
                view_coaches()
            if i==3:
                remove_coaches()
            if i==4:
                update_desc()
            if i==5:
                view_booked()
            if i==6:
                check=False
        except:
            print('Please give valid input')
check_1=True
if username=='user':
     while check_1 is True:
        print('\n1. Book Tickets')
        print('2. Exit\n')
        try:
            i=int(input())
            if i not in [1,2]:
                i='temp'
            i=int(i)
            if i==1:
                check_1=book_ticket()
            if i==2:
                check_1=False
        except:
            print('Please give valid input')
       
