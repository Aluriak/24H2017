# -*- coding: utf-8 -*-

import defaults as df
import re
from collections import defaultdict
import json

def main():
# ('Sentences', 's18')
# ('WhiteRabbitEasy', 'node_VhTU')
# ('WhiteRabbitLinear', 'node_sZFy')

# ('MissingShadesOfGray', 'message')
# ('Pong', 'prelude')
#    basic_regex = re.compile("/(.*)/(.*)")
    std_regex = re.compile("/(.*)/(prelude|enigma|answer|message)([0-9]?)")
    all_enigmas = defaultdict(dict)


    question_found = False
    prev_key = ''
    prev_subkey = ''
    with open(df.STR_DUMP, 'r', encoding='utf-8') as fd:

        for line in fd:

            std_match = std_regex.match(line)

            if std_match:
                # Question name
                prev_key = std_match.group(1)
                # Answer / enigma + number (optional)
                prev_subkey = std_match.group(2) + std_match.group(3) # TODO to tuple ? : str((, ))

                print("Q FOUND")
                print(prev_key, prev_subkey)


                print(line)
                question_found = True

            elif question_found:

                if line[0] != '/':
#                    print(prev_key, prev_subkey)
                    print("LA", line)
                    try:
                        all_enigmas[prev_key][prev_subkey] += line
                    except KeyError:
                        all_enigmas[prev_key][prev_subkey] = line
                else:
                    question_found = False

    # Handle WhiteRabbit* : /WhiteRabbitLinear/node_hdnl
    #  "AcFZ": "The White Rabbit is gone to \"TvDA\"\n",
    # Handle Sentences : /Sentences/s39
    node_regex = re.compile("/(WhiteRabbitLinear|WhiteRabbitEasy)/node_(.*)")
#    extract_node = re.compile('.* "(.*)"$')
    sentence_regex =  re.compile("/Sentences/(.*)")

    with open(df.STR_DUMP, 'r', encoding='utf-8') as fd:
        for line in fd:

            node_match = node_regex.match(line)
            sentence_match = sentence_regex.match(line)

            if node_match:
                #print(node_match.groups())
                # The next line contains the next node (there is only 1 line (?))
#                next_line_match = extract_node.match(next(fd))
#                print(next_line_match)
#                print(next(fd)[-6:-2]) # Last letters (always)
                # Rapid parse/verif:
                next_line = next(fd)
                if next_line[-7] != '"':
                    all_enigmas[node_match.group(1)][node_match.group(2)] = next_line
                else:
#                all_enigmas[node_match.group(1)][node_match.group(2)] = next_line_match.group(1)
                    all_enigmas[node_match.group(1)][node_match.group(2)] = next_line[-6:-2]

            if sentence_match:
                # Same thing
                all_enigmas["Sentences"][sentence_match.group(1)] = next(fd)

#    print(all_enigmas)

    nb_regex = re.compile("(enigma|answer)([0-9])")

#    for k, v in all_enigmas.items():
#
#        formatted_data = dict()
#
#        for sub_k, sub_v in v.items():
#
#            nb_match = nb_regex.match(sub_k)
#
#            if 'enigma' in sub_k:
#
#                if nb_match:
#                    print(sub_k, nb_match.group(2))
#                    formatted_data[sub_v] = v['answer' + nb_match.group(2)]
#
#
#        if len(formatted_data) != 0:
#            print(formatted_data)
##            all_enigmas[k] = formatted_data


    with open("./mem_dump/formatted.txt", "w", encoding="utf-8") as fd:
        fd.write(json.dumps(all_enigmas, sort_keys=True, indent=4))

    print(len(all_enigmas), "loaded.. GL & HF")


if __name__ == "__main__":

    main()

#TathamUnruly
#SudXtrem
#BracesMatch
#ThreeBigsEviler
#DifferenceEviler
#SimonSays
#Welcome
#AveCaesar
#JustHexa
#JustHexaEvil
#Difference
#DesreverSort
#MissingShadesOfGray
#TinyOverflow
#Sentences
#ThreeBigs
#MrReverse
#RotateAscii
#DearCowTummy
#LostInMaze
#TokenByPairs
#TathamFilling
#WhiteRabbitEasy
#RomanProblems
#DifferenceUnknown
#WhiteRabbitLinear
#Pong

