from genericpath import isfile
import os
import pygame


textures={}
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
__names={}
for __i in os.listdir(path+"/ressource"):
    if isfile(path+"/ressource/"+__i):
        __names[__i[:-len(__i.split('.')[-1])-1]]=__i


def loadTextures():
    for __i in __names.keys():
        textures[__i]=pygame.transform.scale(pygame.image.load(path+"/ressource/"+__names[__i]),(160,160))
    __names.clear()




