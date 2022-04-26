from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_pokemons():
    return {
        'name': fake.sentence(nb_words=6),
        'id' : fake.random_number(digits=2, fix_len=True),
        'description': fake.sentence(nb_words=12),
        'rarity': fake.random_number(digits=2, fix_len=True),
        'mega_form': fake.random_number(digits=1, fix_len=True),
        'mega_form_unit': 'forms',
        'base_stats': fake.text(3000),
        'created_at': fake.date_time(),
        'hunter': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_pokemons())