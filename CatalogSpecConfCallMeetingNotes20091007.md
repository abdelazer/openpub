# Attendees #

  * Keith
  * Liza
  * Raj
  * Cart
  * Tim
  * Hadrien
  * Peter

# Open Search and use of Accept headers #

It was generally agreed that the use of Accept headers may be a way to implement faceted searching using Open Search, but pursuing an Open Search extension may be the most appropriate way to support this.

There is a method to support faceted search but it requires some work on the server side which I did not understand [FIXME](FIXME.md).

# Acquisition links #

We agreed on a method to indicate that an HTML shopping cart will be provided to acquire a title, but we need additional work on describing other forms of paid acquisition.

# Atom summary versus content #

Currently the atom:content element can include arbitrary HTML markup, but this puts a burden on simpler reading systems (such as Flash-based ones) that cannot handle arbitrary markup.

However, the ability to have some basic formatting is desirable.

**We will require atom:content with @type="text" to provide additional enticement copy for an entry, but that content may be empty.**

# Hierarchical catalogs #

Keith is concerned that hierarchical catalogs are difficult to aggregate, but they are attractive for simple catalog providers and consumers.

**Hadrien to write up some recommended @rel values ("featured", "bestsellers") for sub-catalogs, and the ability to include sub-catalogs will be retained.**