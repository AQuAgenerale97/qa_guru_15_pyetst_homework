from selene import browser, be
import pytest

github_email = browser.element('#email')


def test_github_desktop_version(browser_config):
    if browser_config == 'mobile':
        pytest.skip(reason='Это разрешение экрана для мобильной версии!')

    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()

    github_email.should(be.visible)


def test_github_mobile_version(browser_config):
    if browser_config == 'desktop':
        pytest.skip(reason='Это разрешение экрана для десктопной версии!')

    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()

    github_email.should(be.visible)
