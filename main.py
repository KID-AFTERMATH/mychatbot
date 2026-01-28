import streamlit as st


from collections import Counter
import random

class LotteryApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.previous_numbers = []  # Store previous inputs

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text='Enter historical lottery numbers (comma-separated, one set per line):')
        self.layout.add_widget(self.label)

        self.input_field = TextInput(hint_text='e.g. 1,5,12,19,23,34\n1,2,3,4,5,6', multiline=True)
        self.layout.add_widget(self.input_field)

        self.result_label = Label(text='Suggested Lottery Numbers will appear here.')
        self.layout.add_widget(self.result_label)

        button = Button(text='Generate Numbers')
        button.bind(on_press=self.generate_numbers)
        self.layout.add_widget(button)

        return self.layout

    def analyze_frequency(self, data):
        flat_list = [num for sublist in data for num in sublist]
        frequency = Counter(flat_list)
        return frequency

    def generate_numbers(self, instance):
        # Get input from the user
        input_data = self.input_field.text.strip().splitlines()
        historical_data = [list(map(int, line.split(','))) for line in input_data if line]

        # Store previous inputs for future predictions
        self.previous_numbers.extend(historical_data)

        # Analyze frequency of numbers from previous inputs
        frequency = self.analyze_frequency(self.previous_numbers)
        suggested_numbers = self.generate_suggested_numbers(frequency)

        self.result_label.text = f'Suggested Lottery Numbers: {suggested_numbers}'

    def generate_suggested_numbers(self, frequency, count=6):
        # Get the most common numbers
        most_common = frequency.most_common(count)
        # Randomize the selection of the suggested numbers
        suggested = [num for num, _ in most_common]
        # Randomize the suggested numbers to avoid duplicates
        random.shuffle(suggested)

        # If we need to ensure 6 unique numbers, we can add random numbers
        while len(suggested) < count:
            new_number = random.randint(1, 52)  # Assuming lottery numbers are between 1 and 52
            if new_number not in suggested:
                suggested.append(new_number)

        return suggested[:count]

if __name__ == '__main__':
    LotteryApp().run()
