from projeto_retas.graphic.graphic import __graphic_creator
import matplotlib.pyplot as plt


def picture_generation(point_a: tuple, point_b: tuple):
    """Creates a graphic recieving two points (A and B) in X,Y axle coordinates
     in form of tuples then saves this graphic in a png picture.

     Args:
        point_a(tuple): Coordinates in axle X,Y from first point.
        point_b(tuple): Coordinates in axle X,Y from second point.

    """
    __graphic_creator(point_a, point_b)
    plt.savefig('pictures/folder_to_pics/graphic.png')
