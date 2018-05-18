class Player(object):
    name = ""
    team = ""
    postition = ""
    city = ""
    state = ""
    twitter = ""

    def __init__(self, name, team, postition, city, state):
        self.name = name
        self.team = team
        self.postition = postition
        self.city = city
        self.state = state        

    def __str__(self):
        return self.name