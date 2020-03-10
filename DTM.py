"""

This program simulates Deterministic Turing Machine (DTM)

 There are 4 types of DTM implementations here:
     1) A simple binary based deterministic Turing Machine returns "Yes" or "No";
     
        E.g., Set dtm = 'deter' and input_file_name = 'DTM_Deter_Input1.txt'
        
     2) An unary based Turing Machine for addition;
     
        E.g., Set dtm = 'add' and input_file_name = 'DTM_Add_Input1.txt'
        
     3) An unary based Turing Machine for subtraction;
     
        E.g., Set dtm = 'sub' and input_file_name = 'DTM_Sub_Input1.txt'
        
     4) An unary based Turing Machine for multiplication;

        E.g., Set dtm = 'mul' and input_file_name = 'DTM_Mul_Input1.txt'

This program will read an input file, run TM operations,
display results and export final outputs.

 @author RabbitCaesar

"""

import os


# Read file
def load_input(file_name):
    f = open(file_name, 'r')
    return f.read()

"""
Class "Tape"
"""
class Tape(object):

    # constructor
    def __init__(self, inputTape = ''):
        self.__tape = {}
        for i in range(len(inputTape)):
           self.__tape[i] = inputTape[i]

    # getter
    def __getitem__(self, index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return 'b'

    # setter
    def __setitem__(self, pos, char):
        self.__tape[pos] = char

    # string convertor
    def __str__(self):
        s = ''
        lower_index = min(self.__tape.keys())
        upper_index = max(self.__tape.keys())
        for i in range(lower_index, upper_index):
            s += self.__tape[i]
        return s

"""
Class "DTM"

    - get_tape()
    - get_state()
    - states_control()
    - halt()
    - deter_result()
"""
class DTM(object):

    # constructor
    def __init__(self
                 ,tape = ''
                 ,initial_state = None
                 ,halt_states = None
                 ,trans_function = None
                 ,blank_symbol = None):

        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__current_state = initial_state
        self.__blank_symbol = blank_symbol

        if trans_function == None:
            self.__trans_function = {}
        else:
            self.__trans_function = trans_function
        if halt_states == None:
            self.__halt_states = set()
        else:
            self.__halt_states = set(halt_states)

    def get_tape(self):
        return str(self.__tape)

    def get_state(self):
        return str(self.__current_state)

    # States control method; his method handles all the
    # operations of TM in accordance with transition function lookup
    def states_control(self):
        char_under_head = self.__tape[self.__head_position]
        key = (self.__current_state, char_under_head)
        # operations based on transition function
        if key in self.__trans_function:
            value = self.__trans_function[key]
            self.__tape[self.__head_position] = value[1]
            # move right
            if value[2] == 'R':
                self.__head_position += 1
            # move left
            elif value[2] == 'L':
                self.__head_position -= 1
            # stay
            elif value[2] == 'N':
                self.__head_position += 0
            self.__current_state = value[0]

    # Stop TM
    def halt(self):
        if self.__current_state in self.__halt_states:
            return True
        else:
            return False

    # Return deterministic result
    def deter_result(self):
        if self.__current_state == 'qY':
            return 'Yes'
        elif self.__current_state == 'qN':
            return 'No'


# Transition function lookup
def trans_function(dmt_type):
    # Binary based simple deterministic TM
    if dmt_type == 'deter':
        return {
                ('q0', '0'): ('q0', '0', 'R'),
                ('q0', '1'): ('q0', '1', 'R'),
                ('q0', 'b'): ('q1', 'b', 'L'),
                ('q1', '0'): ('q2', 'b', 'L'),
                ('q1', '1'): ('q3', 'b', 'L'),
                ('q1', 'b'): ('qN', 'b', 'L'),
                ('q2', '0'): ('qY', 'b', 'L'),
                ('q2', '1'): ('qN', 'b', 'L'),
                ('q2', '2'): ('qN', 'b', 'L'),
                ('q3', '0'): ('qN', 'b', 'L'),
                ('q3', '1'): ('qN', 'b', 'L'),
                ('q3', '2'): ('qN', 'b', 'L')
                }
    # Unary based TM for addition
    if dmt_type == 'add':
        return {('q0', '$'): ('q1', '$', 'R'),
                ('q1', 'b'): ('qf', 'b', 'N'),
                ('q1', '1'): ('q1', '1', 'R'),
                ('q1', '&'): ('q2', '1', 'R'),
                ('q2', '1'): ('q2', '1', 'R'),
                ('q2', 'b'): ('q3', 'b', 'L'),
                ('q3', '1'): ('q4', 'b', 'L'),
                ('q4', '1'): ('q4', '1', 'L'),
                ('q4', '$'): ('qf', '$', 'N')
                }
    # Unary based TM for subtraction
    elif dmt_type == 'sub':
        return  {('q0', '$'): ('q0', '$', 'R'),
                 ('q0', 'b'): ('qf', 'b', 'N'),
                 ('q0', '1'): ('q1', '1', 'R'),
                 ('q1', '1'): ('q1', '1', 'R'),
                 ('q1', 'b'): ('q2', 'b', 'R'),
                 ('q2', 'b'): ('q2', 'b', 'R'),
                 ('q2', '1'): ('q3', '1', 'R'),
                 ('q3', '1'): ('q4', '1', 'L'),
                 ('q3', 'b'): ('q6', 'b', 'L'),
                 ('q4', '1'): ('q5', 'b', 'L'),
                 ('q5', 'b'): ('q5', 'b', 'L'),
                 ('q5', '1'): ('q2', 'b', 'R'),
                 ('q5', '$'): ('q2', '$', 'R'),
                 ('q6', '1'): ('q7', 'b', 'L'),
                 ('q7', 'b'): ('q7', 'b', 'L'),
                 ('q7', '$'): ('qf', '$', 'N'),
                 ('q7', '1'): ('q8', 'b', 'L'),
                 ('q8', '1'): ('q8', '1', 'L'),
                 ('q8', '$'): ('qf', '$', 'N')
                 }
    # Unary based TM for multiplication
    elif dmt_type == 'mul':
        return {('q0', '$'): ('q0', '$', 'R'),
                ('q0', '1'): ('q1', 'X', 'R'),
                ('q1', '1'): ('q1', '1', 'R'),
                ('q1', '*'): ('q2', '*', 'R'),
                ('q2', 'Y'): ('q2', 'Y', 'R'),
                ('q2', '1'): ('q3', 'Y', 'R'),
                ('q2', '$'): ('q6', '$', 'L'),
                ('q3', '1'): ('q3', '1', 'R'),
                ('q3', '$'): ('q4', '$', 'R'),
                ('q4', '0'): ('q4', '0', 'R'),
                ('q4', 'b'): ('q5', '0', 'L'),
                ('q5', '0'): ('q5', '0', 'L'),
                ('q5', '$'): ('q5', '$', 'L'),
                ('q5', '1'): ('q5', '1', 'L'),
                ('q5', 'Y'): ('q5', 'Y', 'L'),
                ('q5', '*'): ('q2', '*', 'R'),
                ('q6', 'Y'): ('q6', '1', 'L'),
                ('q6', '*'): ('q7', '*', 'L'),
                ('q7', '1'): ('q7', '1', 'L'),
                ('q7', 'X'): ('q8', 'X', 'R'),
                ('q8', '1'): ('q0', '1', 'N'),
                ('q8', '*'): ('q9', '*', 'R'),
                ('q9', '0'): ('q9', '0', 'R'),
                ('q9', '$'): ('q9', '$', 'R'),
                ('q9', '1'): ('q9', '1', 'R'),
                ('q9', 'b'): ('qf', 'b', 'N'),
                }

# Calculate decimal result for unary based TMs
def count_result(dtm_type,tape):
    cnt = 0
    if dtm_type == 'add' or dtm_type == 'sub':
        for i in range(len(tape)):
            if tape[i] == '1':
                cnt += 1
    elif dtm_type == 'mul':
        for i in range(len(tape)):
            if tape[i] == '0':
                cnt += 1
    return cnt

# Display and export final outputs
def final_output(dtm_type,file_name):
    outputTape = ''

    if dtm_type == 'deter':
        outputTape = t.get_tape()

        print('\nOutput Tape:\n' + outputTape)
        print('\nHalt State:\n' + t.get_state())
        print('\nDTM Result:\n' + t.deter_result())

        f = open(file_name.replace('Input','Output'), "w")
        f.write(outputTape + '\nHalt State: ' + t.get_state()
                           + '\nDTM Result: '  + t.deter_result())
        f.close()

    elif dtm_type == 'add' or dtm_type == 'sub' or dtm_type == 'mul':
        n = count_result(dtm_type, t.get_tape())
        if dtm_type == 'add' or dtm_type == 'sub':
            outputTape = t.get_tape()
        elif dtm_type == 'mul':
            outputTape = t.get_tape()[len(t.get_tape()) - n::].replace('0', '1')

        print('\nOutput Tape:\n' + outputTape)
        print('\nDecimal Result:\n' + str(n))

        f = open(file_name.replace('Input','Output'), "w")
        f.write(outputTape + '\nDecimal Result: ' + str(n))
        f.close()

"""
Driver executes DTM
"""
if __name__ == "__main__":

    # Set directory
    os.chdir('')

    # Choose DTM type; could be 'deter', 'add', 'sub', 'mul'.
    dtm = 'deter'

    # Specify input file to load
    input_file_name = 'DTM_Deter_Input1.txt'
    inputTape = load_input(input_file_name)

    # Construct DTM
    t = DTM(tape=inputTape
            , initial_state='q0'
            , halt_states={'qY', 'qN'} if dtm == 'deter' else {'qf'}
            , trans_function=trans_function(dtm)
            , blank_symbol='b')

    print('\nInput File Name:\n' + input_file_name)
    print('\nInput Tape:\n' + t.get_tape())

    while not t.halt():
        t.states_control()

    final_output(dtm,input_file_name)
