import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from math import *

from pandas.io.formats import style
from data_preprocessing import *
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots


# 기본적인 stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


app.layout = html.Div(
    className="main",
    children=[

        # 기본적인 인터페이스 부분 구현(Title, id search, ...)
        html.Div(
            className="interface",
            children=[
                html.H1(children='라이프로그 데이터 프로젝트'),
                # 사용자의 입력 받기
                html.Div([
                    html.Div(["ID: ", dcc.Input(id='my-input', value='ID를 입력하세요!', type='text')]
                    ),
                    html.Button(id='submit-button', type='submit', children='Submit'),
                ], className='id-search'),
            ]
        ),

        # html.Br(),
        # html.Div(id='my-output'),

        # 해당 사용자의 id가 없을 경우 메세지
        html.Div([
            dcc.ConfirmDialog(
                id='no-id',
                message="해당 아이디의 사용자가 존재하지 않습니다.",
            )
        ]),

        # 그래프 부분 구현
        html.Div(
            className="graph",
            children = [
            html.Div([
                # 사용자의 activity graph 출력
                html.Div(children=[
                    dcc.Graph(id='activity'),
                ], style={'width':'100%'}),

                # 사용자의 sencor contact pe graph와 해당 연령층 ssensor contact pie grapg 출력
                html.Div(children=[
                    dcc.Graph(id='sensor'),
                ], style={'width':'100%'}),
            ], style={'float':'left', 'width':'50%'}),


            ## 스타일 수정 필요
            html.Div([
                # 사용자의 순이 대화 분석 dialog 출력
                html.Div(id='sooni-talk', style={'text-align':'center', 'border':'1px solid grey'}),


                # 사용자의 순이 활동 분석 dialog 출력
                html.Div(id='sooni-activity-analysis', style={'text-align':'center'}),


                # 사용자의 순이 활동 분석 그래프 출력
                html.Div([
                    dcc.Graph(id='sooni-activity'),
                ], style={'width':'100%'}),
            ], style={'display':'inline-block', 'width':'50%'}),
        ]),

    ]
)

# 사용자의 입력에 대한 콜백 함수 구현
# id 값을 치고 click 버튼을 누르면 해당 id에 대한 그래프와 정보가 시각화됨.
@app.callback(
    Output('sensor', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my-input', 'value')]
)
def update_activity(clicks,input_value):

    data = user_data(input_value)
    sensor_data = data[2]
    pi_labels, pi_values = zip(*sensor_data)
    age_data = user_age_activity_data(int(input_value))
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.add_trace(go.Pie(labels=pi_labels, values=pi_values, name="activity ratio", title='사용자의 행동 비율'),1,1)
    fig.add_trace(go.Pie(labels=age_data.index, values=age_data, name="age activity ratio",title='동일 연령대 사용자의 행동 비율'),1,2)
    return fig


@app.callback(
    Output('activity', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my-input', 'value')]
)
def update_activity(clicks,input_value):

    data = user_data(input_value)
    activity_data = user_activity_pattern(data)
    activity_figure = px.bar(activity_data, orientation='h', title='activity pattern')
    return activity_figure



# 순이 활동 그래프
@app.callback(
    Output(component_id='sooni-activity', component_property='figure'),
    [Input(component_id='submit-button', component_property='n_clicks')],
    [State('my-input', 'value')],
)
def update_sooni_activity_fig(clicks, input_value):

    # 사용자 데이터 불러오기
    data = user_data(input_value)
    sooni_activity_data = user_sooni_activity_pattern(data) # data return 하는것으로 바꾸기
    
    sooni_activity_figure = px.bar(sooni_activity_data, x='순이 활동', y='활동 횟수', color='순이 활동', template='ggplot2', title='순이 활동 분석')
    return sooni_activity_figure


# 순이 활동 분석 dialog
@app.callback(
    Output(component_id='sooni-activity-analysis', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks')],
    [State('my-input', 'value')],
)
def update_sooni_activity_analysis(clicks, input_value):
    # 사용자 데이터 불러오기
    data = user_data(input_value)[-1]
    act, cnt = zip(*data)
    cnt = sum(cnt)  # 순이 활동 횟수의 합계

    # 사용자의 연령대의 데이터 불러오기
    age_data = user_age_sooni_data(int(input_value))
    age_avg_activity_data = ceil(list(age_data)[1])

    return [html.H2('8월 순이 활동 분석'),
                html.H4(f"8월 한달 동안 순이와 {cnt}번의 활동을 하셨어요!"),
                html.H5(f"동일 연령대 분들 평균: {age_avg_activity_data}번")]



@app.callback(
    Output(component_id='sooni-talk', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks')],
    [State('my-input', 'value')],
)
def update_sooni_talk(clicks, input_value):
    # 사용자 데이터 불러오기
    data = user_data(input_value)[1]
    cnt = data[0]

    # 사용자의 연령대의 데이터 불러오기
    age_data = user_age_sooni_data(int(input_value))
    age_avg_activity_data = ceil(list(age_data)[0])

    return [ html.H2("8월 순이 대화 분석"),
                html.H3(f"8월 한달 동안 순이와 {cnt}번 대화하셨어요!"),
                html.H4(f"동일 연령대 분들 평균: {age_avg_activity_data}번")]


@app.callback(
    Output('no-id', 'displayed'),
    [Input('submit-button', 'n_clicks')],
    [State('my-input', 'value')]
)
def check_id_valid(clicks, input_value):
    if clicks is not None:
        try:
            data = pd.read_csv("./test/hs_"+str(input_value)+"_m08_0903_1355.csv", index_col = 0, encoding='cp949')
        except:
            try:
                data = pd.read_csv("./test/hs_"+str(input_value)+"_m08_0903_1356.csv", index_col = 0, encoding='cp949')
            except:
                return True
        return False


@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks')],
    [State('my-input', 'value')],
)
def update_output_div(clicks, input_value):
   if clicks is not None:

        # 사용자 데이터 불러오기
        data = user_data(input_value) # data return 하는것으로 바꾸기
        print(input_value)
        print(data) 




        


if __name__ == '__main__':
    app.run_server()