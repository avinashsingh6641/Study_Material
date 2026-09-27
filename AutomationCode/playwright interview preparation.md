27-09-2026
# Playwright
Locators
-
<pre>
  |_
    page.get_by_role("button", name="Login")
    page.get_by_text("Welcome")
    page.get_by_label("Username")
    page.get_by_placeholder("Enter username")
    page.get_by_test_id("login-button")
    page.locator("#username")
    page.locator(".login-button")

  locators methods
  |_
      locator.click()
      locator.fill("text")
      locator.press("Enter")
      checkbox.check()
      checkbox.uncheck()
      checkbox.set_checked(True)
      dropdown.select_option("India")
      locator.hover()
      locator.focus()
      locator.blur()
      locator.clear()
      
      locator.text_content()
      locator.inner_text()
      locator.input_value()
      locator.get_attribute("href")
      
      locator.is_visible()
      locator.is_enabled()
      locator.is_checked()
      locator.is_editable()
  
  common assertion
  |_
      expect(page).to_have_title("Login Page")
      expect(locator).to_be_visible()
      expect(locator).to_be_hidden()
      expect(locator).to_be_enabled()
      expect(locator).to_be_disabled()
      expect(locator).to_be_checked()
      expect(locator).to_have_text("Hello")
      expect(locator).to_contain_text("Hello")
      expect(locator).to_have_value("admin")
      expect(locator).to_have_attribute("href", "/home")
      expect(page).to_have_url("https://example.com/home")
</pre>
Browser context
-
<pre>
  A BrowserContext provides an isolated browser session.
  Useful for:
    |_ Separate users
    |_ Cookies
    |_ Local storage
    |_ Authentication
    |_ Parallel tests
    |_ Test isolation
</pre>

Handling Multiple Pages/Tabs
-
<pre>
  with context.expect_page() as new_page_info:
    page.get_by_text("Open new tab").click()
  
  new_page = new_page_info.value
  
  new_page.wait_for_load_state()
  print(new_page.title())

  similary goes for
      |_ expect_popup()
      |_ expect_dialog()
</pre>
Screenshot
-
<pre>
  page.screenshot(path="screenshot.png")
</pre>
File Upload
-
<pre>
  page.locator("input[type='file']").set_input_files(
    "testdata/sample.pdf"
  )
  For a file chooser:
  with page.expect_file_chooser() as fc_info:
    page.get_by_text("Upload").click()

  file_chooser = fc_info.value
  file_chooser.set_files("sample.pdf")
</pre>
Download
-
<pre>
  with page.expect_download() as download_info:
      page.get_by_text("Download").click()
  
  download = download_info.value
  download.save_as("downloads/file.pdf")
</pre>
Frames / Iframes
-
<pre>
  frame = page.frame_locator("#payment-frame")
  frame.get_by_label("Card Number").fill("4111111111111111")
  other method:
    frame = page.frame(name="my_frame")
</pre>
Mouse & Keyboard
-
<pre>
  mouse
    |_
      page.mouse.click(100, 200)
      page.mouse.move(100, 200)
      page.mouse.down()
      page.mouse.up()
      page.mouse.wheel(0, 500)
  keyboard
    |_
      page.keyboard.press("Enter")
      page.keyboard.press("Control+A")
      page.keyboard.type("Hello")
</pre>
API
-
<pre>
  from playwright.sync_api import sync_playwright

  with sync_playwright() as p:
  
      api = p.request.new_context(
          base_url="https://api.example.com"
      )
  
      response = api.get("/users")
  
      print(response.status)
      print(response.json())
  
      api.dispose()
</pre>
Questions
-
<pre>
  What is Playwright, and why would you choose Playwright over Selenium?
    |_ Playwright is a modern browser automation framework developed by Microsoft.
      It supports Chromium, Firefox, and WebKit and provides features such as auto-waiting,
      reliable locators, browser-context isolation, network interception, and built-in API testing through APIRequestContext.
      Browser contexts allow us to create isolated sessions, which is useful for test isolation and parallel execution.
      Compared with Selenium, Playwright has strong built-in support for modern web applications and 
      reduces the need for manual synchronization because of its auto-waiting mechanism.
  
  What is the difference between Browser, BrowserContext, and Page in Playwright?
    |_ Browser represents the actual browser instance launched by Playwright, such as Chromium, Firefox, or WebKit.
       BrowserContext is an isolated browser session with its own cookies, local storage, and session state.
       Multiple contexts can exist within one browser.
       Page represents a single browser tab/window within a context, and one context can contain multiple pages.
  
  What is a Locator in Playwright, and what is the difference between page.locator() and get_by_role()?
    |_ A Locator is a mechanism in Playwright for finding and interacting with elements.
      It provides methods such as click(), fill(), check(), and also supports assertions and state checks.
      page.locator() can use CSS or XPath selectors, while get_by_role() locates an element based on its accessible role and name.
      get_by_role() is generally preferred when it provides a clear, user-facing way to identify the element.
      page.locator() is useful when we need a specific CSS/XPath or other selector.
</pre>
