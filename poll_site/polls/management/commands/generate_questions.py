from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from polls.models import Question


# имя файла является название команды
class Command(BaseCommand):

    # описание команды располагается в параметре help
    help = 'Add new student(s) to the system'

    # все аргументы парсяться в этом методе
    def add_arguments(self, parser):

        parser.add_argument('-l', '--len', type=int, default=10)

    # сама логика команды распологается здесь
    def handle(self, *args, **options):
        # для работы с Faker надо его заинициализировать
        faker = Faker()

        # для вывода информации о выполнении команды лучше использовать self.stdout.write вместо print
        self.stdout.write('Start generating Questions')
        for _ in range(options['len']):
            self.stdout.write('Generating Question {}'.format(_ + 1))
            question = Question()
            # faker имеет большое количество разной генерируемой информации один из них name()
            question.question_text = faker.text(max_nb_chars=50)
        self.stdout.write('End generating Questions')
