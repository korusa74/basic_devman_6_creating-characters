import random
import file_operations
import ast
from faker import Faker


def main():
    skills = []
    runic_skills = []
    letters = {}
    charsheet_way = "pattern/charsheet.svg"

    with open('data/skills.txt') as s:  # распаковка списка умений
        skills = [current_skill.rstrip() for current_skill in s.readlines()]
    with open('data/letters_mapping.txt') as l:  # распаковка словаря с буквами
        letters = ast.literal_eval(l.read())

    for skill in skills:    # замена букв в списке умений
        skill.split()
        for letter in skill:
            skill = skill.replace(letter, letters[letter])
        runic_skills.append(skill)

    for i in range(1, 11):  # генерация карточек
        fake = Faker("ru_RU")
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        job = fake.job()
        town = fake.city()
        correct_skills = random.sample(runic_skills, 3)
        context = {
            "first_name": first_name,
            "last_name": last_name,
            "job": job,
            "town": town,
            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18),
            "skill_1": correct_skills[0].replace("е", 'е͠'),
            "skill_2": correct_skills[1].replace("е", 'е͠'),
            "skill_3": correct_skills[2].replace("е", 'е͠')}
        file_way = f'output/result{i}.svg'
        file_operations.render_template(charsheet_way, file_way, context)


if __name__ == '__main__':
    main()
