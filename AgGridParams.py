# MÉTODO QUE FAZ UMA LINHA BLINKAR DE ACORDO COM AS CONDIÇÕES PASSADAS EM 'CONDITION'
# A ANIMAÇÃO DO BLINK FICA NO CSS, NO QUAL É IMPORTADO PARA A LINHA STYLE, ATRAVÉS DO PARÂMETRO 'ANIMATION:NOME DO ATRIBUTO CSS'
getRowStyle = {
    "styleConditions": [
        {
            "condition": "params.data.TEMPO_RESTANTE <= 30 ",
            "style": {
                "animation": "blink 1s infinite",
                },
            },

        {
            "condition": "params.data.TEMPO_RESTANTE > 30 && params.data.TEMPO_RESTANTE <= 60 ",
            "style": {
                "backgroundColor": "#FFFD55"
                },
        },
    ],
}
#DEFINIÇÃO DAS COLUNAS QUE SERÃO EXIBIDAS NO GRID, ASSIM COMO ALGUNS PARÂMETROS
columnDefs=[
    {'headerName': 'LEITO', 'field': 'DS_LEITO', 'width': '50px','headerClass': 'ag-header-cell-label','suppressStickyLabel': True,"autoHeight": True,"cellStyle": {'fontSize': '1.313rem'}},
    {'headerName': 'LOTE', 'field': 'NR_SEQUENCIA', 'width': '50px',"autoHeight": True,"cellStyle": {'fontSize': '1.313rem'}},
    {'headerName': 'HORARIO', 'field': 'DT_PRIM_HORARIO', 'width': '60px',"autoHeight": True,"cellStyle": {'fontSize': '1.313rem'}},
    {'headerName': 'ATB', 'field': 'IE_ATB', 'width': '50px','cellRenderer': 'markdown','width': '30px',"autoHeight": True},
]


dashGridOptions={
    "loadingOverlayComponent": "CustomLoadingOverlay",
    "loadingOverlayComponentParams": {"loadingMessage": "Carregando...",},
    "overlayNoRowsTemplate": "Sem lotes pendentes"
}