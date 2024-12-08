from selene import browser, be
import pytest

github_email = browser.element('#email')

desktop = pytest.mark.parametrize('browser_config', [(1440, 1080), (1920, 1080)], indirect=True,
                                  ids=['desktop_1440x1080', 'desktop_1920x1080'])
mobile = pytest.mark.parametrize('browser_config', [(360, 740), (412, 915)], indirect=True,
                                 ids=['mobile_360x740', 'mobile_412x915'])


@desktop
def test_github_desktop_version(browser_config):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()

    github_email.should(be.visible)


@mobile
def test_github_mobile_version(browser_config):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()

    github_email.should(be.visible)
