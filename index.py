import dash
from tkinter.font import names
from dash import Dash, html, dcc, Input, Output, State, callback
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import base64
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import dash_dangerously_set_inner_html
from collections import deque
import random
from datetime import datetime, timedelta
import time
import sqlite3
from plotly.subplots import make_subplots
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from colorama import Fore, Back, Style



#import des csv / excel
df_classeur=pd.read_csv('data/Classeur2.csv', sep=";")
df_prod_of_plast = pd.read_csv('data\global-plastics-production.csv', sep=",|/|\t",engine="python")
df_prod_global=pd.read_csv('data\cumulative-global-plastics.csv', sep=",|/|\t",engine="python")
df_prod2=pd.read_csv('data\Global plastics production (million tonnes)2.csv', sep=",|/|\t",engine="python")
df_cons=pd.read_csv('data\df_cons.csv', sep=",|/|\t",engine="python")
df=pd.read_csv('data\CO2percapita.csv')
df2=pd.read_csv('data\df.csv',sep=",")
dp2=pd.read_csv('data\dechets_plastiques_europe.csv', sep=';',header=0 )
df_cons2=pd.read_csv('data\df_cons2.csv', sep=",")
df_categorie=pd.read_csv('data\df_categorie.csv', sep=",")
pie=pd.read_csv('data/pie.csv', sep=",")
recycle=pd.read_csv('data/recycle.csv', sep=",")
fg=pd.read_csv('data/fg.csv', sep=",")
df_graph=pd.read_csv('data/fg.csv', sep=",")
df_classeur=pd.read_csv('data/Classeur2.csv', sep=",")
proj=pd.read_csv('data\projection.csv', sep=';',header=0 )

#tentative
dechet_hab=70
prix_tonne=1500
result='input1'*dechet_hab

#import des images
menace = 'assets\menace.png.jpeg'
encoded_menace = base64.b64encode(open(menace, 'rb').read())
decode_image_menace = html.Img(src='data:image/png;base64,{}'.format(encoded_menace.decode()),style={'height':'30%', 'width':'67%'})
dramastic = 'assets\Dramastique.png'
encoded_dramastic = base64.b64encode(open(dramastic, 'rb').read())
plastique_dram="assets\save the earth.png"
encoded_plast_dramastic = base64.b64encode(open(plastique_dram, 'rb').read())
bag1="assets/bag_worcloud_en.png"
encoded_bag1 = base64.b64encode(open(bag1, 'rb').read())
bag2="assets/nuage_mots.png"
encoded_bag2 = base64.b64encode(open(bag2, 'rb').read())

#Import couleur
#Import des graphiques indépendants
#SUJET
fig12 = px.pie(pie, values='Tonnes', names='statut', color_discrete_sequence=px.colors.sequential.Teal)
fig12.update_layout(
    title= dict(font=dict(color= '#534340',size=30),
                                text='<b>Plus de 60% du plastique mondial est dans la nature </b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088',
                    barmode="overlay",
                   )

#IMPACT
fig3 = go.Figure(data=[go.Bar(x=df_prod2['Year'],
                            y=df_prod2['max emit'],
                            name='Max(3.5kg/eq)',
                            marker=dict(color='#614124')
                            )])
fig3.add_trace(
    go.Bar(x=df_prod2['Year'],
            y=df_prod2['min emit'],name='Min(1.7kg/eq)',
            marker=dict(color='#CC704B'))
)
fig3.update_layout(
    title= dict(font=dict(color= '#534340',size=30),
                                text='<b>CO2 emission from plastic prod. in kg</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088',
                    barmode="overlay",
                   )
fig3.update_yaxes(title='<b>Global CO2 emission from plastic production in kg</b>')
fig3.update_xaxes(title='Years')
fig5= go.Figure(data=[go.Bar(x=df['Entity'],
                        y=df['CO2eq max'],
                        name='max',
                        marker=dict(color='#614124'))])
fig5.add_trace(
    go.Bar(x=df['Entity'],y=df['CO2eq min'],
            name='min',
            marker=dict(color='#CC704B')
            )
)
fig5.update_layout(barmode='overlay',xaxis={'categoryorder':'total descending'},plot_bgcolor='#E8C07D', paper_bgcolor='#9FC088')
fig5.update_yaxes(title='<b>CO2 emission per capita per day(2010)</b>')
fig5.update_layout(title= dict(font=dict(color= '#534340',size=30),
                                text='<b>CO2 Emission per capita per day</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088')

#PRODUCTION
fig1=go.Figure(data=[go.Scatter(x=df_prod_of_plast.Year,y=df_prod_of_plast['Global plastics production (million tonnes)'],marker_color='#019267')])
fig1.update_layout(
    xaxis_title_text='<b>Year</b>', 
    yaxis_title_text='<b>Global plastics production (miion tonnes)</b>')
fig1.update_layout(
    title= dict(font=dict(color= '#534340',size=30),
                                text='<b>Production of plastic in the world</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088',
                   )
fig1.update_xaxes(color='#534340')
fig1.update_yaxes(color='#534340')
fig2=go.Figure(data=[go.Scatter(x=df_prod_global.Year,y=df_prod_global['Cumulative global plastics production (million tonnes)'],marker_color='#019267')])
fig2.update_layout(
    xaxis_title_text='<b>Year</b>', 
    yaxis_title_text='<b>Cumulative plastics production (miion tonnes)</b>')
fig2.update_layout(
    title= dict(font=dict(color= '#534340',size=30),
                                text='<b>Cumulative of production</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088',
                   )
fig2.update_xaxes(color='#534340')
fig2.update_yaxes(color='#534340')

#CONSOMMATION
fig4= go.Figure(data=[go.Bar(x=df_cons['Pays'],
                        y=df_cons['total'],
                        name='max',
                        marker=dict(color='#614124'))])

fig4.update_layout(barmode='overlay',xaxis={'categoryorder':'total descending'},plot_bgcolor='#E8C07D', paper_bgcolor='#9FC088')
fig4.update_yaxes(title='<b>Consumption in Millions tonnes</b>')
fig4.update_layout(
    title= dict(font=dict(color= '#534340',size=25),
                                text='<b>Plastic consumption over 10 years by country</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088')

map_fig = px.scatter_geo(df_cons2,
                         locations ='alpha3',
                         color='alpha3',
                         size='2019',
                         opacity = .6,height=700)
map_fig.update_layout(title= dict(font=dict(color= '#534340',size=25),
                                text='<b>Plastic map consumption per habitant</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088',
                    
                    )
map_fig.update_geos(
    visible=True, resolution=50, scope="europe")

#TRAITEMENT
fig6 = go.Figure()
fig6.add_trace(go.Bar(y=pd.to_numeric(df2['2018']), x=df2['Country'],marker_color='#019267'))
fig6.update_layout(barmode='overlay', xaxis={'categoryorder':'total descending'})
fig6.update_yaxes(title='<b> Millions tonnes</b>')
fig6.update_layout(
    title= dict(font=dict(color= '#534340',size=25),
                                text='<b> Déchets plastiques par tonne en Europe pour 2018</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088',
                    barmode="overlay",
                   )
fig7 = px.line(dp2, x='Year', y='Union européenne')
fig7.update_layout(title_text='<b>Evolution des déchets plastiques par tonne en Europe</b> \n', title_x=0.5)
fig7.update_layout(
    title= dict(font=dict(color= '#534340',size=25),
                                text='<b>Evolution des déchets plastiques par tonne en Europe</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088',
                    barmode="overlay",
                   )
fig8 = px.bar(df_categorie, x='PLASTICS_APPLICATIONS', y='Value')
fig8.update_layout(yaxis_range=[0,3000])
fig8.update_layout(
    title= dict(font=dict(color= '#534340',size=30),
                                text='<b>Utilisation de plastiques par application</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088')
df_categorie.sort_values('Value',ascending=False,inplace=True)
fig9= go.Figure(data=[go.Bar(x=df_categorie['PLASTICS_APPLICATIONS'],
                        y=df_categorie['Value'],
                        name='',
                        marker=dict(color='#614124'))])


fig9.update_layout(yaxis_range=[0,3000])
fig9.update_yaxes(title='tonnes'),
fig9.update_layout(
   
    title= dict(font=dict(color= '#534340',size=30),
                                text='<b>Utilisation de plastiques par application</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088')

fig11 = go.Figure()



fig11.add_trace(go.Scatter(   x=dp2['Year'], 
                            y=dp2['Italie'],
                            mode='lines',
                            marker_color="red",   
                            name='Italie'))


fig11.add_trace(go.Scatter(   x=dp2['Year'], 
                            y=dp2['Allemagne'],
                            mode='lines',
                            marker_color="blue",
                            name='Allemagne'))


fig11.add_trace(go.Scatter(   x=dp2['Year'],
                            y=dp2['France'],
                            mode='lines', 
                            marker_color= "yellow",
                            name='France'))

fig11.add_trace(go.Scatter(   x=dp2['Year'],
                            y=dp2['Pays-Bas'],
                            mode='lines', 
                            marker_color='purple',
                            name='Pays-Bas'))

fig11.add_trace(go.Scatter(   x=dp2['Year'],
                            y=dp2['Pologne'],
                            mode='lines', 
                            marker_color='blue',
                            name='Pologne'))

fig11.add_trace(go.Scatter(   x=dp2['Year'],
                            y=dp2['Espagne'],
                            mode='lines', 
                            marker_color='orange',
                            name='Espagne'))                          

fig11.add_trace(go.Scatter(   x=dp2['Year'],
                            y=dp2['Belgique'],
                            mode='lines', 
                            marker_color='grey',
                            name='Belgique'))   


fig11.update_layout(
    title= dict(font=dict(color= '#534340',size=30),
                                text='<b>Evolution des déchets des 7 plus gros emetteur par tonne en Europe</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088',
                    barmode="overlay",
                   )

fig13 = px.pie(recycle, values='Tonnes', names='statut', color_discrete_sequence=px.colors.sequential.speed)
fig13.update_layout(
    title= dict(font=dict(color= '#534340',size=30),
                                text='<b>Fin de vie du plastique en Europe en 2017 </b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088',
                    barmode="overlay",
                   )

#TENDANCE
fig14 = go.Figure()
fig14.add_trace(go.Bar(       x=fg['Scenario'], 
                            y=fg['Plastiques collectes'],
                            marker_color="Teal",   
                            name='Plastiques collectés'))
fig14.add_trace(go.Bar(       x=fg['Scenario'], 
                            y=fg['Plastiques pour recyclage'],
                            marker_color="grey",
                            name='Plastiques pour recyclage'))
fig14.update_yaxes(title='Millions tonnes')
fig14.update_layout(
    title= dict(font=dict(color= '#534340',size=30),
                                text='<b>Scenarii 2050 de gestion des déchets plastiques en Europe (Mt) </b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088',
                    barmode="overlay",
                   )


fig15 = go.Figure()



fig15.add_trace(go.Scatter(   x=proj['Year'], 
                            y=proj['Tendance'],
                            mode='lines',
                            marker_color="red",   
                            name='Tendance'))


fig15.add_trace(go.Scatter(  x=proj['Year'], 
                            y=proj['Scenario 1'],
                            mode='lines',
                            marker_color="blue",
                            name='Scenario 1'))


fig15.add_trace(go.Scatter(   x=proj['Year'], 
                            y=proj['Scenario 2'],
                            mode='lines', 
                            marker_color= "yellow",
                            name='Scenario 2'))

fig15.add_trace(go.Scatter(   x=proj['Year'], 
                            y=proj['Scenario 3'],
                            mode='lines', 
                            marker_color='purple',
                            name='Scenario 3'))

fig15.add_trace(go.Scatter(   x=proj['Year'], 
                            y=proj['Scenario 4'],
                            mode='lines', 
                            marker_color='blue',
                            name='Scenario 4'))


fig15.update_layout(
    title= dict(font=dict(color= '#534340',size=30),
                                text='<b>Projection Scenarii commission Européenne</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088',
                    barmode="overlay",
                   )
#PROPOSITION
df6= pd.read_csv('data/recyclage.csv', sep=';')
fig_recyclage = go.Figure(data=[go.Bar(x=df6['Ville'],
                    y=df6['potentiel recyclage en euro'],
                    name='revenu potentiel',
                    marker=dict(color='#614124'),
                    )
                ])

fig_recyclage.add_trace(go.Bar(x=df6['Ville'],
                    y=df6['revenue '],
                    name='revenu actuel',
                    marker=dict(color='#CC704B'),
                    ))

fig_recyclage.update_layout(barmode='overlay',title= dict(font=dict(color= '#534340',size=30),
                                text='<b>Revenu potentiel vs actuel</b>',
                                x= 0.5,
                                y= 0.95),
                    plot_bgcolor='#E8C07D',
                    paper_bgcolor='#9FC088',)
fig_recyclage.update_xaxes(title='Ville')
fig_recyclage.update_yaxes(title='revenu en €')

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
# the styles for the main content position it to the right of the sidebar and
# add some padding.

sidebar = html.Div(
    [   html.Img(src='data:image/png;base64,{}'.format(encoded_dramastic.decode()),style={'height':'25%', 'width':'110%'}),
        html.H6("Team:",style={'textAlign': 'left','font-weight': 'bold' },),
        html.H6("Céline Joret",style={'textAlign': 'left','font-weight': 'bold'},),
        html.H6("César Ozeer",style={'textAlign': 'left','font-weight': 'bold'},),
        html.H6("David Godignon",style={'textAlign': 'left','font-weight': 'bold'},),
        html.H6("François Brasy",style={'textAlign': 'left','font-weight': 'bold'},),
        html.H2("Menu", className="display-2",style={'textAlign': 'left'},),
        html.Hr(),
        html.P(
            "DATATHON", className="lead",style={'textAlign': 'center'}
        ),
        dbc.Nav(
            [
                dbc.NavLink("Présentation du sujet",className="font-weight-bolder", href="/sujet", active="exact"),
                dbc.NavLink("Impact", href="/impact", active="exact"),
                dbc.NavLink("production", href="/production", active="exact"),
                dbc.NavLink("Consommation", href="/conso", active="exact"),
                dbc.NavLink("Traitement et fin de vie", href="/traitement", active="exact"),
                dbc.NavLink("Tendance et objectif", href="/tendance", active="exact"),
                dbc.NavLink("Proposition", href="/proposition", active="exact"),
                
            ],
            vertical=True,
            pills=True,
        ),
        html.Br(),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content")

app = dash.Dash(__name__,  suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.MINTY]
                )

server = app.server
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

layout_sujet = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Le plastique en Europe", style={"textAlign":"center",'font-weight': 'bold','color':'black'})
        ],width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Carousel(
                items=[
                    {"key": "1", "src": "/assets/plast2.jpg", "img_style":{"max-height":"500px"}},
                    {"key": "2", "src": "/assets/ecologie-globale.jpg", "img_style":{"max-height":"500px"}},
                    {"key": "3", "src": "/assets/plast4.jpg", "img_style":{"max-height":"500px"}},
                    {"key": "4", "src": "assets/save the earth.png", "img_style":{"max-height":"500px"}},
                ],
                controls=True,
                indicators=True,
                interval=2000,
                ride="carousel",
#                 className="carousel-fade"
            )
        ], width=8)
    ], justify="center"),
    html.Br(),
    dbc.Row([
        dbc.Col([
            
             dcc.Graph(id='nbre_film_pays',figure=fig12,style={'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}),
             html.H2("Le plastique représente 10% des emissions mondiales de carbone ", style={"textAlign":"center","color":'white'}),
        ],width=12)    
    ])

])




'''html.Div([
    
    html.Img(src='data:image/png;base64,{}'.format(encoded_plast_dramastic.decode()),style={'height':'30%', 'width':'25%'}),
   

])'''
layout_impact =html.Div([
    html.Div([
     html.Br(),
        html.Div(id='output_data2'),
        html.Br(),
        html.Label(['Choix de graphique:'],style={'font-weight': 'bold', "text-align": "center","color":"white"}),
        dcc.Dropdown(id='my_dropdown2',
            options=[
                    {'label':'CO2 from plastic','value': 'impact'},
                    {'label':'CO2 emission per capita per day(2010)','value': 'impact2' },
                               ],
            optionHeight=35,                    
            value='impact',                   
            disabled=False,                     
            multi=False,                       
            searchable=True,                    
            search_value='',                   
            placeholder='Please select...',     
            clearable=True,                    
            style={'width':"100%", 'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}           
            ),                                                                           
    ],className='eight columns'),
    html.Br(),
     dbc.Col([dcc.Graph(id='our_graph2',style={'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}),], lg=12, md=12, sm=12),

])
    
layout_production =html.Div([
    html.Div([
     html.Br(),
        html.Div(id='output_data'),
        html.Br(),
        html.Label(['Choix de graphique:'],style={'font-weight': 'bold', "text-align": "center", "color":"white"}),
        dcc.Dropdown(id='my_dropdown',
            options=[
                    {'label':'Production of plastic in the world','value': 'prod'},
                    {'label':'Cumulative of production','value': 'prod2' },
                               ],
            optionHeight=35,                    
            value='prod',                   
            disabled=False,                     
            multi=False,                       
            searchable=True,                    
            search_value='',                   
            placeholder='Please select...',     
            clearable=True,                    
            style={'width':"100%", 'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}           
            ),                                                                           
    ],className='eight columns'),
    html.Br(),
     dbc.Col([dcc.Graph(id='our_graph',style={'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}),], lg=12, md=12, sm=12),

])
layout_consommation =html.Div([
html.Div([
    html.Div([
     html.Br(),
        html.Div(id='output_data3'),
        html.Br(),
        html.Label(['Choix de graphique:'],style={'font-weight': 'bold', "text-align": "center","color":"white"}),
        dcc.Dropdown(id='my_dropdown3',
            options=[
                    {'label':'plastic consumption over 10 years by country','value': 'cons'},
                    {'label':'Plastic map per habitant','value': 'cons1' },
                    {'label':'Utilisation de plastiques par application','value': 'cons2' },
                               ],
            optionHeight=35,                    
            value='cons',                   
            disabled=False,                     
            multi=False,                       
            searchable=True,                    
            search_value='',                   
            placeholder='Please select...',     
            clearable=True,                    
            style={'width':"100%", 'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}           
            ),                                                                           
    ],className='eight columns'),
    html.Br(),
     dbc.Col([dcc.Graph(id='our_graph3',style={'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}),], lg=12, md=12, sm=12),

])])
layout_traitement =html.Div([
html.Div([
    html.Div([
     html.Br(),
        html.Div(id='output_data4'),
        html.Br(),
        html.Label(['Choix de graphique:'],style={'font-weight': 'bold', "text-align": "center","color":"white"}),
        dcc.Dropdown(id='my_dropdown4',
            options=[
                    {'label':'Déchets plastiques par tonne en Europe pour 2018','value': 'trait'},
                    {'label':'Evolution des déchets plastiques par tonne en Europe','value': 'trait1' },
                    {'label':'Evolution des déchets des 7 plus gros emetteur par tonne en Europe','value': 'trait2' },
                    {'label':'Fin de vie du plastique en Europe en 2017','value': 'trait3' },
                    
                    
                    
                               ],
            optionHeight=35,                    
            value='trait',                   
            disabled=False,                     
            multi=False,                       
            searchable=True,                    
            search_value='',                   
            placeholder='Please select...',     
            clearable=True,                    
            style={'width':"100%", 'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}           
            ),                                                                           
    ],className='eight columns'),
    html.Br(),
     dbc.Col([dcc.Graph(id='our_graph4',style={'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}),], lg=12, md=12, sm=12),

])])
layout_tendance =html.Div([
html.Div([
    html.Div([
     html.Br(),
        html.Div(id='output_data5'),
        html.Br(),
        html.Label(['Choix de graphique:'],style={'font-weight': 'bold', "text-align": "center","color":"white"}),
        dcc.Dropdown(id='my_dropdown5',
            options=[
                    {'label':'Scenarii 2050 de gestion des déchets plastiques en Europe','value': 'tend'},  
                    {'label':'Projection Scenarii commission Européenne','value': 'tend1'}, ],
            optionHeight=35,                    
            value='tend',                   
            disabled=False,                     
            multi=False,                       
            searchable=True,                    
            search_value='',                   
            placeholder='Please select...',     
            clearable=True,                    
            style={'width':"100%", 'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}           
            ),                                                                           
    ],className='eight columns'),
    html.Br(),
     dbc.Col([dcc.Graph(id='our_graph5',style={'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}),], lg=12, md=12, sm=12),
    html.Img(src='data:image/png;base64,{}'.format(encoded_bag2.decode()),style={'height':'30%', 'width':'35%'}),
    html.Img(src='data:image/png;base64,{}'.format(encoded_bag1.decode()),style={'height':'30%', 'width':'35%'}),



])])
layout_proposition =html.Div([   
                              
        html.H1("Simulation de déchet plastique par nombre de population : ",style={'textAlign': 'left','font-weight': 'bold','color':'black'}),
        html.H3("Entre le nombre d'habitant de ta ville : "),
        dcc.Input(id="habitant", type="number", placeholder="Nombre d'habitant"),
        html.Hr(),
        html.Div(id="number-out"),html.Div(id="number-out1"),html.Div(id="number-out2"),html.Div(id="number-out3"),html.Div(id="number-out4"),
        dbc.Col([dcc.Graph(id='graph',style={'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}),], lg=12, md=12, sm=12),
        dbc.Col([dcc.Graph(id='nbre_film_pays',figure=fig_recyclage,style={'box-shadow':'0px 15px 18px 10px rgba(112,112,112,0.4)','border-radius' : '25px'}),], lg=12, md=12, sm=12),
        html.H2("Solutions pour lutter contre la pollution plastique: ",style={'textAlign': 'left','font-weight': 'bold','color':'black'}),
        html.H3("1) Réduire notre consommation de plastique",style={'textAlign': 'left','font-weight': 'bold','color':'black'}),
        html.H3("2) Mesures réglementaires (usage unique/ exportation des déchets) ",style={'textAlign': 'left','font-weight': 'bold','color':'black'}),
        html.H3("3) Recycler le plastique, Le gouvernement vise 100% de plastiques recyclés d’ici 2025 en France ! ",style={'textAlign': 'left','font-weight': 'bold','color':'black'}),
        html.H3("4) Développement des plastiques “verts” (compostage)",style={'textAlign': 'left','font-weight': 'bold','color':'black'}),
        html.H3("5) Enzymes gloutons de plastique ",style={'textAlign': 'left','font-weight': 'bold','color':'black'}),
        html.H2("Projet Dramastic : Incitation locale des citoyens à la réduction du plastique",style={'textAlign': 'left','font-weight': 'bold','color':'black'}),
        ])
@app.callback(
    Output("number-out", "children"),
    Input("habitant", "value"),
)
def number_render(fval):
    return "Les habitants de cette ville produisent en moyenne: {} kg de plastique par an (70kg de plastique/hab)".format(fval*70)
@app.callback(
    Output("number-out1", "children"),
    Input("habitant", "value"),
)
def number_render(fval):
    return "Soit: {} tonne de déchet par an".format(round(fval*70/1000,2))
@app.callback(
    Output("number-out2", "children"),
    Input("habitant", "value"),
)
def number_render(fval):
    return "Le nombre de kilos recyclé est de : {} (22.5% des plastique recyclé seulement".format(round(fval*70*0.29,0))
@app.callback(
    Output("number-out3", "children"),
    Input("habitant", "value"),
)
def number_render(fval):
    return "Soit en moyenne: {} tonnes de déchet recyclé par an ou encore: {} € (1500€ la tonne en moyenne)".format(round(fval*70/1000*0.29,0),round(fval*70/1000*0.29*1500,0))
@app.callback(
    Output("number-out4", "children"),
    Input("habitant", "value"),
)
def number_render(fval):
    return "Il en reste environs {}tonnes de déchet non recyclé par an ou encore {} € (1500€ la tonne en moyenne)".format(round(fval*70/1000*0.71,0),round(fval*70/1000*0.71*1500,0))
@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input("habitant", "value")]
)
def pie_chart(fval):
    X={'recyle' :fval*70/1000*0.29*1500,'notrecyle':fval*70/1000*1500}
    df_test15=pd.DataFrame.from_dict(X,orient='index',columns=['money'])
    fig15 = px.pie(df_test15, values='money', names=['recylé','pas recyclé'], color_discrete_sequence=px.colors.sequential.Teal)

    fig15.update_layout(
        title= dict(font=dict(color= '#534340',size=30),
                                    text='<b>Recyclage en % </b>',
                                    x= 0.5,
                                    y= 0.95),
                        plot_bgcolor='#E8C07D',
                        paper_bgcolor='#9FC088',
                        barmode="overlay")              
    return fig15

#################
    

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/sujet":
        return layout_sujet
    elif pathname == "/impact":
        return layout_impact
    elif pathname == "/production":
        return layout_production
    elif pathname =="/conso":
        return layout_consommation
    elif pathname =="/traitement":
        return layout_traitement
    elif pathname =="/tendance":
        return layout_tendance
    elif pathname =="/proposition":
        return layout_proposition
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
    
#Callback Production
@app.callback(
    Output(component_id='our_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def choose_graph(column_chosen='prod'):
    if column_chosen=='prod':
        return fig1
    elif column_chosen=='prod2':
        return fig2
    
#Callback impact    
@app.callback(
    Output(component_id='our_graph2', component_property='figure'),
    [Input(component_id='my_dropdown2', component_property='value')]
)
def choose_graph(column_chosen='impact'):
    if column_chosen=='impact':
        return fig3
    elif column_chosen=='impact2':
        return fig5
#Callback consommation
@app.callback(
    Output(component_id='our_graph3', component_property='figure'),
    [Input(component_id='my_dropdown3', component_property='value')]
)
def choose_graph(column_chosen='cons'):
    if column_chosen=='cons':
        return fig4
    elif column_chosen=='cons1':
        return map_fig
    elif column_chosen=='cons2':
        return fig9
    
#Callback Traitement
@app.callback(
    Output(component_id='our_graph4', component_property='figure'),
    [Input(component_id='my_dropdown4', component_property='value')]
)
def choose_graph(column_chosen='trait'):
    if column_chosen=='trait':
        return fig6
    elif column_chosen=='trait1':
        return fig7
    elif column_chosen=='trait2':
        return fig11
    elif column_chosen=='trait3':
        return fig13
#Callback Tendance et objectif
@app.callback(
    Output(component_id='our_graph5', component_property='figure') or Output(component_id='image', component_property='src'),
    [Input(component_id='my_dropdown5', component_property='value')]
)
def choose_graph(column_chosen='tend'):
    if column_chosen=='tend':
        return fig14
    if column_chosen=='tend1':
        return fig15
if __name__ == '__main__':
    app.run_server(debug=True)
