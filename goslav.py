import random as r
import configparser


class Atom:
    def __init__(self, x, y, speed_x, speed_y, name):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.config = config['Atom']
        self.pos = (x, y)
        self.speed = (speed_x, speed_y)
        self.mass = float(self.config['mass'])
        self.radius = float(self.config['radius'])
        self.name = name

    def __str__(self):
        return f"Atom \"{self.name}\"\n" \
            f"Pozycja: {self.pos}\n" \
            f"Prędkość: {self.speed}\n" \
            f"Stałe: masa = {self.mass}, promień = {self.radius}"

    def access_atom(self):
        return self.pos[0], self.pos[1], self.speed[0], self.speed[1]

    def move(self, tickrate=20):
        self.pos = (self.pos[0] + self.speed[0]*(1/int(tickrate)), self.pos[1] + self.speed[1]*(1/int(tickrate)))


class Pojemnik:
    def __init__(self):
        """
        Inicjuje pojemnik, zawierający atomy. Właściwoći definiuje config
        Na ten moment liczba atomów jest związana z wysokością tablicy i jest jer równa,
         a każdy atom pojawia się na środku komórki
        """
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.config = config['Pojemnik']
        self.width = int(self.config['width'])
        self.height = int(self.config['height'])
        self.tickrate = int(self.config['tickrate'])
        self.number_of_atoms = int(self.config['number_of_atoms'])

        self.atoms = []
        for i in range(self.number_of_atoms):
            self.atoms.append(Atom(r.uniform(0, 1), r.uniform(0, self.height),
                                   r.uniform(int(self.config['min_speed']), int(self.config['max_speed'])),
                                   r.uniform(int(self.config['min_speed']), int(self.config['max_speed'])), i))

    def tick(self):
        for i in range(len(self.atoms)):
            self.atoms[i].move(self.tickrate)

    def atoms_pos(self):
        output = []
        for i in range(self.number_of_atoms):
            output.append(self.atoms[i].pos)
        return output

    def atoms_speed(self):
        output = []
        for i in range(self.number_of_atoms):
            output.append(self.atoms[i].speed)
        return output

    def __str__(self):
        return f"Pojemnik po rozmiarach {self.width} x {self.height}, zawierający {len(self.atoms)} atomów"


if __name__ == "__main__":
    atomy = []
    for i in range(3):
        atomy.append(Atom(1, 1, 1, 1, 1))
    print(atomy[1].access_atom())
    pojemnik = Pojemnik()
    print(atomy[0])
    for i in range(5):
        print(pojemnik.atoms[i].access_atom())
    for i in range(5):
        pojemnik.atoms[i].move()
    for i in range(5):
        print(pojemnik.atoms[i].access_atom())
    print(pojemnik)
