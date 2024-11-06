import pygame
import pygame as py
from event_handler import handle_events

py.init()

icon = py.image.load(r"C:\Users\moham\OneDrive\Desktop\Python\PacMan\Pics\Icon.png")
single = py.image.load(r"C:\Users\moham\OneDrive\Desktop\Python\PacMan\Pics\Single.png")
single_blur = py.image.load(r"C:\Users\moham\OneDrive\Desktop\Python\PacMan\Pics\Single - Copy.png")
multi = py.image.load(r"C:\Users\moham\OneDrive\Desktop\Python\PacMan\Pics\Multi.png")
multi_blur = py.image.load(r"C:\Users\moham\OneDrive\Desktop\Python\PacMan\Pics\Multi - Copy.png")


display = py.display.set_mode()
x_display, y_display = display.get_size()
py.display.set_icon(icon)
py.display.set_caption('PacMan')
x_single, y_single = single_blur.get_size()
single_pos = single.get_rect(center = (x_display / 4, y_display / 10 * 3))
x_multi, y_multi = multi_blur.get_size()
multi_pos = multi_blur.get_rect(center = (x_display / 4 * 3, y_display / 10 * 3))
multi2 = multi_blur



buttons_max = 2
buttons = 0
step_key = "Main-notouch"




running = True
while running:

    while step_key == "Main-notouch" and running:

        for event in py.event.get():
            if event.type == pygame.QUIT:
                running = False

        if x_single < 389:
            x_single = x_single * 1.0018
            y_single = y_single * 1.0018
            single2 = py.transform.scale(single_blur , (x_single, y_single))
            single_pos = single2.get_rect(center = (x_display / 4, y_display / 10 * 3))
        elif x_multi < 389:
            x_multi = x_multi * 1.003
            y_multi = y_multi * 1.003
            multi2 = py.transform.scale(multi_blur, (x_multi, y_multi))
            multi_pos = multi2.get_rect(center = (x_display / 4 *  3, y_display / 10 * 3))
        else:
            step_key = "Main-pageoption"

        display.blit(single2, single_pos)
        display.blit(multi2, multi_pos)
        py.display.update()


    while step_key == "Main-pageoption" and running:
        running, buttons, single2, multi2, click = handle_events(display, single_pos, multi_pos, buttons, buttons_max, single, single_blur, multi, multi_blur)
        if click == False:
            display.blit(single2, single_pos)
            display.blit(multi2, multi_pos)
        py.display.update()

py.display.quit()