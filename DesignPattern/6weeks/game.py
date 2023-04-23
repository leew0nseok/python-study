import pygame
import MyVector as mv #vector 클래스

rgb = { # 디스플레이 색상을 나타낼 딕셔너리 
    'BLACK':(0, 0, 0),
    'WHITE':(255, 255, 255),
    'BLUE':(0, 0, 255),
    'GREEN':(0, 255, 0),
    'RED':(255, 0, 0)
}

# Implementor
class Actor: #화면에 등장하는 객체

    def __init__(self, x, y):
        self.pos = mv.MyVector(x, y)
        self.name = ""
        self.skill = ""
    # Actor의 위치 설정 
    def setPos(self, x, y):
        self.pos.x = x
        self.pos.y = y
    # Actor의 위치 이동
    def move(self, delta):
        self.pos = self.pos + delta
    #Actor의 이름 설정
    def setName(self, name):
        self.name = name
    #Actor의 기술 설정
    def setSkill(self, skill):
        pass

# ConcreateImplementatior
class Hero(Actor): # Actor을 상속받은 Hero (ConcreateImplementatior 1)

    def setSkill(self, skill):
        self.skill = skill

# ConcreateImplementatior
class Enermy(Actor): # Actor을 상속받은 Enermy(ConcreateImplementatior 2)

    def setSkill(self, skill):
        self.skill = skill


# Abstraction
class GameFramework:

    def __init__(self):
        self.pygame = pygame
        self.screen = 0

        self.nY = 0 # 스크린의 크기를 담당
        self.nX = 0

        self.hero = 0 # 기능을 실제로 수행하는 위임자가 존재한다.

        print("init")

    def setDisplay(self, nX, nY):  # 디스플레이 설정
        self.nY = nY
        self.nX = nX
        self.screen = self.pygame.display.set_mode([self.nX, self.nY])
        self.pygame.display.set_caption("Prince") #게임창의 이름


    def setHero(self, hero:Actor):
        self.hero = hero # Actor를 인자로 받음

    def ready(self):
        self.pygame.init() #pygame 초기화

    # 다각형을 그리는 함수
    def drawPolygon(self, color, points, thickness):
        self.pygame.draw.polygon(self.screen, color, points, thickness)

    def drawEdges(self):
        p1 = mv.MyVector(0, 0)
        p2 = mv.MyVector(0, 10)
        p3 = mv.MyVector(10, 0)
        
        self.drawPolygon(rgb["WHITE"], [p1.vec(), p2.vec(), p3.vec()], 1)

    def printText(self, msg, color, pos):
        font= self.pygame.font.SysFont("consolas",20)
        textSurface     = font.render(msg,True, color, None) #self.pygame.Color(color)
        textRect        = textSurface.get_rect()
        textRect.topleft= pos
        self.screen.blit(textSurface, textRect)

    #게임 실행
    def launch(self):
        pass


# refinedAbstraction( # Abstraction 클래스에서 하얀색 화면 기능을 추가)
class WhiteGame(GameFramework):

    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()

        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done: 
            clock.tick(60) #set on 30 frames per second

            # alt + f4가 눌렸을때 pygame을 종료하는 코드
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT: #alt + f4
                    print("종료")
                    done = True

                # alt + f4키가 아닌 방향키가 눌렸을때 Actor클래스의 위치를 조정하는 조건문
                elif event.type == self.pygame.KEYDOWN: #키를 눌렀을때
                    print("key down")
                    if event.key == self.pygame.K_LEFT: #어떤키가 눌렸는가? 왼쪽키
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT: # 오른쪽 키가 눌렸을때
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN: # 아래쪽 키
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP: # 위쪽 키
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP: #키를 땟을 경우 KeyFlag를 False로 
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False


            if keyFlag == True: # 키가 눌렸을 때 실행될 코드

                self.hero.move(delta) #주인공의 위치가 업데이트가 됨

                print("pressed", self.hero.pos.getState()) #in console
                self.screen.fill(rgb["WHITE"]) #특성을 살린 부분
                self.printText(self.hero.name, rgb["RED"], self.hero.pos.vec()) 
                self.printText(self.hero.skill, rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()


# refinedAbstraction( # Abstraction 클래스에서 검정색 화면 기능을 추가)
class BlackGame(GameFramework):

    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()

        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done: 
            clock.tick(60) #set on 30 frames per second

            # alt + f4가 눌렸을때 pygame을 종료하는 코드
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT: #alt + f4
                    print("종료")
                    done = True

                # alt + f4키가 아닌 방향키가 눌렸을때 Actor클래스의 위치를 조정하는 조건문
                elif event.type == self.pygame.KEYDOWN: #키를 눌렀을때
                    print("key down")
                    if event.key == self.pygame.K_LEFT: #어떤키가 눌렸는가? 왼쪽키
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT: # 오른쪽 키가 눌렸을때
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN: # 아래쪽 키
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP: # 위쪽 키
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP: #키를 땟을 경우 KeyFlag를 False로 
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False


            if keyFlag == True: # 키가 눌렸을 때 실행될 코드

                self.hero.move(delta)

                print("pressed", self.hero.pos.getState()) #in console
                self.screen.fill(rgb["BLACK"]) #특성화된 부분
                self.printText(self.hero.name, rgb["RED"], self.hero.pos.vec()) 
                self.printText(self.hero.skill, rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()



game = WhiteGame() # Whitegame()으로 수정하면 하얀색 바탕의 게임을 실행하게됨.
game.ready()
game.setDisplay(1500, 1000)
game.drawEdges() # 그려도 되고 안그려도 됨

hero = Hero(0, 0)
hero.setName("prince")
hero.setSkill("swing a sword")

monster = Enermy(50, 50)
monster.setName("weak moster")
monster.setSkill("hit the body")

game.setHero(hero)
# game.setHero(monster)
game.launch()






