from pathlib import Path
import subprocess as sp
import shutil
import os

def generate_visab_yml(visab_path, visab_docfx_path):
    if Path(visab_path).exists():
        return_code = sp.call('mvn javadoc:javadoc', cwd=visab_path, shell=True)
        if return_code == 1:
            exit()

        for file in Path(visab_docfx_path).glob('*.yml'):
            os.remove(file)

        for file in Path(f'{visab_path}/doc/yml-files').glob('*.yml'):
            shutil.copy(file, visab_docfx_path)
