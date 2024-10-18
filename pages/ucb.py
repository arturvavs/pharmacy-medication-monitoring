import dash
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash_ag_grid import AgGrid
import pandas as pd
from warnings import filterwarnings
import database
from sql_p import sql

dash.register_page(__name__, path='/ucb',name='UCB')


layout = html.Div(children=[
    # Cabeçalho
    dbc.Row(
        dbc.Col(html.Div([
            html.Img(src='/assets/logo_branca.png', className='logo'),
            html.H1('LOTES PENDENTES', className='titulo'),
            html.H2('CENTRAL DE DISPENSAÇÃO', className='subtitulo')
        ], className='cabecalho'))
    ),
    
    html.Div([
        dbc.Row([#COLUNA 5º NORTE
            dbc.Col(
                html.Div([
                    dbc.Card([
                        dbc.CardBody([
                            html.H1('1º ANDAR', className='titulo-card'),
                            html.Div(id='lotes-1andar', className='dados-card')
                        ])
                    ], className='card'),

                    html.Div([
                        AgGrid(
                            id='tabela-1andar',
                            columnDefs=[
                                {'headerName': 'LEITO', 'field': 'DS_LEITO', 'width': '50px','headerClass': 'ag-header-cell-label','suppressStickyLabel': True},
                                {'headerName': 'LOTE', 'field': 'NR_SEQUENCIA', 'width': '50px',},
                                {'headerName': 'HORARIO', 'field': 'DT_PRIM_HORARIO', 'width': '60px',},
                                {'headerName': 'ATB', 'field': 'IE_ATB', 'width': '50px','cellRenderer': 'markdown','width': '30px'}
                            ],
                            dashGridOptions={
                                "loadingOverlayComponent": "CustomLoadingOverlay",
                                "loadingOverlayComponentParams": {
                                        "loadingMessage": "Carregando...",
                                        
                                    },
                                "overlayNoRowsTemplate": "Sem lotes pendentes"
                            },
                            dangerously_allow_code=True,
                            columnSize="responsiveSizeToFit",
                            style={"height": 300}
                        )
                    ],style={'width':'400px','padding':'5px'}),
                ]),
                width=6 
            ),
            dbc.Col(# COLUNA 6º NORTE
                html.Div([
                    dbc.Card([
                        dbc.CardBody([
                            html.H1('2º LESTE', className='titulo-card'),
                            html.Div(id='lotes-2leste', className='dados-card')
                        ])
                    ], className='card'),

                    html.Div([
                        AgGrid(
                            id='tabela-2leste',
                            columnDefs=[
                                {'headerName': 'LEITO', 'field': 'DS_LEITO', 'width': '50px','headerClass': 'ag-header-cell-label','suppressStickyLabel': True},
                                {'headerName': 'LOTE', 'field': 'NR_SEQUENCIA', 'width': '50px',},
                                {'headerName': 'HORARIO', 'field': 'DT_PRIM_HORARIO', 'width': '60px',},
                                {'headerName': 'ATB', 'field': 'IE_ATB', 'width': '50px','cellRenderer': 'markdown','width': '30px'}
                            ],
                            dashGridOptions={
                                "loadingOverlayComponent": "CustomLoadingOverlay",
                                "loadingOverlayComponentParams": {
                                        "loadingMessage": "Carregando...",
                                        
                                    },
                                "overlayNoRowsTemplate": "Sem lotes pendentes"
                            },
                            dangerously_allow_code=True,
                            columnSize="responsiveSizeToFit",
                            style={"height": 300}
                        )
                    ],style={'width':'400px','padding':'5px'}),
                ]),
                width=6 
            ),
            dbc.Col( #COLUNA 7º NORTE
                html.Div([
                    dbc.Card([
                        dbc.CardBody([
                            html.H1('3º LESTE', className='titulo-card'),
                            html.Div(id='lotes-3leste', className='dados-card')
                        ])
                    ], className='card'),

                    html.Div([
                        AgGrid(
                            id='tabela-3leste',
                            columnDefs=[
                                {'headerName': 'LEITO', 'field': 'DS_LEITO', 'width': '50px','headerClass': 'ag-header-cell-label','suppressStickyLabel': True},
                                {'headerName': 'LOTE', 'field': 'NR_SEQUENCIA', 'width': '50px',},
                                {'headerName': 'HORARIO', 'field': 'DT_PRIM_HORARIO', 'width': '60px',},
                                {'headerName': 'ATB', 'field': 'IE_ATB', 'width': '50px','cellRenderer': 'markdown','width': '30px'}
                            ],
                            dashGridOptions={
                                "loadingOverlayComponent": "CustomLoadingOverlay",
                                "loadingOverlayComponentParams": {
                                        "loadingMessage": "Carregando...",
                                        
                                    },
                                "overlayNoRowsTemplate": "Sem lotes pendentes"
                            },
                            dangerously_allow_code=True,
                            columnSize="responsiveSizeToFit",
                            style={"height": 300}
                        )
                    ],style={'width':'400px','padding':'5px'}),
                ]),
                width=6 
            ),
        ],style={'display':'flex'})
    ],style={'display':'flex','justify-content':'center'}),

    html.Div([
        dbc.Row([
            dbc.Col([ #COLUNA 5º SUL
                html.Div([
                    dbc.Card([
                        dbc.CardBody([
                            html.H1('3º OESTE', className='titulo-card'),
                            html.Div(id='lotes-3oeste', className='dados-card')
                        ])
                    ], className='card'),
                html.Div([
                        AgGrid(
                            id='tabela-3oeste',
                            columnDefs=[
                                {'headerName': 'LEITO', 'field': 'DS_LEITO', 'width': '50px','headerClass': 'ag-header-cell-label','suppressStickyLabel': True},
                                {'headerName': 'LOTE', 'field': 'NR_SEQUENCIA', 'width': '50px',},
                                {'headerName': 'HORARIO', 'field': 'DT_PRIM_HORARIO', 'width': '60px',},
                                {'headerName': 'ATB', 'field': 'IE_ATB', 'width': '50px','cellRenderer': 'markdown','width': '30px'}
                            ],
                            dashGridOptions={
                                "loadingOverlayComponent": "CustomLoadingOverlay",
                                "loadingOverlayComponentParams": {
                                        "loadingMessage": "Carregando...",
                                        
                                    },
                                "overlayNoRowsTemplate": "Sem lotes pendentes"
                            },
                            dangerously_allow_code=True,
                            columnSize="responsiveSizeToFit",
                            style={"height": 300}
                        )
                    ],style={'width':'400px','padding':'5px'}),
                ]),
            ]),
            dbc.Col([ #COLUNA 6º SUL
                html.Div([
                    dbc.Card([
                        dbc.CardBody([
                            html.H1('UCINCO', className='titulo-card'),
                            html.Div(id='lotes-ucinco', className='dados-card')
                        ])
                    ], className='card'),
                html.Div([
                        AgGrid(
                            id='tabela-ucinco',
                            columnDefs=[
                                {'headerName': 'LEITO', 'field': 'DS_LEITO', 'width': '50px','headerClass': 'ag-header-cell-label','suppressStickyLabel': True},
                                {'headerName': 'LOTE', 'field': 'NR_SEQUENCIA', 'width': '50px',},
                                {'headerName': 'HORARIO', 'field': 'DT_PRIM_HORARIO', 'width': '60px',},
                                {'headerName': 'ATB', 'field': 'IE_ATB', 'width': '50px','cellRenderer': 'markdown','width': '30px'}
                            ],
                            dashGridOptions={
                                "loadingOverlayComponent": "CustomLoadingOverlay",
                                "loadingOverlayComponentParams": {
                                        "loadingMessage": "Carregando...",
                                        
                                    },
                                "overlayNoRowsTemplate": "Sem lotes pendentes"
                            },
                            dangerously_allow_code=True,
                            columnSize="responsiveSizeToFit",
                            style={"height": 300}
                        )
                    ],style={'width':'400px','padding':'5px'}),
                ]),
            ]),
            dbc.Col([#COLUNA 7º SUL
                html.Div([
                    dbc.Card([
                        dbc.CardBody([
                            html.H1('UTI NEO', className='titulo-card'),
                            html.Div(id='lotes-utineo', className='dados-card')
                        ])
                    ], className='card'),
                html.Div([
                        AgGrid(
                            id='tabela-utineo',
                            columnDefs=[
                                {'headerName': 'LEITO', 'field': 'DS_LEITO', 'width': '50px','headerClass': 'ag-header-cell-label','suppressStickyLabel': True},
                                {'headerName': 'LOTE', 'field': 'NR_SEQUENCIA', 'width': '50px',},
                                {'headerName': 'HORARIO', 'field': 'DT_PRIM_HORARIO', 'width': '60px',},
                                {'headerName': 'ATB', 'field': 'IE_ATB', 'width': '50px','cellRenderer': 'markdown','width': '30px'}
                            ],
                            dashGridOptions={
                                "loadingOverlayComponent": "CustomLoadingOverlay",
                                "loadingOverlayComponentParams": {
                                        "loadingMessage": "Carregando...",
                                        
                                    },
                                "overlayNoRowsTemplate": "Sem lotes pendentes"
                            },
                            dangerously_allow_code=True,
                            columnSize="responsiveSizeToFit",
                            style={"height": 300}
                        )
                    ],style={'width':'400px','padding':'5px'}),
                ]),
            ])
        ],style={'display':'flex'}),
    ],style={'display':'flex','justify-content':'center'}),
    dcc.Interval(
            id="interval-component-data",
            interval=10 * 1000,  # Intervalo para atualização automática da página e dos dados
            n_intervals=0,  # Número inicial de intervalos
        ),
],className='container')

@callback(
    Output('lotes-1andar','children'),
    Output('tabela-1andar','rowData'),
    Output('lotes-2leste','children'),
    Output('tabela-2leste','rowData'),
    Output('lotes-3leste','children'),
    Output('tabela-3leste','rowData'),
    Output('lotes-3oeste','children'),
    Output('tabela-3oeste','rowData'),
    Output('lotes-ucinco','children'),
    Output('tabela-ucinco','rowData'),
    Output('lotes-utineo','children'),
    Output('tabela-utineo','rowData'),
    Input('interval-component-data','n_intervals'),
   
)

def update_data(n_intervals):
    atb = '<svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 512 512"><path fill="#b92222" d="M217.4 27.43c-27.9.47-53.1 17.11-64.5 42.84l136.5 41.23c6-35.79-15.5-70.49-50.1-81.02c-6.2-1.88-12.7-2.91-19.2-3.05zm-69.7 60.08c-6.1 35.89 15.4 70.69 50.1 81.19c34.8 10.5 71.9-6.7 86.5-40zm265.5 44.29c-25.3.1-52.2 12.3-72.5 41L215.9 349.7c-33.5 47.4-18.9 97 14.1 120.4c33.1 23.5 84.6 20.8 118.1-26.6l124.7-176.8c33.5-47.5 18.9-97-14.1-120.5c-12.4-8.8-27.3-13.9-43-14.4zm-1.8 17.3c1.3 0 2.6 0 3.8.1c12.1.5 23.5 4.8 33.1 11.7c25.7 18.2 38.6 54.5 9.7 95.4l-64.5 91.5c-35.8-9.6-81.8-42.3-102.7-73l64.7-91.6c16.9-23.9 37-33.7 55.9-34.1M91.25 225.3c-9.62.1-19.11 2.1-27.93 6c-33.11 14.5-50.34 51.5-40.24 86.3l130.72-57.1c-13.1-22.1-36.9-35.5-62.55-35.2m69.65 51.6L30.2 334.1c18.45 31.4 57.3 44 90.6 29.5c33.2-14.6 50.4-51.8 40.1-86.7" /></svg>'
    df_lotes = database.get_data(sql)
    df_lotes['IE_ATB'] = df_lotes['IE_ATB'].apply(lambda x: atb if x == 'ATB' else ' ')
    lotes_1andar = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 117]
    lotes_2leste = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 327]
    lotes_3leste = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 120]
    lotes_3oeste = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 118]
    lotes_ucinco = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 124]
    lotes_utineo = df_lotes[df_lotes["CD_SETOR_ATENDIMENTO"] == 123]
    qt_lotes_1andar = lotes_1andar.shape[0]
    qt_lotes_2leste = lotes_2leste.shape[0]
    qt_lotes_3leste = lotes_3leste.shape[0]
    qt_lotes_3oeste = lotes_3oeste.shape[0]
    qt_lotes_ucinco = lotes_ucinco.shape[0]
    qt_lotes_utineo = lotes_ucinco.shape[0]
    #print(df)
    return qt_lotes_1andar,lotes_1andar.to_dict('records'),qt_lotes_2leste,lotes_2leste.to_dict('records'),qt_lotes_3leste,lotes_3leste.to_dict('records'),qt_lotes_3oeste,lotes_3oeste.to_dict('records'),qt_lotes_ucinco,lotes_ucinco.to_dict('records'),qt_lotes_utineo,lotes_utineo.to_dict('records')