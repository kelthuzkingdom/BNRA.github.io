from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "BNRA Threat Intelligence Dashboard"

app.layout = html.Div([
    html.H1("🔒 BNRA Threat Intelligence Dashboard"),
    html.Hr(),
    
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("System Status"),
            dbc.CardBody([
                html.H4("🟢 ACTIVE", className="text-success"),
                html.P("All systems operational"),
                html.P("Uptime: 24h 15m")
            ])
        ]), width=6),
        
        dbc.Col(dbc.Card([
            dbc.CardHeader("Threat Alerts"),
            dbc.CardBody([
                html.H4("24", className="text-warning"),
                html.P("Threats detected today"),
                html.P("Last threat: 5 minutes ago")
            ])
        ]), width=6)
    ]),
    
    html.Hr(),
    
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Network Traffic"),
            dbc.CardBody([
                html.P("📊 Monitoring active"),
                html.P("Packets/sec: 1,245"),
                html.P("Active connections: 89")
            ])
        ]), width=4),
        
        dbc.Col(dbc.Card([
            dbc.CardHeader("Social Media"),
            dbc.CardBody([
                html.P("🐦 Twitter: Active"),
                html.P("💬 WhatsApp: Ready"),
                html.P("Posts analyzed: 1,234")
            ])
        ]), width=4),
        
        dbc.Col(dbc.Card([
            dbc.CardHeader("Threat Intelligence"),
            dbc.CardBody([
                html.P("🔍 AI Models: Active"),
                html.P("Accuracy: 94.2%"),
                html.P("False positives: 2.3%")
            ])
        ]), width=4)
    ])
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
