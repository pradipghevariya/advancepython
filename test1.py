class Person:
    name = []
    first = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'there is no such user'
        else:
            return self.name[user_id]

    def set_first_name(self, first_name):
        self.first.append(first_name)
        return self.first[len(self.first) - 1]


if __name__ == "__main__":
    person = Person()
    print("User andre is added with id", person.set_name('andre'))
    print("User with id 0 is", person.get_name(0))
