logins = set()
cashbacks = []
persons = {}


class person:
    def __init__(self, login):
        self.login = login
        logins.add(login)
        self.expenses = 0


class cashback:
    def __init__(self, name, percent, threshold):
        self.name = name
        self.percent = percent
        self.threshold = threshold
        self.next = ''


def sort_cashbacks():
    global cashbacks
    cashbacks = sorted(cashbacks, key=lambda cb: cb.threshold)




def add_person(login, password):
    persons[login + password] = person(login)



def get_person(login, password):
    return persons[login+password]

def check_discount_lvl(nperson: person):
    print('chqking dis')
    nplan = cashbacks[0]
    for plan in range(len(cashbacks)):
        if nperson.expenses >= cashbacks[plan].threshold:
            nplan = cashbacks[plan]
            if plan+1 < len(cashbacks):
                print(cashbacks[plan].name)
                nplan.next = 'через ' + str(cashbacks[plan+1].threshold-nperson.expenses) + ' рублей'
            else:
                nplan.next = 'Максимальный уровень'
    return nplan

def for_easy_tests():
    cashbacks.append(cashback('Отсутствует', 0, 0))
    cashbacks.append(cashback('Серебряный', 5, 10_000))
    cashbacks.append(cashback('Золотой', 10, 50_000))
    cashbacks.append(cashback('Платиновый', 20, 250_000))
    sort_cashbacks()

    add_person('Vasya0j', 'Password123')
    persons['Vasya0jPassword123'].expenses = 25_000
    add_person('Petya', 'MySecretPassword')
    persons['PetyaMySecretPassword'].expenses = 100_000
    add_person('Richguy', 'qwerty258')
    persons['Richguyqwerty258'].expenses = 1_000_000
    add_person('newGuy', 'noonewilleverhackpasswordthatlong')


if __name__ == "__main__":
    for_easy_tests()
    p = persons['Vasya0jPassword123']
    print(check_discount_lvl(p).name)