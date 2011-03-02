PyPodio Sample
=====

 This is a sample integration using the PyPodio API Library and the 
 [Active Listings Podio App](https://podio.com/-/store/app/185-active-listings#)

Install
-------
Requirements are:

* PyPodio
* Dolt
* Flask and Dependencies
* httplib2

To install you'll first need to install the Active Listings app linked
above to a Podio Space. Once this is done, add a couple of items, and
record the application's ID.

Then:

    $ git clone git://github.com/podio/sample-flask.git
    $ cd sample-flask
    $ pip install -r reqs.txt

Next, edit the `settings.example.py` and add the required information.
Rename it to `settings.py` when finished. Finally:

    $ python realview.py

If you have any questions, feel free to ask in the Podio API space
, file a bug on the PyPodio page, or find me on Skype at nick.barnwell.

Meta
----

* PyPodio: `git clone git://github.com/podio/podio-py.git`
* Home: <https://github.com/podio/podio-py>
* Bugs: <https://github.com/podio/podio-py/issues>