# Deterministic-Turing-Machine

---------------------------------------------------------------------------------------------------------------------------

IDE - Pycharm 

Python 3.7.2

---------------------------------------------------------------------------------------------------------------------------

This program is an implementation of Deterministic Turing Machine (DTM) in Python. 

It is a multiple-class program in a single .py file. 

Inter classes "Tape" and "DTM" are implemented for tape and TM respectively. Main class is the driver executing the program. 

The primary data structures used here are array (inputs & outputs) and hashmap (lookups for TM transition function).

---------------------------------------------------------------------------------------------------------------------------
 
 There are 4 types of DTM implementations:
 
     1) A simple binary based deterministic Turing Machine returns "Yes" or "No";
     
        Set dtm_type = 'deter'.
        
     2) An unary based Turing Machine for addition;
     
        Set dtm_type = 'add'.
        
     3) An unary based Turing Machine for subtraction;
     
        Set dtm_type = 'sub'.
        
     4) An unary based Turing Machine for multiplication;
     
        Set dtm_type = 'mul'.
 
---------------------------------------------------------------------------------------------------------------------------

High level process flow: read an input file --> run TM operations --> display results --> export final outputs.

@author RabbitCaesar
