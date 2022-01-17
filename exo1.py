import string


class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']
    
        

    def __init__(self, name):
        self.__name = name
        print('initialisation', format(self.__name))


    def eteint(self):
        self.__power=0
    def allumé(self):
        self.__power=1
    


    def stop(self):
        self.__current_speed=0
    def move(self,speed):
        if type(speed)== int:
            self.__current_speed=speed
    def speed(self):
        return self.__current_speed



    def vide (self):
        self.__battery_level=0
    def charge(self,charge):
        if type(charge)== int:
            self.__battery_level=charge
    def charge(self):
        return self.__battery_level

    def shutdown (self):
        self.power=0

        pass

    def running (self):
        self.power=1
        pass

monrobot=Robot("bob")