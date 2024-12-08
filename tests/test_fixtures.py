from selene import browser, be

github_email = browser.element('#email')


def test_github_desktop_version(browser_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()

    github_email.should(be.visible)


def test_github_mobile_version(browser_mobile):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()

    github_email.should(be.visible)
