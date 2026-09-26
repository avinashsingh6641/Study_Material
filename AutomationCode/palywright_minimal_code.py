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

'''
 there are basically two approaches to start the playwright browser
 1) with sync_playwright() as p:
       This is the context-manager approach:
       When the with block ends, Playwright automatically calls its cleanup/stop logic.
       e.g     p.stop() is automatically called
       as you can see above im not calling p.stop() it is called automatically
       It's generally the cleanest approach for scripts.
 2) p = sync_playwright().start()
        This is the manual approach:
        this is more like assigned varibale approach which im using it as a class and object in my regression code
        e.g   p.stop() i will need to call
        as in my regression suit when im calling close browser in finally im calling p.stop()
        
'''


