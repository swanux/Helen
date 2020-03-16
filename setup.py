# from setuptools import setup, find_packages

# with open('README.md') as readme_file:
#     README = readme_file.read()

# # with open('HISTORY.md') as history_file:
# #     HISTORY = history_file.read()

# setup_args = dict(
#     name='hsuite',
#     version='0.6',
#     description='HSuite is the SSU (Simple, Small, Useful) Swiss army for the Linux operating system.',
#     long_description_content_type="text/markdown",
#     long_description=README + '\n\n', # + HISTORY,
#     license='GPLv3',
#     packages=find_packages(),
#     author='Dániel Kolozsi',
#     author_email='dani@kolozsi.net',
#     keywords=['HSuite', 'SSU', 'Swanux'],
#     url='https://github.com/swanux/hsuite'
#     # download_url='https://pypi.org/project/elastictools/'
# )

# install_requires = [
    # 'notify2',
    # 'gi',
    # 'aptdaemon',
    # 'gettext',
    # 'locale',
    # 're',
    # 'github',
    # 'apt',
    # 'configparser',
    # 'webbrowser',
    # 'threading',
    # 'concurrent',
    # 'urllib'
# ]

# if __name__ == '__main__':
#     setup(**setup_args, install_requires=install_requires, include_package_data=True)

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name='hsuite',
    version='0.6',
    description='HSuite is the SSU (Simple, Small, Useful) Swiss army for the Linux operating system.',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n', # + HISTORY,
    license='GPLv3',
    author='Dániel Kolozsi',
    author_email='dani@kolozsi.net',
    url='https://github.com/swanux/hsuite',
    keywords=['HSuite', 'SSU', 'Swanux'],
    packages=find_packages(),
    # package_dir={'': 'DEV_FILES'},
    install_requires=[
        'notify2',
        'pgi',
        'aptdaemon',
        'python-gettext',
        'regex',
        'PyGithub',
        'configparser'
        ],
    entry_points={
        'console_scripts': ['hsuuite-test=DEV_FILES.HSuite:main']
    }
)