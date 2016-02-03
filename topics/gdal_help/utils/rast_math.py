# in the input expression

# explanation of the above line: when a warning is encountered during eval,
# the warning prints the first line of this file, so it might as well say something useful.

__author__ = 'Jwely'

import gdal
import gdalconst
import gdalnumeric
import numpy
import string
import os
import math         # imported so it is available to the users expression evaluation


def rast_math(output_path, expression, *args):
    """
    A raster math calculator that uses GDALs python bindings instead of command line
    interface for simple math. The syntax of this feels more pythonic than the native gdal_calc.py
    syntax. Supports up to 26 raster images for each letter of the alphabet as
    arguments. Supports single band raster images or gdal.Band instances as *args inputs.
    Input expression will be directly evaluated, so users can input numerical constants
    and simple ``numpy`` or ``math`` module operators with lowercase function names. Because
    this function uses python bindings and numpy data structures, be mindful of the memory
    limitations associated with 32-bit python, highly recommend using 64 bit.

    :param output_path: filepath at which to store expression result. Set to False to just return
                        the numeric array instead of saving it.
    :param expression:  the mathematical expression using rasters as A,B,C, etc
    :param args:        Filepaths to single band rasters that represent A,B,C, etc (in order)
                        OR, gdal.Band instances which could be used with multi-band rasters via...
                            ds = gdal.Open(rastpath)
                            bandA = ds.GetRasterBand(1)
                            bandB = ds.GetRasterBand(2)
                            rast_math(outpath, "numpy.log(A) + 3 * B", bandA, bandB)
    :return:            the output path to the file created by this function

    An example for the ubiquitous NDVI calculation from landsat bands:

    ..code-block: python

        root = r"my_landsat_directory"              # directory with landsat tiffs
        A_path = os.path.join(root, "tile_B5.TIF")  # filepath to Band5
        B_path = os.path.join(root, "tile_B4.TIF")  # filepath to Band4
        out_path = os.path.join(root, "NDVI.TIF")   # filepath of new output image

        rast_math(out_path, "(A + B) / (A - B)", A_path, B_path)

    An example where we want to conditionally mask one raster by another, say
    image "A" is our raster with data, and image "B" is a mask where a value of 1
    indicates a bad value, and zero indicates a good value.

    ..code-block:python

        rast_math(out_path, "A * (B == 0)", A_path, B_path)
    """

    # set up the iterators and structures
    datasets = {}   # dictionary where actual data will go
    eval_args = {}  # dictionary with string literals to be evaluated as code
    alphabet = string.ascii_uppercase[:len(args)]

    # format the expression with curly brackets around letters
    print("Executing expression '{0}'".format(expression))
    for letter in alphabet:
        expression = expression.replace(letter, "{%s}" % letter)

    # create the numpy arrays from raster datasets with gdal
    for arg, letter in zip(args, alphabet):

        # handle filepath input and raise exception for invalid filepaths
        if isinstance(arg, str):
            if not os.path.exists(arg):
                raise Exception("file {0} does not exist!".format(arg))

            print("\tLoading {0} as raster '{1}'".format(arg, letter))
            dataset_in = gdal.Open(arg, gdalconst.GA_ReadOnly)
            band = dataset_in.GetRasterBand(1)
            datasets[letter] = numpy.array(band.ReadAsArray(), dtype="float32")

        # handles input type of a gdal.Band instance
        elif isinstance(arg, gdal.Band):
            datasets[letter] = numpy.array(arg.ReadAsArray(), dtype="float32")

        eval_args[letter] = "datasets['{0}']".format(letter)


    # assemble and evaluate the expression
    eval_expression = expression.format(**eval_args)
    print(eval_expression)
    out_array = eval(eval_expression)

    # either save the output or return an output array
    if output_path:
        driver = gdal.GetDriverByName("GTiff")      # create the geotiff driver object
        yshape, xshape = datasets["A"].shape        # set dimensions of output file
        num_bands = 1                               # only supports single band output
        dataset_out = driver.Create(output_path, xshape, yshape, num_bands, gdal.GDT_Float32)
        gdalnumeric.CopyDatasetInfo(dataset_in, dataset_out)
        band_out = dataset_out.GetRasterBand(1)
        gdalnumeric.BandWriteArray(band_out, out_array)
        return os.path.abspath(output_path)

    else:
        return out_array
