class Snake(Character):
    def __init__(self):
        Character.__init__(self)
        self.run = [join('games', 'ssb', 'snake', 'runright.png'), join('games', 'ssb', 'snake', 'runleft.png')]
        self.gun = [join('games', 'ssb', 'snake', 'gunright.png'), join('games', 'ssb', 'snake', 'gunleft.png')]
        self.idle = [join('games', 'ssb', 'snake', 'idleright.png'), join('games', 'ssb', 'snake', 'idleleft.png')]
        self.image, self.rect = _load_image(self.idle[0], 0, 0)
        self.reloadtime = 1500
        self.projectilecount = 2
        self.projectilesound = pygame.mixer.Sound(join('games', 'ssb', 'snake', 'gun.ogg'))
        self.jumpsounds =  [pygame.mixer.Sound(join('games', 'ssb', 'snake', 'huh.ogg')),
        self.jumpsounds =  [pygame.mixer.Sound(join('games', 'ssb', 'snake', 'hah.ogg')),

   

    def make_projectile(self, x, y, charac):
        if charac.direct == 'right':
            self.projectile = snake_Laser(x, y + 24)
            self.projectile.velocity = charac.projectile.velocity
        elif charac.direct == 'left':
            self.projectile = snake_Laser(x - 44, y + 24)
            self.projectile.velocity = charac.projectile.velocity * (-1)

    def projectile_logic(self):
        if (self.projectilecount == 0) and ((pygame.time.get_ticks() - self.no_projectile_time) >= self.reloadtime):
            self.projectilecount = 2