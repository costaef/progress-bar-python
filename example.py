from time import sleep
from progressbar import ProgressBar

def main():
    steps = 50
    progress_bar = ProgressBar(steps)

    ### Customizations, uncomment to see the results

    # progress_bar.prefix_text = '-----> Progress:'
    # progress_bar.suffix_text = 'completed'
    # progress_bar.progress_char = '#'
    # progress_bar.fill_char = '.'

    for i in range(1, steps + 1):
        sleep(0.2)
        progress_bar.show(i)

    # Custom completed message
    #progress_bar.complete('Progress completed!')

    # Default completed message
    progress_bar.complete()

if __name__ == '__main__':
    main()
