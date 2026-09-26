import os
import random

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # setup
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # page = browser.new_page() note if you are not using context you can directly launch page through browser
    page = context.new_page()
    os.makedirs("trace_path/",exist_ok=True)
    # main code go here

    page.goto("https://www.google.com")

    # breakdown
    page.close()
    context.tracing.stop(path=f"trace_path/new_{random.randint(1,999999)}.zip")
    context.close()
    browser.close()

# for opening traces
# playwright show-trace path to trace file
