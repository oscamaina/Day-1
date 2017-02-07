class Car(object):
    """Collection of methods of class car"""
    def __init__(self, name="General", model="GM", car_type="Honda"):
        """Intialising car class"""
        self.car_type = car_type
        self.model = model
        self.name = name
        self.speed = 0

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
         self.num_of_doors = 2
        else:
          self.num_of_doors = 4

        if self.car_type == "trailer":
          self.num_of_wheels = 8
        else:
          self.num_of_wheels = 4

    def is_saloon(self):
      if self.car_type == 'trailer':
        return False
      else:
        return True

    def drive(self, speed):
        if self.car_type == 'trailer':
            if speed != 0:
                speeds = 11 * speed
            self.speed = speeds
            return self
        else:
            self.speed = 10 ** speed 
            return self
