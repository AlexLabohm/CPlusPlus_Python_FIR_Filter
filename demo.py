from FIR_setup import cfilter
import numpy as np
import matplotlib.pyplot as plt

"""
    DEMO Program using cfilter
    
    The demo ECG data is filtered using a 50 Hz notch filter and a high pass
    filter to remove DC
"""

def main():

    sample_rate = 1000.
    num_taps = 3001

    # loading ECG data
    sample = np.loadtxt("demo_ecg.dat")
    # Initialising the output array
    clean = np.zeros(sample.shape)
    
    # Initialising a band stop filter
    fir = cfilter(num_taps, sample_rate, "BS", 45, 55)
    # filtering the ECG data
    for i in range(len(sample)):
        clean[i] = fir._filter(sample[i])
    
    # Initialising a high pass filter
    fir2 = cfilter(num_taps, sample_rate, "HP", 0.7)
    # filtering the ECG data
    for i in range(len(sample)):
        clean[i] = fir2._filter(clean[i])

    # plotting the result
    plt.plot(clean)
    plt.show()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
