if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Press any key to start", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_widht, half_screen_height)
            self.screen.blit(text, text_rect)
        else:
            self.screen.blit(ICON, (half_screen_widht - 10, half_screen_height - 140))
            font = pygame.font.Font(FONT_STYLE, 22)

            ## mostrar a mensagem de "Press any key to restart
            text = font.render("Press any key to restart", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_widht, half_screen_height +20)
            self.screen.blit(text, text_rect)

            ## mostrar score atingido
            text = font.render (f"Score: {self.score}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_widht, half_screen_height +60)
            self.screen.blit(text, text_rect)

            ## mostrar death_count
            text = font.render (f"Death count: {self.death_count}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_widht, half_screen_height +95)
            self.screen.blit(text, text_rect)
            

            ##Criar metodo para remover a repetiçao de codigo para o texto

def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)