# xiaozhan modified for new version
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)  # create a connection
book_weather = client['weather']  # create a new database named weather
sheet_weather = book_weather['sheet_weather_3']   # create table named sheet_weather_3

url = 'https://cdn.heweather.com/china-city-list.txt'
response = requests.get(url)
response.encoding = 'utf8'
data = response.text
data_1 = data.split('\n')
for i in range(6):
    data_1.remove(data_1[0])
for item in data_1:
    # print(item.split('|')[2].strip())     # print the city name, item is a str
    url = 'https://free-api.heweather.com/v5/weather?city=' + item.split('|')[2].strip() + '&key=7d0daf2a85f64736a42261161cd3060b'
    # print(url)
    strhtml = requests.get(url)
    strhtml.encoding = 'utf8'
    time.sleep(1)
    # print(strhtml.text)
    dic = strhtml.json()
    # for item in dic['HeWeather5'][0]['daily_forecast']:
    #     print(item['tmp']['max'])
    # write data into database
    sheet_weather.insert_one(dic)

# find weather results in mongodb

for item in sheet_weather.find({'HeWeather5.basic.city': '北京'}):
    print(item)
# db.sheet_weather_3.find({'HeWeather5.basic.city': '北京'})  这是在命令后里面执行的查询命令，等价于上面的语句
# 网站数据原型
# | CN101010100 | beijing             | 北京               | CN       | China    | 中国     | beijing      | 北京   | beijing       | 北京       | 39.904987 | 116.40529  |
# | CN101010200 | haidian             | 海淀               | CN       | China    | 中国     | beijing      | 北京   | beijing       | 北京       | 39.956074 | 116.31032  |
# | CN101010300 | chaoyang            | 朝阳               | CN       | China    | 中国     | beijing      | 北京   | beijing       | 北京       | 39.92149  | 116.48641  |
#
# D:\Python\python.exe D:/BaiduNetdiskDownload/《Python3爬虫、数据清洗与可视化》配套代码和数据集/《Python3爬虫、数据清洗与可视化》配套代码和数据集/获取城市列表的新代码（原本页面有变动）.py
# {'HeWeather5': [{'aqi': {'city': {'aqi': '85', 'qlty': '良', 'pm25': '63', 'pm10': '84', 'no2': '77', 'so2': '4', 'co': '1.0', 'o3': '5'}}, 'basic': {'city': '北京', 'cnty': '中国', 'id': 'CN101010100', 'lat': '39.90498734', 'lon': '116.4052887', 'update': {'loc': '2019-12-07 20:27', 'utc': '2019-12-07 12:27'}}, 'daily_forecast': [{'astro': {'mr': '14:16', 'ms': '02:00', 'sr': '07:23', 'ss': '16:49'}, 'cond': {'code_d': '100', 'code_n': '101', 'txt_d': '晴', 'txt_n': '多云'}, 'date': '2019-12-07', 'hum': '45', 'pcpn': '0.0', 'pop': '0', 'pres': '1019', 'tmp': {'max': '5', 'min': '-6'}, 'uv': '5', 'vis': '25', 'wind': {'deg': '231', 'dir': '西南风', 'sc': '1-2', 'spd': '9'}}, {'astro': {'mr': '14:42', 'ms': '02:58', 'sr': '07:23', 'ss': '16:49'}, 'cond': {'code_d': '101', 'code_n': '101', 'txt_d': '多云', 'txt_n': '多云'}, 'date': '2019-12-08', 'hum': '50', 'pcpn': '0.0', 'pop': '0', 'pres': '1012', 'tmp': {'max': '5', 'min': '-5'}, 'uv': '1', 'vis': '25', 'wind': {'deg': '346', 'dir': '西北风', 'sc': '1-2', 'spd': '5'}}, {'astro': {'mr': '15:10', 'ms': '03:58', 'sr': '07:24', 'ss': '16:49'}, 'cond': {'code_d': '100', 'code_n': '100', 'txt_d': '晴', 'txt_n': '晴'}, 'date': '2019-12-09', 'hum': '50', 'pcpn': '0.0', 'pop': '0', 'pres': '1012', 'tmp': {'max': '8', 'min': '-3'}, 'uv': '6', 'vis': '25', 'wind': {'deg': '215', 'dir': '西南风', 'sc': '1-2', 'spd': '4'}}], 'now': {'cond': {'code': '100', 'txt': '晴'}, 'fl': '-5', 'hum': '62', 'pcpn': '0.0', 'pres': '1027', 'tmp': '-2', 'vis': '16', 'wind': {'deg': '136', 'dir': '东南风', 'sc': '1', 'spd': '3'}}, 'status': 'ok', 'suggestion': {'air': {'brf': '中', 'txt': '气象条件对空气污染物稀释、扩散和清除无明显影响，易感人群应适当减少室外活动时间。'}, 'comf': {'brf': '很不舒适', 'txt': '白天天气虽然晴好，但天气凉，您会感觉很冷，不舒适，请注意保暖防寒。'}, 'cw': {'brf': '适宜', 'txt': '适宜洗车，未来持续两天无雨天气较好，适合擦洗汽车，蓝天白云、风和日丽将伴您的车子连日洁净。'}, 'drsg': {'brf': '冷', 'txt': '天气冷，建议着棉服、羽绒服、皮夹克加羊毛衫等冬季服装。年老体弱者宜着厚棉衣、冬大衣或厚羽绒服。'}, 'flu': {'brf': '易发', 'txt': '昼夜温差很大，易发生感冒，请注意适当增减衣服，加强自我防护避免感冒。'}, 'sport': {'brf': '较不宜', 'txt': '天气较好，但考虑天气寒冷，推荐您进行室内运动，户外运动时请注意保暖并做好准备活动。'}, 'trav': {'brf': '适宜', 'txt': '天气较好，气温稍低，会感觉稍微有点凉，不过也是个好天气哦。适宜旅游，可不要错过机会呦！'}, 'uv': {'brf': '中等', 'txt': '属中等强度紫外线辐射天气，外出时建议涂擦SPF高于15、PA+的防晒护肤品，戴帽子、太阳镜。'}}}]}
# {'HeWeather5': [{'aqi': {'city': {'aqi': '73', 'qlty': '良', 'pm25': '53', 'pm10': '79', 'no2': '79', 'so2': '3', 'co': '0.9', 'o3': '14'}}, 'basic': {'city': '海淀', 'cnty': '中国', 'id': 'CN101010200', 'lat': '39.95607376', 'lon': '116.31031799', 'update': {'loc': '2019-12-07 20:27', 'utc': '2019-12-07 12:27'}}, 'daily_forecast': [{'astro': {'mr': '14:17', 'ms': '02:00', 'sr': '07:23', 'ss': '16:49'}, 'cond': {'code_d': '100', 'code_n': '101', 'txt_d': '晴', 'txt_n': '多云'}, 'date': '2019-12-07', 'hum': '44', 'pcpn': '0.0', 'pop': '0', 'pres': '1016', 'tmp': {'max': '7', 'min': '-6'}, 'uv': '6', 'vis': '25', 'wind': {'deg': '3', 'dir': '北风', 'sc': '1-2', 'spd': '8'}}, {'astro': {'mr': '14:42', 'ms': '02:58', 'sr': '07:24', 'ss': '16:49'}, 'cond': {'code_d': '101', 'code_n': '101', 'txt_d': '多云', 'txt_n': '多云'}, 'date': '2019-12-08', 'hum': '49', 'pcpn': '0.0', 'pop': '0', 'pres': '1008', 'tmp': {'max': '6', 'min': '-5'}, 'uv': '2', 'vis': '25', 'wind': {'deg': '291', 'dir': '西北风', 'sc': '1-2', 'spd': '1'}}, {'astro': {'mr': '15:10', 'ms': '03:58', 'sr': '07:25', 'ss': '16:49'}, 'cond': {'code_d': '100', 'code_n': '100', 'txt_d': '晴', 'txt_n': '晴'}, 'date': '2019-12-09', 'hum': '49', 'pcpn': '0.0', 'pop': '0', 'pres': '1009', 'tmp': {'max': '9', 'min': '-4'}, 'uv': '6', 'vis': '25', 'wind': {'deg': '312', 'dir': '西北风', 'sc': '1-2', 'spd': '5'}}], 'now': {'cond': {'code': '100', 'txt': '晴'}, 'fl': '-5', 'hum': '66', 'pcpn': '0.0', 'pres': '1025', 'tmp': '-3', 'vis': '16', 'wind': {'deg': '350', 'dir': '北风', 'sc': '0', 'spd': '1'}}, 'status': 'ok', 'suggestion': {'air': {'brf': '中', 'txt': '气象条件对空气污染物稀释、扩散和清除无明显影响，易感人群应适当减少室外活动时间。'}, 'comf': {'brf': '极不舒适', 'txt': '白天天气虽然晴好，但气温低，您会感觉十分寒冷，极不舒适，请注意保暖，并避免出门，以防冻伤。'}, 'cw': {'brf': '适宜', 'txt': '适宜洗车，未来持续两天无雨天气较好，适合擦洗汽车，蓝天白云、风和日丽将伴您的车子连日洁净。'}, 'drsg': {'brf': '冷', 'txt': '天气冷，建议着棉服、羽绒服、皮夹克加羊毛衫等冬季服装。年老体弱者宜着厚棉衣、冬大衣或厚羽绒服。'}, 'flu': {'brf': '易发', 'txt': '昼夜温差很大，易发生感冒，请注意适当增减衣服，加强自我防护避免感冒。'}, 'sport': {'brf': '较不宜', 'txt': '天气较好，但考虑天气寒冷，推荐您进行室内运动，户外运动时请注意保暖并做好准备活动。'}, 'trav': {'brf': '适宜', 'txt': '天气较好，气温稍低，会感觉稍微有点凉，不过也是个好天气哦。适宜旅游，可不要错过机会呦！'}, 'uv': {'brf': '中等', 'txt': '属中等强度紫外线辐射天气，外出时建议涂擦SPF高于15、PA+的防晒护肤品，戴帽子、太阳镜。'}}}]}
# {'HeWeather5': [{'aqi': {'city': {'aqi': '92', 'qlty': '良', 'pm25': '68', 'pm10': '83', 'no2': '77', 'so2': '4', 'co': '0.9', 'o3': '1'}}, 'basic': {'city': '朝阳', 'cnty': '中国', 'id': 'CN101010300', 'lat': '39.92148972', 'lon': '116.48641205', 'update': {'loc': '2019-12-07 20:27', 'utc': '2019-12-07 12:27'}}, 'daily_forecast': [{'astro': {'mr': '14:16', 'ms': '01:59', 'sr': '07:22', 'ss': '16:48'}, 'cond': {'code_d': '100', 'code_n': '101', 'txt_d': '晴', 'txt_n': '多云'}, 'date': '2019-12-07', 'hum': '45', 'pcpn': '0.0', 'pop': '0', 'pres': '1021', 'tmp': {'max': '5', 'min': '-5'}, 'uv': '5', 'vis': '25', 'wind': {'deg': '4', 'dir': '北风', 'sc': '1-2', 'spd': '6'}}, {'astro': {'mr': '14:41', 'ms': '02:58', 'sr': '07:23', 'ss': '16:48'}, 'cond': {'code_d': '101', 'code_n': '101', 'txt_d': '多云', 'txt_n': '多云'}, 'date': '2019-12-08', 'hum': '51', 'pcpn': '0.0', 'pop': '0', 'pres': '1014', 'tmp': {'max': '5', 'min': '-4'}, 'uv': '0', 'vis': '25', 'wind': {'deg': '358', 'dir': '北风', 'sc': '1-2', 'spd': '6'}}, {'astro': {'mr': '15:09', 'ms': '03:58', 'sr': '07:24', 'ss': '16:48'}, 'cond': {'code_d': '100', 'code_n': '100', 'txt_d': '晴', 'txt_n': '晴'}, 'date': '2019-12-09', 'hum': '50', 'pcpn': '0.0', 'pop': '0', 'pres': '1014', 'tmp': {'max': '9', 'min': '-4'}, 'uv': '5', 'vis': '25', 'wind': {'deg': '225', 'dir': '西南风', 'sc': '1-2', 'spd': '5'}}], 'now': {'cond': {'code': '100', 'txt': '晴'}, 'fl': '-3', 'hum': '59', 'pcpn': '0.0', 'pres': '1026', 'tmp': '0', 'vis': '16', 'wind': {'deg': '167', 'dir': '东南风', 'sc': '1', 'spd': '5'}}, 'status': 'ok', 'suggestion': {'air': {'brf': '中', 'txt': '气象条件对空气污染物稀释、扩散和清除无明显影响，易感人群应适当减少室外活动时间。'}, 'comf': {'brf': '很不舒适', 'txt': '白天天气虽然晴好，但天气凉，您会感觉很冷，不舒适，请注意保暖防寒。'}, 'cw': {'brf': '适宜', 'txt': '适宜洗车，未来持续两天无雨天气较好，适合擦洗汽车，蓝天白云、风和日丽将伴您的车子连日洁净。'}, 'drsg': {'brf': '较冷', 'txt': '建议着厚外套加毛衣等服装。年老体弱者宜着大衣、呢外套加羊毛衫。'}, 'flu': {'brf': '易发', 'txt': '昼夜温差很大，易发生感冒，请注意适当增减衣服，加强自我防护避免感冒。'}, 'sport': {'brf': '较不宜', 'txt': '天气较好，但考虑天气寒冷，推荐您进行室内运动，户外运动时请注意保暖并做好准备活动。'}, 'trav': {'brf': '适宜', 'txt': '天气较好，气温稍低，会感觉稍微有点凉，不过也是个好天气哦。适宜旅游，可不要错过机会呦！'}, 'uv': {'brf': '中等', 'txt': '属中等强度紫外线辐射天气，外出时建议涂擦SPF高于15、PA+的防晒护肤品，戴帽子、太阳镜。'}}}, {'aqi': {'city': {'aqi': '73', 'qlty': '良', 'pm25': '53', 'pm10': '73', 'no2': '59', 'so2': '24', 'co': '1.4', 'o3': '17'}}, 'basic': {'city': '朝阳', 'cnty': '中国', 'id': 'CN101071201', 'lat': '41.57675934', 'lon': '120.4511795', 'update': {'loc': '2019-12-07 20:27', 'utc': '2019-12-07 12:27'}}, 'daily_forecast': [{'astro': {'mr': '14:00', 'ms': '01:43', 'sr': '07:11', 'ss': '16:27'}, 'cond': {'code_d': '100', 'code_n': '100', 'txt_d': '晴', 'txt_n': '晴'}, 'date': '2019-12-07', 'hum': '67', 'pcpn': '0.0', 'pop': '0', 'pres': '985', 'tmp': {'max': '2', 'min': '-12'}, 'uv': '3', 'vis': '25', 'wind': {'deg': '197', 'dir': '西南风', 'sc': '1-2', 'spd': '6'}}, {'astro': {'mr': '14:24', 'ms': '02:42', 'sr': '07:12', 'ss': '16:27'}, 'cond': {'code_d': '100', 'code_n': '100', 'txt_d': '晴', 'txt_n': '晴'}, 'date': '2019-12-08', 'hum': '58', 'pcpn': '0.0', 'pop': '0', 'pres': '979', 'tmp': {'max': '6', 'min': '-10'}, 'uv': '5', 'vis': '23', 'wind': {'deg': '272', 'dir': '西风', 'sc': '1-2', 'spd': '8'}}, {'astro': {'mr': '14:51', 'ms': '03:43', 'sr': '07:13', 'ss': '16:28'}, 'cond': {'code_d': '101', 'code_n': '100', 'txt_d': '多云', 'txt_n': '晴'}, 'date': '2019-12-09', 'hum': '66', 'pcpn': '0.0', 'pop': '0', 'pres': '982', 'tmp': {'max': '4', 'min': '-9'}, 'uv': '2', 'vis': '24', 'wind': {'deg': '295', 'dir': '西北风', 'sc': '1-2', 'spd': '1'}}], 'now': {'cond': {'code': '100', 'txt': '晴'}, 'fl': '-6', 'hum': '43', 'pcpn': '0.0', 'pres': '1007', 'tmp': '-3', 'vis': '16', 'wind': {'deg': '209', 'dir': '西南风', 'sc': '2', 'spd': '6'}}, 'status': 'ok', 'suggestion': {'air': {'brf': '中', 'txt': '气象条件对空气污染物稀释、扩散和清除无明显影响，易感人群应适当减少室外活动时间。'}, 'comf': {'brf': '极不舒适', 'txt': '白天天气虽然晴好，但气温低，您会感觉十分寒冷，极不舒适，请注意保暖，并避免出门，以防冻伤。'}, 'cw': {'brf': '适宜', 'txt': '适宜洗车，未来持续两天无雨天气较好，适合擦洗汽车，蓝天白云、风和日丽将伴您的车子连日洁净。'}, 'drsg': {'brf': '寒冷', 'txt': '天气寒冷，建议着厚羽绒服、毛皮大衣加厚毛衣等隆冬服装。年老体弱者尤其要注意保暖防冻。'}, 'flu': {'brf': '易发', 'txt': '昼夜温差很大，易发生感冒，请注意适当增减衣服，加强自我防护避免感冒。'}, 'sport': {'brf': '较不宜', 'txt': '天气较好，但考虑天气寒冷，推荐您进行室内运动，户外运动时请注意保暖并做好准备活动。'}, 'trav': {'brf': '较适宜', 'txt': '天气较好，同时又有微风伴您一路同行。稍冷，较适宜旅游，您仍可陶醉于大自然的美丽风光中。'}, 'uv': {'brf': '弱', 'txt': '紫外线强度较弱，建议出门前涂擦SPF在12-15之间、PA+的防晒护肤品。'}}}, {'aqi': {'city': {'aqi': '54', 'qlty': '良', 'pm25': '38', 'pm10': '50', 'no2': '51', 'so2': '23', 'co': '0.9', 'o3': '23'}}, 'basic': {'city': '朝阳', 'cnty': '中国', 'id': 'CN101060110', 'lat': '43.86491013', 'lon': '125.31803894', 'update': {'loc': '2019-12-07 20:27', 'utc': '2019-12-07 12:27'}}, 'daily_forecast': [{'astro': {'mr': '13:39', 'ms': '01:22', 'sr': '06:59', 'ss': '16:01'}, 'cond': {'code_d': '100', 'code_n': '100', 'txt_d': '晴', 'txt_n': '晴'}, 'date': '2019-12-07', 'hum': '74', 'pcpn': '0.0', 'pop': '0', 'pres': '996', 'tmp': {'max': '-6', 'min': '-13'}, 'uv': '2', 'vis': '25', 'wind': {'deg': '227', 'dir': '西南风', 'sc': '3-4', 'spd': '15'}}, {'astro': {'mr': '14:02', 'ms': '02:23', 'sr': '07:00', 'ss': '16:00'}, 'cond': {'code_d': '101', 'code_n': '101', 'txt_d': '多云', 'txt_n': '多云'}, 'date': '2019-12-08', 'hum': '95', 'pcpn': '0.0', 'pop': '0', 'pres': '989', 'tmp': {'max': '0', 'min': '-10'}, 'uv': '1', 'vis': '4', 'wind': {'deg': '250', 'dir': '西南风', 'sc': '1-2', 'spd': '6'}}, {'astro': {'mr': '14:27', 'ms': '03:26', 'sr': '07:01', 'ss': '16:01'}, 'cond': {'code_d': '407', 'code_n': '101', 'txt_d': '阵雪', 'txt_n': '多云'}, 'date': '2019-12-09', 'hum': '88', 'pcpn': '0.0', 'pop': '2', 'pres': '993', 'tmp': {'max': '2', 'min': '-13'}, 'uv': '1', 'vis': '24', 'wind': {'deg': '247', 'dir': '西南风', 'sc': '1-2', 'spd': '7'}}], 'now': {'cond': {'code': '100', 'txt': '晴'}, 'fl': '-14', 'hum': '58', 'pcpn': '0.0', 'pres': '998', 'tmp': '-9', 'vis': '16', 'wind': {'deg': '177', 'dir': '南风', 'sc': '2', 'spd': '10'}}, 'status': 'ok', 'suggestion': {'air': {'brf': '良', 'txt': '气象条件有利于空气污染物稀释、扩散和清除，可在室外正常活动。'}, 'comf': {'brf': '极不舒适', 'txt': '白天天气虽然晴好，但气温低，您会感觉十分寒冷，极不舒适，请注意保暖，并避免出门，以防冻伤。'}, 'cw': {'brf': '适宜', 'txt': '适宜洗车，未来持续两天无雨天气较好，适合擦洗汽车，蓝天白云、风和日丽将伴您的车子连日洁净。'}, 'drsg': {'brf': '寒冷', 'txt': '天气寒冷，建议着厚羽绒服、毛皮大衣加厚毛衣等隆冬服装。年老体弱者尤其要注意保暖防冻。'}, 'flu': {'brf': '易发', 'txt': '天冷，发生感冒机率较大，请注意适当增加衣服，加强自我防护避免感冒。'}, 'sport': {'brf': '较不宜', 'txt': '天气较好，但考虑天气寒冷，风力较强，推荐您进行室内运动，若在户外运动请注意保暖并做好准备活动。'}, 'trav': {'brf': '一般', 'txt': '天气较好，温度低，加之风稍大，让人感觉很冷，会对外出有影响，外出旅游请注意防寒保暖。'}, 'uv': {'brf': '最弱', 'txt': '属弱紫外线辐射天气，无需特别防护。若长期在户外，建议涂擦SPF在8-12之间的防晒护肤品。'}}}, {'aqi': {'city': {'aqi': '47', 'qlty': '优', 'pm25': '18', 'pm10': '47', 'no2': '21', 'so2': '6', 'co': '0.5', 'o3': '99'}}, 'basic': {'city': '潮阳', 'cnty': '中国', 'id': 'CN101280502', 'lat': '23.26233673', 'lon': '116.6026001', 'update': {'loc': '2019-12-07 20:27', 'utc': '2019-12-07 12:27'}}, 'daily_forecast': [{'astro': {'mr': '14:19', 'ms': '02:00', 'sr': '06:42', 'ss': '17:27'}, 'cond': {'code_d': '101', 'code_n': '100', 'txt_d': '多云', 'txt_n': '晴'}, 'date': '2019-12-07', 'hum': '60', 'pcpn': '0.0', 'pop': '0', 'pres': '1022', 'tmp': {'max': '21', 'min': '9'}, 'uv': '6', 'vis': '25', 'wind': {'deg': '59', 'dir': '东北风', 'sc': '3-4', 'spd': '18'}}, {'astro': {'mr': '14:52', 'ms': '02:50', 'sr': '06:43', 'ss': '17:28'}, 'cond': {'code_d': '100', 'code_n': '100', 'txt_d': '晴', 'txt_n': '晴'}, 'date': '2019-12-08', 'hum': '58', 'pcpn': '0.0', 'pop': '0', 'pres': '1020', 'tmp': {'max': '20', 'min': '10'}, 'uv': '5', 'vis': '25', 'wind': {'deg': '53', 'dir': '东北风', 'sc': '3-4', 'spd': '18'}}, {'astro': {'mr': '15:28', 'ms': '03:42', 'sr': '06:44', 'ss': '17:28'}, 'cond': {'code_d': '101', 'code_n': '100', 'txt_d': '多云', 'txt_n': '晴'}, 'date': '2019-12-09', 'hum': '80', 'pcpn': '0.0', 'pop': '1', 'pres': '1016', 'tmp': {'max': '21', 'min': '11'}, 'uv': '3', 'vis': '25', 'wind': {'deg': '-1', 'dir': '无持续风向', 'sc': '1-2', 'spd': '10'}}], 'now': {'cond': {'code': '100', 'txt': '晴'}, 'fl': '13', 'hum': '56', 'pcpn': '0.0', 'pres': '1024', 'tmp': '15', 'vis': '16', 'wind': {'deg': '57', 'dir': '东北风', 'sc': '2', 'spd': '8'}}, 'status': 'ok', 'suggestion': {'air': {'brf': '中', 'txt': '气象条件对空气污染物稀释、扩散和清除无明显影响，易感人群应适当减少室外活动时间。'}, 'comf': {'brf': '较舒适', 'txt': '白天虽然天气晴好，但早晚会感觉偏凉，午后舒适、宜人。'}, 'cw': {'brf': '适宜', 'txt': '适宜洗车，未来持续两天无雨天气较好，适合擦洗汽车，蓝天白云、风和日丽将伴您的车子连日洁净。'}, 'drsg': {'brf': '较舒适', 'txt': '建议着薄外套、开衫牛仔衫裤等服装。年老体弱者应适当添加衣物，宜着夹克衫、薄毛衣等。'}, 'flu': {'brf': '少发', 'txt': '各项气象条件适宜，无明显降温过程，发生感冒机率较低。'}, 'sport': {'brf': '较适宜', 'txt': '天气较好，但因风力稍强，户外可选择对风力要求不高的运动，推荐您进行室内运动。'}, 'trav': {'brf': '适宜', 'txt': '天气较好，风稍大，但温度适宜，是个好天气哦。适宜旅游，您可以尽情地享受大自然的无限风光。'}, 'uv': {'brf': '中等', 'txt': '属中等强度紫外线辐射天气，外出时建议涂擦SPF高于15、PA+的防晒护肤品，戴帽子、太阳镜。'}}}]}
