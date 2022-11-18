import matplotlib.pyplot as plt
from math import sqrt


def __graphic_creator(point_a: tuple, point_b: tuple):
    """Creates a graphic with A and B coordenates in (X,Y) axle.

    Args:
        point_a(tuple): Coordinates in axle X,Y from first point.
        point_b(tuple): Coordinates in axle X,Y from second point.

    """
    axle_x = append_coordinates_x(point_a, point_b)
    axle_y = append_coordinates_y(point_a, point_b)
    distance = two_points_distance(axle_x, axle_y)
    plt.plot(axle_x, axle_y, color=list_of_colors(2))
    coordinates_a = plt.scatter(point_a[0], point_a[1], color=list_of_colors(0))
    coordinates_b = plt.scatter(point_b[0], point_b[1], color=list_of_colors(1))
    plt.title(f'Traçando retas entre 2 pontos no plano (X,Y).\nDistância = {distance:.4f}')
    config(coordinates_a, coordinates_b)


def append_coordinates_x(point_a: tuple, point_b: tuple) -> list:
    """Creates axle X for points A and B.

    Args:
        point_a(tuple): Coordinates in axle X,Y from first point.
        point_b(tuple): Coordinates in axle X,Y from second point.

    Returns:
        axle_x(list): List of Points A and B in axle X.

    """
    axle_x = list()
    axle_x.append(point_a[0])
    axle_x.append(point_b[0])
    return axle_x


def append_coordinates_y(point_a: tuple, point_b: tuple) -> list:
    """Creates axle Y for points A and B.

    Args:
        point_a(tuple): Coordinates in axle X,Y from first point.
        point_b(tuple): Coordinates in axle X,Y from second point.

    Returns:
        axle_y(list): List of Points A and B in axle Y.

    """
    axle_y = list()
    axle_y.append(point_a[1])
    axle_y.append(point_b[1])
    return axle_y


def two_points_distance(axle_x: list, axle_y: list) -> float:
    """Creates the legnth of discance for two points in (X,Y) axle.

    Args:
        axle_x(list): List of Points A and B in axle X.
        axle_y(list): List of Points A and B in axle Y.

    Returns:
        distance(float): the distance value for two points in (X,Y) axle.
    """
    distance = sqrt((axle_x[1] - axle_x[0]) ** 2 + (axle_y[1] - axle_y[0]) ** 2)
    return distance


def list_of_colors(color: int) -> str:
    """Recieve a number and returns a color.

    Args:
        color(int): number from color.

    Returns:
        colors[color](str): If colors[color] exists returns a color. If it doesn't, assert value error.
    """
    if type(color) == int:
        colors = ['blue', 'red', 'black']
        if color == 0:
            return colors[0]
        elif color == 1:
            return colors[1]
        elif color == 2:
            return colors[2]
        else:
            assert ValueError(f'Color must be in range 0-2. Not {color}')
    else:
        assert TypeError(f'Color type must be integer. Not {type(color)}')


def config(coordinates_a,
           coordinates_b):
    """Creates a graphic configuration.

    Args:
        coordinates_a(matplotlib.collections.PatchCollection): The coordinates in graphic from A point.
        coordinates_b(matplotlib.collections.PatchCollection): The coordinates in graphic from B point.

    """
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
