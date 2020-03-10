# importing the modules useful for data analysis and visualization
import pandas as pd
import plotly.express as px

# reading the data set as a dataframe
PL = pd.read_csv('premier_league.csv')
print(PL)

# representation of chart with rankings of teams at end of championship
# The champion of the 2018-2019 season is Man City and the relegated teams are Cardiff, Fulham and Huddersfield

fig = px.bar(PL, x='Team', y='Position', barmode='group', title = 'Final ranking of championship',color = 'Total_Points',height = 600)
fig.update_layout(xaxis_title='Team name', font=dict(family='Calibri',size=14),title = dict(x = 0.5, y = 0.9,
                  xanchor = 'center',yanchor = 'top'))
fig.show()

# representation of chart which show the defensive of teams
# it is observed that Liverpool has the most powerful defensive(22 goals received) and Fulham has the worst defensive(81 goals received)

PL['Total_Received_Goals'] = PL.Home_received_goals + PL.Away_received_goals
fig1 = px.pie(PL, values='Total_Received_Goals', names='Team', labels= PL.Team,
              title = 'Defensive in championship', height = 600)
fig1.update_layout(font=dict(family='Calibri',size=16),title = dict(x = 0.45, y = 0.9, xanchor = 'center',yanchor = 'top'))
fig1.update_traces(textposition='inside')
fig1.show()

# representation of chart which show the offensive of teams
# it is observed that Man City is the team with the best attack and Huddersfield is the team with the most non-productive attack

PL['Total_Scored_Goals'] = PL.Home_scored_goals + PL.Away_scored_goals
fig2 = px.bar(PL, x='Team', y='Total_Scored_Goals', barmode='group', title = 'Offensive in championship', height = 600)
fig2.update_layout(xaxis_title='Team Name',yaxis_title='Total goals scored', font=dict(family='Calibri',size=14),
                   title = dict(x = 0.5, y = 0.9, xanchor = 'center',yanchor = 'top'))
fig2.show()

# representation of chart which show points per game rate of each team
# it is observed that Man City and Liverpool have the best PPG rate and Huddersfield is the last in the ranking

fig3 = px.scatter(PL, x='Team', y='PPG', color = 'Matches_played', title = 'Points per game (PPG)', height = 600)
fig3.update_layout(xaxis_title='Team name',yaxis_title='Goals per game', font=dict(family='Arial',size=14),
                   title = dict(x = 0.45, y = 0.9, xanchor = 'center',yanchor = 'top'))
fig3.show()

# representation of chart which show the goals difference situations (total scored goals - total received goals)
# it is observed that Huddrsfield have the biggest goals difference and Man City have the smallest goals difference

fig4 = px.bar(PL, x = 'Goals_difference', y='Team', title = 'Goals difference', height = 600, color = 'Total_Points',
              orientation='h')
fig4.update_layout(xaxis_title = 'Goals number', yaxis_title='Team name', font=dict(family='Calibri',size=16),
                   title = dict(x = 0.45, y = 0.9, xanchor = 'center',yanchor = 'top'))
fig4.show()

# representation of chart wich show the situation of draws in championship
# it is observed that Southampton has achieved the most draws this season
# Tottenham and Man City had the least draw at the end of season being equal

PL['Total_Draws'] = PL.Home_Draws + PL.Away_Draws
fig5 = px.bar(PL, x='Team', y='Total_Draws', barmode='group', title='Draws in the championship', height=600)
fig5.update_layout(xaxis_title='Name of teams', yaxis_title='Total draws', font=dict(family='Calibri', size=14),
                   title = dict(x = 0.5, y = 0.9, xanchor = 'center',yanchor = 'top'))
fig.show()

# representation of chart which show the situation of goals scored at home
# it is observed that Man City and Liverpool are at the top of the ranking and Huddersfield is the last in ranking

fig6 = px.density_heatmap(PL, x='Team', y='Home_scored_goals', marginal_x='rug', marginal_y='histogram',
                          color_continuous_scale=px.colors.sequential.Viridis, title = 'Goals scored at home in championship')
fig6.update_layout(xaxis_title='Team name',yaxis_title='Total scored home goals', font=dict(family='Calibri',size=14),
                   title = dict(x = 0.5, y = 0.9, xanchor = 'center',yanchor = 'top'))
fig6.show()

# representation of chart which show the situation of goals scored away
# Southampton, Brighton, Cardiff, Fulham and Huddersfield scored away between 10 and 19 goals
# Man City and Liverpool scored away the most goals

fig7 = px.density_heatmap(PL, x='Team', y='Away_scored_goals', marginal_x='rug', marginal_y='histogram',
                          color_continuous_scale=px.colors.sequential.Plasma, title = 'Goals scored away in championship')
fig7.update_layout(xaxis_title='Team name',yaxis_title='Total scored away goals', font=dict(family='Calibri',size=14),
                   title = dict(x = 0.5, y = 0.9, xanchor = 'center',yanchor = 'top'))
fig7.show()

# representation of chart which show the situation of goals received at home
# Man City, Liverpoo, Arsenal and Tottenham received the fewest goals at home
# Cardiff, Fulham and Huddesfield collected the most goals at home

fig8 = px.density_heatmap(PL, x='Team', y='Home_received_goals', marginal_x='rug', marginal_y='histogram',
                          color_continuous_scale=px.colors.sequential.Inferno, title = 'Goals received at home in championsip')
fig8.update_layout(xaxis_title='Team name',yaxis_title='Total received home goals', font=dict(family='Calibri',size=14),
                   title = dict(x = 0.5, y = 0.9, xanchor = 'center',yanchor = 'top'))
fig8.show()

# representation of chart which show the situation of goals received away
# Again Man City and Liverpool received the least goals away and Fulham and Huddersifield are the last in the ranking

fig9 = px.density_heatmap(PL, x='Team', y='Away_received_goals', marginal_x='rug', marginal_y='histogram',
                          color_continuous_scale=px.colors.sequential.Inferno, title = 'Goals received away in championsip')
fig9.update_layout(xaxis_title='Team name',yaxis_title='Total received away goals', font=dict(family='Calibri',size=14),
                   title = dict(x = 0.5, y = 0.9, xanchor = 'center',yanchor = 'top'))
fig9.show()

# Teams with the best form in the last 5 matches that have reached at least 3 consecutive victories

consecutive_3wins = PL[PL['Form'].str.contains('WWW')]['Team']
print(consecutive_3wins)

# Teams with the worst form in the last 5 matches that have reached at least 3 consecutive losses

consecutive_3losses = PL[PL['Form'].str.contains('LLL')]['Team']
print(consecutive_3losses)
