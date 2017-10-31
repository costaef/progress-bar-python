class ProgressBar:
    def __init__(self, steps=10):
        self.steps = steps
        self.prefix_text = ''
        self.suffix_text = ''
        self.progress_char = '█'
        self.fill_char = '-'
        self.__completed = False

    def show(self, current_value):
        if current_value > self.steps:
            self.complete()
            return

        progress = '{0:{fill}{align}{length}}'.format(
            self.progress_char * current_value,
            fill=self.fill_char,
            align='<',
            length=self.steps)

        percent = '{0:.1f}'.format(100 * (current_value / float(self.steps)))

        bar_text = '{0} |{1}| {2}% {3}'.format(
            self.prefix_text, progress, percent,
            self.suffix_text)

        print(bar_text, end='\r')

    def complete(self, message='-----> Completed!'):
        if not self.__completed:
            print()
            print(message)
            self.__completed = True
