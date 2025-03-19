Start_amo = '10'
Player_health = '100'

player_name = input('player name:')
number_of_enimies = input("How meany enmies do you wnat:")
print(f'Name:{player_name}')
print(f'Health:{Player_health}')
print(f'Number of enimies (max is 5): {number_of_enimies}')
print(f'Bullets: {Start_amo}')

while True:
    start = input('Do you want to start    y/n')
    if start =='y':
        if number_of_enimies == '1':
            Shot1_in_1 = input("you encounter an enemy what do you do.   Shoot(1)  Exit(2)")
            if Shot1_in_1 =='1':
                        Bullets_arter_1_in_1 = int(Start_amo) - 2
                        print(f'you hit him in 2 shots. you have {Bullets_arter_1_in_1} bullets')

                        print("You have killed all of the enimies")
                        print('Good Job Soldier')
                        break 

        if number_of_enimies == '2':
                       
            Shot1_in_2 = input("you encounter an enemy what do you do.   Shoot(1)  Exit(2)")
            if Shot1_in_2 =='1':
                        Bullets_arter_1_in_2 = int(Start_amo) - 2
                        print(f'you hit him in 2 shots. you have {Bullets_arter_1_in_2} bullets')

                        Move_forward = input('do you want to move forward   y/n')
                        if Move_forward == 'y':
                                Shot2_in_2 = input("you encounter an other enemy what do you do.   Shoot(1)  Exit(2)")
                                if Shot2_in_2 =='1':
                                    Bullets_arter_2_in_2 = int(Bullets_arter_1_in_2) - 3
                                    print(f'you hit him in 3 shots. you have {Bullets_arter_2_in_2}')

                                    print("You have killed all of the enimies")
                                    print('Good Job Soldier')
                                    break
            
        if number_of_enimies == '3':
                       
            Shot1_in_3 = input("you encounter an enemy what do you do.   Shoot(1)  Exit(2)")
            if Shot1_in_3 =='1':
                        Bullets_arter_1_in_3 = int(Start_amo) - 2
                        print(f'you hit him in 2 shots. you have {Bullets_arter_1_in_3} bullets')

                        Move_forward = input('do you want to move forward   y/n')
                        if Move_forward == 'y':
                                Shot2_in_3 = input("you encounter an other enemy what do you do.   Shoot(1)  Exit(2)")
                                if Shot2_in_3 =='1':
                                    Bullets_arter_2_in_3 = int(Bullets_arter_1_in_3) - 3
                                    print(f'you hit him in 3 shots. you have {Bullets_arter_2_in_3}')
                                    
                                    Move_forward = input('do you want to move forward   y/n')
                                    if Move_forward == 'y':
                                            Shot3_in_3 = input("you encounter an other enemy what do you do.   Shoot(1)  Exit(2)")
                                            if Shot3_in_3 =='1':
                                                Bullets_arter_3_in_3 = int(Bullets_arter_2_in_3) - 3
                                                print(f'you hit him in 3 shots. you have {Bullets_arter_3_in_3}')
                                                print("You have killed all of the enimies")
                                                print('Good Job Soldier')
                                                break

    if Shot1_in_1 or Shot1_in_2 or Shot2_in_2 or Shot1_in_3 or Shot2_in_3 or Shot3_in_3 =='2':
        print("you are a babby")
        break
    if Move_forward == 'n':
        print("you are a babby")
        break