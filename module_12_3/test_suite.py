import unittest
from unittest import TextTestRunner
from module_12_3.runner_test import RunnerTest
from module_12_3.tournament_test import TournamentTest

tournamantTS = unittest.TestSuite()

tournamantTS.addTests((
    unittest.TestLoader().loadTestsFromTestCase(RunnerTest),
    unittest.TestLoader().loadTestsFromTestCase(TournamentTest)
))

runner = TextTestRunner(verbosity=2)
runner.run(tournamantTS)