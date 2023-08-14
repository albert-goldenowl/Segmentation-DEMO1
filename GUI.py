import pygame
from config import frameshape
import cv2
import numpy as np
import onnxruntime as ort
import pygame_gui
from pygame_gui.elements import UIButton
from pygame_gui.windows import UIColourPickerDialog

target_shape = (256, 256, 3)
frame_shape = frameshape
half_width = target_shape[0] // 2
half_height = target_shape[1] // 2
x0 = frame_shape[0] // 2 - half_width
y0 = frame_shape[1] // 2 - half_height
x1 = frame_shape[0] // 2 + half_width
y1 = frame_shape[1] // 2 + half_height



ort_session = ort.InferenceSession('model.onnx')
input_name = ort_session.get_inputs()[0].name
output_name = ort_session.get_outputs()[0].name
def create_img(mask_output):
    r = np.zeros((256, 256), dtype=np.uint8)
    g = np.zeros((256, 256), dtype=np.uint8)
    b = np.zeros((256, 256), dtype=np.uint8)
    r[mask_output == 1] = 250
    r[mask_output == 2] = 36
    r[mask_output == 3] = 42
    r[mask_output == 4] = 115

    g[mask_output == 1] = 50
    g[mask_output == 2] = 179
    g[mask_output == 3] = 125
    g[mask_output == 4] = 51

    b[mask_output == 1] = 83
    b[mask_output == 2] = 83
    b[mask_output == 3] = 209
    b[mask_output == 4] = 128

    output = np.stack([b, g, r], axis=-1)
    return output
def create_img_bg(roi, mask_output):
    b, g, r = cv2.split(roi)
    r[mask_output == 1] = 250
    r[mask_output == 2] = 36
    r[mask_output == 3] = 42
    r[mask_output == 4] = 115

    g[mask_output == 1] = 50
    g[mask_output == 2] = 179
    g[mask_output == 3] = 125
    g[mask_output == 4] = 51

    b[mask_output == 1] = 83
    b[mask_output == 2] = 83
    b[mask_output == 3] = 209
    b[mask_output == 4] = 128

    output = np.stack([b, g, r], axis=-1)
    return output

pygame.init()
width = frameshape[0]
height = frameshape[1]
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shape Segmentation')
ui_manager = pygame_gui.UIManager((width, height))
fps = 30
clock = pygame.time.Clock()
start = True
white = (255, 0, 255)
dark_green = (152, 238, 204)
light_green = (208, 245, 190)
font = pygame.font.Font(None, 35)
start_text = font.render('Start', True, white)
setting_text = font.render('Setting', True, white)
quit_text = font.render('Quit', True, white)
back_text = font.render('Back', True, white)
rgb_square_text = font.render('Change color of Square', True, white)
rgb_circle_text = font.render('Change color of Circle', True, white)
rgb_triangle_text = font.render('Change color of Triangle', True, white)
rgb_star_text = font.render('Change color of Star', True, white)

quit_text_rect = quit_text.get_rect(center=(width // 2, 320))
start_text_rect = start_text.get_rect(center=(width // 2, 220))
setting_text_rect = setting_text.get_rect(center=(width // 2, 270))
back_text_rect = back_text.get_rect(center=(width // 2, 270))

rgb_square_rect = rgb_square_text.get_rect(center=(width // 2, 60))


start_menu = False
cam_menu = False
setting_menu = True

rgb_square = (250, 50, 83) #1
rgb_circle = (36, 179, 83) #2
rgb_triangle = (42, 125, 209) #3
rgb_star = (115, 51, 128) #4


# cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

while start:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and start_menu == True:
            if width // 2 - 70 <= mouse[0] <= width // 2 - 70 + 140 and 200 <= mouse[1] <= 240:
                cam_menu = True

                start_menu = False
            elif width // 2 - 70 <= mouse[0] <= width // 2 - 70 + 140 and 250 <= mouse[1] <= 290:
                cam_menu = False
                setting_menu = True

            elif width // 2 - 70 <= mouse[0] <= width // 2 - 70 + 140 and 300 <= mouse[1] <= 340:
                # start = False
                cam_menu = False
                # cam.release()
                pygame.quit()
        if setting_menu == True and event.type == pygame.MOUSEBUTTONDOWN:
            if width // 2 - 150 <= mouse[0] <= width // 2 - 150 + 300 and 40 <= mouse[1] <= 80:
                color_picker = UIColourPickerDialog(pygame.Rect(30, 30, 400, 400), ui_manager, window_title='Change color of Square')
                print(color_picker)
        ui_manager.process_events(event)
    if start_menu:
        window.fill((251, 255, 220))
        if width // 2 - 70 <= mouse[0] <= width // 2 - 70 + 140 and 200 <= mouse[1] <= 240:
            pygame.draw.rect(window, light_green, [width / 2 - 70, 200, 140 ,40], border_radius=5)
        else:
            pygame.draw.rect(window, dark_green, [width / 2 - 70, 200, 140 ,40], border_radius=5)

        if width // 2 - 70 <= mouse[0] <= width // 2 - 70 + 140 and 250 <= mouse[1] <= 290:
            pygame.draw.rect(window, light_green, [width / 2 - 70, 250, 140 ,40], border_radius=5)
        else:
            pygame.draw.rect(window, dark_green, [width / 2 - 70, 250, 140 ,40], border_radius=5)

        if width // 2 - 70 <= mouse[0] <= width // 2 - 70 + 140 and 300 <= mouse[1] <= 340:
            pygame.draw.rect(window, light_green, [width / 2 - 70, 300, 140 ,40], border_radius=5)
        else:        
            pygame.draw.rect(window, dark_green, [width / 2 - 70, 300, 140 ,40], border_radius=5)
        window.blit(quit_text, quit_text_rect)
        window.blit(start_text, start_text_rect)
        window.blit(setting_text, setting_text_rect)
    if cam_menu:
        
        pass
        # ret, frame = cam.read()
        # frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)



        # frame_rgb = np.rot90(frame_rgb)
        # frame = pygame.surfarray.make_surface(frame_rgb).convert()
        # frame = pygame.transform.flip(frame, True, False)
        # window.blit(frame, (0, 0))
    if setting_menu:

        window.fill((251, 255, 220))
        pygame.draw.rect(window, rgb_square, (30, 30, 90, 90)) 
        pygame.draw.circle(window, rgb_circle, (75, 190), 45)
        pygame.draw.polygon(window, rgb_triangle, ((75, 260), (30, 340), (120, 340)))
        pygame.draw.polygon(window, rgb_star, ((75, 350), (60, 380), (20, 380), (50, 400), (40, 430), (75, 410), (110, 430),
                                               (100, 400), (130, 380), (90, 380)))
        if width // 2 - 150 <= mouse[0] <= width // 2 - 150 + 300 and 40 <= mouse[1] <= 80:
            pygame.draw.rect(window, light_green, [width / 2 - 150, 40, 300 ,40], border_radius=5)

        else:
            pygame.draw.rect(window, dark_green, [width / 2 - 150, 40, 300 ,40], border_radius=5)
        window.blit(rgb_square_text, rgb_square_rect)




    pygame.display.update()
    clock.tick(fps)

