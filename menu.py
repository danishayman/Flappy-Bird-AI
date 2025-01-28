import pygame
from variables import WIN_WIDTH, WIN_HEIGHT, STAT_FONT, BG_IMG

class Menu:
    def __init__(self):
        self.button_width = 200
        self.button_height = 50
        self.button_x = (WIN_WIDTH - self.button_width) // 2
        self.button_y = (WIN_HEIGHT - self.button_height) // 2
        self.button_rect = pygame.Rect(self.button_x, self.button_y, 
                                     self.button_width, self.button_height)
        self.button_color = (0, 200, 0)
        self.button_hover_color = (0, 255, 0)

    def draw_start_screen(self, win):
        win.blit(BG_IMG, (0, 0))
        
        # Hover effect
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.button_hover_color if self.button_rect.collidepoint(mouse_pos) \
            else self.button_color
        
        # Draw button
        pygame.draw.rect(win, current_color, self.button_rect)
        
        # Button text
        text = STAT_FONT.render("START GAME", True, (255, 255, 255))
        text_x = self.button_x + (self.button_width - text.get_width()) // 2
        text_y = self.button_y + (self.button_height - text.get_height()) // 2
        win.blit(text, (text_x, text_y))
        
        # Instructions
        instr_text = STAT_FONT.render("Click button or press SPACE", True, (255, 255, 255))
        win.blit(instr_text, (WIN_WIDTH//2 - instr_text.get_width()//2, self.button_y + 100))

    @staticmethod
    def check_start_trigger(events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
        return False