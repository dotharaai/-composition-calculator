#!/usr/bin/env python3
# Calculate composition of alloy
#
# arguments:
# argv[0] : dictionary, { 'element_name': element_composition, ... }
# argv[1] : float, alloy_weight [g]
import sys
from elements import ELEMENTS



def composition(arg):
    mol_mass = 0
    mass = float(arg[1]) # 最終生成質量
    t = int(arg[2]) # t元系
    elms = {}
    for i in range(t):
        elms.update({arg[3+i]:float(arg[3+i+t])})
        
    for name, val in elms.items():
        elem = ELEMENTS[name]
        mol_mass += elem.mass * val
        
    for name, val in elms.items():
        elem = ELEMENTS[name]
        print(elem.name, mass / mol_mass * val * elem.mass)
    print()

if __name__ == "__main__":
    composition(sys.argv)
    
    