#rock paper scissors
import random
x = ['r','p','s']
while True:
    choice = input('r or p or s \n')
    computerc = random.choice(x)
    print(choice)
    print(computerc)
    if choice=='quit':
        break
    elif choice != 'r' and choice !='p' and choice!='s':
        print('choose from r or p or s')
        continue
    elif choice==computerc:
        print('tie try again')
    elif choice == 'r' and computerc =='s':
        print('you win!')
        break
    elif choice == 's' and computerc =='p':
        print('you win!')            
        break
   
    elif choice=='p' and computerc =='r':
        print('you win!')
        break             
    else:
        print('you lost')