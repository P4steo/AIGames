import pandas as pd
import scipy
from scipy import sparse

X_CORNER = 21.943
Y_CORNER = -67.5
PIXEL_LENGTH = 0.0131


def convert_coordinates_to_pixels(x, y):
    index_x = int(round((x - X_CORNER) / PIXEL_LENGTH))
    index_y = int(round(-(y - Y_CORNER) / PIXEL_LENGTH))

    sparsed_data = scipy.sparse.load_npz('npz/plik1.npz')
    df = pd.DataFrame.sparse.from_spmatrix(sparsed_data)
    return df[index_y][index_x]


print(convert_coordinates_to_pixels(32.86916111111111, -97.04050277777777))

#   y y y
# x
# x

