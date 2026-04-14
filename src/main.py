from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(storage_state='state.json')
    page = context.new_page()

    page.goto('https://ds-login.imile.com/')

    texto = page.locator('.right-content .title').text_content()

    print(texto, flush = True)

    