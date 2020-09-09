# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.s_to = None
        self.w_to = None
        self.n_to = None
        self.e_to = None
        
    def __str__(self):
        output = f'{self.name}: {self.description}\n'
        if self.s_to:
            return output + '\n' + 'You have entered from ' + self.s_to.name + '\n'
        elif self.w_to:
            return output + '\n' + 'You have entered from ' + self.w_to.name + '\n'
        elif self.e_to:
            return output + '\n' + 'You have entered from ' + self.e_to.name + '\n'
        elif self.n_to:
            return output + '\n' + 'You have entered from ' + self.n_to.name + '\n'
        return output

    # def other_rooms(self, direction):
    #     if direction == 'n':
    #         return self.n_to
    #     elif direction == 'e':
    #         return self.e_to
    #     elif direction =='s':
    #         return self.s_to
    #     elif direction == 'w':
    #         return self.w_to
    #     else:
    #         return None