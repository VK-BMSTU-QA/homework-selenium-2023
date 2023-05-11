export EMAIL_CART="test@reazon.com"
export PASSWORD_CART="reazon"
export LOGIN_DEFAULT="you@example.com"
export PWD_DEFAULT="kXkjc728dnAD#@"
export LOGIN_AUTH="test@test"
export PWD_AUTH="123456"
export LOGIN_PROFILE="basetest@example.com"
export PWD_PROFILE="ka@ld34o(12Cafk"

pytest --alluredir=allure-results hw/code/test*.py
