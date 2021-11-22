if __name__ == '__main__':
    import sys # when run, not imported
    more(open(sys.argv[1]).read(), 10) # page contents of file on cmdline