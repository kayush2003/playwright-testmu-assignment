from playwright.sync_api import Page, expect
import re

def test_simple_form_demo(page: Page):

    page.goto("https://www.testmuai.com/selenium-playground/")

    page.get_by_text("Simple Form Demo").click()

    expect(page).to_have_url(re.compile(".*simple-form-demo.*"))

    message = "Welcome to TestMu AI"

    # Anchor to left column containing Enter Message label
    left_section = page.locator("text=Enter Message").locator("..").locator("..")

    input_box = left_section.get_by_role("textbox")
    input_box.fill(message)

    left_section.get_by_role("button", name="Get Checked Value").click()

    # Anchor to right panel using "Your Message:" label
    right_section = page.locator("text=Your Message").locator("..")

    expect(right_section).to_contain_text(message)