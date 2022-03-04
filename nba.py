from nba_api.stats.static import *
import json
# import data processing function
from data_processing import process_result
# Import sys dependency to extract command line arguments
import sys
import pandas as pd


players_dict = players.get_players()# .get_active_players()

# Export the data as a json file
#with open('export_p.json', 'w') as f:
#    json.dump(players_dict, f)

#print(players_dict)


all_players_list = process_result(players_dict)

#print(all_players_list)

def get_data(name):
    # Get a particular player
    a_player = ''
    #name ='tim duncan' #'tony parker'
    #print(all_players_list)
    for p in range(len(all_players_list)):
        #print(all_players_list.iloc[p])
        if all_players_list.iloc[p]['full_name'].lower() == name.lower():
            a_player = all_players_list.iloc[p]
            a_player.to_csv('player.csv', index=True, index_label='Player_id')
            #found = True
            break

        else:
            #print('Player not find.')
            a_player = pd.DataFrame(columns=['id','full_name','first_name','last_name','is_active'])
            a_player.to_csv('player.csv', index=True)

    #print(a_player)

#get_data('tony parker')

#if __name__ == '__name__':
#    get_data(sys.argv[1])


