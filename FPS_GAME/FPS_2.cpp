#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>

class Player {
public:
    std::string name;
    int health;
    int ammo;

    Player(std::string playerName) : name(playerName), health(100), ammo(10) {}

    void shoot() {
        if (ammo > 0) {
            ammo--;
            std::cout << name << " shoots! Ammo left: " << ammo << std::endl;
        } else {
            std::cout << "Out of ammo!" << std::endl;
        }
    }

    void takeDamage(int damage) {
        health -= damage;
        if (health <= 0) {
            std::cout << name << " has been defeated!" << std::endl;
        } else {
            std::cout << name << " health: " << health << std::endl;
        }
    }
};

class Enemy {
public:
    int health;

    Enemy() : health(50) {}

    void attack(Player& player) {
        int damage = rand() % 20 + 1;
        player.takeDamage(damage);
    }
};

class Game {
public:
    Player player;
    Enemy enemy;

    Game(std::string playerName) : player(playerName) {
        srand(static_cast<unsigned int>(time(0)));
    }

    void start() {
        std::cout << "Game Start! " << player.name << " vs Enemy!" << std::endl;
        while (player.health > 0 && enemy.health > 0) {
            std::string action;
            std::cout << "Choose action (shoot/exit): ";
            std::cin >> action;

            if (action == "shoot") {
                player.shoot();
                if (player.ammo < 10) {
                    enemy.health -= 10;
                    std::cout << "Enemy health: " << enemy.health << std::endl;
                }
                if (enemy.health > 0) {
                    enemy.attack(player);
                }
            } else if (action == "exit") {
                std::cout << "Exiting game." << std::endl;
                break;
            } else {
                std::cout << "Invalid action!" << std::endl;
            }
        }
    }
};

int main() {
    std::string playerName;
    std::cout << "Enter your player name: ";
    std::cin >> playerName;

    Game game(playerName);
    game.start();

    return 0;
}
