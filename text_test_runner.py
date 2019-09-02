import unittest
from searchproduct.searchproduct import SearchTests
from test_suites.test_suites import HomePageTest

search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

unittest.TextTestRunner(verbosity = 2).run(smoke_tests)