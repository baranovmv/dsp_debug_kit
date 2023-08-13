# dsp_debug_kit

This is a tiny toolset I use when I develop and debug any signal processing code in C or C++. Basically it augments
`gdb` with ability to plot a signal or its spectrum by calling python from inside gdb.

It uses [gdb_numpy|https://github.com/TorosFanny/gdb_numpy] repo which is python3 version of 
[M.Mo on codeproject |http://www.codeproject.com/Articles/669606/Analyzing-C-Cplusplus-matrix-in-the-gdb-debugger-w]. 
Thanks to both authors.


## Installation

1. Run `git submodule init && git submodule update`.

2. Call `./setup.sh`, it will add necessary pathes to `~/.gdbinit`.
As

**If you are having troubes debugging in CLion:**

`gdb_numpy`` could take some time to evaluate so in clion it might be usefull to increase timeout for instructino 
evaluation:

1. In `help->Find Action...` type "registry"

2. Start typing `cidr.debugger.timeout.evaluate` to find this parameter.

3. Increase this value by seceral times. 120000 worked in my case.


## Use cases

Lets say we have a C++ snippet with an array with a sinewave:

```
#include <array>
#include <algorithm>
#include <math.h>

int main() {
    constexpr size_t n = 1024;
    std::array<float, n> signal;
    // Fill signal with a sinewave
    std::generate(signal.begin(), signal.end(),
        [n=0] () mutable {return sinf(2*M_PI*(float)n++ / 100); });


    return 0;
}
```

1. Put a breakpoint on line with return statement.

2. Type in gdb console:

```
(gdb) py x = gdn.to_array("(float*)signal.data()", (1024,))
(gdb) py plt.plot(x); plt.show()
```

3. You should see a window with a plot of signal in time-domain.

4. Type ` py semispect(x, 10)` to see spectrum of a signal in log scale.


Take a look into  python cde in this folder to see what is available.
`