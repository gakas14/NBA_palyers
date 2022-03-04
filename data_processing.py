#  Conver processing code to function
import pandas as pd


def process_result(data):
    df = pd.read_json('export_p.json')
    df = pd.DataFrame(df, columns=['id','full_name','first_name','last_name','is_active'])
    df.set_index('id', inplace=True)
    # Exporting to CSV
    df.to_csv('all_players_list.csv')


    return df


def get_number_of_player(data):
    # Get the number total of active and no active players
    df_status = {}
    df_status = pd.DataFrame(df_status, index=['Active_players', 'No_active_players'], columns=['Number_of_Players'])
    df_status['Number_of_Players'] = [data['is_active'].value_counts()[1], data['is_active'].value_counts()[0]]
    return df_status

def get_most_common_names(data):
    df_last_name = data.last_name.value_counts()
    df_last_name = pd.DataFrame(df_last_name)

    df_first_name = data.first_name.value_counts()
    df_first_name = pd.DataFrame(df_first_name)

    return df_last_name,df_first_name