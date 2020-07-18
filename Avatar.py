from random import randint


class Avatar:
    def __init__(self, attack_points, life_points, experience_points, velocity_points):
        self.velocity_points = velocity_points
        self.experience_points = experience_points
        self.life_points = life_points
        self.attack_points = attack_points

    def getLevel(self):
        if self.experience_points > 100:
            level = int(1 + (self.experience_points - 100) / 50)
        else:
            level = 1
        return level

    def calcNecessaryPoints(self):
        necessary_points = 100 + (self.getLevel() * 50)
        return necessary_points

    def calcMaxPointsEnemy(self):
        max = 99 + (self.getLevel() + 1) * 50
        return max

    def calcMinPointsEnemy(self):
        min = 100 + (self.getLevel() - 2) * 50
        return min

    def calcRangePointsToFight(self):
        if self.getLevel() == 1:
            return [0, 199]
        elif self.getLevel() == 2:
            return [0, 249]
        else:
            return [self.calcMinPiontsEnemy(), self.calcMaxPointsEnemy()]

    def levelUp(self):
        option = randint(0, 2)
        if option == 0:
            self.attack_points += 1
        elif option == 1:
            self.velocity_points += 3
        else:
            self.life_points += 3

    def setFightingExperience(self, victory: bool):
        last_level = self.getLevel()
        if victory:
            self.experience_points += 100
        else:
            self.experience_points += 20

        for i in range(last_level - self.getLevel()):
            self.levelUp()
