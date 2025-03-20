START_AMMO = 10
PLAYER_HEALTH = 100

def encounter_enemy(enemy_number, bullets_left):
    shots_required = [2, 3, 3, 1]  # Shots required for each enemy
    action = input(f"You encounter enemy {enemy_number}. What do you do? Shoot(1) Exit(2): ")
    if action == '1':
        bullets_left -= shots_required[enemy_number - 1]
        print(f"You hit enemy {enemy_number} in {shots_required[enemy_number - 1]} shots. You have {bullets_left} bullets left.")
        return bullets_left, True
    elif action == '2':
        print("You are a baby.")
        return bullets_left, False
    else:
        print("Invalid input. You missed your chance!")
        return bullets_left, False

def game():
    player_name = input("Player name: ")
    try:
        number_of_enemies = int(input("How many enemies do you want (max is 4): "))
        if number_of_enemies < 1 or number_of_enemies > 4:
            print("Invalid number of enemies. Please choose between 1 and 4.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    print(f"Name: {player_name}")
    print(f"Health: {PLAYER_HEALTH}")
    print(f"Number of enemies: {number_of_enemies}")
    print(f"Bullets: {START_AMMO}")

    bullets_left = START_AMMO
    for enemy in range(1, number_of_enemies + 1):
        move_forward = input("Do you want to move forward? y/n: ")
        if move_forward.lower() != 'y':
            print("You are a baby.")
            return

        bullets_left, success = encounter_enemy(enemy, bullets_left)
        if not success:
            return

        if bullets_left <= 0:
            print("You ran out of bullets. Game over!")
            return

    print("You have killed all the enemies. Good job, Soldier!")

if __name__ == "__main__":
    while True:
        start = input("Do you want to start? y/n: ")
        if start.lower() == 'y':
            game()
        elif start.lower() == 'n':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")