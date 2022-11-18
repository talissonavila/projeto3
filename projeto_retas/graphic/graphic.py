import matplotlib.pyplot as plt
from math import sqrt


def __graphic_creator(point_a: tuple, point_b: tuple):
    """Creates a graphic with A and B coordenates in (X,Y) axle.

    Args:
        point_a(tuple): Coordinates in axle X,Y from first point.
        point_b(tuple): Coordinates in axle X,Y from second point.

    """
    axle_x = []
    axle_y = []
    axle_x.append(point_a[0])
    axle_x.append(point_b[0])
    axle_y.append(point_a[1])
    axle_y.append(point_b[1])
    distance = sqrt((axle_x[1] - axle_x[0])**2 + (axle_y[1] - axle_y[0])**2)
    colors = ['blue', 'red', 'black']
    plt.plot(axle_x, axle_y, color=colors[2])
    coordinates_a = plt.scatter(point_a[0], point_a[1], color=colors[0])
    coordinates_b = plt.scatter(point_b[0], point_b[1], color=colors[1])
    plt.title(f'Traçando retas entre 2 pontos no plano (X,Y).\nDistância = {distance:.4f}')
    plt.xlabel('Eixo X', fontsize=14)
    plt.ylabel('Eixo Y', fontsize=14)
    plt.grid()
    plt.legend((coordinates_a, coordinates_b),
               ('Ponto A', 'Ponto B'),
               scatterpoints=1,
               loc='lower left',
               ncol=2,
               fontsize=7
               )


def shows_graphic(point_a: tuple, point_b: tuple):
    """Recieves coordinates for A and B, creates a graphic then show it.

    Args:
        point_a(tuple): Coordinates in axle X,Y from first point.
        point_b(tuple): Coordinates in axle X,Y from second point.

    """
    __graphic_creator(point_a, point_b)
    plt.show()

