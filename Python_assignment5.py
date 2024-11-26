
class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.__battery_level = battery_level  

    def turn_on(self):
        print(f"{self.brand} {self.model} is now ON.")

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def charge(self, amount):
        self.__battery_level += amount
        if self.__battery_level > 100:
            self.__battery_level = 100
        print(f"{self.brand} {self.model} is charged to {self.__battery_level}%.")

    def get_battery_level(self):
        return self.__battery_level  

class CameraPhone(Smartphone):
    def __init__(self, brand, model, battery_level, camera_resolution):
        super().__init__(brand, model, battery_level)
        self.camera_resolution = camera_resolution 

    def take_photo(self):
        print(f"Taking a photo with {self.brand} {self.model}'s {self.camera_resolution} MP camera.")

    def charge(self, amount):
        self.__battery_level += amount
        if self.__battery_level > 90:  
            self.__battery_level = 90
        print(f"{self.brand} {self.model} CameraPhone is charged to {self.__battery_level}%. Max is 90%.")

phone1 = Smartphone("Samsung", "Galaxy S21", 50)
phone1.turn_on()
phone1.make_call("123-456-7890")
phone1.charge(30)
print(f"Battery Level: {phone1.get_battery_level()}%\n")
phone2 = CameraPhone("Apple", "iPhone 13", 70, 12)
phone2.turn_on()
phone2.make_call("987-654-3210")
phone2.take_photo()
phone2.charge(20)
print(f"Battery Level: {phone2.get_battery_level()}%\n")
