from sandpile.core import Sandpile

def main():
    # pile = Sandpile(size=20)
    
    # # Drop grains at the center
    # for _ in range(10000):
    #     pile.add_grain(10, 10)
    #     pile.topple()

    # pile.visualize()


    pile = Sandpile(size=20)
    pile.animate(num_frames=300, drop_location=(10, 10))