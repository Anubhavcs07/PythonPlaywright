import re
from playwright.sync_api import Page, expect

def test_page_has_title(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page).to_have_title("Practice Page")
