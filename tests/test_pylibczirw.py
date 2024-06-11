import requests
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import os


def test_import():
    import pylibCZIrw

# see https://colab.research.google.com/github/zeiss-microscopy/OAD/blob/master/jupyter_notebooks/pylibCZIrw/pylibCZIrw_3_0_0.ipynb#scrollTo=2a43afb5
def test_pylibczirw():
    from pylibCZIrw import czi as pyczi

    # Folder containing the input data
    INPUT_FOLDER = 'data/inputs/'

    # Path to the data on GitHub
    GITHUB_DATA_PATH = 'https://raw.githubusercontent.com/zeiss-microscopy/OAD/master/jupyter_notebooks/pylibCZIrw/data.zip'

    # Download training data
    if not (os.path.isdir(INPUT_FOLDER)):
        compressed_data = './data.zip'
        if not os.path.isfile(compressed_data):
            import io
            response = requests.get(GITHUB_DATA_PATH, stream=True)
            compressed_data = io.BytesIO(response.content)

        import zipfile
        with zipfile.ZipFile(compressed_data, 'r') as zip_accessor:
            zip_accessor.extractall('./')

    czifile_5dstack = os.path.join(INPUT_FOLDER, r"T=3_Z=5_CH=2_X=240_Y=170.czi")


    with pyczi.open_czi(czifile_5dstack) as czidoc:

        # define some plane coordinates
        plane_1 = {'C': 0, 'Z': 2, 'T': 1}
        plane_2 = {'C': 1, 'Z': 3, 'T': 2}

        # equivalent to reading {'C': 0, 'Z': 0, 'T': 0}
        frame_0 = czidoc.read()

        # get the shape of the 2d plane - the last dime indicates the pixel type
        # 3 = BGR and 1 = Gray
        print("Array Shape: ", frame_0.shape)

        # get specific planes
        frame_1 = czidoc.read(plane=plane_1)
        frame_2 = czidoc.read(plane=plane_2)

        fig, ax = plt.subplots(1, 3, figsize=(15, 5))
        ax[0].imshow(frame_0[...,0], cmap=cm.inferno)
        ax[0].set_title("Frame_0")
        ax[1].imshow(frame_1[...,0], cmap=cm.inferno)
        ax[1].set_title("Frame_1")
        ax[2].imshow(frame_2[...,0], cmap=cm.Greens_r)
        ax[2].set_title("Frame_2")
