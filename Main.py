import pygame
import random

import Player
import Inventory
import Items
import Menu
import Monsters

pygame.init()

win = pygame.display.set_mode((1536, 288))
bg = pygame.image.load('assets/Pics/environment-preview.jpg').convert()
pygame.display.set_caption("Welcome to the Overlords RPG!")

screenWidth = 1536

# Sound effects
hitSound = pygame.mixer.Sound('assets/Sound/Skeleton Roar.wav')
bulletSound = pygame.mixer.Sound('assets/Sound/Arrow.wav')
swordSound = pygame.mixer.Sound('assets/Sound/Sword2.wav')
# deathSound = pygame.mixer.Sound('death_sound.wav')

# Background Music
music = pygame.mixer.music.load('assets/Sound/Risen.wav')
pygame.mixer.music.play(-1)


# Frame rate
clock = pygame.time.Clock()



# Globals
start_intro = Menu.Start(450, 75, 100, 50)
exit_intro = Menu.Exit(450, 200, 100, 50)
Cii_intro = Menu.Character_image_intro(450, 125, 100, 50)
font = pygame.font.SysFont("Sans", 30, True, True)
Chosen = Player.MainPlayer(0, 215, 50, 37)
inventory = Inventory.Inventory(0, 20, 0)
m_spawn = random.randrange(400, 700, 50)
Skeleton = Monsters.Enemy(m_spawn, 217, 22, 33, 1150)
Skeleton2 = Monsters.Enemy(m_spawn, 217, 22, 33, 1150)
bone = Items.Item(500, 217)
bullets = []
attacks = []
monsters = []
num_monsters = 3
monsters_on_screen = 0
items = []


def redraw_game_window():
    # Base screen UI
    win.blit(bg, (0, 0))
    txt = font.render('Hp: ', 1, (0, 0, 255))
    hp_txt = font.render("{}".format(Chosen.health), 1, (200, 50, 50))
    win.blit(hp_txt, (65, 35))
    win.blit(txt, (0, 10))

    # Character and Monsters
    Chosen.draw(win)
    inventory.draw(win)
    Skeleton.draw(win)
    Skeleton2.draw(win)

    # Items
    for bone in items:
        bone.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    for attack in attacks:
        attack.draw(win)
    pygame.display.update()


# Main Loop
def game_loop():
    spawn_time = 0
    attack_cool = 0

    run = True
    while run:
        win = pygame.display.set_mode((1536, 288))
        clock.tick(27)

        if spawn_time > 0:
            spawn_time += 1
        if spawn_time > 150:
            spawn_time = 0

        if Chosen.hitBox[1] < Skeleton.hitBox[1] + Skeleton.hitBox[3] and Chosen.hitBox[1] + Chosen.hitBox[3] > \
                Skeleton.hitBox[1]:
            if Chosen.hitBox[0] + Chosen.hitBox[2] > Skeleton.hitBox[0] and Chosen.hitBox[0] < Skeleton.hitBox[0] + \
                    Skeleton.hitBox[2]:
                if Skeleton.left:
                    Skeleton.x += 20

                elif Skeleton.right:
                    Skeleton.x -= 20
                Skeleton.walkCount += 1
                Skeleton.attack = True
                Chosen.hit()
        else:
            Skeleton.attack = False

        if attack_cool > 0:
            attack_cool += 1
        if attack_cool > 20:
            attack_cool = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Menu.game_intro()

        if Skeleton.drop:
            if len(items) < 1:
                items.append(Items.Item((Skeleton.x + Skeleton.width // 2), Skeleton.y + Skeleton.height // 2))
                Skeleton.drop = False

        # bullet: Projectile
        for bullet in bullets:
            if Skeleton.hitBox[1] + Skeleton.hitBox[3] > bullet.y > Skeleton.hitBox[1]:
                if Skeleton.hitBox[0] < bullet.x < Skeleton.hitBox[0] + Skeleton.hitBox[2]:
                    Skeleton.hit()
                    Skeleton.health -= 2
                    bullets.pop(bullets.index(bullet))

            if Chosen.x + 100 > bullet.x > Chosen.x - 100 and bullet.x > 0:
                Chosen.a_bow = False

            if 1500 > bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        for attack in attacks:
            if Skeleton.hitBox[1] + Skeleton.hitBox[3] > attack.y > Skeleton.hitBox[1]:
                if Skeleton.hitBox[0] < attack.x < Skeleton.hitBox[0] + Skeleton.hitBox[2]:
                    Skeleton.hit()
                    Skeleton.health -= 5
                    attacks.pop(attacks.index(attack))
                elif len(attacks) <= 0:
                    print("missed!")

            if Chosen.x + 75 > attack.x > Chosen.x - 75 and attack.x > 0:
                attack.x += attack.vel
                Chosen.a_attack = False
            else:
                if len(attacks) == 0:
                    print("missed!")
                elif len(attacks) > 0:
                    attacks.pop(attacks.index(attack))

        keys = pygame.key.get_pressed()

        # BOW ATTACK
        if keys[pygame.K_SPACE] and attack_cool == 0:
            bulletSound.play()
            Chosen.a_bow = True
            if Chosen.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 50:
                bullets.append(
                    Player.Projectile(round(Chosen.x + Chosen.width // 2), round(Chosen.y + Chosen.height // 2), facing))
                attack_cool = 1
            elif len(bullets) >= 50:
                Chosen.a_bow = False

        # SWORD ATTACK
        if keys[pygame.K_z] and attack_cool == 0:
            Chosen.a_attack = True
            if Chosen.left:
                facing = -1
            else:
                facing = 1
            if len(attacks) < 1:
                swordSound.play()
                attacks.append(Player.Swing(round(Chosen.x + Chosen.width // 2), round(Chosen.y + Chosen.height // 2), facing))
                attack_cool = 1
            else:
                Chosen.a_attack = False

        # MOVE LEFT
        if keys[pygame.K_LEFT] and Chosen.x > Chosen.vel:
            Chosen.x -= Chosen.vel
            Chosen.left = True
            Chosen.right = False
            Chosen.standing = False

        # MOVE RIGHT
        elif keys[pygame.K_RIGHT] and Chosen.x < screenWidth - Chosen.width - Chosen.vel:
            Chosen.x += Chosen.vel
            Chosen.right = True
            Chosen.left = False
            Chosen.standing = False
        else:
            Chosen.standing = True

        # PICK UP KEY
        if keys[pygame.K_x]:
            for bone in items:
                if Chosen.hitBox[1] < bone.x and Chosen.hitBox[1] + Chosen.hitBox[3] < bone.x:
                    if Chosen.hitBox[0] + Chosen.hitBox[2] > bone.x > Chosen.hitBox[0]:
                        print(items[0])
                        items.pop(items.index(bone))
                        inventory.objects.append(bone)
        # JUMP
        if not Chosen.isJump:
            if keys[pygame.K_UP]:
                Chosen.isJump = True
                Chosen.walkCount += 1
        else:
            if Chosen.jumpCount >= Chosen.j_land:
                neg = 1
                if Chosen.jumpCount < 0:
                    neg = -1
                Chosen.y -= (Chosen.jumpCount ** 2) * 0.5 * neg
                Chosen.jumpCount -= 1
            else:
                Chosen.isJump = False
                Chosen.jumpCount = 7

        if keys[pygame.K_ESCAPE]:
            Menu.game_intro()


        redraw_game_window()


Menu.game_intro()
game_loop()
pygame.quit()
