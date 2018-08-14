chimera-sonoff plugin
=====================

Controls SONOFF switches with Tasmota firmware: https://github.com/arendst/Sonoff-Tasmota

Usage
-----

Install plugin and configure with the ports you want to control.

Installation
------------

Install using pip:

::

    pip install -U https://github.com/astroufsc/chimera-sonoff/archive/master.zip


Configuration Example
---------------------

An configuration example to control the 4th port of a SONOFF 4ch as primary mirror *M1* fan.

::

    fans:
      type: SONOFF
      name: M1fan
      device: 192.168.0.1
      output: 4
      user: admin
      password: admin


Tested Hardware (for instruments)
---------------------------------

This plugin was tested on these hardware:

* Sonoff-Tasmota 5.14.0, Sonoff-Tasmota 5.14.0


Contact
-------

For more information, contact us on chimera's discussion list:
https://groups.google.com/forum/#!forum/chimera-discuss

Bug reports and patches are welcome and can be sent over our GitHub page:
https://github.com/astroufsc/chimera-sonoff/
