from playwright.sync_api import Page, expect

def test_drag_and_drop_slider(page: Page):

    page.goto("https://www.testmuai.com/selenium-playground/")

    page.get_by_text("Drag & Drop Sliders").click()

    slider = page.locator("input[value='15']")

    # Proper way to change slider
    slider.fill("95")

    range_value = page.locator("#rangeSuccess")
    expect(range_value).to_have_text("95")