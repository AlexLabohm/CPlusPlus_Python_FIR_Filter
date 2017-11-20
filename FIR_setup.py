import C_FIR
import scipy.signal as signal
import numpy as np

"""
    FIR Filter with C++ filter method
    
    This class setups a FIR filter written in C++ code using a SWIG generated interface.
    The filter coefficients are generated using scipy.signal.firwin() and are passed to 
    the C++ FIR constructor.
    The _filter method calls the C++ filter method and thus the actual filter operation is
    done using only C++ code.
    
    Example
    The constructor takes the number of taps, the sampling rate, the type of the filter and
    the filtered frequencies.
    For example, setting up a band stop filter:
    
    band_stop = FIR_setup(3001, 1000, 'BS', 45, 55)
    
    (Note: firwin requieres an odd number of taps)
    And filtering a sample array:
    
    for i in range(len(sample)):
        clean_sample[i] = band_stop._filter(sample[i])
        
    (Refer to demo.py for a complete demo)
     
"""


class cfilter:

    def __init__(self, num_taps, sampling_rate, filter_type, f1, f2=0):
        # Initialising the class variables
        # casting operations are done in order to ensure correct data types

        self.taps = int(num_taps)
        self.fs = float(sampling_rate)
        self.f1 = float(f1)
        self.f2 = float(f2)

        # calculating the coefficients
        coefficients = np.zeros(self.taps)

        if filter_type.upper() == "LP":
            coefficients = self.lowpass()

        elif filter_type.upper() == "HP":
            coefficients = self.highpass()

        elif filter_type.upper() == "BS":
            coefficients = self.bandstop()

        elif filter_type.upper() == "BP":
            coefficients = self.bandpass()

        else:
            print "Unknown Filter type."
            print "Choose either LP (Lowpass), HP (Highpass), BP (Bandpass) or BS (Bandstop)"

        # Initialising the C++ Fir filter class
        self.fir = C_FIR.FIR(coefficients)

    # methods to calculate the FIR coefficients
    def lowpass(self):
        f = self.f1 / self.fs * 2.
        coefficients = signal.firwin(self.taps, f)
        coefficients = np.asarray(coefficients, dtype=np.double)
        return coefficients

    def highpass(self):
        f = self.f1 / self.fs * 2.
        coefficients = signal.firwin(self.taps, f, pass_zero=False)
        coefficients = np.asarray(coefficients, dtype=np.double)
        return coefficients

    def bandpass(self):
        f1 = self.f1 / self.fs * 2.
        f2 = self.f2 / self.fs * 2.
        coefficients = signal.firwin(self.taps, [f1, f2], pass_zero=False)
        coefficients = np.asarray(coefficients, dtype=np.double)
        return coefficients

    def bandstop(self):
        f1 = self.f1 / self.fs * 2.
        f2 = self.f2 / self.fs * 2.
        coefficients = signal.firwin(self.taps, [f1, f2])
        coefficients = np.asarray(coefficients, dtype=np.double)
        return coefficients

    # filtering the input signal by calling the C++ filter method
    def _filter(self, filter_input):
        output = self.fir.filter(filter_input)
        return output
