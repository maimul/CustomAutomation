from setuptools import setup

setup(
    name='serunaiAutomation',
    version='2.0',
    description='Serunai Automation',
    author='Maimul',
    author_email='maimulskates@gmail.com',
    packages=['serunaiAutomation'],
    py_modules=['serunaiAutomation.serunaiAutomate'],
    entry_points={
        'console_scripts': [
            'serunaiAutomation = serunaiAutomation.serunaiAutomate:main',
        ],
    },
)