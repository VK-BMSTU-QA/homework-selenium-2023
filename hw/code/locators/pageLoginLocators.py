class LoginPageParams:
    URL_PAGE_LOGIN = 'login'
    URL_PAGE_SIGNUP = '/signup/'

    CLASS_BUTTON_OPEN_REG_WINDOW = 'modal__login__switch__btn'
    X_BUTTON_OPEN_REG_WINDOW = "/html/body/div/div[1]/div/div/div/div[2]/div/a"
    X_INPUT_EMAIL = "//input[@placeholder='Укажите адрес электронной почты']"
    X_INPUT_PASSWORD = "//input[@placeholder='Введите пароль']"
    X_BUTTON_LOGIN = "//button[contains(text(), 'Войти')]"
    CLASS_WRONG_INPUT = 'modal__input_red_border'
    CLASS_MODAL = 'modal__background'
