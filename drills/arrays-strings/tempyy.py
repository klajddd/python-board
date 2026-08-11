#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'solve' function below.

def solve(e):
    # Write your code here

    map_feed = {}
    output = []
    for entry in e:

        # ----------------------

        formatted_entry = [element for element in entry.split()]

        # check what type of trade it is
        if formatted_entry[2] == 'b':

            # check if there are opposite trades in the book
            if 's' in map_feed:
                sell_entries = map_feed['s']
                if formatted_entry[4] == 'm':
                    # implemented market trade
                    sell_entries.sort(key=lambda x: x[5])

                    # while the size of the deal is bigger than zero
                    while int(formatted_entry[3]) > 0:
                        quantity = min(int(sell_entries[0][3]), int(formatted_entry[3]))
                        matched_trade = [
                            formatted_entry[0] + " " + formatted_entry[1] + " " + sell_entries[0][1] + " " +
                            sell_entries[0][5] + " " + str(quantity)]
                        output.append(matched_trade)
                        formatted_entry[3] = str(int(formatted_entry[3]) - quantity)
                        sell_entries[0][3] = str(int(sell_entries[0][3]) - quantity)
                        if int(sell_entries[0][3]) <= 0:
                            sell_entries.pop(0)
                            if len(sell_entries) < 1:
                                map_feed.pop('s', None)

                else:
                    # implement limit trade
                    pass


            # check for limit/market trade
            else:
                if formatted_entry[4] == 'l':

                    # store the trade in the book
                    if 'b' in map_feed:
                        map_feed['b'].append(formatted_entry)
                    else:
                        map_feed['b'] = [formatted_entry]
        # sell trade
        else:
            # check if there are opposite trades in the book
            if 'b' in map_feed:
                buy_entries = map_feed['b']
                if formatted_entry[4] == 'm':
                    # implement market trade scenario
                    for buy_entry in map_feed['b']:
                        if buy_entry[5] >= formatted_entry[5]:
                            # IMPLEMENTED DO DEAL
                            pass
                        else:
                            if formatted_entry[4] == 'l':

                                # store the trade in the book
                                if 's' in map_feed:
                                    map_feed['s'].append(formatted_entry)
                                else:
                                    map_feed['s'] = [formatted_entry]
                else:
                    # implement limit trade scenario
                    buy_entries.sort(key=lambda x: x[5])
                    for buy_entry in buy_entries:
                        if float(buy_entry[5]) >= float(formatted_entry[5]):
                            # perform operation
                            continue
                    if int(formatted_entry[3]) > 0:
                        # store the trade in the book
                        if 's' in map_feed:
                            map_feed['s'].append(formatted_entry)
                        else:
                            map_feed['s'] = [formatted_entry]

            else:
                if formatted_entry[4] == 'l':

                    # store the trade in the book
                    if 's' in map_feed:
                        map_feed['s'].append(formatted_entry)
                    else:
                        map_feed['s'] = [formatted_entry]

        # ----------------------
    #
    # for el in output:
    #     print(el[0][1:len(el[0])])

    output_format = []

    for zentry in output:
        entry = zentry[0].split(" ")
        time = entry[0]
        buy_id = int(entry[1])
        sell_id = int(entry[2])
        price = float(entry[3])
        quantity = int(entry[4])
        output_format_entry = [time, buy_id, sell_id, price, quantity]
        for el in output_format_entry:
            print(el, end=" ")
        print()
        output_format.append(output_format_entry)



    return output_format


if __name__ == '__main__':


    e = ['09:30:00 1 b 100 l 9.99',
    '09:31:00 2 b 1000 l 9.95',
    '09:32:00 3 s 100 l 10.01',
    '09:33:00 4 s 1000 l 10.05',
    '09:41:00 5 b 200 m -1.00']
    solve(e)

