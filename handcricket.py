#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import time
import random
import sys
pygame.init()
pygame.font.init()

cricket = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Hand Cricket')
fpsController = pygame.time.Clock()
bg = pygame.image.load('stadium.jpg')
bgRect = bg.get_rect()


def end(userscore, computerscore):
    cricket = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Hand Cricket')
    fpsController = pygame.time.Clock()
    bg = pygame.image.load('end.jpg')
    bg = pygame.transform.scale(bg, (1280, 720))
    bgRect = bg.get_rect()
    cricket.fill(pygame.Color(255, 255, 255))
    cricket.blit(bg, bgRect)
    pygame.display.update()
    pygame.display.flip()
    fpsController.tick(10)
    while True:
        if userscore > computerscore:
            cricket.blit(pygame.font.SysFont('arial',
                         50).render('YOU WON!', 1, (0, 0, 255)), (475,
                         350))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
        if userscore < computerscore:
            cricket.blit(pygame.font.SysFont('arial',
                         50).render('YOU LOST!', 1, (0, 0, 255)), (475,
                         350))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
        if userscore == computerscore:
            cricket.blit(pygame.font.SysFont('arial',
                         50).render('MATCH TIED!', 1, (0, 0, 255)),
                         (475, 350))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
        cricket.fill(pygame.Color(255, 255, 255))
        cricket.blit(bg, bgRect)
        pygame.display.update()
        pygame.display.flip()
        fpsController.tick(10)


def user_bat(target=100000):
    cricket = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Hand Cricket')
    fpsController = pygame.time.Clock()
    bg = pygame.image.load('stadium.jpg')
    bgRect = bg.get_rect()
    runs = 0
    wickets = 0
    bowl = 0

    def runs_wickets(r, w):
        sFont = pygame.font.SysFont('arial', 40)
        ssurf = sFont.render(' Runs :{0}'.format(r), True,
                             pygame.Color(0, 0, 0))
        ssurf1 = sFont.render(' Wickets :{0}'.format(w), True,
                              pygame.Color(0, 0, 0))
        srect1 = ssurf1.get_rect()
        srect1.midtop = (600, 100)
        srect = ssurf.get_rect()
        srect.midtop = (600, 70)
        cricket.blit(ssurf, srect)
        cricket.blit(ssurf1, srect1)

    def batsman(r):
        sFont = pygame.font.SysFont('arial', 70)
        ssurf = sFont.render('Batsman: {0}'.format(r), True,
                             pygame.Color(0, 0, 0))
        srect = ssurf.get_rect()
        srect.midtop = (990, 50)
        cricket.blit(ssurf, srect)

    def bowler(r):
        sFont = pygame.font.SysFont('arial', 70)
        ssurf = sFont.render('Bowler: {0}'.format(r), True,
                             pygame.Color(0, 0, 0))
        srect = ssurf.get_rect()
        srect.midtop = (250, 50)
        cricket.blit(ssurf, srect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                computer_input = random.randrange(0, 7)
                left_list = [
                    'l0.jpg',
                    'l1.jpg',
                    'l2.jpg',
                    'l3.jpg',
                    'l4.jpg',
                    'l5.jpg',
                    'l6.jpg',
                    ]
                left_list = list(map(lambda x: pygame.image.load(x),
                                left_list))
                left_list = list(map(lambda x: pygame.transform.scale(x,
                                (128, 128)), left_list))
                right_list = [
                    'r0.jpg',
                    'r1.jpg',
                    'r2.jpg',
                    'r3.jpg',
                    'r4.jpg',
                    'r5.jpg',
                    'r6.jpg',
                    ]
                right_list = list(map(lambda x: pygame.image.load(x),
                                 right_list))
                right_list = list(map(lambda x: pygame.transform.scale(x,
                                 (128, 128)), right_list))

                if event.key == pygame.K_0:
                    user_input = 0
                if event.key == pygame.K_1:
                    user_input = 1
                if event.key == pygame.K_2:
                    user_input = 2
                if event.key == pygame.K_3:
                    user_input = 3
                if event.key == pygame.K_4:
                    user_input = 4
                if event.key == pygame.K_5:
                    user_input = 5
                if event.key == pygame.K_6:
                    user_input = 6
                cricket.blit(left_list[computer_input], (200, 150))
                cricket.blit(right_list[user_input], (950, 150))
                bat = user_input
                bowl = computer_input

                if bat == bowl:
                    wickets += 1
                    myFont = pygame.font.SysFont('arial', 100)
                    Osurf = myFont.render('OUT', True,
                            pygame.Color(255, 0, 0))
                    Orect = Osurf.get_rect()
                    Orect.midtop = (600, 250)
                    cricket.blit(Osurf, Orect)
                    pygame.display.flip()
                    time.sleep(1)
                    if wickets >= 5:
                        return runs
                elif bat == 0:

                    runs += bowl
                elif bat != bowl:
                    runs += bat
                batsman(bat)
                bowler(bowl)
                pygame.display.update()
                time.sleep(1)
                if runs > target:
                    return runs
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        cricket.fill(pygame.Color(255, 255, 255))
        cricket.blit(bg, bgRect)
        batsman('_')
        bowler('_')
        runs_wickets(runs, wickets)
        pygame.display.update()
        pygame.display.flip()
        fpsController.tick(10)


def user_bowl(target=100000):
    cricket = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Hand Cricket')
    fpsController = pygame.time.Clock()
    bg = pygame.image.load('stadium.jpg')
    bgRect = bg.get_rect()
    runs = 0
    wickets = 0
    bowl = 0

    def runs_wickets(r, w):
        sFont = pygame.font.SysFont('arial', 40)
        ssurf = sFont.render(' Runs :{0}'.format(r), True,
                             pygame.Color(0, 0, 0))
        ssurf1 = sFont.render(' Wickets :{0}'.format(w), True,
                              pygame.Color(0, 0, 0))
        srect1 = ssurf1.get_rect()
        srect1.midtop = (600, 100)
        srect = ssurf.get_rect()
        srect.midtop = (600, 70)
        cricket.blit(ssurf, srect)
        cricket.blit(ssurf1, srect1)

    def batsman(r):
        sFont = pygame.font.SysFont('arial', 70)
        ssurf = sFont.render('Batsman: {0}'.format(r), True,
                             pygame.Color(0, 0, 0))
        srect = ssurf.get_rect()
        srect.midtop = (250, 50)
        cricket.blit(ssurf, srect)

    def bowler(r):
        sFont = pygame.font.SysFont('arial', 70)
        ssurf = sFont.render('Bowler: {0}'.format(r), True,
                             pygame.Color(0, 0, 0))
        srect = ssurf.get_rect()
        srect.midtop = (990, 50)
        cricket.blit(ssurf, srect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                computer_input = random.randrange(0, 7)
                left_list = [
                    'l0.jpg',
                    'l1.jpg',
                    'l2.jpg',
                    'l3.jpg',
                    'l4.jpg',
                    'l5.jpg',
                    'l6.jpg',
                    ]
                left_list = list(map(lambda x: pygame.image.load(x),
                                left_list))
                left_list = list(map(lambda x: pygame.transform.scale(x,
                                (128, 128)), left_list))
                right_list = [
                    'r0.jpg',
                    'r1.jpg',
                    'r2.jpg',
                    'r3.jpg',
                    'r4.jpg',
                    'r5.jpg',
                    'r6.jpg',
                    ]
                right_list = list(map(lambda x: pygame.image.load(x),
                                 right_list))
                right_list = list(map(lambda x: pygame.transform.scale(x,
                                 (128, 128)), right_list))

                if event.key == pygame.K_0:
                    user_input = 0
                if event.key == pygame.K_1:
                    user_input = 1
                if event.key == pygame.K_2:
                    user_input = 2
                if event.key == pygame.K_3:
                    user_input = 3
                if event.key == pygame.K_4:
                    user_input = 4
                if event.key == pygame.K_5:
                    user_input = 5
                if event.key == pygame.K_6:
                    user_input = 6
                cricket.blit(left_list[computer_input], (200, 150))
                cricket.blit(right_list[user_input], (950, 150))
                bat = computer_input
                bowl = user_input
                if bat == bowl:
                    wickets += 1
                    myFont = pygame.font.SysFont('arial', 100)
                    Osurf = myFont.render('OUT', True,
                            pygame.Color(255, 0, 0))
                    Orect = Osurf.get_rect()
                    Orect.midtop = (600, 250)
                    cricket.blit(Osurf, Orect)
                    pygame.display.flip()
                    time.sleep(1)
                    if wickets >= 5:
                        return runs
                elif bat == 0:

                    runs += bowl
                elif bat != bowl:
                    runs += bat
                batsman(bat)
                bowler(bowl)
                pygame.display.update()
                time.sleep(1)
                if runs > target:
                    return runs
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        cricket.fill(pygame.Color(255, 255, 255))
        cricket.blit(bg, bgRect)
        batsman('_')
        bowler('_')
        runs_wickets(runs, wickets)
        pygame.display.update()
        pygame.display.flip()
        fpsController.tick(10)


def toss():
    cricket = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Hand Cricket')
    fpsController = pygame.time.Clock()
    bg = pygame.image.load('toss.jpg')
    bg = pygame.transform.scale(bg, (1280, 720))
    bgRect = bg.get_rect()
    cricket.fill(pygame.Color(255, 255, 255))
    cricket.blit(bg, bgRect)
    pygame.display.flip()
    fpsController.tick(10)
    cricket.blit(pygame.font.SysFont('arial', 50).render('Toss:', 1,
                 pygame.Color(255, 0, 0)), (0, 0))
    cricket.blit(pygame.font.SysFont('arial',
                 50).render('1.Choose Odd or Even (o or e)', 1, (0, 0,
                 0)), (0, 75))
    pygame.display.update()
    time.sleep(2)
    oddoreven = ''
    userchoice = ''
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    cricket.blit(pygame.font.SysFont('arial',
                                 50).render('5.You chose to bat', 1,
                                 (0, 0, 0)), (0, 375))
                    pygame.display.update()
                    time.sleep(2)
                    userscore = user_bat()
                    cricket.blit(pygame.font.SysFont('arial',
                                 50).render('INNINGS COMPLETED', 1, (0,
                                 0, 255)), (375, 350))
                    pygame.display.update()
                    time.sleep(2)
                    computerscore = user_bowl(userscore)
                    count += 1
                    break
                if event.key == pygame.K_f:
                    cricket.blit(pygame.font.SysFont('arial',
                                 50).render('5.You chose to field', 1,
                                 (0, 0, 0)), (0, 375))
                    pygame.display.update()
                    time.sleep(2)
                    computerscore = user_bowl()
                    cricket.blit(pygame.font.SysFont('arial',
                                 50).render('INNINGS COMPLETED', 1, (0,
                                 0, 255)), (375, 350))
                    pygame.display.update()
                    time.sleep(2)
                    userscore = user_bat(computerscore)
                    count += 1
                    break
                elif oddoreven == 'e' or oddoreven == 'o':
                    if event.key == pygame.K_0:
                        user_input = 0
                    elif event.key == pygame.K_1:
                        user_input = 1
                    elif event.key == pygame.K_2:
                        user_input = 2
                    elif event.key == pygame.K_3:
                        user_input = 3
                    elif event.key == pygame.K_4:
                        user_input = 4
                    elif event.key == pygame.K_5:
                        user_input = 5
                    elif event.key == pygame.K_6:
                        user_input = 6

                    computer_input = random.randrange(0, 7)
                    cricket.blit(pygame.font.SysFont('arial',
                                 50).render('3.You:' + str(user_input)
                                 + ',Computer:' + str(computer_input),
                                 1, (0, 0, 0)), (0, 225))
                    pygame.display.update()
                    time.sleep(2)
                    if (computer_input + user_input) % 2 == 0 \
                        and oddoreven == 'o':
                        c = random.randrange(1, 3)
                        if c == 1:
                            cricket.blit(pygame.font.SysFont('arial',
                                    50).render('4.You lost, Computer chose to bowl'
                                    , 1, (0, 0, 0)), (0, 300))
                            pygame.display.update()
                            time.sleep(2)
                            userscore = user_bat()
                            cricket.blit(pygame.font.SysFont('arial',
                                    50).render('INNINGS COMPLETED', 1,
                                    (0, 0, 255)), (375, 350))
                            pygame.display.update()
                            time.sleep(2)
                            computerscore = user_bowl(userscore)
                        elif c == 2:
                            cricket.blit(pygame.font.SysFont('arial',
                                    50).render('4.You lost, Computer chose to bat'
                                    , 1, (0, 0, 0)), (0, 300))
                            pygame.display.update()
                            time.sleep(2)
                            computerscore = user_bowl()
                            cricket.blit(pygame.font.SysFont('arial',
                                    50).render('INNINGS COMPLETED', 1,
                                    (0, 0, 255)), (375, 350))
                            pygame.display.update()
                            time.sleep(2)
                            userscore = user_bat(computerscore)
                        count += 1
                        break
                    elif (computer_input + user_input) % 2 == 1 \
                        and oddoreven == 'e':
                        c = random.randrange(1, 3)
                        if c == 1:
                            cricket.blit(pygame.font.SysFont('arial',
                                    50).render('4.You lost, Computer chose to bowl'
                                    , 1, (0, 0, 0)), (0, 300))
                            pygame.display.update()
                            time.sleep(2)
                            userscore = user_bat()
                            cricket.blit(pygame.font.SysFont('arial',
                                    50).render('INNINGS COMPLETED', 1,
                                    (0, 0, 255)), (375, 350))
                            pygame.display.update()
                            time.sleep(2)
                            computerscore = user_bowl(userscore)
                        if c == 2:
                            cricket.blit(pygame.font.SysFont('arial',
                                    50).render('4.You lost, Computer chose to bat'
                                    , 1, (0, 0, 0)), (0, 300))
                            pygame.display.update()
                            time.sleep(2)
                            computerscore = user_bowl()
                            cricket.blit(pygame.font.SysFont('arial',
                                    50).render('INNINGS COMPLETED', 1,
                                    (0, 0, 255)), (375, 350))
                            pygame.display.update()
                            time.sleep(2)
                            userscore = user_bat(computerscore)
                        count += 1
                        break
                    elif (computer_input + user_input) % 2 == 1 \
                        and oddoreven == 'o':
                        cricket.blit(pygame.font.SysFont('arial',
                                50).render('4.You won the toss :Bat(b) or Field(f)'
                                , 1, (0, 0, 0)), (0, 300))
                        pygame.display.update()
                        time.sleep(2)
                        continue
                    elif (computer_input + user_input) % 2 == 0 \
                        and oddoreven == 'e':
                        cricket.blit(pygame.font.SysFont('arial',
                                50).render('4.You won the toss :Bat(b) or Field(f)'
                                , 1, (0, 0, 0)), (0, 300))
                        pygame.display.update()
                        time.sleep(2)
                        continue
                if event.key == pygame.K_e:
                    oddoreven = 'e'
                    cricket.blit(pygame.font.SysFont('arial',
                                 50).render('2.Enter a num(0 to 6)', 1,
                                 (0, 0, 0)), (0, 150))
                    pygame.display.update()
                    time.sleep(2)
                if event.key == pygame.K_o:
                    oddoreven = 'o'
                    cricket.blit(pygame.font.SysFont('arial',
                                 50).render('2.Enter a num(0 to 6)', 1,
                                 (0, 0, 0)), (0, 150))
                    pygame.display.update()
                    time.sleep(2)
        if count == 1:
            break
    return [userscore, computerscore]


lst = toss()
end(lst[0], lst[1])

