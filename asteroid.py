
import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.radius = radius
    
    def draw(self, surface):
        pygame.draw.circle(
            surface,
            "white",
            (self.position.x, self.position.y),
            self.radius,
            2
        )


    def update(self, dt):
        self.position.x += self.velocity.x*dt
        self.position.y += self.velocity.y*dt

    def split(self):
        
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        new_velocity1 = self.velocity.rotate(angle)*1.5
        new_velocity2 = self.velocity.rotate(-angle)*1.5

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1
    
        asteroid2 = Asteroid(self.position.x,self.position.y, new_radius)
        asteroid2.velocity = new_velocity2

