class SelectorsLogin:
    URL_PAGE_LOGIN = '/login/'
    URL_PAGE_SIGNUP = '/signup/'

    CLASS_BUTTON_OPEN_REG_WINDOW = 'primary-btn-small'
    CLASS_NAME_MODAL_INPUT = 'js-modal__input' 
    EMAIL_INPUT = 0
    PASSWORD_INPUT = 1
    CLASS_NAME_BUTTON_LOGIN = "modal__input__button-auth"
    X_BUTTON_OPEN_REG_WINDOW = "//div[contains(concat(' ', normalize-space(@class), ' '), ' auth__wrapper ')]/div[2]/div/a"
    X_INPUT_EMAIL = "//input[@placeholder='Укажите адрес электронной почты']"
    X_INPUT_PASSWORD = "//input[@placeholder='Введите пароль']"
    X_BUTTON_LOGIN = "//button[contains(text(), 'Войти')]"
    CLASS_WRONG_INPUT = 'modal__input_red_border'
    CLASS_MODAL = 'modal__background'
