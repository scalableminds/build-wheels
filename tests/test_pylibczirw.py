from pylibCZIrw import czi as pyczi


def test_pylibczirw(czipath):
    # open the CZI document to read the
    with pyczi.open_czi(czipath) as czidoc:
        # get the image dimensions as a dictionary, where the key identifies the dimension
        total_bounding_box = czidoc.total_bounding_box

        # get the total bounding box for all scenes
        total_bounding_rectangle = czidoc.total_bounding_rectangle

        # get the bounding boxes for each individual scene
        scenes_bounding_rectangle = czidoc.scenes_bounding_rectangle

        # read a 2D image plane and optionally specify planes, zoom levels and ROIs
        image2d = czidoc.read(plane={"T": 1, "Z": 2, "C": 0}, zoom=1.0, roi=(0, 0, 50, 100))

        assert image2d is not None
