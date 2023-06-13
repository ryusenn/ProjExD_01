import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img01 = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img02 = pg.transform.flip(bg_img01,True,False)
    kk_img_1 = pg.image.load("ex01/fig/3.png")
    kk_img_1 = pg.transform.flip(kk_img_1,True,False)
    kk_img_2= pg.transform.rotozoom(kk_img_1,3,1.0)
    kk_img_3 = pg.transform.rotozoom(kk_img_1,6,1.0)
    kk_img_4 = pg.transform.rotozoom(kk_img_1,9,1.0)
    kk_imgs = [kk_img_1,kk_img_2,kk_img_3,kk_img_4]

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1

        if tmr == 3200:
            tmr = 0
        screen.blit(bg_img01, [-tmr, 0])
        screen.blit(bg_img02,[1600-tmr,0])
        screen.blit(bg_img01,[3200-tmr,0])

        screen.blit(kk_imgs[tmr%4],[300,200])
        
        pg.display.update()       
        clock.tick(1000)

   


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()