"""
Author : d4m1ts
Version : 0.0.1
"""
import argparse
import sys
from libs import bing
from src import Scan
from color import *

def menu():
    parse = argparse.ArgumentParser()
    parse.add_argument('-k',dest='keyword',metavar='inurl:example',
                       help="sql injection keyword")
    parse.add_argument('-p',dest='page_num',metavar='5',
                       help="page of websites to look for in search engine")
    args = parse.parse_args()
    return args
def main():
    args = menu()
    if len(sys.argv) == 1:
        print ('Please add -h to get help ')
        sys.exit(0)
    keyword = str(args.keyword)
    page_num = int(args.page_num)

    instance = bing.Bing(keyword,page_num)
    links = (instance.bing())

    scan = Scan.Scan(links)
    scan.main()
if __name__ == '__main__':
    printYellow ('''
===============================================================================

 _________________   .____    .___    _________
 /   _____/\_____  \ |    |   |   |  /   _____/ ____ _____    ____
 \_____  \  /  / \  \|    |   |   |  \_____  \_/ ___\\\\__  \  /    \\
 /        \/   \_/.  \    |___|   |  /        \  \___ / __ \|   |  \\
/_______  /\_____\ \_/_______ \___| /_______  /\___  >____  /___|  /
        \/        \__>       \/             \/     \/     \/     \/
                                                                    d4m1ts
===============================================================================
        ''')
    main()
