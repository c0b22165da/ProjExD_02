import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900
idou={pg.K_UP:(0,-5),
      pg.K_LEFT:(-5,0),
      pg.K_RIGHT:(5,0),
      pg.K_DOWN:(0,5)}


def check_idou(x):
    yoko=True
    tate=True
    if x.top < 0 or x.bottom > HEIGHT:
        tate=False
    if x.right > WIDTH or x.left < 0:
        yoko=False

    return yoko,tate


accs=[a for a in range(1,11)]


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img_over = pg.image.load("ex02/fig/8.png")
    kk_img_overz = pg.transform.rotozoom(kk_img_over, 0, 2.0)
    kk_img_t=pg.transform.flip(kk_img,True,False)
    kk_img_shoumen = pg.transform.rotozoom(kk_img_t, 0, 2.0)
    kk_img_migiue = pg.transform.rotozoom(kk_img_t, 45, 2.0)
    kk_img_ue = pg.transform.rotozoom(kk_img_t, 90, 2.0)
    kk_img_hidariue = pg.transform.rotozoom(kk_img, -45, 2.0)
    kk_img_gyaku = pg.transform.rotozoom(kk_img,0, 2.0)
    kk_img_hidarisita = pg.transform.rotozoom(kk_img, 45, 2.0)
    kk_img_sita = pg.transform.rotozoom(kk_img, 90, 2.0)
    kk_img_migisita = pg.transform.rotozoom(kk_img_t, -45, 2.0)
    kk_muki={(5,0):kk_img_shoumen,
             (5,-5):kk_img_migiue,
             (0,-5):kk_img_ue,
             (-5,-5):kk_img_hidariue,
             (-5,0):kk_img_gyaku,
             (-5,5):kk_img_hidarisita,
             (0,5):kk_img_sita,
             (5,5):kk_img_migisita,
             (0,0):kk_img_shoumen}
    kk_rct=kk_img.get_rect()
    kk_rct.center=(900,400)
    clock = pg.time.Clock()
    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))#黒をすかす
    tmr = 0
    img_rct=(enn.get_rect())
    x=random.randint(0,WIDTH)
    y=random.randint(0,HEIGHT)
    img_rct.center=(x,y)
    vx,vy=5,5
    font = pg.font.Font(None, 80)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(img_rct)==True:
            screen.blit(bg_img,[0,0])
            screen.blit(kk_img_overz, kk_rct)
            pg.display.update()
            clock.tick(1)
            return
        avx,avy=vx*accs[min(tmr//500,9)],vy*accs[min(tmr//500,9)]


        screen.blit(bg_img, [0, 0])
        key_lst=pg.key.get_pressed()
        goukei=[0,0]
        for key,mv in idou.items():
            if key_lst[key]:
                goukei[0]+=mv[0]
                goukei[1]+=mv[1]
        kk_rct.move_ip(goukei)
        if check_idou(kk_rct) != (True,True):
            kk_rct.move_ip(-goukei[0], -goukei[1])
        screen.blit(kk_muki[tuple(goukei)], kk_rct)
        img_rct.move_ip(avx,avy)
        yoko,tate=check_idou(img_rct)
        if not yoko:
            vx*=-1
        if not tate:
            vy*=-1
        screen.blit(enn,img_rct)
        txt = font.render(str(tmr//30), True, (255, 255, 255))
        screen.blit(txt, [1400, 800])
        pg.display.update()
        tmr += 1
        clock.tick(30)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()