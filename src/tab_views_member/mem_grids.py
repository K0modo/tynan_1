"""  SPECIALTY GRID1 COLUMN DEFINITIONS  """

grid1_defaultColDef = {
    'editable': True,
    'sortable': True,
    'filter': True,
    # 'floatingFilter': True,
    'unSortIcon': True,
}

grid1_category_filterparams = {
    'closeOnApply': True,
    'debounceMs': 500,
    'buttons': ['apply', 'clear', 'reset', 'cancel'],
    'filterOptions': ['contains'],

}

grid1_columnDefs = [
    {
        'field': 'mem_acct',
        'headerName': 'ID',
        'filter': False,
        'sortable': False,
        'width': 60
    },
    {
        'field': 'specialty',
        'headerName': 'Specialty',
        'resizable': True,
        'filterParams': grid1_category_filterparams,
        # 'flex': 2

    },
    {
        'field': 'CHARGES',
        'headerName': 'Charges',
        'type': 'rightAligned',
        # 'width': 120,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format('($,.0f')(params.value)"},
        # 'flex': 1
    },
    {
        'field': 'CLAIMS_COUNT',
        'headerName': 'Count',
        'type': 'rightAligned',
        # 'width': 120,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
        # 'flex': 1
    },
    {
        'field': 'AVERAGE',
        'headerName': 'Average',
        'type': 'rightAligned',
        # 'width': 120,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format('($,.0f')(params.value)"},
        # 'flex': 1
    },
    {
        'field': 'MAX',
        'headerName': 'Max',
        'type': 'rightAligned',
        # 'width': 120,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format('($,.0f')(params.value)"},
        # 'flex': 1
    },

    {
        'field': 'DEDUCT_COPAY',
        'headerName': 'CoPay',
        'type': ['rightAligned'],
        # 'width': 120,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format('($,.0f')(params.value)"},
        # 'flex': 1
    },
]

""" The Callback returns "rowData" as a dictionary to this function -> 'make_spec_grid1'
    AG Grid 'rowSelection' option acts on "selectedRows" and "rowData" property"""

# def make_spec_grid1(id):
#
#     grid = dag.AgGrid(
#         id=id,
#         defaultColDef=grid1_defaultColDef,
#         columnDefs=grid1_columnDefs,
#         columnSize='sizeToFit',
#         style={'height': 600},
#         dashGridOptions={
#             'pagination': True,
#             'paginationAutoPageSize': True,
#             'rowSelection': 'single'
#         },
#     )
#
#     return grid

########################################################################################

"""  SPECIALTY GRID2 COLUMN DEFINITIONS  """

spec_grid2_defaultColDef = {
    'sortable': True,
    'filter': True,
    'floatingFilter': False,
    'unSortIcon': True,
    'resizable': True,
    'columnSize': 'autoSize',
}

spec_grid2_category_filterparams = {
    'closeOnApply': True,
    'debounceMs': 500,
    'buttons': ['apply', 'clear', 'reset', 'cancel'],
    'filterOptions': ['contains'],
}

spec_grid2_columnDefs = [
    {
        'field': 'specialty',
        'resizable': True,
        'width': 280,
        'filterParams': spec_grid2_category_filterparams,
        # 'flex': 2
    },
    {
        'field': 'trans_date',
        'headerName': 'Date',
    },
    {
        'field': 'claim_id',
        'filterParams': spec_grid2_category_filterparams,
        # 'width': 120
    },
    {
        'field': 'charge_allowed',
        'headerName': 'Charge',
        'type': 'rightAligned',
        # 'width': 120,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format('$,.0f')(params.value)"},
        # 'flex': 1
    },
    {
        'field': 'deduct_copay',
        'headerName': 'CoPay',
        'type': ['rightAligned'],
        # 'width': 130,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format('$,.0f')(params.value)"},
        # 'flex': 1
    },
]

########################################################################################

"""  MEMBER CLAIMS GRID COLUMN DEFINITIONS  """

member_claims_defaultColDef = {
    'sortable': True,
    'filter': True,
    'floatingFilter': False,
    'unSortIcon': True,
    'resizable': True,
    'columnSize': 'autoSize',
}

member_claims_category_filterparams = {
    'closeOnApply': True,
    'debounceMs': 500,
    'buttons': ['apply', 'clear', 'reset', 'cancel'],
    'filterOptions': ['contains'],
}

member_claims_filterparams = {
    'closeOnApply': True,
    'debounceMs': 500,
    'buttons': ['apply', 'clear', 'reset', 'cancel'],
}

member_claims_columnDefs = [
    {'field': 'claim_id',
     'filterParams': member_claims_category_filterparams,
     },
    {'field': 'period',
     'filterParams': member_claims_category_filterparams,
     'filter': 'agNumberColumnFilter',
     },
    {'field': 'injury_disease',
     'filterParams': member_claims_category_filterparams,
     },
    {'field': 'specialty',
     'filterParams': member_claims_category_filterparams,
     },
    {'field': 'facility_class',
     'headerName': 'Facility',
     'filterParams': member_claims_category_filterparams,
     },
    {'field': 'charge_allowed',
     'headerName': 'Charge',
     'filter': 'agNumberColumnFilter',
     'filterParams': member_claims_filterparams,
     'valueFormatter': {"function": "d3.format('$,.0f')(params.value)"},
     },
    {'field': 'deduct_copay',
     'filter': 'agNumberColumnFilter',
     'valueFormatter': {"function": "d3.format('$,.0f')(params.value)"},
     },
]
