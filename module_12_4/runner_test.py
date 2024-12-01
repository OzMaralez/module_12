import unittest
import logging
from unittest import TestCase
from module_12_4.rt_with_exceptions import Runner
import module_12_4.logging_settings

class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом методе заморожены")
    def test_walk(self):
        try:
            runner = Runner('Duck', speed=-4)

            logging.info('"test_walk" выполнен успешно')

            for _ in range(10):
                runner.walk()

            self.assertEqual(runner.distance, 50)
        except ValueError:
            logging.warning("Не верная скорость для Runner", exc_info=True)

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