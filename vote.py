from playwright.sync_api import sync_playwright

qtd = 1
votosRealizados = 0
while qtd < 2:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        #headless=False
        page = browser.new_page()
        page.goto("https://vote.globesoccer.com/vote/best-men-club-2023/?index=9&embed=false")
        page.wait_for_timeout(2000)
        page.get_by_text("VOTE").click()
        #print(page.title())
        page.wait_for_timeout(1500)
        votosRealizados = votosRealizados + 1
        print(votosRealizados)

        browser.close()
