from dash import Dash, dcc, html, dash_table, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

# from dashapp import server as application

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.FONT_AWESOME],
)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
df = pd.read_excel('AidDatasGlobalChineseDevelopmentFinanceDataset_v2.0.xlsx', sheet_name='Global_CDF2.0')
year_list = df['Commitment Year'].dropna().unique()
country_list = df['Recipient'].dropna().unique()
indicator_test = df.select_dtypes("float64")
indicator_list = indicator_test.columns.unique()

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(
    html.H2(children='Belt and Road Dataset',
            className="text-center bg-primary text-white p-2",
            ),
        )
    ),
            dbc.Row
                (
                [
                    dbc.Col
                        (
                        dcc.Graph(
                            id='indicator_map_chart',
                            figure={}
                        )
                    )
                ]
            ),
                    dbc.Row
                        (
                        [
                            dbc.Tabs(
                                [
                            dbc.Tab(dcc.Markdown('''
                        
                        **Introduction**
                        
                        
                        The Belt and Road Initiative (BRI) is a global development strategy proposed by the Chinese government in 2013. 
                        It aims to enhance connectivity and promote economic cooperation between countries in Asia, Europe, Africa, and beyond. 
                        The initiative consists of two main components: the Silk Road Economic Belt and the 21st Century Maritime Silk Road.
                        The Silk Road Economic Belt refers to the land-based infrastructure network that seeks to revive the ancient Silk Road 
                        trading routes. It involves the construction of roads, railways, pipelines, and other transportation infrastructure across 
                        Central Asia, the Middle East, and Europe. These projects aim to facilitate trade and boost economic integration among 
                        participating countries. The 21st Century Maritime Silk Road focuses on developing maritime infrastructure and connectivity. It aims to improve 
                        port facilities, construct shipping lanes, and strengthen maritime cooperation between countries in the Indo-Pacific region, 
                        including Southeast Asia, South Asia, and East Africa. The initiative seeks to promote maritime trade and maritime cultural 
                        exchanges. The Belt and Road Initiative emphasizes economic cooperation and seeks to address infrastructure gaps in developing countries. 
                        It aims to foster regional integration, enhance trade, and spur economic growth by connecting markets and facilitating the 
                        flow of goods, capital, and information. It also aims to promote people-to-people exchanges, cultural understanding, and 
                        sustainable development.
                        
                        
                        **_"Since the inauguration of China’s Belt and Road Initiative in 2013, its bold vision has become China’s most important global 
                        economic and foreign policy instrument."_**
                        
                        
                        


                        
                        **Articles**
                        * [China's Massive Belt and Road Initiative](https://www.cfr.org/backgrounder/chinas-massive-belt-and-road-initiative)
                        * [What is China's Belt and Road Initiative?](https://www.chathamhouse.org/2021/09/what-chinas-belt-and-road-initiative-bri)
                        * [China’s $900 billion New Silk Road. What you need to know](https://www.weforum.org/agenda/2017/06/china-new-silk-road-explainer/)
                        * [How China’s Belt and Road Initiative is faring](https://www.gisreportsonline.com/r/belt-road-initiative/)
                        
                        
                        '''),
                                    tab_id="tab1", label="Belt and Road Initiative"),


                        dbc.Tab(dcc.Markdown('''
                            
                        **Criticisms**
                        
                        The Belt and Road Initiative (BRI) has faced several criticisms from various stakeholders. While the initiative aims to promote 
                        economic cooperation and infrastructure development, the following concerns have been raised:

                        1. Debt Trap: One of the primary concerns is the potential debt trap that participating countries may fall into. Critics
                        argue that some projects under the BRI are financially unsustainable and could burden countries with high levels of debt. 
                        There have been cases where countries struggling to repay their loans have had to hand over control of strategic assets or 
                        ports to Chinese companies or even face economic and political pressure.

                        2. Lack of Transparency and Accountability: The BRI has faced criticism for its lack of transparency and accountability in 
                        project selection, bidding processes, and financial arrangements. Critics argue that the lack of openness can lead to corruption,
                        mismanagement, and unequal distribution of benefits. The absence of proper environmental and social impact assessments has also 
                        been raised as a concern.

                        3. Environmental Impact: The BRI has been criticized for its potential adverse environmental impacts. Some infrastructure projects, 
                        such as dams, ports, and railways, may contribute to deforestation, habitat destruction, and pollution. Critics argue that 
                        insufficient environmental safeguards and regulations could lead to ecological damage, particularly in sensitive areas.

                        4. Geopolitical Motives: Some view the BRI as a tool for China to expand its geopolitical influence. Critics argue that the 
                        initiative could be used to gain strategic advantages, access to resources, and control over key transportation routes. 
                        Concerns have been raised about potential political dependencies and the impact on regional stability and sovereignty.

                        5. Labor and Human Rights Concerns: The BRI has faced scrutiny regarding labor and human rights standards in project implementation. 
                        Critics claim that labor conditions, worker safety, and human rights protections may be compromised in some projects, particularly
                        in countries with weak regulations. There have been reports of inadequate labor protections, forced displacement of local communities,
                        and disregard for indigenous rights.

                        6. Unequal Distribution of Benefits: Critics argue that the benefits of the BRI projects may not be evenly distributed among 
                        participating countries. Concerns have been raised about a lack of local job creation, limited technology transfer, and 
                        limited participation of local companies in project contracts. Some argue that the initiative could exacerbate existing 
                        economic inequalities and deepen the dependency of participating countries on China.
                        
                        **_"China’s colossal infrastructure investments may usher in a new era of trade and growth for economies in Asia and beyond. 
                        But skeptics worry that China is laying a debt trap for borrowing governments."_**
                        
                        '''),tab_id="tab2", label="Analysis"),
                        dbc.Tab(
                            dcc.Markdown('''
                        
                        **Full Description**
                        
                        AidData’s Global Chinese Development Finance Dataset, Version 2.0. records the known universe of projects (with development, commercial, or representational intent) supported by official financial and in-kind commitments (or pledges) from China from 2000-2017, with implementation details covering a 22-year period (2000-2021). The dataset captures 13,427 projects worth $843 billion financed by more than 300 Chinese government institutions and state-owned entities across 165 countries in every major region of the world. AidData systematically collected and quality-assured all projects in the dataset using the 2.0 version of our Tracking Underreported Financial Flows (TUFF) methodology.

                        **Funding**: This dataset was made possible through a cooperative agreement (AID-OAA-A-12-00096) between USAID's Global Development Lab and AidData at William and Mary under the Higher Education Solutions Network (HESN) Program. We also gratefully acknowledge financial support from the William and Flora Hewlett Foundation, the Ford Foundation, and the Smith Richardson Foundation. We also acknowledge that previous versions of the dataset would not have been possible without generous financial support from the John D. and Catherine T. MacArthur Foundation, Humanity United, United Nations University-WIDER, the Academic Research Fund of Singapore’s Ministry of Education, and the German Research Foundation.
                        
                        [AidData’s Global Chinese Development Finance Dataset](https://www.aiddata.org/data/aiddatas-global-chinese-development-finance-dataset-version-2-0)
                        '''),
                            tab_id="tab3", label="Data Set Description"),

                            ],
                        id="tabs",
                        active_tab="tab1",
                            )
                            ]
                    ),

    dbc.Row(
        dbc.Col(
            html.H4(children='Belt and Road Tracker',
                    className="text-center bg-primary text-white p-2",
                    ),
        )
    ),
    dbc.Row(
        dbc.Col(
            html.H6(children='Select an Indicator and Year',
                    style={"color": "grey", "backgroundColor": "white"},
                    ),
        )
    ),
    html.Div(

        [
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Dropdown(id='indicator_dropdown',
                                     value='Amount (Nominal)',
                                     options=[
                                         {'label': i, 'value': i} for i in indicator_list

                                     ], multi=False, placeholder='Choose Indicator...'
                                     )
                    ),


                    dbc.Col(
                        dcc.RangeSlider(
                            id="years-range",
                            min=2000,
                            max=2017,
                            step=1,
                            value=[2005, 2006],
                            marks={
                                2000: "2000",
                                2001: "'01",
                                2002: "'02",
                                2003: "'03",
                                2004: "'04",
                                2005: "'05",
                                2006: "'06",
                                2007: "'07",
                                2008: "'08",
                                2009: "'09",
                                2010: "'10",
                                2011: "'11",
                                2012: "'12",
                                2013: "'13",
                                2014: "'14",
                                2015: "'15",
                                2016: "'16",
                                2017: "2017",
                            },
                        ),
                    )
                ]
            )

        ],
    ),
                dbc.Row
                    (
                    [
                    dbc.Col(
                    dcc.Graph(
                        id='indicator_map_chart1',
                        figure={}
                    )
                    ),
                    dbc.Col(
                        dcc.Graph(
                            id='area_chart',
                            figure={}
                        )
                    )
                        ]
                ),
    dbc.Row(
        dbc.Col(
            html.H4(children='Country Explore',
                    className="text-center bg-primary text-white p-2",
                    ),
        )
    ),
    dbc.Row(
        [
    dbc.Col([
        html.H4(children="Set Country category"),
        dcc.Dropdown(id='country_dropdown',
                     value=['Albania', 'Algeria'],
                     options=[
                         {'label': i, 'value': i} for i in country_list

                     ], multi=True, placeholder='Choose Country...'
                     ),
        ]
    ),

    dbc.Col([
        html.H4(children="Set X-axis category"),
        dcc.Dropdown(id='crossfilter-xaxis-column',
                     value='Amount (Nominal)',
                     options=['Implementation Start Year', 'Completion Year',
       'Amount (Original Currency)', 'Amount (Constant USD2017)',
       'Amount (Nominal)', 'Maturity', 'Interest Rate', 'Grace Period',
       'Management Fee', 'Commitment Fee', 'Grant Element',
       'Project Implementation Score', 'Loan Detail Score'

                     ], multi=False, placeholder='Choose X Indicator...'
                     ),
        ]
    ),
            dbc.Col([
                    html.H4(children="Set Y-axis category"),
                dcc.Dropdown(id='crossfilter-yaxis-column',
                             value='Maturity',
                             options=['Implementation Start Year', 'Completion Year',
       'Amount (Original Currency)', 'Amount (Constant USD2017)',
       'Amount (Nominal)', 'Maturity', 'Interest Rate', 'Grace Period',
       'Management Fee', 'Commitment Fee', 'Grant Element',
       'Project Implementation Score', 'Loan Detail Score'

                             ], multi=False, placeholder='Choose y Indicator...'
                             ),
                ]
            ),

dbc.Col([
                    html.H4(children="Set Z-axis category"),
                dcc.Dropdown(id='crossfilter-zaxis-column',
                             value='Amount (Original Currency)',
                             options=['Implementation Start Year', 'Completion Year',
       'Amount (Original Currency)', 'Amount (Constant USD2017)',
       'Amount (Nominal)', 'Maturity', 'Interest Rate', 'Grace Period',
       'Management Fee', 'Commitment Fee', 'Grant Element',
       'Project Implementation Score', 'Loan Detail Score'

                             ], multi=False, placeholder='Choose Z Indicator...'
                             ),
                ]
            ),
            ]
    ),

    html.Div
        (
        [
            dbc.Col(
                [dcc.Graph(
                    id="crossfilter-indicator-scatter",
                    figure={},
                    hoverData={
                        "points": [{"customdata": "Albania"}]
                    },
                ),
                ],
            ),
            dbc.Row
                (
                [
                    dbc.Col
                        (
                        dcc.Graph(
                            id='bar_chart',
                            figure={}
                        )
                    ),
                    dbc.Col
                        (
                        dcc.Graph(
                            id='line_chart',
                            figure={}
                        )
                    )

                ]
            )
        ]
    ),


],
    fluid=True,

)


@app.callback(Output('indicator_map_chart', 'figure'),
              Input('indicator_dropdown', 'value'))
def display_generic_map_chart(indicator):
    dff = df.copy()
    if indicator is None:
        raise PreventUpdate
    else:
        dff = df.groupby(['Recipient'])[indicator].sum().reset_index()
        fig = px.choropleth(dff, locations='Recipient', locationmode='country names', color=indicator,
                            color_continuous_scale=px.colors.sequential.Oranges, title=f'Accumulatted {indicator}',
                            hover_name='Recipient', projection='equirectangular')
        fig.layout.geo.showframe = False
        fig.update_layout(
            title_x=0.5,
            annotations=[dict(
                x=0.55,
                y=-0.1,
                xref='paper',
                yref='paper',
                text='Source: <a href="https://www.aiddata.org/data/aiddatas-global-chinese-development-finance-dataset-version-2-0">\
                    AidData A Research Lab at William and Mary</a>',
                showarrow=False
            )]
        )
        # fig.layout.coloraxis.colorbar.title =\'indicator'
        return fig


@app.callback(Output('indicator_map_chart1', 'figure'),
              Input('years-range', 'value'),
              Input('indicator_dropdown', 'value'))
def display_generic_map_chart(years_chosen, indicator):
    dff = df.copy()

    if indicator is None:
        raise PreventUpdate

    # elif years_chosen[0] == years_chosen[1]:
    #    raise PreventUpdate
    else:
        df1 = dff[dff['Commitment Year'].between(years_chosen[0], years_chosen[1])]
        df_year = df1.groupby(['Recipient'])[indicator].sum().reset_index()
        fig = px.choropleth(df_year, locations='Recipient', locationmode='country names', color=indicator,
                            color_continuous_scale=px.colors.sequential.Oranges, title=f'Total {indicator} from {years_chosen[0]} to {years_chosen[1]}',
                            hover_name='Recipient')
        fig.layout.geo.showframe = False
        fig.update_layout(
            title_x=0.5,
            annotations=[dict(
                x=0.55,
                y=-0.1,
                xref='paper',
                yref='paper',
                text='Source: <a href="https://www.aiddata.org/data/aiddatas-global-chinese-development-finance-dataset-version-2-0">\
                    AidData A Research Lab at William and Mary</a>',
                showarrow=False
            )]
        )
        # fig.layout.coloraxis.colorbar.title =\'indicator'
        return fig

@app.callback(Output('area_chart', 'figure'),
              Input('years-range', 'value'),
              Input('indicator_dropdown', 'value'))
def display_generic_map_chart(years_chosen, indicator):
    dff = df.copy()

    if indicator is None:
        raise PreventUpdate

    # elif years_chosen[0] == years_chosen[1]:
    #    raise PreventUpdate
    else:
        df1 = dff[dff['Commitment Year'].between(years_chosen[0], years_chosen[1])]
        df_year = df1.groupby(['Recipient', 'Recipient Region','Sector Name' ])[indicator].sum().reset_index()
        fig = px.treemap(df_year, path=['Recipient Region', 'Recipient', 'Sector Name'], values=indicator, title=f'Total {indicator} from {years_chosen[0]} to {years_chosen[1]}')
        #fig.layout.geo.showframe = False'Sector Name'
        fig.update_layout(
            title_x=0.5,
            annotations=[dict(
                x=0.55,
                y=-0.1,
                xref='paper',
                yref='paper',
                text='Source: <a href="https://www.aiddata.org/data/aiddatas-global-chinese-development-finance-dataset-version-2-0">\
                    AidData A Research Lab at William and Mary</a>',
                showarrow=False
            )]
        )
        # fig.layout.coloraxis.colorbar.title =\'indicator'
        return fig


@app.callback(Output('bar_chart', 'figure'),
              Input('indicator_dropdown', 'value'),
              Input('country_dropdown', 'value'))
def display_generic_map_chart(indicator, country):
    dff = df.copy()
    if indicator is None or len(country) == 0:
        raise PreventUpdate
    else:
        df1 = dff[dff['Recipient'].isin(country)]
        df_year = df1.groupby(['Commitment Year', 'Recipient'])[indicator].sum().reset_index()
        fig = px.bar(df_year, x="Commitment Year", y=indicator, color='Recipient', barmode='group', title=f'{indicator} by year')
        # fig.layout.coloraxis.colorbar.title =\'indicator'
        fig.update_layout(
            title_x=0.5,
            annotations=[dict(
                x=0.55,
                y=-0.1,
                xref='paper',
                yref='paper',
                text='Source: <a href="https://www.aiddata.org/data/aiddatas-global-chinese-development-finance-dataset-version-2-0">\
                            AidData A Research Lab at William and Mary</a>',
                showarrow=False
            )]
        )
        return fig


@app.callback(Output('line_chart', 'figure'),
              Input('indicator_dropdown', 'value'),
              Input('country_dropdown', 'value'))
def display_generic_map_chart(indicator, country):
    dff = df.copy()
    if indicator is None or len(country) == 0:
        raise PreventUpdate
    else:
        df1 = dff[dff['Recipient'].isin(country)]
        df_year = df1.groupby(['Commitment Year', 'Recipient'])[indicator].sum().reset_index()
        fig = px.line(df_year, x="Commitment Year", y=indicator, color='Recipient', title=f'{indicator} by year')
        # fig.layout.coloraxis.colorbar.title =\'indicator'
        fig.update_layout(
            title_x=0.5,
            annotations=[dict(
                x=0.55,
                y=-0.1,
                xref='paper',
                yref='paper',
                text='Source: <a href="https://www.aiddata.org/data/aiddatas-global-chinese-development-finance-dataset-version-2-0">\
                            AidData A Research Lab at William and Mary</a>',
                showarrow=False
            )]
        )
        return fig

@app.callback(
    Output("crossfilter-indicator-scatter", "figure"),
    Input("crossfilter-xaxis-column", "value"),
    Input("crossfilter-yaxis-column", "value"),
    Input("crossfilter-zaxis-column", "value")
)
def update_graph(
    xaxis_column_name,
    yaxis_column_name,
    zaxis_column_name

):
    dff = df.copy()
    indicator = dff.select_dtypes("float64")
    df2 = pd.merge(indicator, df['Recipient'], left_index=True, right_index=True)
    df2 = df2.groupby('Recipient').sum().reset_index()
    #mean_value_x = dff[xaxis_column_name].mean()
    #mean_value_y = dff[yaxis_column_name].mean()
    #mean_value_z = dff[zaxis_column_name].mean()
    #df1 = dff[dff['Commitment Year'].between(years_chosen[0], years_chosen[1])]
    #dff[xaxis_column_name] = dff[xaxis_column_name].fillna(value=mean_value_x, inplace=True)
    #dff[yaxis_column_name] = dff[yaxis_column_name].fillna(value=mean_value_y, inplace=True)
    #dff[zaxis_column_name] = dff[zaxis_column_name].fillna(value=mean_value_z, inplace=True)

    fig = px.scatter(df2,
        x=xaxis_column_name,
        y=yaxis_column_name,
        size = zaxis_column_name,
        #color = df1['Recipient'],
        hover_name=df2['Recipient']
    )



    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
