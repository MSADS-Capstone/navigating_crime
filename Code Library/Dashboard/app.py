from dash import Dash, html, dcc, Input, Output
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
from sklearn import metrics
import pickle
app = Dash(__name__)

with open('freq_cols.pkl', 'rb') as f:
    freq_cols = pickle.load(f)

df_roc = pd.read_csv('models.csv')
df_preds_eda = pd.read_csv('df_preds_roc.csv')

server = app.server

models = df_roc.columns[:-1].tolist()

options = {'age_bin': 'Age bin',  'Type': 'Type', 'Victim_Sex': 'Victim Sex', 
           'Victim_Desc': 'Victim Descent', 'Time_of_Day': 'Time of Day', 
           'Month': 'Month', 'AREA_NAME': 'Area Name', 'Premises': 'Premises'}

options_preds = df_preds_eda.drop(columns='Predictions').columns.tolist()

app.layout = html.Div(children=[
    html.H1(children="Dashboard - Identifying Safer Pedestrian Routes in Los Angeles"),
    html.Div([
        html.Div([html.H2(children="Absolute and Normalized Bar Graphs")], style={'text-align': 'center'}),
        dcc.Dropdown(id='col', options=[{'label': val, 'value': key} for key, val in options.items()], value='age_bin'),
        dcc.Graph(id='bar-graph' )
        ], style={'width': '50%', 'display': 'inline-block'}),
    html.Div([
        html.Div([html.H2(children="ROC Curves")], style={'text-align': 'center'}),
        dcc.Dropdown(id='model', options=models, value=models, multi=True),
        dcc.Graph(id='roc-graph' )
        ], style={'width': '50%', 'display': 'inline-block'}),
    html.Div([    
        html.Div([html.H2(children="Confusion Matrices")], style={'text-align': 'center'}),        
        dcc.Dropdown(id='model-conf', options=models, value=models[0]),    
        dcc.Graph(id='conf-graph' )
        ], style={'width': '50%', 'display': 'inline-block'}),
    html.Div([            
        html.Div([html.H2(children="Columnar ROC Plots")], style={'text-align': 'center'}),
        dcc.Dropdown(id='roc-col', options=options_preds, value=options_preds[0]),    
        dcc.Graph(id='roc-col-graph' )
        ], style={'width': '50%', 'display': 'inline-block'})
])

@app.callback(
    Output('roc-graph', 'figure'),
    Input('model', 'value')
)
def update_roc(models):
    if type(models) is not list:
        models = [models]
    
    fig = make_subplots(rows=1, cols=1)
    for model in models:
        roc = metrics.roc_curve(df_roc['y_val'], df_roc[model])
        fpr,tpr,thresholds = metrics.roc_curve(df_roc['y_val'], df_roc[model])
        auc = metrics.auc(fpr, tpr)
        fig.add_trace(go.Scatter(x=fpr, y=tpr, name=f'{model}: auc = {auc:.2}'))
    
    fig.add_trace(go.Scatter(x=[0,1], y=[0,1],  showlegend=False, line=dict(color='black', dash='dot')))
    fig.update_layout(title = f'<b>ROC Curves for {model}</b>', height = 800)
    fig.update_xaxes(title_text = '<b>False Positive Rate</b>')
    fig.update_yaxes(title_text = '<b>True Positive Rate</b>')
    return fig

@app.callback(
    Output('bar-graph', 'figure'),
    Input('col', 'value')
)
def update_figure(col):
    color_map = { 'Less Serious': '#00BFC4','More Serious': '#F8766D' }
    #df_stack=df.groupby([col,'crime_severity']).size().reset_index()
    #df_stack['Percentage']=df.groupby([col,'crime_severity']).size().groupby(level=0).apply(lambda 
    #        x:100 * x/float(x.sum())).values
    #df_stack.columns= [col,'crime_severity', 'Counts', 'Percentage']
    #df_stack['Percentage'] = df_stack['Percentage'].map('{:,.2f}%'.format) 
    df_stack = freq_cols[col]

    fig = make_subplots(rows=2, cols=1, vertical_spacing=0.2)

    for name, rows in df_stack.groupby('crime_severity'):
        fig.add_trace(go.Bar(x = rows[col], y = rows['Counts'], name=name, marker_color = color_map[name], legendgroup=name), row=1,col=1)

    for name, rows in df_stack.groupby('crime_severity'):
        fig.add_trace(go.Bar(x = rows[col], y = rows['Percentage'],marker_color = color_map[name], showlegend=False, legendgroup=name), row=2,col=1)

    fig.update_layout(barmode='stack')
    fig.update_layout(title = f'<b>Crime Severity by {col}</b>', height = 800)
    fig.update_xaxes(title_text = f'<b>{col}</b>', row=2, col=1)
    fig.update_yaxes(title_text = '<b>Count</b>', row=1, col=1)
    fig.update_yaxes(title_text = '<b>Frequency</b>', row=2, col=1)
    return fig

@app.callback(
    Output('roc-col-graph', 'figure'),
    Input('roc-col', 'value'))
def update_roc_col(column):
    fig = go.Figure()
    
    # filter by each unique value in column    
    for name, rows in df_preds_eda.groupby(column):               
        # plot roc curve
        fpr, tpr, thresholds = metrics.roc_curve(rows['Crime_Code'], rows['Predictions'])
        y_preds = rows['Predictions']
        y_true = rows['Crime_Code']
        count = len(y_true)
        len_h0 = len(y_true[y_true == 0])
        len_h1 = len(y_true[y_true == 1])
            
        roc_auc = metrics.auc(fpr, tpr)
        
        fig.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name=f'AUC for {name} {column} = {roc_auc:.3f}, count: {len(y_true)}, H0: {len_h0}, H1: {len_h1}'))
    
    fig.update_layout(title = f'ROC Curve for Predictions by {column}', xaxis=dict(title='False Positive Rate'), yaxis=dict(title='True Positive Rate'))
    fig.update_yaxes(range=[0,1])
    fig.update_xaxes(range=[0,1])
    fig.update_layout(legend=dict(orientation='h', xanchor='center', x=0.5, y=-.2), height = 800)
    return fig



@app.callback(
    Output('conf-graph', 'figure'),
    Input('model-conf', 'value'))
def update_conf(model):   

    conf = pd.crosstab(df_roc['y_val'] == 1, df_roc[model] > 0.5)
    fig = px.imshow(conf, text_auto=True)
   
    fig.update_layout(title = f'Conusion matrix for {model}', xaxis=dict(title='Predicted'), yaxis=dict(title='Actual'))
    fig.update_layout( height = 800)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)