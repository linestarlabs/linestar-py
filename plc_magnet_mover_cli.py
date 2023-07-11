import click
from linestar.plc_magnet_mover import PLCMagnetMover

@click.group()
def cli():
    pass

@cli.command()
@click.option('--ip', help='PLC IP address', required=True)
def connect(ip):
    magnet_mover = PLCMagnetMover(ip)
    magnet_mover.connect()
    click.echo('Connected to PLC')

@cli.command()
def wake():
    magnet_mover = PLCMagnetMover()
    magnet_mover.wake()
    click.echo('System woke up successfully')

@cli.command()
def move_to_home():
    magnet_mover = PLCMagnetMover()
    magnet_mover.move_to_home()
    click.echo('Moved to home position successfully')

@cli.command()
@click.option('--x', type=float, help='X position', required=True)
@click.option('--y', type=float, help='Y position', required=True)
def go_to_position(x, y):
    magnet_mover = PLCMagnetMover()
    magnet_mover.go_to_position(x, y)
    click.echo(f'Moved to position ({x}, {y}) successfully')

@cli.command()
def report_location():
    magnet_mover = PLCMagnetMover()
    location = magnet_mover.report_location()
    click.echo(f'Current location: {location}')

@cli.command()
def report_error_margin():
    magnet_mover = PLCMagnetMover()
    error_margin = magnet_mover.report_error_margin()
    click.echo(f'Error margin: {error_margin}')

if __name__ == '__main__':
    cli()

