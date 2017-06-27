## Installation ##

## Theano ##

Li-Yi Wei, 2017

Installking Keras ought to install Theano automatically for you.

If not, with anaconda installed, you can just follow the instructions from [here](http://deeplearning.net/software/theano/install_windows.html)

    $ conda install mingw libpython

<!--
## Install Theano with g++ under 64-bit Windows

2017 update: try this only if the above does not work for you.

Li-Yi Wei, 2016

I basically follow the instructions from [here](https://www.kaggle.com/c/otto-group-product-classification-challenge/forums/t/13973/a-few-tips-to-install-theano-on-windows-64-bits) and [here](http://rosinality.ncity.net/doku.php?id=python:installing_theano) but without setting paths (as I have already done so).

1. Install MinGW 64bit.
Download mingw-w64-install.exe at [here](http://sourceforge.net/projects/mingw-w64/files/) and install it.
Architecture is x86_64, Threads is posix, Exception is seh.

2. Install MSYS.
Download MSYS-20111123.zip at [here](http://sourceforge.net/projects/mingw-w64/files/External%20binary%20packages%20%28Win64%20hosted%29/MSYS%20%2832-bit%29/) and extract archive under the directory where MinGW installed (directory that has bin subdirectory).
Run msys.bat and type command
    
    $ sh /postinstall/pi.sh

at the prompt.

3. You should make libpythonXX.a (XX is version number) file manually.
MinGW supports 32bit lib but 64bit not.
First copy pythonXX.dll (i.e. python34.dll) to temporary directory.
Generally you can found pythonXX.dll under C:\Windows\System32 or [Anaconda directory]\libs.
Then run these commands:

    $ gendef pythonXX.dll  
    $ dlltool --as-flags=--64 -m i386:x86-64 -k --output-lib libpythonXX.a --input-def pythonXX.def

4. Copy libpythonXX.a file that you made under the [Python directory]\libs.

5. Make .theanorc under HOME directory with content like this:

    [blas]  
    ldflags = 
    
    [gcc]  
    cxxflags = -shared -I[MinGW directory]\include -L[Python directory]\libs -lpython34 -DMS_WIN64

6. This is my .theanorc:

    [blas]
    ldflags = 
     
    [gcc]
    cxxflags = -shared -I C:\programs\MinGW\mingw64\include -L C:\programs\Anaconda3\libs -lpython35 -DMS_WIN64 -D_hypot=hypot

7. Run this to verifying installation:

    import theano  
    theano.test()
-->

## [Keras](https://keras.io/) ##

The default Keras backend seems to be TensorFlow.
See [here](https://keras.io/backend/) about switching to Theano.

## OpenBLAS ##

In case you don't want the default BLAS with Theano (due to various reasons such as [memory leak](https://github.com/fchollet/keras/issues/5935) or [speed](http://ankivil.com/making-theano-faster-with-cudnn-and-cnmem-on-windows-10/)), you can install OpenBLAS as an alternative.

Below is a summary from [here](http://ankivil.com/making-theano-faster-with-cudnn-and-cnmem-on-windows-10/) for Windows:

* Download [mingw64_dll.zip](http://sourceforge.net/projects/openblas/files/v0.2.14/mingw64_dll.zip/download)

* Download [OpenBLAS-v0.2.14-Win64-int32.zip](http://sourceforge.net/projects/openblas/files/v0.2.14/OpenBLAS-v0.2.14-Win64-int32.zip/download)

* Create a directory to put OpenBLAS, 'C:\openblas' for instance

* Copy the DLLs from 'mingw64_dll' and 'OpenBlas/bin' into C:\openblas

* Add to following lines to your .theanorc file:

    [blas]
    ldflags = -LC:\openblas -lopenblas
     
* Add 'C:\OpenBlas' to the 'PATH' environment variable

* Run [check_blas.py](check_blas.py) for verification

