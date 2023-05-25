class SelectorsNavigation:
    URL_TAG_POPULAR = f'/collection/tag-popular/'
    URL_MAIN = '/'
    # check logo redirect
    CLASS_NAME_LOGO = 'header__navlink'
    CLASS_NAME_PREVIEW_FILM = 'js-main-page-preview-film'

    # check popular button redirect
    CLASS_NAME_HEADER_POPULAR_BUTTON = 'js-header__navlink-my-films'
    CLASS_NAME_COLLECTION_PAGE_TITLE = 'page__collection__title'
    POPULAR_COLLECTION_PAGE_TITLE = 'Популярное'

    # check premieres button redirect
    CLASS_NAME_HEADER_PREMIERES_BUTTON = 'js-header__navlink-top-250'
    CLASS_NAME_PREMIERES_PAGE_TITLE = 'premiere-page__title'
    PREMIERES_PAGE_TITLE = 'Премьеры'

    # check collections button open modal window
    X_PATH_HEADER_COLLECTIONS_BUTTON = "//a[@class='header__navlink js-header__navlink-my-colls']"
    MODAL_AUTH_CLASS_NAME = 'auth__wrapper'

    # check collections button with auth redirect
    CLASS_NAME_USER_COLLECTION_PAGE_TITLE = 'user-collection-list__title'
    USER_COLLECTION_PAGE_TITLE = 'Ваши коллекции'

    # check login button open modal window
    CLASS_NAME_HEADER_LOGIN_BUTTON = 'js-header__login__btn'