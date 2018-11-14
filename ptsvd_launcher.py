try:
    ptvs_lib_path = os.path.join(os.path.dirname(__file__), 'ptvsd')
    sys.path.append(ptvs_lib_path)
    try:
        import ptvsd
        import ptvsd.debugger as vspd
        from ptvsd.__main__ import main
        ptvsd_loaded = True
    except ImportError:
        ptvsd_loaded = False
        raise
    vspd.DONT_DEBUG.append(os.path.normcase(__file__))
except:
    traceback.print_exc()
    print('''
