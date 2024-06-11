def pytest_addoption(parser):
    # default from https://github.com/zeiss-microscopy/OAD/blob/3b5d5e595707f1a7110ccd524b6adb10ccea65cd/Testdata/Translocation_comb_96_5ms.czi
    parser.addoption("--czipath", action="store", default="testdata/Translocation_comb_96_5ms.czi")

def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.czipath
    if 'czipath' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("czipath", [option_value])
