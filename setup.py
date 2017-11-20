from distutils.core import setup, Extension
import numpy

# Remove the "-Wstrict-prototypes" compiler option, which isn't valid for C++.
import distutils.sysconfig
cfg_vars = distutils.sysconfig.get_config_vars()
for key, value in cfg_vars.items():
    if type(value) == str:
        cfg_vars[key] = value.replace("-Wstrict-prototypes", "")
# ==================================

try:
        numpy_include = numpy.get_include()
except AttributeError:
        numpy_include = numpy.get_numpy_include()

FIR_module = Extension('_C_FIR',
                       sources=['C_FIR_wrap.cxx', 'FIR.cpp'],
                       include_dirs=[numpy_include]
                       )

setup(name='C_FIR',
      ext_modules=[FIR_module],
      py_modules=["_C_FIR"]
      )
