#!/usr/bin/env python
# coding: utf-8

# In[43]:


import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# In[44]:


import pandas as pd
import operator as op
import random as rd
idSet = pd.read_excel("./test/user_profile.xlsx")



# In[45]:


def sort_dict(dic):
    sDict = sorted(dic.items(), key=op.itemgetter(1), reverse=True)
    return sDict


# In[46]:

# 사용자의 ID 처리
idlist = list(idSet.iloc[:,0])
# idNum =  232
# print(idNum)

# In[47]:


def load_file(idNum):
    try:
        data = pd.read_csv("./test/hs_"+str(idNum)+"_m08_0903_1355.csv", index_col = 0, encoding='cp949')
    except FileNotFoundError:
        data = pd.read_csv("./test/hs_"+str(idNum)+"_m08_0903_1356.csv", index_col = 0, encoding='cp949')
        
    return data


# In[48]:


# data = load_file(idNum)


# In[49]:


def time_slice(lst):
    
    cnt = {'0-3시': 0, '3-6시' : 0, '6-9시' : 0, '9-12시' : 0, '12-15시' : 0, '15-18시' : 0, '18-21시' : 0,'21-24시' : 0}
    
    for i in lst:
        if int(i.split()[1][:2]) >= 0 and int(i.split()[1][:2]) <= 2:
            cnt['0-3시'] += 1
        elif int(i.split()[1][:2]) > 2 and int(i.split()[1][:2]) <= 5:
            cnt['3-6시'] += 1
        elif int(i.split()[1][:2]) > 5 and int(i.split()[1][:2]) <= 8:
            cnt['6-9시'] += 1
        elif int(i.split()[1][:2]) > 8 and int(i.split()[1][:2]) <= 11:
            cnt['9-12시'] += 1
        elif int(i.split()[1][:2]) > 11 and int(i.split()[1][:2]) <= 14:
            cnt['12-15시'] += 1
        elif int(i.split()[1][:2]) > 14 and int(i.split()[1][:2]) <= 17:
            cnt['15-18시'] += 1
        elif int(i.split()[1][:2]) > 17 and int(i.split()[1][:2]) <= 20:
            cnt['18-21시'] += 1
        else:
            cnt['21-24시'] += 1

    return cnt


# In[50]:


def go_out_freq(data):
    actList = list(data.loc[data["Act"] == "외출",'Time'])

    if actList == []:
        return [0, 0, "외출 기록 없음"]
    
    cnt = time_slice(actList)    
    cnt = sort_dict(cnt)
    
    total = len(actList)
    mode = cnt[0][1]
    when = cnt[0][0]
    
    for i in range(1,4):
        if cnt[0][1] == cnt[i][1]:
            when += ", "+ cnt[i][0]
    
    return [total, mode, when]


# In[51]:


# go_out_freq(data)


# In[52]:


def talk_with_sooni(data):
    talkLength = 0
    talkLength += len(list(data.loc[pd.isnull(data["STT_1"]) == False, "STT_1"]))
    talkLength += len(list(data.loc[pd.isnull(data["STT_2"]) == False, "STT_2"]))
    talkLength += len(list(data.loc[pd.isnull(data["STT_3"]) == False, "STT_3"]))
    
    return talkLength


# In[53]:


# talk_with_sooni(data)


# In[54]:


def talk_history(data):

    # STT_1에서 사용자의 응답이 있는 경우를 살핀다.
    answerList = list(data.loc[pd.isnull(data["STT_1"]) == False, "STT_1"])

    # 1. 사용자의 응답이 없는 경우
    if answerList == []:
        answer = "대화 기록 없음"

        # 사용자의 응답이 없는 순이의 메세지까지 포함한 내역을 Load한다.
        talkList = list(data.loc[pd.isnull(data["Message_1"]) == False, "Message_1"])

        # 그마저도 없는 경우 두 항목 모두 '대화 기록 없음'
        if talkList == [] or talkList.count("프로그램 메시지") == len(talkList):
            question = "대화 기록 없음"
            return question, answer

        # 있는 경우, 순이의 메세지를 포함해 return
        question = rd.choice(talkList)
    
        while question == "프로그램 메시지":
            question = rd.choice(talkList)
            
        return question, answer

    # 2. 사용자의 응답이 있는 경우
    else:

        # 사용자의 응답과 그에 대응하는 순이의 메세지를 함께 return
        talkList = list(data.loc[pd.isnull(data["STT_1"]) == False, "Message_1"])
        
        index = rd.randrange(len(answerList))
        answer = answerList[index]
        question = talkList[index]        
        
        return question, answer


# In[55]:


# talk_history(data)


# In[56]:


# talkList = list(data.loc[pd.isnull(data["STT_1"]) == False, "Message_1"])


# In[57]:


def contact_sensor(data):
    lst = ["냉장고", "리모콘", "변기", "싱크대", "전자렌지", "창문"]
    result = {'0-3시': [], '3-6시' : [], '6-9시' : [], '9-12시' : [],
              '12-15시' : [], '15-18시' : [], '18-21시' : [],'21-24시' : []}

    for i in lst:

        # lst에 들어있는 항목 중 하나를 뽑아 시간대를 ctClice로 추린다.
        ctList = list(data.loc[data["Z"] == i,'Time'])
        ctSlice = time_slice(ctList)

        # result에 해당 시간대에 맞춰 (lst항목, 해당 시간대에서의 횟수)
        # 를 append하여 추가한다.
        for j in ctSlice:
            result[j].append((i, ctSlice[j]))
    
    return result


# In[58]:

# 사용자의 타임라인을 작성
# 사용자의 기록을 24시간으로 나누어서 각 활동의 시간대를 추출
# 해당 활동을 가장 많이 한 시간대 2~3개를 그래프로 그림


def user_timeline(data):
    lst = [["Z", "약"], ['Z', '프로그램'], ['Z', '리모콘'], ['Act', '휴식'], ['Act', '외출'], ['Act', '취침'], ['Act', '기상']]
    result = {'0-3시': [], '3-6시' : [], '6-9시' : [], '9-12시' : [],
              '12-15시' : [], '15-18시' : [], '18-21시' : [],'21-24시' : []}

    columns = ["음식 섭취", "리모콘", '수면', '기상', '휴식', '실내운동하기', '실외운동하기']
    index = ['0-3시', '3-6시', '6-9시', '9-12시', '12-15시', '15-18시', '18-21시', '21-24시'] 

    # 사용자의 음식 먹는 시간을 추림
    ctList = list(data.loc[(data['Act'] == '음식출납') | (data['Act'] == '음식데우기'), 'Time'])
    ctSlice = time_slice(ctList)
    for j in ctSlice:
        result[j].append(("음식 섭취", ctSlice[j]))

    
    # 사용자의 활동을 정리
    for k, v in lst:

        ctList = list(data.loc[data[k] == v, 'Time'])
        ctSlice = time_slice(ctList)

        for j in ctSlice:
            result[j].append((v, ctSlice[j]))


    # 활동 횟수가 많은 순으로 정렬
    for k, v in result.items():
        result[k] = sorted(v, key=lambda x:x[1], reverse=True)

    print(result)
    
    return result

user_timeline(load_file(276))
# In[59]:


def contact_sensor_sum(data):
    cnt = {"냉장고":0, "리모콘":0, "변기":0, "싱크대":0, "전자렌지":0, "창문":0}
    cnt_mv =  {'수면':0, '기상':0, '낮잠':0, '취미활동':0, '실내운동하기':0, '실외운동하기':0}

    
    for i in list(cnt.keys()):
        ctList = list(data.loc[data["Z"] == i,'Z'])
        cnt[i] += len(ctList)
    
    for k in cnt_mv.keys():
        ctList = list(data.loc[data['State'] == k, 'State'])
        cnt_mv[k] += len(ctList)

    cnt.update(cnt_mv)
    return sort_dict(cnt)


# In[62]:


# print(contact_sensor_sum(data))


#In[]:

def moving_history(data):
    # 데이터 중에서 부동과 매우 활동에 해당하는 내역들을 추출 
    lst = ['수면', '기상', '낮잠', '취미활동', '실내운동하기', '실외운동하기']
    result = {'0-3시': [], '3-6시' : [], '6-9시' : [], '9-12시' : [],
              '12-15시' : [], '15-18시' : [], '18-21시' : [],'21-24시' : []}

    for i in lst:
        # lst에 들어있는 항목 중 하나를 뽑아 시간대를 mvSlice로 추린다.
        mvList = list(data.loc[data['State'] == i, 'Time'])
        mvSlice = time_slice(mvList)

        # 각 시간대에 (항목, 횟수)를 추가, 반환
        for j in mvSlice:
            result[j].append((i, mvSlice[j]))
    
    return result


# In[63]:


def join_program(data):
    programDict = {}
    joinList = list(data.loc[data["Z"] == "프로그램",'State'])
    
    for i in joinList:
        if i in programDict.keys():
            continue
        else:
            programDict[i] = joinList.count(i)
    
    programDict = sort_dict(programDict)
    
    if len(programDict) < 4:
        for i in range(4 - len(programDict)):
            programDict.append(('NaN', 0))
    
    return programDict[:4]


# In[64]:


# result = join_program(data)


# In[65]:


# result


# In[66]:


def talk_over_average(data, tAvg):
    if talk_with_sooni(data) >= tAvg:
        return True
    else:
        return False


# In[67]:


dataSet = {}

talkAvg = 0

for i in idlist:
    dataSet[i] = []
    data = load_file(i)
    
    try:
        data.iloc[0,0]
    except:
        dataSet[i] = [-1]
        continue
    
    talkAvg += talk_with_sooni(data)
    
    dataSet[i].append(go_out_freq(data))

    dataSet[i].append([talk_with_sooni(data), talk_history(data)])
    dataSet[i].append(contact_sensor_sum(data))

    contact_sensor_list = contact_sensor(data)
    moving_history_list = moving_history(data)
    for k in contact_sensor_list.keys():
        contact_sensor_list[k] += moving_history_list[k]
    dataSet[i].append(contact_sensor_list)

    dataSet[i].append(join_program(data))


talkAvg /= len(idlist)

for i in idlist:
    data = load_file(i)
    
    try:
        data.iloc[0,0]
    except:
        continue
    
    dataSet[i][1].insert(1, talk_over_average(data, talkAvg))
    dataSet[i][1].insert(2, talkAvg)




# 사용자 개개인의 데이터 셋을 돌려주는 함수
def user_data(id):
    talkAvg = 0

    dataSet = []
    data = load_file(id)
    
    try:
        data.iloc[0,0]
    except:
        dataSet = [-1]
        
    
    talkAvg += talk_with_sooni(data)
    
    dataSet.append(go_out_freq(data))

    dataSet.append([talk_with_sooni(data), talk_history(data)])
    dataSet.append(contact_sensor_sum(data))

    contact_sensor_list = contact_sensor(data)
    moving_history_list = moving_history(data)
    for k in contact_sensor_list.keys():
        contact_sensor_list[k] += moving_history_list[k]
    dataSet.append(contact_sensor_list)

    dataSet.append(join_program(data))

    talkAvg /= len(idlist)
        
    dataSet[1].insert(1, talk_over_average(data, talkAvg))

    return dataSet

# In[ ]:

# 한글 깨짐 방지
matplotlib.rcParams['font.family'] = 'NanumSquare_ac'
# matplotlib.font_manager._rebuild()

# 아래의 user_pattern 함수에서 활동 분석 부분을 그래프 제외하고 data만 리턴
def user_activity_pattern(data):
    dataActivity = data[3]

    index = ["냉장고", "리모콘", "변기", "싱크대", "전자렌지", "창문", '수면', '기상', '낮잠', '취미활동', '실내운동하기', '실외운동하기']
    columns = ['0-3시', '3-6시', '6-9시', '9-12시', '12-15시', '15-18시', '18-21시', '21-24시']
    df = pd.DataFrame(np.zeros((12, 8)), index=index, columns=columns)

    for k, v in dataActivity.items():
        for sensor, cnt in v:
            df.loc[sensor, k] = cnt

    df_percentage = df.transpose()
    df_percentage = df_percentage.div(df_percentage.sum(axis=1), axis=0)*100
    
    ret = []
    ret.append(df_percentage.iloc[0:2,:])
    ret.append(df_percentage.iloc[2:4,:])
    ret.append(df_percentage.iloc[4:6,:])
    ret.append(df_percentage.iloc[6:8,:])

    return df_percentage


def user_sooni_activity_pattern(data):
    dataSooniActivity = data[-1]
    columns, index = zip(*dataSooniActivity)
    df = pd.DataFrame(np.zeros((len(columns), 2)), columns=["활동 횟수", "순이 활동"])

    for i, item in enumerate(dataSooniActivity):
        df.loc[i, "활동 횟수"] = item[1]
        df.loc[i, "순이 활동"] = item[0]

    return df



# 개인 사용자의 생활 패턴 분석
def user_pattern(id, data):
    global idSet

    dataSooni = data[1]
    dataSensorCnt = data[2]
    dataActivity = data[3]


    # 외출 빈도 분석
    user_age = idSet.loc[id, 'age'] - 5 # idx가 0부터 시작
    freqOutingList = age[user_age].loc[id, ['전체 외출 횟수', '해당 시간 외출 횟수', '가장 많이 나간 시간']].copy()
    freqOutingValues = list(freqOutingList.values)[:2][:]
    freqOutingValues.append(age[user_age]['전체 외출 횟수'].mean())
    plt.bar(['전체 외출 횟수', '해당 시간 외출 횟수', '연령대 평균'], freqOutingValues, color='rgb')
    # plt.show()

    print(f'가장 많이 외출하시는 시간은 {freqOutingList[2]}입니다.')


    # 활동 분석

    # 100% 누적 막대 그래프
    index = ["냉장고", "리모콘", "변기", "싱크대", "전자렌지", "창문", '수면', '기상', '낮잠', '취미활동', '실내운동하기', '실외운동하기']
    columns = ['0-3시', '3-6시', '6-9시', '9-12시', '12-15시', '15-18시', '18-21시', '21-24시']
    df = pd.DataFrame(np.zeros((12, 8)), index=index, columns=columns)
    
    for k, v in dataActivity.items():
        for sensor, cnt in v:
            df.loc[sensor, k] = cnt

    # 각 활동을 한 횟수를 비율로 변환하여 누적 막대 그래프로 표현
    df_percentage = df.transpose()
    df_percentage = df_percentage.div(df_percentage.sum(axis=1), axis=0)*100
    df_percentage.plot(kind="barh", stacked=True, colormap='RdBu')
    plt.box(False)
    plt.title('시간대별 사용자의 패턴 분석')
    # plt.show()


    # 센서에 접촉한 횟수를 파이 그래프로 표현
    pi_label, pi_data = zip(*dataSensorCnt)
    plt.pie(pi_data, labels=pi_label, autopct='%.1f%%')
    plt.legend(loc='upper left')
    plt.title('8월 사용자의 패턴 분석')
    # plt.show()



    # 순이 대화 분석

    # 사용자의 대화 횟수와 연령대의 평균 대화 횟수 비교 그래프
    sooniTalkList = [age[user_age].loc[id, '순이 대화 횟수'], age[user_age]['순이 대화 횟수'].mean()]
    sooniTalkLabel = ['사용자 순이 대화 횟수', '연령대 평균 대화 횟수']
    plt.bar(sooniTalkLabel, sooniTalkList, color='rgb')
    # plt.show()

    # 가장 많이 한 대화 출력
    print(dataSooni[2])

    # 사용자의 활동 횟수와 연령대의 평균 활동 횟수 비교 그래프
    sooniActCntList = [age[user_age].loc[id, '순이 활동 횟수'], age[user_age]['순이 활동 횟수'].mean()]
    sooniActLabel = ['사용자 순이 활동 횟수', '연령대 평균 활동 횟수']
    plt.bar(sooniActLabel, sooniActCntList, color='rgb')
    # plt.show()


    # 사용자가 활동한 것이 있으면 그래프로 출력
    sooniActList = age[user_age].loc[id, '순이 활동']
    if sooniActList[0][0] != 'NaN':
        act, cnt = zip(*sooniActList)
        plt.bar(act, cnt, color='rgb')
        # plt.show()




idSet = pd.read_excel("./test/user_profile.xlsx")
# 프로필 데이터의 age column을 5, 6, 7, 8 로 단순화
idSet['age'] = idSet['age'].apply(lambda x:x//10)

# 프로필 데이터에서 id column을 index로 변경
idSet = idSet.set_index(keys=['id'], inplace=False, drop=True)


# 연령대별 활동의 평균 분석
# 각 연령대별로 사용자의 활동 내역을 묶음

columns = ["냉장고", "리모콘", "변기", "싱크대", "전자렌지", "창문", '수면', '기상', '낮잠', '취미활동', '실내운동하기', '실외운동하기', '전체 외출 횟수', '해당 시간 외출 횟수', '가장 많이 나간 시간', '순이 대화 횟수', '순이 활동 횟수', '순이 활동']

# 각 연령대별 데이터프레임
age_5 = pd.DataFrame(columns=columns)
age_6 = pd.DataFrame(columns=columns)
age_7 = pd.DataFrame(columns=columns)
age_8 = pd.DataFrame(columns=columns)

# 각 연령대의 정보를 저장하는 데이터프레임을 하나의 리스트에 보관하여
# 연령대별 활용이 쉽게 만듬 (단순 idx 참조로 해당 연령대의 데이터프레임을 얻을 수 있음)
age = [age_5, age_6, age_7, age_8]

for i in idlist:
    try:
        # dataSet에서 외출 빈도 수와 센서에 해당되는 정보를 각각 불러옴
        freqOutingCntList = dataSet[i][0]
        sensorCntList = dataSet[i][2]
        sooniTalkCntList = dataSet[i][1]
        sooniActCntList = dataSet[i][4]
    except:
        continue
    user_age = idSet.loc[i, 'age'] - 5
    age[user_age].loc[i, '전체 외출 횟수':'가장 많이 나간 시간'] = freqOutingCntList[:]
    age[user_age].loc[i, '순이 대화 횟수'] = sooniTalkCntList[0]
    age[user_age].loc[i, '순이 활동 횟수'] = sum([i[1] for i in sooniActCntList])
    age[user_age].loc[i, '순이 활동'] = sooniActCntList[:]

    for sensor, cnt in sensorCntList:
        age[user_age].loc[i, sensor] = cnt

# 사용자의 ID에 따른 나이별 생활 패턴 data 가져오기
def user_age_activity_data(id):
    user_age=idSet.loc[id,'age']-5
    data =age[user_age].iloc[:,:12].sum()
    return data

# 사용자의 ID에 따른 나이별 순이 대화 및 활동 data와 연령대 평균 데이터 가져오기 
def user_age_sooni_data(id):
    user_age=idSet.loc[id,'age']-5
    data =age[user_age].iloc[:,15:].mean()
    return data

# 각 연령대별 평균 활동 패턴을 파이 그래프로 구현
# for i, ageData in enumerate(age):
#     plt.pie(ageData.iloc[:,:12].sum(), labels=columns[:12] ,autopct='%.1f%%')
#     plt.title(f'{i+5}0대 사용자의 평균 활동 패턴')
#     plt.show()
    

# user_pattern(276, dataSet[276])


# 정보가 없는 사람들의 경우 처리
def not_found(i):
    pass
