import click
import random


@click.command()
@click.option('--numbers', nargs=3, type=int, help='Add two numbers together.')
def add(numbers):
    result = numbers[0] + numbers[1]
    print(f'{numbers [0]} + {numbers [1]} = {result}')


if __name__ == '__main__':
    add()