import click
import random


@click.command()
@click.option('--total', default=3, help='Number of vegetables to output.')
@click.option('--gravy', default=False, help='Append "with gravy" to the vegetables.')
def veg(total, gravy):
    for number in range(total):
        choice = random.choice(['Carrot', 'Potato', 'Turnip', 'Parsnip'])
        if gravy:
            print(f'{choice} with gravy')
        else:
            print(choice)


if __name__ == '__main__':
    veg()