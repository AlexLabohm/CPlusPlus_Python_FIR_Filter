# C++ FIR filter extension module for Python

This Python package uses a SWIG generated interface to setup a FIR filter
class using C++ code. The module *FIR_setup.py* provides the class *cfilter*,
which generates the FIR coefficients for the desired filter and passes
these to the C++ FIR class constructor using the SWIG interface.
The C++ FIR class provides a filter method that can be called using the
*_filter* method of *cfilter*.
The filter method written in C++ improves the performance of the filter
operation substantially compared to a filter method written in Python code.
However, the FIR coefficients can be easily generated in Python using
*scipy.signal.firwin()*.

## Getting Started

Building and installing the C_FIR module requires the interface file *numpy.i* which contains
the relevant typemap used to map numpy arrays unto C++ arrays. Therefore, *numpy.i* must
be located in the directory where the wrapper is developed.
(Reference: https://docs.scipy.org/doc/numpy-1.13.0/reference/swig.interface-file.html)

### Structure
This package is build around a C++ FIR filter class. This class is wrapped
using SWIG and *FIR_setup.py* imports the generated C_FIR module to initialise
the C++ filter  class with the Python generated FIR coefficients array.
(A *setup.py* file to build the C_FIR module is included in the distribution.)
*FIR_setup.py* provides the *cfilter* class to do just that. Therefore, to use
this package the following import statement is needed:

```
from FIR_setup import cfilter
```


## Building the C_FIR module using SWIG

Firstly, the C++ files *FIR.hpp* and *FIR.cpp* must be compiled.
For Linux / Mac this can be done using the following command
(Its important to use the -c flag here):

```
g++ -c FIR.hpp FIR.cpp
```

The interface file *C_FIR.i* is compiled using SWIG (http://www.swig.org)
by executing the following command:

```
swig -c++ -python C_FIR.i
```

Now, the extension module can be build using:

```
python setup.py build_ext --inplace
```


## Demo

A demo program is included with *demo.py*. This implements a 50 Hz notch filter
and a high pass filter and performs the filter operations on a ECG sample.


## License

This project is licensed under the MIT License

