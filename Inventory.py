import pygame

slot1miejsce = True
slot2miejsce = True
slot3miejsce = True
slot4miejsce = True

slot1miejsce2 = True
slot2miejsce2 = True
slot3miejsce2 = True
slot4miejsce2 = True

xItem1 = 1473
yItem1 = 406
xItem2 = 1556
yItem2 = 406

pygame.init()
window = pygame.display.set_mode((1920, 1080))

eq1 = pygame.image.load("Assets/Ekwipunek.png")



Item1click = False
Item2click = False

siekiera = False
kilof = False

class tlo:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.image = pygame.image.load("Assets/mapa.png")

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

    def tick(self):
        pass

class Item1:
    def __init__(self, x_cord, y_cord, file_name):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_image = pygame.image.load(f"{file_name}.png")
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.button_image.get_width(), self.button_image.get_height())

    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                    global Item1click
                    Item1click = True
                    return True
            else:
                Item1click = False


    def draw(self, window):
        if Item1click == True:
            global xItem1, yItem1
            xItem1 = pygame.mouse.get_pos()[0]
            yItem1 = pygame.mouse.get_pos()[1]

        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.button_image, (self.x_cord, self.y_cord))
        else:
            window.blit(self.button_image, (self.x_cord, self.y_cord))


class Item2:
    def __init__(self, x_cord, y_cord, file_name):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_image = pygame.image.load(f"{file_name}.png")
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.button_image.get_width(), self.button_image.get_height())


    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                global Item2click
                Item2click = True
                return True
            else:
                Item2click = False




    def draw(self, window):
        if Item2click == True:
            global xItem2, yItem2
            xItem2 = pygame.mouse.get_pos()[0]
            yItem2 = pygame.mouse.get_pos()[1]

        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.button_image, (self.x_cord, self.y_cord))
        else:
            window.blit(self.button_image, (self.x_cord, self.y_cord))

class Slot1main:
    def __init__(self):
        self.x_cord = 1690
        self.y_cord = 235
        self.image = pygame.image.load("Assets/slot.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Slot1:
    def __init__(self):
        self.x_cord = 1470
        self.y_cord = 400
        self.image = pygame.image.load("Assets/slot.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Slot2:
    def __init__(self):
        self.x_cord = 1560
        self.y_cord = 400
        self.image = pygame.image.load("Assets/slot.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Slot3:
    def __init__(self):
        self.x_cord = 1650
        self.y_cord = 400
        self.image = pygame.image.load("Assets/slot.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Slot4:
    def __init__(self):
        self.x_cord = 1740
        self.y_cord = 400
        self.image = pygame.image.load("Assets/slot.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


def main():
    slot1main = Slot1main()
    slot1 = Slot1()
    slot2 = Slot2()
    slot3 = Slot3()
    slot4 = Slot4()
    Tlo = tlo()
    run = True
    clock = 0
    ep = False


    while run:
        keys = pygame.key.get_pressed()
        global xItem1, yItem1
        global xItem2, yItem2
        global slot1miejsce
        global slot2miejsce
        global slot3miejsce
        global slot1miejsce2
        global slot2miejsce2
        global slot3miejsce2
        global slot4miejsce
        global slot4miejsce2
        global siekiera
        global kilof
        button1 = Item1(xItem1, yItem1, "Assets/Kilof Drewniany ")
        button2 = Item2(xItem2, yItem2, "Assets/Siekiera drewniana")

        if keys[pygame.K_e]:
            ep = True
        if keys[pygame.K_ESCAPE]:
            ep = False

        if slot1.hitbox.colliderect(button1.hitbox):
            xItem1 = 1473
            yItem1 = 406
            slot1miejsce = False

        if slot2.hitbox.colliderect(button1.hitbox):
            xItem1 = 1563
            yItem1 = 406
            slot2miejsce = False


        if slot3.hitbox.colliderect(button1.hitbox):
            xItem1 = 1653
            yItem1 = 406
            slot3miejsce = False

        if slot4.hitbox.colliderect(button1.hitbox):
            xItem1 = 1743
            yItem1 = 406
            slot4miejsce = False

        if slot1.hitbox.colliderect(button2.hitbox):
            xItem2 = 1473
            yItem2 = 406
            slot1miejsce2 = False

        if slot2.hitbox.colliderect(button2.hitbox):
            xItem2 = 1563
            yItem2 = 406
            slot2miejsce2 = False

        if slot3.hitbox.colliderect(button2.hitbox):
            xItem2 = 1653
            yItem2 = 406
            slot3miejsce2 = False

        if slot4.hitbox.colliderect(button2.hitbox):
            xItem2 = 1743
            yItem2 = 406
            slot4miejsce2 = False

        if slot1main.hitbox.colliderect(button1.hitbox):
            kilof = True
            xItem1 = 1693
            yItem1 = 243
            if button1.hitbox.colliderect(button2.hitbox):
                if slot1miejsce == True:
                    xItem2 = 1473
                    yItem2 = 406
                if slot2miejsce == True:
                    xItem2 = 1563
                    yItem2 = 406
                if slot3miejsce == True:
                    xItem2 = 1653
                    yItem2 = 406
                if slot4miejsce == True:
                    xItem2 = 1743
                    yItem2 = 406



        if slot1main.hitbox.colliderect(button2.hitbox):
            siekiera = True
            xItem2 = 1690
            yItem2 = 243
            if button1.hitbox.colliderect(button2.hitbox):
                if slot1miejsce == True:
                    xItem2 = 1473
                    yItem2 = 406
                if slot2miejsce == True:
                    xItem2 = 1563
                    yItem2 = 406
                if slot3miejsce == True:
                    xItem2 = 1653
                    yItem2 = 406
                if slot4miejsce == True:
                    xItem2 = 1743
                    yItem2 = 406






        if not slot1.hitbox.colliderect(button2.hitbox) | slot2.hitbox.colliderect(button2.hitbox)| slot3.hitbox.colliderect(button2.hitbox)| slot4.hitbox.colliderect(button2.hitbox)|button2.hitbox.colliderect(slot1main.hitbox):
            xItem2 = 1473
            yItem2 = 406

        if not slot1.hitbox.colliderect(button1.hitbox) | slot2.hitbox.colliderect(button1.hitbox)| slot3.hitbox.colliderect(button1.hitbox)|slot4.hitbox.colliderect(button1.hitbox) | slot1main.hitbox.colliderect(button1.hitbox):
            xItem1 = 1556
            yItem1 = 406

        if not slot1.hitbox.colliderect(button1.hitbox):
            slot1miejsce = True
        if not slot2.hitbox.colliderect(button1.hitbox):
            slot2miejsce = True
        if not slot3.hitbox.colliderect(button1.hitbox):
            slot3miejsce = True
        if not slot4.hitbox.colliderect(button1.hitbox):
            slot4miejsce = True

        if not slot1.hitbox.colliderect(button2.hitbox):
            slot1miejsce2 = True
        if not slot2.hitbox.colliderect(button2.hitbox):
            slot2miejsce2 = True
        if not slot3.hitbox.colliderect(button2.hitbox):
            slot3miejsce2 = True
        if not slot4.hitbox.colliderect(button2.hitbox):
            slot4miejsce2 = True


        if button1.hitbox.colliderect(button2.hitbox):
            if slot1miejsce == False and slot2miejsce == True:
                xItem1 = 1556
                yItem1 = 406
                if slot1miejsce == False and slot3miejsce == True:
                    xItem1 = 1653
                    yItem1 = 406
                    if slot1miejsce == False and slot4miejsce == True:
                        xItem1 = 1743
                        yItem1 = 406


            if slot2miejsce == False and slot1miejsce == True:
                xItem1 = 1473
                yItem1 = 406
                if slot2miejsce == False and slot3miejsce == True:
                    xItem1 = 1653
                    yItem1 = 406
                    if slot2miejsce == False and slot4miejsce == True:
                        xItem1 = 1743
                        yItem1 = 406


            if slot3miejsce == False and slot1miejsce == True:
                xItem1 = 1473
                yItem1 = 406
                if slot3miejsce == False and slot2miejsce == True:
                    xItem1 = 1653
                    yItem1 = 406
                    if slot3miejsce == False and slot4miejsce == True:
                        xItem1 = 1743
                        yItem1 = 406

            if slot4miejsce == False and slot1miejsce == True:
                xItem1 = 1473
                yItem1 = 406
                if slot4miejsce == False and slot2miejsce == True:
                    xItem1 = 1556
                    yItem1 = 406
                    if slot4miejsce == False and slot3miejsce == True:
                        xItem1 = 1653
                        yItem1 = 406



        clock += pygame.time.Clock().tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if keys[pygame.K_c]:
            run = False




        Tlo.draw()
        Tlo.tick()
        if ep == True:
            window.blit(eq1, (0,0))
            slot1.tick()
            slot1.draw()
            slot2.tick()
            slot2.draw()
            slot3.tick()
            slot3.draw()
            slot4.draw()
            slot4.tick()
            slot1main.tick()
            slot1main.draw()
            button1.draw(window)
            button1.tick()
            button2.draw(window)
            button2.tick()
        pygame.display.update()


if __name__ == "__main__":
    main()
