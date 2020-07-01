import webbrowser
import time

try:
    webbrowser.open_new_tab('https://leetcode.com')
    time.sleep(2)   # added this to take first browser to open the other tabes otherwise it opens all tabes in new window
    webbrowser.open_new_tab("https://www.hackerrank.com")
    webbrowser.open_new_tab("https://www.hackerearth.com")
    webbrowser.open_new_tab("https://a2oj.com/ladder?ID=4")
    webbrowser.open_new_tab("https://codeforces.com")
    webbrowser.open_new_tab("https://github.com")
    webbrowser.open_new_tab("https://www.codechef.com")
    webbrowser.open_new_tab("https://www.geeksforgeeks.org")
    webbrowser.open_new_tab("https://cp-algorithms.com")
    webbrowser.open_new_tab("https://atcoder.jp")
except Exception:
    print("some error happend")
"""
pat = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chromex', None, webbrowser.BackgroundBrowser(pat))
webbrowser.get('chromex').open_new_tab_new_tab("www.google.com")

"""