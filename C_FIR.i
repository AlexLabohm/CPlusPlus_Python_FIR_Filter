
%module C_FIR

%{
#define SWIG_FILE_WITH_INIT
#include "FIR.hpp"

%}

%include "numpy.i"
%include "typemaps.i"
%init %{
import_array();
%}

%apply (int DIM1, double* INPLACE_ARRAY1) {(int taps, double coefficients[])}

class FIR{
public:
    FIR(int taps, double coefficients[]);
    double filter(double input);
    ~FIR();
};

