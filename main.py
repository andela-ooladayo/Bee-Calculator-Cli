import click


@click.group()
def cli():
    """
    Bee Commandline Calculator
    """
    

@click.command(help="Home Page!")
def home():

    N, M = 22, 66

    for i in xrange(1, N, 2):
        click.echo(click.style((".|."*i).center(M, "="), fg="green"))

    click.echo(click.style(" BEE CALCULATOR ".center(M, "="), fg="red"))

    for i in xrange(N-2, -1, -2): 
        click.echo(click.style((".|."*i).center(M, "="), fg="green"))



@click.command(help="Add Method!")
@click.option("--value", "-v", nargs=2, help="numbers to perform operation on")
def add(value):
    if value:
        click.echo("============================")
        ans = int(value[0]) + int(value[1])
        click.echo(">>>  %s" %ans)
        click.echo("============================")
    else:
        value = click.prompt("Enter your numbers here (separate them with a space)")
        click.echo(int(value.split(" ")[0]) + int(value.split(" ")[1]))


@click.command(help="Subtract Method!")
@click.option("--value", "-v", nargs=2, help="numbers to perform operation on")
def subtract(value):
    if value:
        click.echo(int(value[0]) - int(value[1]))
    else:
        value = click.prompt("Enter your numbers here (separate them with a space)")
        click.echo(int(value.split(" ")[0]) - int(value.split(" ")[1]))


@click.command(help="Multiply Method!")
@click.option("--value", "-v", nargs=2, help="numbers to perform operation on")
def multiply(value):
    if value:
        click.echo(int(value[0]) * int(value[1]))
    else:
        value = click.prompt("Enter your numbers here (separate them with a space)")
        click.echo(int(value.split(" ")[0]) * int(value.split(" ")[1]))


@click.command(help="Division Method!")
@click.option("--value", "-v", nargs=2, help="numbers to perform operation on")
def division(value):
    if value:
        click.echo(int(value[0]) / int(value[1]))
    else:
        value = click.prompt("Enter your numbers here (separate them with a space)")
        click.echo(int(value.split(" ")[0]) / int(value.split(" ")[1]))




cli.add_command(home)
cli.add_command(add)
cli.add_command(subtract)
cli.add_command(multiply)
cli.add_command(division)


if __name__ == "__main__":
    cli()