import datetime


class Character:
    '''self._CharacterName = name as string
    self._DateOfBirth = dob as date
    self._Intelligence = i as real
    self._Speed = speed as integer'''

    def __init__(self, name, dob, i, speed):
        self._CharacterName = name
        self._DateOfBirth = dob
        self._Intelligence = i
        self._Speed = speed

    def GetIntelligence(self):
        return self._Intelligence

    def GetName(self):
        return self._CharacterName

    def SetIntelligence(self, intelligence):
        self._Intelligence = intelligence

    def Learn(self):
        self._Intelligence *= 1.1

    def ReturnAge(self):
        return 2023 - self._DateOfBirth.year  # assuming that date is in datetime.datetime


FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30)

FirstCharacter.Learn()
print(
    f"{FirstCharacter.GetName()} is {FirstCharacter.ReturnAge()} years old with Intelligence of {FirstCharacter.GetIntelligence()}")


class MagicCharacter(Character):
    def __init__(self, Element, name, dob, i, speed):
        self._Element = Element
        super().__init__(name, dob, i, speed)

    def Learn(self):
        if self._Element == "fire" or "water":
            self._Intelligence *= 1.2
        if self._Element == "earth":
            self._Intelligence *= 1.3
        else:
            self._Intelligence *= 1.1


FireMagic = MagicCharacter("fire","Light", datetime.datetime(2018, 3, 3), 75, 22)
FireMagic.Learn()
