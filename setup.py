from distutils.core import setup

setup(name='mysqltools-python',
      version='2.18.09.01',
      scripts=['bin/mtlsmonitor','bin/mtlsbackup'],
      packages=['mtls'],
      maintainer='Neeky',
      maintainer_email='neeky@live.com',
      url='https://github.com/Neeky/python-mysqltools',
      install_requires=['mysql-connector-python>=8.0.12'],
      python_requires='>=3.1.*,'
      )


      
