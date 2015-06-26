__version__ = 0.1

import argparse
import urllib2
import webbrowser


def execute_search(query):
    query = urllib2.quote("\\{}".format(query))
    url = "https://duckduckgo.com/?q={}".format(query)
    webbrowser.open_new_tab(url)


def execute_full_search(query):
    query = urllib2.quote("{}".format(query))
    url = "https://duckduckgo.com/?q={}".format(query)
    webbrowser.open_new_tab(url)


def command_line_runner():
    parser = argparse.ArgumentParser(description='Search DuckDuckGo right from your terminal')
    parser.add_argument('query', type=str, nargs="*", help="Your search query here")
    parser.add_argument('-a', action='store_true')
    args = parser.parse_args()
    if not args.query:
        parser.print_help()
    else:
        if not args.a:
            execute_search(' '.join(args.query))
        else:
            execute_full_search(' '.join(args.query))

if __name__ == "__main__":
    command_line_runner()
