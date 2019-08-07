from setuptools import setup, find_packages

requirements = []
try:
    with open('requirements.txt', 'r') as reqs:
    	requirements = [r.strip() for r in reqs.readlines()]
except:
    print('no requirements given')

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='ColabComponent',
	packages=find_packages(),
	version='0.0.3',
	license='MIT',
	description='A React.js inspired Component for building a simple reactive UI in Google Colaboratory.',
	author='Paweł A. Pierzchlewicz',
	author_email='paul@teacode.io',
	url='https://github.com/PPierzc/ColabComponent',
	keywords=['python', 'colab', 'react', 'ui', 'component'],
	install_requires=requirements,
	long_description=long_description,
	long_description_content_type="text/markdown",
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3'
	],
)
