Start_amo = '10'
Player_health = '100'

player_name = input('player name:')
number_of_enimies = input("How meany enmies do you wnat:")
print(f'Name:{player_name}')
print(f'Health:{Player_health}')
print(f'Number of enimies (max is 5): {number_of_enimies}')
print(f'Bullets: {Start_amo}')

while True:
    if number_of_enimies == '1':
            start = input("Are you ready to start: y/n")

            if start == 'y':
                print('starting.....')
                Shot1 = input("you encounter an enemy what do you do.   Shoot(1)  Exit(2)")
                if Shot1 =='1':
                    Bullets_arter_1 = int(Start_amo) - 2
                    print(f'you hit him in 2 shots. you have {Bullets_arter_1}')

                    print("You have killed all of the enimies")
                    print('Good Jod Soldier')
                    break

                if Shot1 =='2':
                    print("As you run away like a babby he shoots you")
                    print('You are DEAD')
                    break 
                  
    if number_of_enimies == '2':
         start = input("Are you ready to start: y/n")

        if start == 'y':
                print('starting.....')
                Shot1 = input("you encounter an enemy what do you do.   Shoot(1)  Exit(2)")
                if Shot1 =='1':
                    Bullets_arter_1 = int(Start_amo) - 2
                    print(f'you hit him in 2 shots. you have {Bullets_arter_1}')

                    print("You have killed all of the enimies")
                    print('Good Jod Soldier')
                    break
                
                if Shot1 =='2':
                    print("As you run away like a babby he shoots you")
                    print('You are DEAD')
                    break   