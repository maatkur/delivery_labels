# tasks.py
from invoke import task
import os


@task
def deploy(ctx):
    # Volta a rodar de dentro de deploy/
    ctx.run("cd deploy && python deploy.py")

    dist_path = os.path.abspath("deploy/dist")
    if os.path.exists(dist_path):
        ctx.run(f"explorer {dist_path}")
    else:
        print("Pasta 'dist' não encontrada. Verifica se o deploy rolou direitinho!")