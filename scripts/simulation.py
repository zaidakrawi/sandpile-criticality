from sandpile.core import Sandpile

def main():
    pile = Sandpile(size=20)
    
    # Drop grains at the center
    for _ in range(1000):
        pile.add_grain(10, 10)
        pile.topple()

    pile.visualize()