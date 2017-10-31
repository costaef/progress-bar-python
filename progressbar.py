class ProgressBar:
    def __init__(self, steps=10):
        """Inits the progress bar with the default attributes.

        Keyword arguments:
        steps -- the total number of steps that the progress bar will show

        """

        self.steps = steps
        self.prefix_text = ''
        self.suffix_text = ''
        self.progress_char = '█'
        self.fill_char = '░'
        self.__completed = False

    def show(self, current_value):
        """Show the progress bar with current progress value.

        Keyword arguments:
        current_value -- the current progress value

        """

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
        """Stops the progress bar and show the completed message.

        Keyword arguments:
        message -- the completed progress message shown below the bar

        """

        if not self.__completed:
            print()
            print(message)
            self.__completed = True
