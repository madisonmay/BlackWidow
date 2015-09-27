BlackWidow
==========

Visualizing Python Project Import Graphs

Installation:

::

    sudo pip install blackwidow

Demo with:

::

    python -m blackwidow.web [package_name]

Optionally pass in a list of file patterns to exclude

::

    python -m blackwidow.web [package_name] --exclude *test*

Once the visualization is displayed, you can inspect file names by
hovering over a node.

Sample results:

Requests:
'''''''''

|Requests Project Graph|

Flask:
''''''

|Flask Project Graph|

BlackWidow:
'''''''''''

|BlackWidow Project Graph|

.. |Requests Project Graph| image:: http://i.imgur.com/RdUrRAC.png
.. |Flask Project Graph| image:: http://i.imgur.com/az7huA2.png
.. |BlackWidow Project Graph| image:: http://i.imgur.com/BroPIu8.png
