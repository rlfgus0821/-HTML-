import streamlit as st
import requests

# 이건 행정동까지 포함한 api_key인데 행정동은 위도와 경도가 필요하다
# def get_weather_data(lat, lon):
#     api_key =
#     url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     return response.json()
#
# weather_data = get_weather_data(latitude, longitude)
# print(weather_data)


def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&lang=kr&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "weather_description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "wind_deg": data["wind"]["deg"]
        }
        return weather
    else:
        return f"Error: Unable to fetch weather data (Status code: {response.status_code})"


def recommend_food(weather):
    temperature = weather["temperature"]
    description = weather["weather_description"]

    if temperature > 30:
        return "더운 날씨에는 시원한 냉면이나 아이스크림을 추천합니다!"
    elif temperature > 20:
        return "따뜻한 날씨에는 가벼운 샐러드나 과일 주스를 추천합니다!"
    elif temperature > 10:
        return "선선한 날씨에는 국물 요리나 따뜻한 차를 추천합니다!"
    else:
        return "추운 날씨에는 따뜻한 국물 요리나 커피를 추천합니다!"


# API 키 입력 (사용자가 입력할 수 있도록 설정)
st.title('서울시 행정구 날씨 정보 및 음식 추천')
api_key =

seoul_districts = [
    ("Gangnam-gu,Seoul,KR", "서울시 강남구"), ("Gangdong-gu,Seoul,KR", "서울시 강동구"), ("Gangbuk-gu,Seoul,KR", "서울시 강북구"),
    ("Gangseo-gu,Seoul,KR", "서울시 강서구"), ("Gwanak-gu,Seoul,KR", "서울시 관악구"), ("Gwangjin-gu,Seoul,KR", "서울시 광진구"),
    ("Guro-gu,Seoul,KR", "서울시 구로구"), ("Geumcheon-gu,Seoul,KR", "서울시 금천구"), ("Nowon-gu,Seoul,KR", "서울시 노원구"),
    ("Dobong-gu,Seoul,KR", "서울시 도봉구"), ("Dongdaemun-gu,Seoul,KR", "서울시 동대문구"), ("Dongjak-gu,Seoul,KR", "서울시 동작구"),
    ("Mapo-gu,Seoul,KR", "서울시 마포구"), ("Seodaemun-gu,Seoul,KR", "서울시 서대문구"), ("Seocho-gu,Seoul,KR", "서울시 서초구"),
    ("Seongdong-gu,Seoul,KR", "서울시 성동구"), ("Seongbuk-gu,Seoul,KR", "서울시 성북구"), ("Songpa-gu,Seoul,KR", "서울시 송파구"),
    ("Yangcheon-gu,Seoul,KR", "서울시 양천구"), ("Yeongdeungpo-gu,Seoul,KR", "서울시 영등포구"), ("Yongsan-gu,Seoul,KR", "서울시 용산구"),
    ("Eunpyeong-gu,Seoul,KR", "서울시 은평구"), ("Jongno-gu,Seoul,KR", "서울시 종로구"), ("Jung-gu,Seoul,KR", "서울시 중구"),
    ("Jungnang-gu,Seoul,KR", "서울시 중랑구")
]

district_kor = [district[1] for district in seoul_districts]
selected_district = st.selectbox('날씨 정보를 확인할 행정구를 선택하세요', district_kor)

if st.button('날씨 정보 가져오기'):
    selected_location = [district[0] for district in seoul_districts if district[1] == selected_district][0]
    weather_info = get_weather(api_key, selected_location)

    if isinstance(weather_info, dict):
        food_recommendation = recommend_food(weather_info)
        st.write(f"위치: {selected_district}")
        st.write(f"현재 온도: {weather_info['temperature']}°C")
        st.write(f"체감 온도: {weather_info['feels_like']}°C")
        st.write(f"최저 온도: {weather_info['temp_min']}°C")
        st.write(f"최고 온도: {weather_info['temp_max']}°C")
        st.write(f"기압: {weather_info['pressure']} hPa")
        st.write(f"습도: {weather_info['humidity']}%")
        st.write(f"날씨 설명: {weather_info['weather_description']}")
        st.write(f"풍속: {weather_info['wind_speed']} m/s")
        st.write(f"풍향: {weather_info['wind_deg']}°")
        st.write(f"추천 음식: {food_recommendation}")
    else:
        st.error("날씨 정보를 가져올 수 없습니다.")
