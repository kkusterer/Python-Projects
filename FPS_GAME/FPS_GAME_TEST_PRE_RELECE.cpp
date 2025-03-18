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

    Player(std::string playerName) : name(playerName), health(100), ammo(30) {}

    void shoot() {
        if (ammo > 0) {
            ammo--;
            std::cout << name << " shoots! Ammo left: " << ammo << std::endl;
        } else {
            std::cout << name << " is out of ammo!" << std::endl;
        }
    }

    void takeDamage(int damage) {
        health -= damage;
        if (health <= 0) {
            std::cout << name << " has been killed!" << std::endl;
        } else {
            std::cout << name << " takes " << damage << " damage! Health left: " << health << std::endl;
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
        std::cout << "Game started! " << player.name << " vs Enemy!" << std::endl;
        while (player.health > 0 && enemy.health > 0) {
            player.shoot();
            enemy.attack(player);
        }
        if (player.health > 0) {
            std::cout << player.name << " wins!" << std::endl;
        } else {
            std::cout << "Enemy wins!" << std::endl;
        }
    }
};

int main() {
    Game game("Player1");
    game.start();
    return 0;
}
