import datetime


class USER_TYPE:
    NORMAL_USER = 0
    COMPANY_USER = 1
    
class CHOICES:
    GENDER = ((0, "未設定"), (1, "男性"), (2, "女性"))
    STATUS = ((0, "今すぐ転職したい"), (1, "いい求人があれば転職したい"), (2, "休会"))
    EDUCATION_STATUS = ((0, "卒業"), (1, "中退"), (2, "在学中"))
    PRIVATE = ((0, "公開"), (1, "非公開"))
    SCHOOL_TYPE = ((0, "高等学校"), (1, "高等専門学校"), (2, "専門学校・短大"), (3, "大学"), (4, "大学院"), (5, "その他学校"))

    #1〜50
    NUMBERS_LIST =[]
    for x in range(0, 51):

        number_tuple = (x, str(x)+"年") 
        NUMBERS_LIST.append(number_tuple)
    NUMBERS = tuple(NUMBERS_LIST)
    
    #1950〜今年
    today = datetime.date.today()
    YEARS_LIST =[]
    for x in range(1950, today.year):
        year_tuple = (x,x) 
        YEARS_LIST.append(year_tuple)
    YEARS = tuple(YEARS_LIST)

    #1〜12
    MONTHS_LIST =[]
    for x in range(1, 13):
        month_tuple = (x,x) 
        MONTHS_LIST.append(month_tuple)
    MONTHS = tuple(MONTHS_LIST)

    








