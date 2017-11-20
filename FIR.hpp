//
//  FIR.hpp
//
//  Created by Alexander Labohm on 04/11/2017.
//  Copyright © 2017 Alexander Labohm.
//

#ifndef FIR_hpp
#define FIR_hpp

#include <stdio.h>
#include <algorithm>
#include <iterator>
#include <vector>

// FIR filter class
class FIR{
private:
    // Variables for the number of filter taps
    // and the current position in the buffer
    int num_taps, current;
    // vectors for the buffer and the filter coefficients
    std::vector<double> buffer;
    std::vector<double> coeff;
    
public:
    // Constructor
    FIR(int taps, double coefficients[]);
    // filter method
    double filter(double input);
 
};

#endif /* FIR_hpp */
