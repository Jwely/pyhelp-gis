import os
import pip


def install_wheels(wheel_directory=None):
    """
    Simple function to use pip to install any .whl files in a directory.
    Defaults to installing .whl files in THIS directory.

    :param wheel_directory: filepath to folder with wheel files to install
    """

    if wheel_directory is None:
        wheel_directory = os.path.dirname(os.path.realpath(__file__))

    print(wheel_directory)

    wheels = [fname for fname in os.listdir(wheel_directory) if ".whl" in fname]
    for wheel in wheels:
        pip.main(["install", "--upgrade", wheel])




if __name__ == "__main__":
    install_wheels()