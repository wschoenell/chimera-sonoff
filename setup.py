from distutils.core import setup

setup(
    name='chimera_sonoff',
    version='0.0.1',
    packages=['chimera_sonoff', 'chimera_sonoff.instruments'],
    install_requires=["urllib2", "json"],
    scripts=[],
    url='http://github.com/astroufsc/chimera-sonoff',
    license='GPL v2',
    author='William Schoenell',
    author_email='william@astro.ufsc.br',
    description='Chimera plugin for Tasmota SONOFF switches'
)
