# Use a loop to attack the skeleton.
# Its blunt sword hardly does any damage, but it has huge knockback.

enemy = self.findNearestEnemy()
self.bash(enemy)

loop:
    self.attack(enemy)