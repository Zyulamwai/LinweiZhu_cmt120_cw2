import requests
from datetime import datetime

def get_cardiff_weather(api_key):
    # 卡迪夫的经纬度
    lat = 51.481583
    lon = -3.179090

    # 构建请求 URL
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourly,minutely,alerts,daily&units=metric&appid={api_key}"

    # 发起请求
    response = requests.get(url)

    # 检查响应状态
    if response.status_code == 200:
        data = response.json()
        # 提取当前
        day_data = data["current"]
        # 用于存储简化的天气数据
        simple_weather_data = {}
        # 将 Unix 时间戳转换为日期
        date = datetime.utcfromtimestamp(day_data["dt"]).strftime('%Y-%m-%d')
        temp = day_data["temp"]

        # weather_description = day_data["weather"][0]["description"]
        icon = f"https://openweathermap.org/img/wn/{day_data['weather'][0]['icon']}.png"
        weather_main = day_data["weather"][0]["main"]

        simple_weather_data = {
            "date": date,
            "temp": temp,
            "icon": icon,
            "weather_main": weather_main
        }
        return simple_weather_data
    else:
        print("Error: Unable to fetch weather data")
        return False

if __name__ == "__main__":
    # 使用您的 API 密钥
    api_key = "2e08607733b93dc21cb624c61b75aad8"
    weather_data = get_cardiff_weather(api_key)

    print(weather_data)