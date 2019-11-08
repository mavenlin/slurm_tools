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
    ],
    scripts=[
        'scripts/argparse',
        'scripts/clear_tb',
        'scripts/config',
        'scripts/connect',
        'scripts/pack',
        'scripts/slurm',
        'scripts/slurm_grep',
        'scripts/slurm_submit',
        'scripts/tb',
        'scripts/utils.sh',
    ],
)
