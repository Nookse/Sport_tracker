class create_user:
    def __init__(self, name : str, age : int, height : int , weight : int , ID : int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.ID = ID

if __name__ == "__main__":
    theo = create_user('theo', 21, 174, 70, 22)
    print(theo.name)
    print(theo.height)
    print(theo.ID)
