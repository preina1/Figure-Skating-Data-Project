import streamlit as st
import pandas as pd
import numpy as np
import regex as re
import matplotlib.pyplot as plt
 
st.title('Figure Skating Medals Won by USA in the Winter Olympics')
st.markdown('''This dashboard presents data of the figure skating 
    medals won by the USA in the history of the Winter Olympics. 
    Data Source: [Wikipedia](https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_figure_skating#:~:text=Figure%20skating%20has%20been%20part,29%20representing%20National%20Olympic%20Committees.)''')
st.header('Olympic Medals by Type')
st.subheader('Summary Table')

#load data
men = pd.read_excel('Men Singles Medals Wiki.xlsx')
ladies = pd.read_excel('Ladies Singles Medals Wiki.xlsx')
pairs = pd.read_excel('Pairs Medals Wiki.xlsx')
icedance = pd.read_excel('Ice Dance Medals Wiki.xlsx')

#Data Cleaning for Men's Singles
men = men.set_index(['Games'])
men = men.drop(men.index[2])
men_country = men.loc['details']

inx = np.arange(1,52,2)
men = men.drop(men.index[inx])
#men_new = pd.merge(men, men_country, how='left', left_index=True, right_index=True)
men.reset_index(inplace=True)

games = [x for x in men['Games']]
men_country['Olympic Games'] = games
men_country.reset_index(inplace=True)
men_country.drop('Games', inplace=True, axis=1)
#men_country

men_gold = [x for x in men_country['Gold']]
men_silver = [x for x in men_country['Silver']]
men_bronze = [x for x in men_country['Bronze']]

us_men_gold = []
us_men_silver = []
us_men_bronze = []
us_men_total = []

for country in men_gold:
    #remove whitespace from string
    country = (re.sub('[\s+]', '', country))
    if country == 'UnitedStates':
        gold = 1
        us_men_gold.append(gold)
    else:
        gold = 0
        us_men_gold.append(gold)


for country in men_silver:
    #remove whitespace from string
    country = (re.sub('[\s+]', '', country))
    if country == 'UnitedStates':
        silver = 1
        us_men_silver.append(silver)
    else:
        silver = 0
        us_men_silver.append(silver)


for country in men_bronze:
    #remove whitespace from string
    country = (re.sub('[\s+]', '', country))
    if country == 'UnitedStates':
        bronze = 1
        us_men_bronze.append(bronze)
    else:
        bronze = 0
        us_men_bronze.append(bronze)

total_men=[]       
for i in range(len(us_men_gold)):
    total = us_men_gold[i] + us_men_silver[i] + us_men_bronze[i]
    total_men.append(total)


men_country['Total U.S.'] = total_men
#men_country

#Data Cleaning for Ladies Singles
ladies = ladies.set_index(['Games'])
ladies = ladies.drop(ladies.index[2])
ladies_country = ladies.loc['details']

inx = np.arange(1,52,2)
ladies = ladies.drop(ladies.index[inx])
ladies.reset_index(inplace=True)

games = [x for x in ladies['Games']]
ladies_country['Olympic Games'] = games
ladies_country.reset_index(inplace=True)
ladies_country.drop('Games', inplace=True, axis=1)

ladies_gold = [x for x in ladies_country['Gold']]
ladies_silver = [x for x in ladies_country['Silver']]
ladies_bronze = [x for x in ladies_country['Bronze']]

us_ladies_gold = []
us_ladies_silver = []
us_ladies_bronze = []
us_ladies_total = []

for country in ladies_gold:
    #remove whitespace from string
    country = (re.sub('[\s+]', '', country))
    if country == 'UnitedStates':
        gold = 1
        us_ladies_gold.append(gold)
    else:
        gold = 0
        us_ladies_gold.append(gold)


for country in ladies_silver:
    #remove whitespace from string
    country = (re.sub('[\s+]', '', country))
    if country == 'UnitedStates':
        silver = 1
        us_ladies_silver.append(silver)
    else:
        silver = 0
        us_ladies_silver.append(silver)


for country in ladies_bronze:
    #remove whitespace from string
    country = (re.sub('[\s+]', '', country))
    if country == 'UnitedStates':
        bronze = 1
        us_ladies_bronze.append(bronze)
    else:
        bronze = 0
        us_ladies_bronze.append(bronze)

total_ladies = []

for i in range(len(us_ladies_gold)):
    total = us_ladies_gold[i] + us_ladies_silver[i] + us_ladies_bronze[i]
    total_ladies.append(total)


ladies_country['Total U.S.'] = total_ladies
#ladies_country

#Data Cleaning for Pairs
pairs = pairs.set_index(['Games'])
pairs = pairs.drop(pairs.index[2])
pairs_country = pairs.loc['details']

inx = np.arange(1,52,2)
pairs = pairs.drop(pairs.index[inx])
pairs.reset_index(inplace=True)

games = [x for x in pairs['Games']]
pairs_country['Olympic Games'] = games
pairs_country.reset_index(inplace=True)
pairs_country.drop('Games', inplace=True, axis=1)

pairs_gold = [x for x in pairs_country['Gold']]
pairs_silver = [x for x in pairs_country['Silver']]
pairs_bronze = [x for x in pairs_country['Bronze']]

us_pairs_gold = []
us_pairs_silver = []
us_pairs_bronze = []
us_pairs_total = []

for string in pairs_gold:
    country = string[-4:-1]
    if country == 'USA':
        gold = 1
        us_pairs_gold.append(gold)
    else:
        gold = 0
        us_pairs_gold.append(gold)

for string in pairs_silver:
    if type(string) is float:
        silver = 0
        us_pairs_silver.append(silver)
    else:
        country = string[-4:-1]
        if country == 'USA':
            silver = 1
            us_pairs_silver.append(silver)
        else:
            silver = 0
            us_pairs_silver.append(silver)
        
for string in pairs_bronze:
    country = string[-4:-1]
    if country == 'USA':
        bronze = 1
        us_pairs_bronze.append(bronze)
    else:
        bronze = 0
        us_pairs_bronze.append(bronze)

total_pairs = []
for i in range(len(us_pairs_gold)):
    total = us_pairs_gold[i] + us_pairs_silver[i] + us_pairs_bronze[i]
    total_pairs.append(total)
    
pairs_country['Total U.S.'] = total_pairs
#pairs_country

#Data Cleaning for Ice Dance
icedance = icedance.set_index(['Games'])
#icedance = icedance.drop(icedance.index[2])
icedance_country = icedance.loc['details']

inx = np.arange(1,25,2)
icedance = icedance.drop(icedance.index[inx])
icedance.reset_index(inplace=True)

games = [x for x in icedance['Games']]
icedance_country['Olympic Games'] = games
icedance_country.reset_index(inplace=True)
icedance_country.drop('Games', inplace=True, axis=1)

icedance_gold = [x for x in icedance_country['Gold']]
icedance_silver = [x for x in icedance_country['Silver']]
icedance_bronze = [x for x in icedance_country['Bronze']]

us_icedance_gold = []
us_icedance_silver = []
us_icedance_bronze = []
us_icedance_total = []

for string in icedance_gold:
    country = string[-4:-1]
    if country == 'USA':
        gold = 1
        us_icedance_gold.append(gold)
    else:
        gold = 0
        us_icedance_gold.append(gold)

for string in icedance_silver:
    if type(string) is float:
        silver = 0
        us_icedance_silver.append(silver)
    else:
        country = string[-4:-1]
        if country == 'USA':
            silver = 1
            us_icedance_silver.append(silver)
        else:
            silver = 0
            us_icedance_silver.append(silver)
        
for string in icedance_bronze:
    country = string[-4:-1]
    if country == 'USA':
        bronze = 1
        us_icedance_bronze.append(bronze)
    else:
        bronze = 0
        us_icedance_bronze.append(bronze)

total_icedance = []
for i in range(len(us_icedance_gold)):
    total = us_icedance_gold[i] + us_icedance_silver[i] + us_icedance_bronze[i]
    total_icedance.append(total)
    
icedance_country['Total U.S.'] = total_icedance
#icedance_country

my_zeros = np.zeros(13, dtype=int)
my_zeros = list(my_zeros)

new_icedance_gold = my_zeros + us_icedance_gold
new_icedance_silver = my_zeros + us_icedance_silver
new_icedance_bronze = my_zeros + us_icedance_bronze
#print(new_icedance_gold)

total_icedance_new = []
for i in range(len(new_icedance_gold)):
    total = new_icedance_gold[i] + new_icedance_silver[i] + new_icedance_bronze[i]
    total_icedance_new.append(total)

#Totals by medal type
total_gold = [us_men_gold[i] + us_ladies_gold[i] + us_pairs_gold[i] + new_icedance_gold[i] for i in range(len(us_men_gold))]
total_silver = [us_men_silver[i] + us_ladies_silver[i] + us_pairs_silver[i] + new_icedance_silver[i] for i in range(len(us_men_silver))]
total_bronze = [us_men_bronze[i] + us_ladies_bronze[i] + us_pairs_bronze[i] + new_icedance_bronze[i] for i in range(len(us_men_bronze))]

#ADDING TEAM EVENT MEDALS
total_bronze[23] = total_bronze[23] + 1
total_bronze[24] = total_bronze[24] + 1
total_silver[25] = total_silver[25] + 1

total_team = np.zeros(26, dtype=int)
total_team[23] = 1
total_team[24] = 1
total_team[25] = 1

total_count = [total_gold[i] + total_silver[i] + total_bronze[i] for i in range(len(total_gold))]
 
usa = pd.DataFrame(men_country['Olympic Games'])
usa['Gold'] = total_gold
usa['Silver'] = total_silver
usa['Bronze'] = total_bronze
usa['Total'] = total_count
usa_inx = usa.set_index('Olympic Games')
usa_inx.drop('Total', inplace=True, axis=1)
usa_inx

usa2 = pd.DataFrame(men_country['Olympic Games'])
usa2['Bronze'] = total_bronze
usa2['Silver'] = total_silver
usa2['Gold'] = total_gold
usa2['Total'] = total_count
usa2.set_index(['Olympic Games'])

usa_bycat = pd.DataFrame(men_country['Olympic Games'])
usa_bycat['Men'] = total_men
usa_bycat['Ladies'] = total_ladies
usa_bycat['Pairs'] = total_pairs
usa_bycat['Ice Dance'] = total_icedance_new
usa_bycat['Team'] = total_team
usa_bycat_inx = usa_bycat.set_index('Olympic Games')

#ADD INTERACTIVITY HERE MEDAL TYPE
st.subheader('Medals per Olympics')

with st.form('my_form'):
    selected_olympics = st.selectbox(label='Olympics', options=usa['Olympic Games'])
    submitted = st.form_submit_button('Submit')

    if submitted:

        filtered_olympics = usa[usa['Olympic Games']== selected_olympics]
        filtered_olympics.set_index('Olympic Games', inplace=True)
        #to place separate columns per Olympics
        fo2 = filtered_olympics.T 
        fo2 = fo2.reset_index()
        fo2 = fo2.drop(fo2.index[3])
        fo2 = fo2.rename(columns={'index': 'Type', selected_olympics: 'Count'})
        #fo2

        #BAR CHART 2
        fig2, ax_bar = plt.subplots()
        
        #this is for stacked bars
        #plt.bar(filtered_olympics['Olympic Games'], filtered_olympics['Bronze'], color='darkgoldenrod')
        #plt.bar(filtered_olympics['Olympic Games'], filtered_olympics['Silver'],bottom = filtered_olympics['Bronze'], color='gray')
        #plt.bar(filtered_olympics['Olympic Games'], filtered_olympics['Gold'],bottom = filtered_olympics['Bronze'] + filtered_olympics['Silver'], color='gold')
        
        #this is for separate bars
        c = ['gold', 'gray','darkgoldenrod']
        colors = {'Gold':'gold', 'Silver':'gray', 'Bronze':'darkgoldenrod'}         
        labels = list(colors.keys())
        plt.bar(fo2['Type'], fo2['Count'], color = c)
        #handles plt only to generate label handles
        handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
        plt.legend(handles, labels)

        #plt.legend(['Gold','Silver','Silver'])
        plt.ylabel('Number of medals')
        #plt.title('Medals Won in ')
        #plt.grid(b=True, axis='y')
        fig2.set_figwidth(10)
        fig2.align_xlabels()
        plt.yticks([])

        plt.ylim(0,6)
        plt.yticks([1, 2, 3, 4, 5, 6]) 
        plt.grid(axis = 'y')
        #plt.show()
        #fig2.tight_layout()
        fig2.subplots_adjust(bottom=0.35)

        st.pyplot(fig2)

st.subheader('Summary Chart')

#BAR CHART 2
fig2, ax_bar = plt.subplots()

plt.bar(usa['Olympic Games'], usa['Bronze'],color='darkgoldenrod')
plt.bar(usa['Olympic Games'], usa['Silver'],bottom = usa['Bronze'], color='gray')
plt.bar(usa['Olympic Games'], usa['Gold'],bottom = usa['Bronze'] + usa['Silver'], color='gold')
#plt.bar(usa['Olympic Games'], usa['Total'], bottom = usa['Bronze'] + usa['Silver'] + usa['Gold'], color='blue')
#plt.plot(usa['Olympic Games'], usa['Total'],'-o', color='blue')
plt.legend(['Bronze','Silver','Gold'], fontsize='18')
plt.ylabel('Number of medals', fontsize='18')
#plt.title('USA Olympic Medal Count in Figure Skating by Medal Type')
#plt.grid(b=True, axis='y')
fig2.set_figwidth(20)
fig2.set_figheight(10)
fig2.align_xlabels()
plt.yticks([])

plt.ylim(0,6)
plt.yticks([1, 2, 3, 4, 5, 6], fontsize='18') 
plt.grid(axis = 'y')
plt.xticks(rotation = 45, ha='right', fontsize='18');
fig2.subplots_adjust(bottom=0.35)

st.pyplot(fig2)

#ADD INTERACTIVITY HERE BY CATEGORY
st.header('Olympic Medals by Category')
st.subheader('Summary Table')
usa_bycat_inx

st.subheader('Medals per Olympics')

with st.form('my_form2'):
    selected_olympics = st.selectbox(label='Olympics', options=usa_bycat['Olympic Games'])
    submitted = st.form_submit_button('Submit')

    if submitted:

        filt_ol = usa_bycat[usa_bycat['Olympic Games']== selected_olympics]
        filt_ol.set_index('Olympic Games', inplace=True)
        #to place separate columns per Olympics
        fo3 = filt_ol.T 
        fo3 = fo3.reset_index()
        fo3 = fo3.rename(columns={'index': 'Category', selected_olympics: 'Count'})
        #fo3

        #BAR CHART 4
        fig4, ax_bar = plt.subplots()
        #this is for stacked bar plot
        #plt.bar(filt_ol['Olympic Games'], filt_ol['Men'], color='blue')
        #plt.bar(filt_ol['Olympic Games'], filt_ol['Ladies'],bottom = filt_ol['Men'], color='orange')
        #plt.bar(filt_ol['Olympic Games'], filt_ol['Pairs'], bottom = filt_ol['Men'] + filt_ol['Ladies'], color='green')
        #plt.bar(filt_ol['Olympic Games'], filt_ol['Ice Dance'], bottom = filt_ol['Men'] + filt_ol['Ladies'] + filt_ol['Pairs'], color='purple')
        #plt.bar(filt_ol['Olympic Games'], filt_ol['Team'], bottom = filt_ol['Men'] + filt_ol['Ladies'] + filt_ol['Pairs'] + filt_ol['Ice Dance'], color = 'olive')
        
        #this is for separate bars
        c = ['blue', 'orange','green', 'purple', 'olive']
        colors = {'Men':'blue', 'Ladies':'orange', 'Pairs':'green', 'Ice Dance (added in 1976)':'purple', 'Team (added in 2014)':'olive'}         
        labels = list(colors.keys())
        plt.bar(fo3['Category'], fo3['Count'], color = c)
        #handles plt only to generate label handles
        handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
        plt.legend(handles, labels)

        #plt.legend(['Men','Ladies','Pairs','Ice Dance (added in 1976)', 'Team (added in 2014)'])
        plt.ylabel('Number of medals')
        #plt.title('USA Olympic Medal Count in Figure Skating by Category')
        #plt.grid(b=True, axis='y')
        fig4.set_figwidth(10)
        fig4.align_xlabels()
        plt.yticks([])
        plt.ylim(0,6)        
        plt.yticks([1, 2, 3, 4, 5, 6]) 
        plt.grid(axis='y')
        fig4.subplots_adjust(bottom=0.35)
        fig4.subplots_adjust(bottom=0.35)

        st.pyplot(fig4)

st.subheader('Summary Chart')

#BAR CHART 4
fig4, ax_bar = plt.subplots()

plt.bar(usa_bycat['Olympic Games'], usa_bycat['Men'], color='blue')
plt.bar(usa_bycat['Olympic Games'], usa_bycat['Ladies'],bottom = usa_bycat['Men'], color='orange')
plt.bar(usa_bycat['Olympic Games'], usa_bycat['Pairs'], bottom = usa_bycat['Men'] + usa_bycat['Ladies'], color='green')
plt.bar(usa_bycat['Olympic Games'], usa_bycat['Ice Dance'], bottom = usa_bycat['Men'] + usa_bycat['Ladies'] + usa_bycat['Pairs'], color='purple')
plt.bar(usa_bycat['Olympic Games'], usa_bycat['Team'], bottom = usa_bycat['Men'] + usa_bycat['Ladies'] + usa_bycat['Pairs'] + usa_bycat['Ice Dance'], color = 'olive')
plt.legend(['Men','Ladies','Pairs','Ice Dance (added in 1976)', 'Team (added in 2014)'], fontsize='18')
plt.ylabel('Number of medals', fontsize='18')
#plt.grid(b=True, axis='y')
fig4.set_figwidth(20)
fig4.set_figheight(10)
fig4.align_xlabels()
plt.yticks([])

plt.ylim(0,6)        
plt.yticks([1, 2, 3, 4, 5, 6], fontsize='18') 
plt.grid(axis='y')
plt.xticks(rotation = 45, ha='right', fontsize='18');
fig4.subplots_adjust(bottom=0.35)

st.pyplot(fig4)
