from line_bot_Luis import *
#1. 今日新增最多國家
sql_cmd_1 = "SELECT * FROM world_situation WHERE day_new = (SELECT MAX(day_new) FROM world_situation WHERE update_time='" + today + "')"
query_data_1 = db.engine.execute(sql_cmd_1)
situation_1 = list(query_data_1)

#2. 染疫人數最多國家
sql_cmd_2 = "SELECT * FROM world_situation WHERE sum = (SELECT MAX(sum) FROM world_situation WHERE update_time='" + today + "')"
query_data_2 = db.engine.execute(sql_cmd_2)
situation_2 = list(query_data_2)

#3. 近7日新增最快國家
sql_cmd_3 = "SELECT * FROM world_situation WHERE update_time='" + today + "'"
query_data_3 = db.engine.execute(sql_cmd_3)
situation_3 = list(query_data_3)

#4. 近7日下降最快國家(不一定是7日可於下方修改)
minus_day = 7   #扣幾日修改處
today = datetime.datetime.today()
today -= datetime.timedelta(days=minus_day)
#print(today.strftime("%Y-%m-%d"))
sql_cmd_4 = "SELECT * FROM world_situation WHERE update_time='" + str(today.strftime("%Y-%m-%d")) + "'"
query_data_4 = db.engine.execute(sql_cmd_4)
situation_4 = list(query_data_4)
#print(len(situation_4))
slope = []
for i in range(len(situation_4)):
    #print(situation_3[i][2])
    #print(situation_4[i][2])
    slope.append((situation_3[i][2] - situation_4[i][2])/7)
slope_max = max(slope)
slope_min = min(slope)

#print("slope_max:",slope_max,"index:",slope.index(slope_max),"country:",situation_3[slope.index(slope_max)][5])
#print("slope_min:",slope_min,"index:",slope.index(slope_min),"country:",situation_3[slope.index(slope_min)][5])

country_1 = situation_1[0][5]
#print(country_1)
country_2 = situation_2[0][5]
#print(country_2)
country_3 = situation_3[slope.index(slope_max)][5]
country_4 = situation_3[slope.index(slope_min)][5]