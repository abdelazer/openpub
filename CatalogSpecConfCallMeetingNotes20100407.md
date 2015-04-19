﻿#summary Meeting notes from the 7 April 2010 call

# Roll call #

Present: Ed S, Eric, Keith, Hadrien

Regrets: Peter B, Liza D

# Agenda #

  * New HTML relation in practice
  * Full entries
  * Spec & issue updates


# Discussion #

## New HTML relation in practice (autodiscovery) ##

Hadrien did change the autodiscovery links from his Feedbooks HTML:

> 

&lt;link rel="related" type="application/atom+xml;profile=opds-catalog" title="Feedbooks | OPDS catalog" href="/catalog.atom" /&gt;



He's concerned that changing the types inside of Catalogs might cause more problems with existing reading systems.

He believes that he'd probably be able to change the HTTP Content-type header.

## Full entries ##

Hadrien wonders how to encourage more OPDS clients to implement support for full entries. We do need to do more work for explaining the way that this can be used and the history from AtomPub and other work.

Are there other components we need to consider to help the browsers of mobile devices discover Catalogs inside pages?

## Spec & issue updates ##

Ed S has run into problems with the validation suite. He's written a script to crawl catalogs, so he'll commit that script and the catalogs he's collected.

Hadrien is concerned that he has not been able to get traction for faceted browsing based on top-level links in the feed. An example: If you search for a book, you get a list of results but also a bunch of links that might help you browse the results more easily by filtering. These suggestions could be presented to improve contextual browsing. He's wondering about the demand for that sort of user-experience (in addition to the technical questions).