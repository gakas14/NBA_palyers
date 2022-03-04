# Import base streamlit dependency
import streamlit as st
# Import pandas to load the analytics data
import pandas as pd
# Import
from nba import get_data
from data_processing import get_number_of_player
from data_processing import get_most_common_names
# Import subprocess
from subprocess import call

import plotly.express as px

# Set page width to wide
st.set_page_config(layout='wide')

# Create sidebar
st.sidebar.markdown("This dashboard allows you to get the list of all players in NBA history, get the most last and first name of players, also get a comparison of active and no active player.")
st.sidebar.markdown("To get started <ol><li>You can search a particular player.</li> <li>You can see the list of all players</li> "
                    "<li>Comparaison of active and no active player.</li>"
                    "<li>Top 5 of the most common last and first name</li>"
                    "</ol>", unsafe_allow_html=True)
# Imput
player_name = st.text_input('Search for a particular player here <Player full name>', value=" ")
df_player = pd.DataFrame



# Button
if st.button('Get Data'):
    # Reinitialise the player file
    #df_player.to_csv('player.csv')

    # Run the code to get the data
    st.write(player_name.upper(), "'s profile.")
    get_data(player_name)
    #call(['python', 'nba.py', player_name])


    # Load the data for a single player
    df_player = pd.read_csv('player.csv')

    # Show a single player
    df_player

# Load the data for all players
df = pd.read_csv('all_players_list.csv')

# Plot viz
st.write('Number of active and non active players.')
df_status = get_number_of_player(df)
fig = px.histogram(df_status, x=df_status.index, y=df_status.Number_of_Players, color=df_status.index)
st.plotly_chart(fig, use_container_width=True)

# Get the most common last and first name
df_last_name, df_first_name = get_most_common_names(df)

st.write('Top 5 of most common last name at the right and Top 5 of most common first name at the left in NBA History.')
left_col, right_col = st.columns(2)

#st.write('Top 5 of most common last name in NBA History.')
last_name_top5 = df_last_name.head()
fig_last = px.histogram(last_name_top5, x=last_name_top5.index, y=last_name_top5.last_name, color=last_name_top5.index,
                       labels={'index': 'Last Name', 'last_name': 'total names'})
left_col.plotly_chart(fig_last, use_container_width=True)

#st.write('Top 5 of most common first name in NBA History.')
first_name_top5 = df_first_name.head()
fig_first = px.histogram(first_name_top5, x=first_name_top5.index, y=first_name_top5.first_name,
                       color=first_name_top5.index, labels={'index': 'First Name', 'first_name': 'total names'})
right_col.plotly_chart(fig_first, use_container_width=True)


# Show tabular dataframe in streamlit
st.write('Full players list:')
df




