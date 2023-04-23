"""
class Dog:
    def __init__(self, name, age, gender, breed, DNA):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.DNA = DNA

    def __repr__(self):
        return f'{self.name},{self.age},{self.gender},{self.breed},{self.DNA}'
        
choco = Dog("choco", 2, "male", "shihTzu", "ATAGGCTTACCGATGG..")
baduk = Dog("baduk", 3, "female", "jindo", "ATAGGCTTACCGATGG..")
"""

"""
# 모든 강아지들의 DNA 같은 경우
class Dog:
    DNAseq = "ATAGGCTTACCGATGG.."
    def __init__(self, name, age, gender, breed):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed

    def __repr__(self):
        return f'{self.name},{self.age},{self.gender},{self.breed},{self.DNAseq}'

choco = Dog("choco", 2, "male", "shihTzu")
baduk = Dog("baduk", 3, "female", "jindo")
"""

# 강아지 종마다 DNA 다른 경우
class DogBreedDNA:
    def __init__(self, breed, DNA):
        self.breed = breed
        self.DNA = DNA
    def __repr__(self):
        return f'{self.DNA}'
    
class Dog:
    DNAtable = {}
    @staticmethod
    def addDNA(breed, DNA):
        breed_DNA = DogBreedDNA(breed, DNA)
        Dog.DNAtable[breed] = breed_DNA

    def __init__(self, name, age, gender, breed):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        if breed not in Dog.DNAtable:
            raise RuntimeError(f"{breed} is not in DNAtable")

    def __repr__(self):
        return f'{self.name},{self.age},{self.gender},{self.breed},{Dog.DNAtable[self.breed]}'
    
Dog.addDNA("shihTzu", "ATAGGCTTACCGATGG..")
Dog.addDNA("jindo", "GGCTTACCGATGGTAGT..")

choco = Dog("choco", 2, "male", "shihTzu")
baduk = Dog("baduk", 3, "female", "jindo")
bobbi = Dog("bobbi", 1, "female", "shiba") # 시바는 없기때문에 오류

print(choco)
print(baduk)