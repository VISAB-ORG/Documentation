import subprocess as sp
from generate_visab import generate_visab_yml

docfx_path = '../docfx_project'
visab_docfx_path = docfx_path + '/api_visab'
visab_path = '../../VISAB'


# Generate and copy visab files
generate_visab_yml(visab_path, visab_docfx_path)

# Build docfx
sp.call('docfx build',cwd=docfx_path, shell=True)