import pytest
from selene import browser

github_base_url = 'https://github.com'


@pytest.fixture(scope='function', params=[(1440, 1080), (1280, 720), (1920, 1080)],
                ids=['desktop_1440_1080', 'desktop_1280_720', 'desktop_1920_1080'])
def browser_desktop(request):
    browser.config.base_url = github_base_url

    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(360, 740), (390, 844), (412, 915)],
                ids=['mobile_360x740', 'mobile_390x844', 'mobile_412x915'])
def browser_mobile(request):
    browser.config.base_url = github_base_url

    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(1440, 1080), (1920, 1080), (360, 740), (412, 915)],
                ids=['desktop_1440x1080', 'desktop_1920x1080', 'mobile_360x740', 'mobile_412x915'])
def browser_config(request):
    browser.config.base_url = 'https://github.com'

    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    if width >= 800:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()
