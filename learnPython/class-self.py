class Human(object):
    laugh = 'hahaha'
    def show_laugh(self):
        print(self.laugh)

    def laugh_10th(self):
        for i in range(10):
            self.show_laugh()

lingdu = Human()

lingdu.show_laugh()

lingdu.laugh_10th()


class happyBird():
    def __init__(self,more_words):
        print('we are happy birds',more_words)

summer = happyBird('happy,happy')

