'''You have a list of timestamps. Each timestamp is a time when there was a glitch in the network. 

If 3 or more glitches happen within one second (duration), you need to print the timestamp of the first glitch in that window.

input_lst = [2.1, 2.5, 2.9, 3.0, 3.6, 3.9, 5.2, 5.9, 6.1, 8.2, 10.2, 11.3, 11.8, 11.9]

The output list should be:

[2.1, 5.2, 11.3]

Glitch windows: [2.1, 2.5, 2.9, 3.0], [5.2, 5.9, 6.1], [11.3, 11.8, 11.9]
You can't consider [3.6, 3.9] since the number of glitches < 3

A particular timestamp will fall into one window only. So since 3.0 already fell into the first window, it can't fall into the second window.

Try to solve this today we can discuss tomorrow.'''

input_lst = [2.1, 2.5, 2.9, 3.0, 3.6, 3.9, 5.2, 5.9, 6.1, 8.2, 10.2, 11.3, 11.8, 11.9]

previous_sec = 0
output_list = []

while input_lst:
    try:
        peak_first = input_lst[0]
        peak_third = input_lst[2]
        if (int(peak_first) == int(peak_third) or
            peak_third < int(peak_first)+1.2):
                current_sec = int(peak_first)
                if previous_sec+1.2 > peak_third:
                    previous_sec = peak_third
                    input_lst.pop(0)
                    continue 
                if previous_sec != current_sec:
                    output_list.append(peak_first)
                    previous_sec = current_sec
        input_lst.pop(0)
    except Exception:
        break

print(output_list)
