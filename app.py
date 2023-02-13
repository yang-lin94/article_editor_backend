import click

from api import create_app
from api.database.models import *


app = create_app()

@app.cli.command()
def hello():
    """My custom command."""
    click.echo("Hello from my custom command!")

@app.cli.command()
def initdb():
    """初始化資料庫"""
    db.drop_all()
    db.create_all()
    click.echo("已完成初始化資料庫")

@app.cli.command()
def forge():
    db.drop_all()
    click.echo("Dropped all tables.")

if __name__ == '__main__':
    app.run(debug=True)
