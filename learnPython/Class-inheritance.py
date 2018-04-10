#类的继承
class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'

class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False

summer = Chicken()

print('小鸡是否有翅膀:',summer.have_feather)

print('小鸡的行走方式：',summer.way_of_move)

crow  = Oriole()

print('乌鸦的繁殖方式:',crow.way_of_reproduction)

print('乌鸦的行走方式：',crow.way_of_move)