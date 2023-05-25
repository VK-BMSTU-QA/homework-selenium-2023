class SelectorsProfile:
    URL_PAGE_PROFILE = '/profile/'
    CLASS_CHANGE_SVG = 'profile__change__svg'
    CLASS_FORM_CHANGE = 'profile__change'
    CLASS_FORM_DISPLAY_NONE = 'dysplay-none'
    CLASS_FORM_DISPLAY_FLEX = 'dysplay-flex'
    CLASS_NAME_SAVE_NEW_NAME = 'profile__input__button'
    CLASS_NAME_INFO_VALUE = 'profile__info__value'
    RATES = 1
    COLLS = 2
    CLASS_NAME_FIELD_NAME = "profile__username"

    XPATH_DATE_REG_BLOCK = "//div[contains(text(), 'Дата регистрации:')]"
    XPATH_COUNT_RATE_BLOCK = "//div[contains(text(), 'Оценок:')]"
    XPATH_COUNT_COLLECTIONS_BLOCK = "//div[contains(text(), 'Коллекций:')]"
    XPATH_COUNT_REVIEWS_BLOCK = "//div[contains(text(), 'Рецензий:')]"

    XPATH_INPUT_NEW_USERNAME = "//input[@placeholder='Введите новое имя пользователя']"

