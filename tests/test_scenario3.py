from playwright.sync_api import Page, expect

def test_input_form_submit(page: Page):

    page.goto("https://www.testmuai.com/selenium-playground/")
    page.get_by_text("Input Form Submit").click()

    # Click submit without filling anything
    page.get_by_role("button", name="Submit").click()

    # Validate HTML5 validation is triggered
    first_name = page.get_by_placeholder("eg: John").first
    validation_message = first_name.evaluate("el => el.validationMessage")
    assert validation_message != ""

    # Now fill the form
    first_name.fill("John")
    page.get_by_placeholder("eg: Doe").first.fill("Doe")
    page.get_by_placeholder("name@company.com").fill("john@test.com")
    page.locator("#inputPassword4").fill("Password123")
    page.locator("#company").fill("Test Company")

    page.select_option("select[name='country']", label="United States")

    page.locator("#city").fill("New York")
    page.locator("#address1").fill("Street 1")
    page.locator("#address2").fill("Street 2")
    page.locator("#state").fill("NY")
    page.locator("#zip").fill("10001")

    page.get_by_role("button", name="Submit").click()

    # Validate success message
    expect(
        page.get_by_text(
            "Thanks for contacting us, we will get back to you shortly."
        )
    ).to_be_visible()