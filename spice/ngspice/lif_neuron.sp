* ============================================================
* Simple Leaky Integrate-and-Fire Neuron Concept
* Tool: ngspice-compatible netlist
* ============================================================

* Parameters
.param Cmem = 1p
.param Rleak = 100Meg
.param Iin = 10n
.param Vreset = 0

* Input current charges membrane capacitor
Iinput 0 mem DC {Iin}

* Leak path
Rleak mem 0 {Rleak}

* Membrane capacitance
Cmem mem 0 {Cmem} IC=0

* TODO:
* Add threshold/reset behavior using a behavioral switch or subcircuit.
* For now, this file only shows passive membrane charging with leakage.

.tran 1n 5u
.control
run
plot v(mem)
.endc

.end
