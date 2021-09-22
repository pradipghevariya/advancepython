import unittest
from test1 import Person as PersonClass


class POneTest(unittest.TestCase):
    person = PersonClass()
    user_id = []
    user_name = []
    first_name = []

    def test_set_name(self):
        for i in range(4):
            name = 'name' + str(i)
            self.user_name.append(name)
            user_id = self.person.set_name(name)
            self.assertIsNotNone(user_id)
            self.user_id.append(user_id)
        print("finish test case")

    def test_get_name(self):
        for i in range(7):
            if i < len(self.user_id):
                self.assertEqual(self.user_name[i], self.person.get_name(self.user_id[i]))
            else:
                self.assertEqual('there is no such user', self.person.get_name(i))

    def test_set_first_name(self):
        for i in range(5):
            n = "name" + str(i)
            self.first_name.append(n)
            self.assertEqual(self.first_name[i], self.person.set_first_name(self.first_name[i]))


if __name__ == "__main__":
    if __name__ == "__main__":
        unittest.main()
