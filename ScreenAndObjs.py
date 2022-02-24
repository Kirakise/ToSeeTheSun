import pygame
import Objects.Player as Pl
WIDTH = 360
HEIGHT = 480
BulletCount = 0
EnemyNum = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
objects = {"Player": Pl.Player()}
sprites = pygame.sprite.Group()