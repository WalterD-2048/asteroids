from circleshape import *
from constants import *
from random import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius , 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        random_angle = uniform(20, 50)
        newV1 = self.velocity.rotate(random_angle) * 1.2
        newV2 = self.velocity.rotate(-random_angle) * 1.2
        newRadius = self.radius - ASTEROID_MIN_RADIUS

        newA1 = Asteroid(self.position.x, self.position.y, newRadius) 
        newA1.velocity = newV1
        newA2 = Asteroid(self.position.x, self.position.y, newRadius)
        newA2.velocity = newV2

        for group in self.groups():
             group.add(newA1)
             group.add(newA2)
        



    



    
    

