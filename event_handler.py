import pygame as py

def handle_events(display, single_blur_pos, multi_blur_pos, buttons, buttons_max, single, single_blur, multi, multi_blur):
    click = False
    for event in py.event.get():
        if event.type == py.QUIT:
            return False, buttons, single_blur, multi_blur, False

        elif event.type == py.KEYDOWN:
            if (event.key == py.K_LEFT) and ((buttons - 1) >= 0):
                click = True
                buttons -= 1

            elif (event.key == py.K_RIGHT) and ((buttons + 1) < buttons_max):
                click = True
                buttons += 1

            elif event.key == py.K_RETURN:
                if buttons == 0:
                    display.fill((0, 0, 0))
                elif buttons == 1:
                    display.fill((0, 0, 0))


        if event.type == py.MOUSEBUTTONDOWN:
            if py.mouse.get_pressed()[0]:
                print("s")


        if single_blur_pos.collidepoint(py.mouse.get_pos()):
            return True, buttons, single, multi_blur, False
        elif multi_blur_pos.collidepoint(py.mouse.get_pos()):
            return True, buttons, single_blur, multi, False


    return True, buttons, single_blur, multi_blur, click
