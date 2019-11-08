from setuptools import setup, find_packages

setup(
    name='slurm_tools',
    version='1.0',
    description='handy script to slurm',
    url='http://github.com/mavenlin/slurm_tools',
    author='Min Lin',
    author_email='mavenlin@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'uuid',
        'gitpython',
        'git-archive-all',
    ],
    scripts=[
        'scripts/setup_cc',
        'scripts/remote_run',
        'scripts/argparse',
        'scripts/tb',
        'scripts/clear_tb',
        'scripts/slurm_config',
        'scripts/slurm_connect',
        'scripts/slurm_pack',
        'scripts/slurm',
        'scripts/slurm_grep',
        'scripts/slurm_submit',
        'scripts/slurm_utils.sh',
    ],
)
