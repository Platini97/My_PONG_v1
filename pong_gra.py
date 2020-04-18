#Gra PONG
#Piła odbija się od 3 ścian lub paletki
#jeśli odbije się od dolnego podłoża to przegrywasz

from superwires import games, color
import random
games.init(screen_width=640,screen_height=480,fps=50)

class Rocket(games.Sprite):
    """Rakieta do odbijania piłki"""

    image = games.load_image("rakieta_pong.png")
    def __init__(self):
        """Inicjalizuje rakietę"""
        super(Rocket, self).__init__(image = Rocket.image,
                                    x = games.mouse.x,
                                    bottom = games.screen.height)
        self.score = games.Text(value=0, size=60, color=color.white,
                                top=5, right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        """Zmień pozycję X myszy"""

        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """Sprawdź czy gracz odbił piłkę"""
        for ball in self.overlapping_sprites:
            self.score.value += 1
            self.score.right = games.screen.width - 10

            ball.handle_caught()




class Ball(games.Sprite):
    """Piłka do gry"""
    image = games.load_image("pilka_pong.png")
    speed = 8
    points = 0
    change = False



    def __init__(self):
        """Inicjaluzuję piłkę"""
        super(Ball, self).__init__(image = Ball.image,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    dy = Ball.speed,
                                    dx =  Ball.speed)

        self.score = games.Text(value=0, size=60, color=color.white,
                                x = games.screen.width/2+110,
                                y = games.screen.height/2)






    def update(self):
        """Sprawdź czy dolny brzeg piłki dotknął dołu ekranu"""
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
        elif self.right > games.screen.width:
            self.dx = -self.dx
            self.change = False
        elif self.left < 0:
            self.dx = -self.dx
            self.change = True
        elif self.top < 0:
            self.dy = -self.dy




    def handle_caught(self):
        """Odbicie piłki jeśli dotknął"""
        if self.change == True:
            self.dx = random.randrange(10, 15) * (1)
        else:
            self.dx = random.randrange(10, 15) * (-1)
        self.dy = random.randrange(10, 15) * (-1)
        self.score.value += 1




    def end_game(self):
        """Koniec gry"""
        end_message = games.Message(value = "Koniec gry: ",
                                    size = 45,
                                    color = color.white,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)
        games.screen.add(self.score)


def main():
    the_ball = Ball()
    games.screen.add(the_ball)

    the_rocket = Rocket()
    games.screen.add(the_rocket)

    games.mouse.is_visible = False

    games.screen.event_grab = True
    games.screen.mainloop()


# start programu
main()



















