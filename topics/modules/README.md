## Obtaining and installing modules

Modules are collections of functions and classes that allow the programmer to actually do things. Obtaining and installing them
should be the easy part. These tips can help you out.

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

One advantage to this method is that it is explicitly using the python interpreter you have defined in your project to run `get-pip.py`, which
means it is garunteed to install pip for that interpreter. The same logic exists behind using pip to install modules from wheel files.

### Installing modules with `pip`


