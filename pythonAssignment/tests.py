'''
    Sample program to take comma separated names as an input and select 5 random winners
    from them and export the result in a csv.
'''

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'pythonAssignment.settings'

from winners.views import WinnerDecider

winner_decider = WinnerDecider()

# Call the select_winners method to select winners and write them to a CSV file
winners = winner_decider.select_winners()
if isinstance(winners, str):
    print(winners)
else:
    print(f"The top 5 winners are exported to csv.")