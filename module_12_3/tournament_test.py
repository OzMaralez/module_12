import unittest
from unittest import TestCase
from module_12_3.runner_and_tournament import Tournament, Runner

class TournamentTest(TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen, "Тесты в этом методе заморожены")
    def setUp(self):
        self.Useyn = Runner('Усэйн', 10)
        self.Andrey = Runner('Андрей', 9)
        self.Nik = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key} | result: ')
            for place, part in value.items():
                print(f'\tМесто {place} - Бегун {part.name}')

    @unittest.skipIf(is_frozen, "Тесты в этом методе заморожены")
    def test1_tournament(self):
        tournament = Tournament(90, self.Useyn, self.Nik)
        tournament_result = tournament.start()
        self.all_results["Test1"] = tournament_result
        self.assertTrue(tournament_result[max(self.all_results["Test1"].keys())] == 'Ник', 'louse test1')

    @unittest.skipIf(is_frozen, "Тесты в этом методе заморожены")
    def test2_tournament(self):
        tournament = Tournament(90, self.Andrey, self.Nik)
        tournament_result = tournament.start()
        self.all_results["Test2"] = tournament_result
        self.assertTrue(tournament_result[max(self.all_results["Test2"].keys())] =='Ник', 'louse test2')

    @unittest.skipIf(is_frozen, "Тесты в этом методе заморожены")
    def test3_tournament(self):
        tournament = Tournament(90, self.Useyn, self.Andrey, self.Nik)
        tournament_result = tournament.start()
        self.all_results["Test3"] = tournament_result
        self.assertTrue(tournament_result[max(self.all_results["Test3"].keys())] == 'Ник', 'louse test3')