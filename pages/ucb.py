import dash
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash_ag_grid import AgGrid
import pandas as pd
from warnings import filterwarnings
import database
from sql_p import sql,sql_aux
from AgGridParams import getRowStyle,columnDefs,dashGridOptions

dash.register_page(__name__, path='/ucb',name='UCB')


layout = html.Div(children=[
    html.Div([
        html.Img(src='/assets/logo_branca.png', className='logo'),
        html.H1('LOTES PENDENTES',className='titulo'),
        html.H2('CENTRAL DE DISPENSAÇÃO',className='subtitulo'),
    ],className='header'),

    html.Div([
        html.Div([
            dbc.Card([
                html.H1('1º ANDAR',className='titulo-card'),
                html.H2(className='subtitulo-card', id='qt_pendentes_1a')
                    ], className='card'),
            AgGrid(
                id='tabela-1andar',
                columnDefs=columnDefs,
                getRowStyle = getRowStyle,
                dashGridOptions=dashGridOptions,
                dangerously_allow_code=True,
                columnSize="responsiveSizeToFit",
                style={"height": 320}
            )
        ],className='andar-card'),
        html.Div([
            dbc.Card([
                html.H1('2º ANDAR',className='titulo-card'),
                html.H2(className='subtitulo-card', id='qt_pendentes_2a')
                    ], className='card'),
            AgGrid(
                id='tabela-2andar',
                columnDefs=columnDefs,
                getRowStyle = getRowStyle,
                dashGridOptions=dashGridOptions,
                dangerously_allow_code=True,
                columnSize="responsiveSizeToFit",
                style={"height": 320}
            )
        ],className='andar-card'),
        html.Div([
            dbc.Card([
                html.H1('3º OESTE',className='titulo-card'),
                html.H2(className='subtitulo-card', id='qt_pendentes_3oeste')
                    ], className='card'),
            AgGrid(
                id='tabela-3oeste',
                columnDefs=columnDefs,
                getRowStyle = getRowStyle,
                dashGridOptions=dashGridOptions,
                dangerously_allow_code=True,
                columnSize="responsiveSizeToFit",
                style={"height": 320}
            )
        ],className='andar-card')
    ],className='up-row'),
    html.Div([
        html.Div([
            dbc.Card([
                html.H1('UTI NEO',className='titulo-card'),
                html.H2(className='subtitulo-card', id='qt_pendentes_utineo')
                    ], className='card'),
            AgGrid(
                id='tabela-utineo',
                columnDefs=columnDefs,
                getRowStyle = getRowStyle,
                dashGridOptions=dashGridOptions,
                dangerously_allow_code=True,
                columnSize="responsiveSizeToFit",
                style={"height": 320}
            )
        ],className='andar-card'),
        html.Div([
            dbc.Card([
                html.H1('UCINCO',className='titulo-card'),
                html.H2(className='subtitulo-card', id='qt_pendentes_ucinco')
                    ], className='card'),
            AgGrid(
                id='tabela-ucinco',
                columnDefs=columnDefs,
                getRowStyle = getRowStyle,
                dashGridOptions=dashGridOptions,
                dangerously_allow_code=True,
                columnSize="responsiveSizeToFit",
                style={"height": 320}
            )
        ],className='andar-card'),
        html.Div([
            dbc.Card([
                html.H1('3º LESTE',className='titulo-card'),
                html.H2(className='subtitulo-card', id='qt_pendentes_3leste')
                    ], className='card'),
            AgGrid(
                id='tabela-3leste',
                columnDefs=columnDefs,
                getRowStyle = getRowStyle,
                dashGridOptions=dashGridOptions,
                dangerously_allow_code=True,
                columnSize="responsiveSizeToFit",
                style={"height": 320}
            )
        ],className='andar-card')
    ],className='up-row'),

    dcc.Interval(
            id="interval-component-data",
            interval=20 * 1000,
            n_intervals=0,
        ),
],className='container')


@callback(
    Output('tabela-1andar','rowData'),
    Output('tabela-2andar','rowData'),
    Output('tabela-3oeste','rowData'),
    Output('tabela-utineo','rowData'),
    Output('tabela-ucinco','rowData'),
    Output('tabela-3leste','rowData'),
    Output('qt_pendentes_1a','children'),
    Output('qt_pendentes_2a','children'),
    Output('qt_pendentes_3oeste','children'),
    Output('qt_pendentes_utineo','children'),
    Output('qt_pendentes_ucinco','children'),
    Output('qt_pendentes_3leste','children'),
    Input('interval-component-data','n_intervals'),  
)

def update_data(n_intervals):
    atb = '<svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 512 512"><path fill="#b92222" d="M217.4 27.43c-27.9.47-53.1 17.11-64.5 42.84l136.5 41.23c6-35.79-15.5-70.49-50.1-81.02c-6.2-1.88-12.7-2.91-19.2-3.05zm-69.7 60.08c-6.1 35.89 15.4 70.69 50.1 81.19c34.8 10.5 71.9-6.7 86.5-40zm265.5 44.29c-25.3.1-52.2 12.3-72.5 41L215.9 349.7c-33.5 47.4-18.9 97 14.1 120.4c33.1 23.5 84.6 20.8 118.1-26.6l124.7-176.8c33.5-47.5 18.9-97-14.1-120.5c-12.4-8.8-27.3-13.9-43-14.4zm-1.8 17.3c1.3 0 2.6 0 3.8.1c12.1.5 23.5 4.8 33.1 11.7c25.7 18.2 38.6 54.5 9.7 95.4l-64.5 91.5c-35.8-9.6-81.8-42.3-102.7-73l64.7-91.6c16.9-23.9 37-33.7 55.9-34.1M91.25 225.3c-9.62.1-19.11 2.1-27.93 6c-33.11 14.5-50.34 51.5-40.24 86.3l130.72-57.1c-13.1-22.1-36.9-35.5-62.55-35.2m69.65 51.6L30.2 334.1c18.45 31.4 57.3 44 90.6 29.5c33.2-14.6 50.4-51.8 40.1-86.7" /></svg>'
    df_lotes = database.get_data(sql_aux)
    df_lotes['IE_ATB'] = df_lotes['IE_ATB'].apply(lambda x: atb if x == 'ATB' else ' ')

    lotes_1andar = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 117]
    lotes_2andar = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 327]
    #lotes_3andar = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"].isin([120,118])]
    lotes_3oeste = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 118]
    lotes_3leste = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 120]
    lotes_utineo = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 123]
    lotes_ucinco = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 124]

    qt_lotes_1a = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 117].shape[0]
    qt_lotes_2a = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 327].shape[0]
    #qt_lotes_3a = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"].isin([120,118])].shape[0]
    qt_lotes_3oeste = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 118].shape[0]
    qt_lotes_3leste = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 120].shape[0]
    qt_lotes_utineo = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 123].shape[0]
    qt_lotes_ucinco = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 124].shape[0]

    return (lotes_1andar.to_dict('records'),lotes_2andar.to_dict('records'),lotes_3oeste.to_dict('records'),lotes_utineo.to_dict('records'),
    lotes_ucinco.to_dict('records'),lotes_3leste.to_dict('records'),f"[{qt_lotes_1a}]",f"[{qt_lotes_2a}]",f"[{qt_lotes_3oeste}]",f"[{qt_lotes_utineo}]",f"[{qt_lotes_ucinco}]",f"[{qt_lotes_3leste}]"
    )