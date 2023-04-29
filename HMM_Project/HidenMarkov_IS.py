from math import *
from hmm import *
class HidenMarkov:

    #A 
    statesSet = {'S1', 'S2', 'S3'}
    
    """
    NOTE:  The probability numbers indicated below are in log2 form.  That is,
    the probability number =  2^number so for example 2^-1 = 0.5,  and 
    2^-2 = 0.25 ... etc.   The reason for this is that Log2 is used to represent
    probabilities so that underflow or overflow is not encounrered.  
    
    If you wish to change the probabilities in the tables below, than simple calculate 
    Log2(probability that you want/need).  For example Log2(0.33) = -0.6252,  and 
    Log2(0.5) = -1,  and so forth. 
    """
    
    #pi:
    start_probability = {'S1': -2, 'S2': -1, 'S3': -2}
    #tau:
    trans_probability = {'S1': {'S1': -1,  'S2': -1.321928,     'S3': -3.321928},
                         'S2'  : {'S1': -float('Inf'),  'S2': -1.,     'S3': -1.},
                         'S3': {'S1': -1.736966,  'S2': -2.321928,     'S3': -1.}}
    #e:
    emit_propability = {'S1': {'A': -1.321928,    'C': -1.736966,  'T': -2.321928,  'G': -3.321928},
                        'S2': {'A': -2.,   'C': -2., 'T': -2., 'G': -2.},
                        'S3': {'A': -3.321928,    'C': -2.321928,  'T': -1.736966,  'G': -1.321928}}

    def __init__(self, input_seq):
        self.input_seq = input_seq
    
    def print_dptable(self,V):
        print ("    ")
        for i in range(len(V)): 
            print ("%7s" % i)
        print

        for y in V[0].keys():
            print ("%.5s: " % y)
            for t in range(len(V)):
                print ("%.7s" % ("%f" % V[t][y]))
            print

    def viterbi(self, obs, states, start_p, trans_p, emit_p):
        V = [{}]

        for state in states:
            V[0][state] = {"prob": pow(10, start_p[state]) * pow(10,emit_p[state][obs[0]]), "prev": None}

        for t in range(1, len(obs)):
            V.append({})

            for state in states:
                max_transition_probability = V[t - 1][states[0]]["prob"] * pow(10,trans_p[states[0]][state])
                previously_selected_state = states[0]

                for previous_state in states[1:]:
                    transition_probability = V[t - 1][previous_state]["prob"] * pow(10,trans_p[previous_state][state])  
                    if transition_probability > max_transition_probability:
                        max_transition_probability = transition_probability
                        previously_selected_state = previous_state

                max_probability = max_transition_probability * pow(10,emit_p[state][obs[t]])
                V[t][state] = {"prob": max_probability, "prev": previously_selected_state}

        for line in dptable(V):
            print(line)

        opt = []
        max_probability = 0.0
        best_state = None
        # Getting the most probable state
       
        for state, data in V[-1].items():    
            if data["prob"] > max_probability:
                max_probability = data["prob"]
                best_state = state
        
        opt.append(best_state)
       
        previous = best_state

        # Back tracking untill you reach the first observation
        for t in range(len(V) - 2, -1, -1):
            opt.insert(0, V[t + 1][previous]["prev"])
            previous = V[t + 1][previous]["prev"]
        

        print ("The most probable hidden path sequence that produced the observed sequence " + input_seq + " is the path: " +" ".join(opt) + " with highest probability of %s" % max_probability)

def dptable(V):
    # Print a table of steps from dictionary
    yield " " * 5 + "     ".join(("%3d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%lf" % v[state]["prob"]) for v in V)


if __name__ == '__main__':
    input_seq = None
    with open("c:/Users/idansim/Dropbox/Masters/Semester 4/CS 223 Bioinformatics/In_Class/Prog_assignemnt_2/hmm_input_seq.txt") as f: # I had to directly path the file  
        input_seq = f.readline().strip()
        print()
        print("HMM input sequence: ", input_seq)
        hm = HidenMarkov(input_seq)
        hm.viterbi(input_seq, list(hm.statesSet), hm.start_probability, hm.trans_probability, hm.emit_propability)

