def text_browser_append_text(text_browser, text):
    import time

    text_browser.append(text)
    text_browser.moveCursor(text_browser.textCursor().End)
    time.sleep(0.2)
