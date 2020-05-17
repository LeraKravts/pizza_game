import click
from time_deco import time_deco
from pizza import Margarita, Pepperoni, Hawaiian


@click.group()
def cli():
    pass


@cli.command()
def menu():
    Margarita().__str__()
    Pepperoni().__str__()
    Hawaiian().__str__()


@cli.command()
@click.option('--delivery',
              is_flag=True,
              help='Если у вас доставка, введите в консоль --delivery')
@click.argument('pizza', nargs=1)
@time_deco((input('Доставка? Введите + или - ')))
def bake(pizza: str, delivery: bool):
    if delivery:
        print(pizza, '\N{bus} to you!')
    else:
        print(f'Пицца будет вас ждать!')


if __name__ == '__main__':
    cli()
