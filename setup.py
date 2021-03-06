from setuptools import setup

setup(name='detect_simpsons_paradox',
      version='0.1',
      description='utilities to detect simpson\'s paradox',
      url='http://github.com/brownsarahm/DetectSimpsonParadox',
      author='Sarah M Brown',
      author_email='smb@sarahmbrown.org',
      license='MIT',
      packages=['detect_simpsons_paradox','sp_data_util'],
      zip_safe=False,
      install_requires=['matplotlib', 'Numpy', 'Scipy', 'seaborn', 'pandas'])
