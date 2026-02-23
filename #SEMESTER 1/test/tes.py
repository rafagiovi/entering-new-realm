class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def serang(self, musuh):
        damage = self.attack
        musuh.hp -= damage
        print(f"{self.nama} menyerang {musuh.nama} dengan damage {damage}. {musuh.nama} HP sekarang {musuh.hp}")

def battle(player, enemy):
    ronde = 1
    while player.hp > 0 and enemy.hp > 0:
        print(f"\n --- Ronde {ronde} ---")
        player.serang(enemy)
        
        if enemy.hp <= 0:
            print(f"{enemy.nama} tumbang! {player.nama} menang 🎉")
            break

        if player.hp <= 0:
            print(f"{player.nama} kalah... {enemy.nama} menang 👾")
            break
    ronde += 1 



player = Character("Rafa", 50, 12, 5)
enemy = Character("Goblin", 40, 8, 3)

battle(player, enemy)