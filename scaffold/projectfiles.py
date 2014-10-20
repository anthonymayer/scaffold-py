'''An extremely ghetto (but functional) way to create the necessary .py files for the scaffold'''
from __future__ import print_function

import io
import os

from scaffold import projectfolders
from scaffold.git_utils import get_user_email_from_git
from scaffold.git_utils import get_user_name_from_git

TEMPLATE_EXTENSION = '.template'


def create_files(project_name, root_dir):
    '''Creates all files necessary for a project skeleton'''
    dest_dir = projectfolders.create_path(
        root_dir,  # Modify the root
        project_name,
    )

    write_inits(project_name, dest_dir)

    templates = find_templates()

    template_dir = get_template_dir()

    for template in templates:
        template_name = get_template_name(template)
        contents = io.open(os.path.join(template_dir, template)).read()
        if template_name in FILE_MAPPINGS:
            contents = FILE_MAPPINGS[template_name](contents, project_name)

        with io.open(os.path.join(dest_dir, template_name), 'w') as file_obj:
            file_obj.write(contents)


def find_templates():
    template_dir = get_template_dir()
    return [
        filename
        for filename in os.listdir(template_dir)
        if filename.endswith(TEMPLATE_EXTENSION)
    ]


def get_template_dir():
    current_dir = os.getcwd()

    return '{0}/scaffold/file_templates'.format(current_dir)


def get_template_name(template):
    return template.replace('.template', '')


def transform_setup_content(contents, project_name):
    # Pass in project description here instead
    project_description = project_name

    author = get_user_name_from_git()
    author_email = get_user_email_from_git()

    return contents.format(
        project_name=project_name,
        optional_project_description='description=\'{0}\','.format(project_description) if project_description else '',
        optional_author='author=\'{0}\','.format(author) if author else '',
        optional_email='author_email=\'{0}\','.format(author_email) if author_email else '',
    )


def transform_tox_content(contents, project_name):
    return contents.replace('{{project_name}}', project_name)


def write_inits(project_name, root_dir):
    '''Creates all __init__.py files necessary for the project skeleton'''

    # Create our file paths first...
    init_paths = {
        'test': os.path.join(root_dir, 'tests', '__init__.py'),
        'project': os.path.join(root_dir, project_name, '__init__.py'),
    }

    # Write the test_init file first
    test_init = open(init_paths['test'], 'w')
    test_init.close()

    # Write the NAME_init second
    project_init = open(init_paths['project'], 'w')
    project_init.close()


FILE_MAPPINGS = {
    # '.coveragerc': transform_coveragerc_content,
    # '.gitattributes': transform_gitattributes_content,
    # '.gitignore': transform_gitignore_content,
    # '.pre-commit-config.yaml': transform_precommitconfig_content,
    # 'Makefile': transform_makefile_content,
    # 'pylintrc': transform_pylintrc_content,
    # 'requirements-dev.txt': transform_requirementsdev_content,
    'setup.py': transform_setup_content,
    'tox.ini': transform_tox_content,
}
