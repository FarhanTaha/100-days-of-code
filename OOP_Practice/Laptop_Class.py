# laptop Class (template/blueprint)
class Laptop:

    def __init__(self, brand, ram, storage, software):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.software = software

    def boot(self):
        print(f"{self.brand} is booting up")

    def shutdown(self):
        print(f"{self.brand} is shutting down")

    def upgrade_ram(self, new_ram):
        self.ram = new_ram
        print(f"{self.brand} RAM upgraded to {self.ram}")

    def installSoftware(self, new_software):
        self.software = new_software
        print(f"{self.software} has been installed on {self.brand}")

# Creating a Laptop Object (My Specifications/Uniqueness)
my_laptop = Laptop("Lenovo", "16GB", "512GB SSD", "VS code")


# Attributes and Methods of my Laptop
my_laptop.boot() # Method: boot up the laptop
print(my_laptop.ram) # Attribute: display current RAM (16GB)
my_laptop.upgrade_ram("32GB") # Method: upgrade RAM to 32GB
print(my_laptop.ram) # Attribute: display updated RAM
print(my_laptop.software) # Attribute: The previous software that was installed (VS code)
my_laptop.installSoftware("Figma") #  Method: Installing new software (FIGMA)
my_laptop.shutdown() # Method: shutdown the laptop
