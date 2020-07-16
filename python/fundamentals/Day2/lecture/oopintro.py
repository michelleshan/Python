class Llama:
    def __init__(self, nameOfLlama, catchphrase, blades_of_grass_eaten, color, texture): #double underscores on both sides
        #ATTRIBUTES GO HERE (inside __init__ function)
        print("__init__ has run!")
        self.name = nameOfLlama
        self.catchphrase = catchphrase
        self.blades_of_grass_eaten = blades_of_grass_eaten
        self.owner = {"name": "Joey", "age": 29}
        self.color = color
        self.texture = texture

    #METHODS GO HERE (inside class)
    def say_info(self):
        print("My name is "+self.name)
        print("I have eaten "+str(self.blades_of_grass_eaten)+" blades of grass")
        return self

    def say_catchphrase(self):
        print(self.catchphrase)
        return self

    def owner_info(self):
        print("My owner's name is "+self.owner['name'])
        return self

    def bodyimage(self):
        print("My fur is "+self.color+" and the texture is "+self.texture)
        return self

#INSTANCES ARE MADE HERE (outside class)
jose = Llama("Jose","What it do?",17,"white","straight") #{name: "Jose"}
harold = Llama("Harold","Howdy",998,"brown","curly") #{name: "Harold"}
harold.say_catchphrase().say_info().bodyimage()
jose.owner_info()