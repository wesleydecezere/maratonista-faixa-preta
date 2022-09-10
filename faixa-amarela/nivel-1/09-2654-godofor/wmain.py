class Character:
    def __init__(self, props):
        self.name = props[0]
      
        values = [int(x) for x in props[1:]]     
        self.power = values[0]
        self.gods = values[1]
        self.deaths = values[2]


n = int(input())

for _ in range(n):
    c = Character(input().split())
    print(c.power)

    
