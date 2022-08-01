import matplotlib.pyplot as plt
import pandas as pd
from random import shuffle


def cast_to_number(string_with_symbols):
    """converts a string to a number by removing commas and percentage signs
    """
    if isinstance(string_with_symbols, float):  # already a number!
        return string_with_symbols
    no_commas = string_with_symbols.replace(',', '')
    no_percent = no_commas.replace('%', '')
    number = float(no_percent)
    return number


def make_random_groups(names: list, group_size: int) -> list:
    """Splits list of names into random groups
    """
    if len(names) % group_size != 0:
        group_size = group_size + 1
    
    shuffle(names)
    groups = [names[i:i+group_size] for i in range(0, len(names), group_size)]
    for i, g in enumerate(groups):
        print(f'\nGroup {i+1}\n--------')
        for n in g:
            print(f'- {n}')
    return groups


def make_simple_graph():
    df = pd.read_csv('../data/tickets_processed.csv')

    x = df['month']
    y1 = df['ticket_volume_received']
    y2 = df['ticket_volume_processed']

    fig = plt.figure(figsize=(12, 5))
    ax = fig.add_subplot()

    ax.plot(x, y2, marker='o', label='Ticket Volume Received', color='red')
    ax.plot(x, y1, marker='D', label='Ticket Volume Processed', color='blue')

    ax.legend()
    ax.yaxis.set_major_formatter('{x:9<5.2f}')
    ax.set_ylim(0,300)
    ax.grid()
    fig.patch.set_linewidth(5)
    fig.patch.set_edgecolor('black')

    return fig