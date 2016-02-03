## Obtaining and installing modules

Modules are collections of functions and classes that allow the programmer to actually do things. Obtaining and installing them
should be the easy part. These tips can help you out, and typically work on government or work computers where you may have limited administrative elevation. Sadly, if you encounter permission errors, you may need to contact your IT guy.

### Installing `pip`

While many packages come with a variety of installers, `pip` is the best way to get consistent success accross operating systems and
configurations. You can download it from their [installation page](https://pip.pypa.io/en/stable/installing/). Download and save a copy 
of `get-pip.py` in the `toipcs/modules` folder of your clone of this repo. In PyCharm, open up this python file, and run it 
(ctrl + shift + F10). To verify that you have installed pip, open up the python console from the bottom left button and type

``` python
import pip
```

If no error is presented, you now have pip. Now lets make sure it is up to date with

``` python
pip.main(["install", "--upgrade", "pip"])
```

One advantage to this method is that it is explicitly using the python interpreter you have defined in your project to run `get-pip.py`, which means it is garunteed to install pip for that interpreter. The same logic exists behind using pip to install modules from wheel files.

### Obtaining modules

A number of popular or common modules come with a variety of different installers, some of which work really well, some of which only work for simple scenarios. This can leave users frustrated and unable to get a module to work at all, and resort to more complex solutions. The gold standard for installing python packages is with [wheel files](http://pythonwheels.com/). Windows users can find just about any wheel file they need at this [unoficial binaries index](http://www.lfd.uci.edu/~gohlke/pythonlibs/), run out of UC Irvine.

A tremendous number of these binaries depend upon numpy with the math kernel library (MKL), and this depends upon microsoft visual studio C++ distributables. You can find links to all of these distributables at the top of the [unoficial binaries index](http://www.lfd.uci.edu/~gohlke/pythonlibs/). Download and install the appropriate ones, or just install them all.

When you select wheel files to download, you will see multiple versions. The two things that matter are
* which version of python you are using
* is that version 64 bit or 32 bit.

if you are unsure which version you are running, open up your python console and use

``` python
import sys
sys.version
```

### Installing modules with `pip`

The simplest way to install modules/packages with `pip` from inside your python environment is with

``` python
import pip
pip.main(["install", "mymodule"])               # to install a module
pip.main(["install", "--upgrade", "mymodule"])  # to force reinstall of the most recent version or wheel file
```

where `"mymodule"` may be a filepath to your wheel file, or (for simple modules) simply the module name. Please be aware that any **other**  python process which is open may prevent packages from installing, so you should close them. I've provided a tiny function for installing many wheel files at once in this repository [here](install_wheels.py). Users can go ahead and download all the wheel files they want to install, place them right here in the modules folder of your clone of this repository, open up `install_wheels.py`, and run it. Since you might go crazy with modules and install a bunch with interdependencies on one another, and the are simply installed in alphabetical order, you may have to run the script two or three times to get them all. Once you get the hang of installing modules, you should install them one at a time in the future.

Modules you will probably want to download wheel files for:
* [`numpy`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy), an essential numerical computing library
* [`matplotlib`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib), allows the creation of graphs and plots
* [`pandas`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pandas), data analysis library
* [`scipy`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy), scientific computing library
* [`gdal`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal), geospatial data abstraction library
* [`fiona`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona), a friendlier API for the `ogr` component in `gdal` for vector based GIS
* [`rasterio`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#rasterio), a friendlier API for raster manipulations with the `gdal` library

Alternatively, for modules which aren't quite as bulky, `pip` can simply retreive the correct version from the python package index with only a name, with a fairly high success rate. When you discover a new package that you would like to try, but you do not have installed, I recommend trying this simple method first, then grabbing a wheel if you encounter issues. As mentioned before, you can do this with 

``` python
import pip
pip.main(["install", "mymodule"])               # to install a module
```

Go ahead and try it with a module of your choice or perhaps a popular http library `requests`.




