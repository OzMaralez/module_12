import unittest
from unittest import TestCase
from module_12_3.runner import Runner

class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом методе заморожены")
    def test_walk(self):
        runner = Runner('Duck')
        for _ in range(10):
            runner.walk()

        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом методе заморожены")
    def test_run(self):
        runner = Runner('Duck')
        for _ in range(10):
            runner.run()

        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом методе заморожены")
    def test_challenge(self):
        runner1 = Runner('Duck1')
        runner2 = Runner('Duck2')
        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)