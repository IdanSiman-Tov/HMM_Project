# obs = ("normal", "cold", "dizzy")
# states = ("Healthy", "Fever")
# start_p = {"Healthy": 0.6, "Fever": 0.4}
# trans_p = {
#     "Healthy": {"Healthy": 0.7, "Fever": 0.3},
#     "Fever": {"Healthy": 0.4, "Fever": 0.6},
# }
# emit_p = {
#     "Healthy": {"normal": 0.5, "cold": 0.4, "dizzy": 0.1},
#     "Fever": {"normal": 0.1, "cold": 0.3, "dizzy": 0.6},
# }


# # obs = ("A", "T", "G", "C", "C", "G")
# # states=("S1","S2","S3")
# # start_p = {'S1': -2, 'S2': -1, 'S3': -2}
# # #tau:
# # trans_p = {'S1': {'S1': -1,  'S2': -1.321928,     'S3': -3.321928},
# #                         'S2'  : {'S1': -float('Inf'),  'S2': -1.,     'S3': -1.},
# #                         'S3': {'S1': -1.736966,  'S2': -2.321928,     'S3': -1.}}
# # #e:
# # emit_p = {'S1': {'A': -1.321928,    'C': -1.736966,  'T': -2.321928,  'G': -3.321928},
# #                     'S2': {'A': -2.,   'C': -2., 'T': -2., 'G': -2.},
# #                     'S3': {'A': -3.321928,    'C': -2.321928,  'T': -1.736966,  'G': -1.321928}}




# def viterbi(obs, states, start_p, trans_p, emit_p):
#     V = [{}]
#     for st in states:
#         V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}
#     # Run Viterbi when t > 0
#     for t in range(1, len(obs)):
#         V.append({})
#         for st in states:
#             max_tr_prob = V[t - 1][states[0]]["prob"] * trans_p[states[0]][st]
#             prev_st_selected = states[0]
#             for prev_st in states[1:]:
#                 tr_prob = V[t - 1][prev_st]["prob"] * trans_p[prev_st][st]
#                 if tr_prob > max_tr_prob:
#                     max_tr_prob = tr_prob
#                     prev_st_selected = prev_st

#             max_prob = max_tr_prob * emit_p[st][obs[t]]
#             V[t][st] = {"prob": max_prob, "prev": prev_st_selected}

#     for line in dptable(V):
#         print(line)

#     opt = []
#     max_prob = 0.0
#     best_st = None
#     # Get most probable state and its backtrack
#     for st, data in V[-1].items():
#         if data["prob"] > max_prob:
#             max_prob = data["prob"]
#             best_st = st
#     opt.append(best_st)
#     previous = best_st

#     # Follow the backtrack till the first observation
#     for t in range(len(V) - 2, -1, -1):
#         opt.insert(0, V[t + 1][previous]["prev"])
#         previous = V[t + 1][previous]["prev"]

#     print ("The steps of states are " + " ".join(opt) + " with highest probability of %s" % max_prob)

# def dptable(V):
#     # Print a table of steps from dictionary
#     yield " " * 5 + "     ".join(("%3d" % i) for i in range(len(V)))
#     for state in V[0]:
#         yield "%.7s: " % state + " ".join("%.7s" % ("%lf" % v[state]["prob"]) for v in V)

# viterbi(obs,
#         states,
#         start_p,
#         trans_p,
#         emit_p)


# import math
# print("log of 2 is: " + str(math.log(-2)))
print(pow(2,3))