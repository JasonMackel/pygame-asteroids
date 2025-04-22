# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import * 
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Shot.containers = (shots, updateable,drawable)
    AsteroidField.containers = (updateable)
    Asteroid.containers = (asteroids,updateable,drawable)
    Player.containers = (updateable,drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
   
    dt = 0

    while True:
        
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()


        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
      


if __name__ == "__main__":
    main()