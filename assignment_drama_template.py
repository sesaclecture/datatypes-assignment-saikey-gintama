# ==========================
# assignment_drama_template.py (학생용 템플릿)
# 조건: 함수/조건문/반복문 금지. 변수 선언과 input(), print()만 사용.
# ==========================

drama1 = {
    "제목": "질투의 화신", 
    "장르": "로코", 
    "주제": "질투", 
    "방영기간": "2016-08-24 ~ 2016-11-10",
    "배우": ["조정석", "공효진"],
    "명대사": "\"나 너 좋아해도 돼? 짝사랑만 할게\""
}

drama2 = {
    "제목": "시그널", 
    "장르": "범죄", 
    "주제": "시간을 초월한 미제사건 수사", 
    "방영기간": "2016-01-22 ~ 2016-03-12",
    "배우": ["이제훈", "김혜수", "조진웅"], 
    "명대사": "\"절대 포기하지 마세요. 과거는 바뀔 수 있습니다.\""
}

new_title = input("새 드라마 제목(예: 응답하라 1988): ")  

new_genre = input("새 드라마 장르(예: 일상): ")
new_theme = input("새 드라마 주제(예: 가족): ")
new_period = input("새 드라마 방영기간(예: 2015-11-06 ~ 2016-01-16): ")
new_actors_input = input("새 드라마 배우들(예: 박보검, 이혜리, 류준렬): ")
new_quote_raw = input("인상 깊었던 대사(예: 어른스러운 아이는 그저 투정이 없을 뿐이다): ")

new_actors = new_actors_input.split(",")
new_quote = f"\"{new_quote_raw}\""

drama3 = {
    "제목": new_title,
    "장르": new_genre,
    "주제": new_theme,
    "방영기간": new_period,
    "배우": new_actors,
    "명대사": new_quote}


upd_title = input("수정(덮어쓰기)할 제목(대상: drama2) (예: 사이키쿠스오의 재난): ")  
upd_genre = input("수정할 장르(예: 일상): ")
upd_theme = input("수정할 주제(예: 초능력): ")
upd_period = input("수정할 방영기간(예: 2016-07-11 ~ 2018-12-28): ")
upd_actors_input = input("수정할 배우들(예: 쿠스오, 슌): ")
upd_quote_raw = input("수정할 명대사(예: 어흑): ")

upd_actors = upd_actors_input.split(",")
upd_quote = f"\"{upd_quote_raw}\""

drama2["제목"] = upd_title
drama2["장르"] = upd_genre
drama2["주제"] = upd_theme
drama2["방영기간"] = upd_period
drama2["배우"] = upd_actors
drama2["명대사"] = upd_quote

print("\n[드라마 1]")
print(f"제목: {drama1['제목']}")
print(f"장르: {drama1['장르']}")
print(f"주제: {drama1['주제']}")
print(f"방영기간: {drama1['방영기간']}")
print(f"배우: {drama1['배우']}")
print(f"명대사: {drama1['명대사']}")

print("\n[드라마 2]  # 수정 후")
print(f"제목: {drama2['제목']}")
print(f"장르: {drama2['장르']}")
print(f"주제: {drama2['주제']}")
print(f"방영기간: {drama2['방영기간']}")
print(f"배우: {drama2['배우']}")
print(f"명대사: {drama2['명대사']}")

print("\n[드라마 3]  # 새로 추가")
print(f"제목: {drama3['제목']}")
print(f"장르: {drama3['장르']}")
print(f"주제: {drama3['주제']}")
print(f"방영기간: {drama3['방영기간']}")
print(f"배우: {drama3['배우']}")
print(f"명대사: {drama3['명대사']}")
