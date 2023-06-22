import os

def make_success_screenshot(browser):

    os.path.abspath(os.path.dirname(__file__))

    if os.path.exists('Screenshots'):
        file_path = os.path.join('Screenshots', f'success_{os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]}.png')
        browser.save_screenshot(file_path)

    else:
        os.mkdir('Screenshots')
        file_path = os.path.join('Screenshots', f'success_{os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]}.png')
        browser.save_screenshot(file_path)

def make_fail_screenshot(browser):

    os.path.abspath(os.path.dirname(__file__))

    if os.path.exists('Screenshots'):
        file_path = os.path.join('Screenshots', f'failed_{os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]}.png')
        browser.save_screenshot(file_path)
    else:
        os.mkdir('Screenshots')
        file_path = os.path.join('Screenshots', f'failed_{os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]}.png')
        browser.save_screenshot(file_path)
