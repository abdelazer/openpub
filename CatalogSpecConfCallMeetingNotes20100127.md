# Roll call #

Peter B, Hadrien G, Raj K, Keith F, Roger S

# Agenda #

  * News update
  * Crawlable feed behavior
  * Consensus on markup for intermediated acquisition links
  * Expanding Catalog generation/generators
  * Update from IA and Ingram on semantic model for borrow and subscribe acquisition types
  * Client requirements for buy, borrow, and subscribe acquisitions
  * Querying feeds for included acquisition formats
  * Components of publications

# Discussion #

## News update ##

  * Keith presented BookSever and OPDS to BISG Webcast and the slides and video are available http://www.bisg.org/events-0-491-bisg-webcastunderstanding-bookserverthe-power-to-find-buy-or-borrow-any-digital-book-in-any-format-at-any-time.php
  * Hadrien spoke Couperin. They are studying ebook use at libraries and universities in France. They've expressed interest and potential support for/recommendation of OPDS. Interest in borrowing.


## Expanding Catalog generation/generators ##

  * Everyone is interested in seeing more Catalogs in the wild
  * Keith would like to see some actual content creators to start dabbling with actually creating some Catalogs, even if they aren't "real"
  * Hadrien is trying to convince French distributors to start creating Catalogs

## Crawlable feed behavior ##

  * Keith just added a section, Complete Publication Collections to the CatalogSpecDraft.
  * The basic recommendation is to make a single, consolidated atom:feed with fh:complete and serve it GZip'd.
  * Raj thinks (nonbindingly) that this sounds like a good start. He would like to see more Catalogs reference a crawlable feed.

## Update from IA and Ingram on semantic model for borrow and subscribe acquisition types ##

  * Raj and Peter spoke with Cart about Ingram's borrowing infrastructure and mechanisms.
  * IA is cautiously reviewing the possibility of support for Ingram's infrastructure.
  * IA is also working on ACS4-based infrastructure that may move into active experimentation soon.
  * Keith will ask for actual spec text from Peter and Raj when he feels it is blocking the finalization of the first SpecDraft.
  * Peter is trying to speak to Steve Potash about BookServer and lending.

## Discussion of Hierarchical Collections versus Publication Collections ##

  * Roger asks for clarification on the distinction between Hierarchical Collections versus Publication Collections.
  * Keith notes that the spec is missing description of Hierarchical Collections. He'll work on that next.
  * Hadrien expects the display of Hierarchical Collections to be the default.
  * Hadrien wonders whether his http://opds-spec.org/sort/new & http://opds-spec.org/sort/popular relations are actually being used. Keith asserts that Ibis Reader is using them.

## Querying feeds for included acquisition formats ##

We need a mechanism for filtering Publication Collections by the media types of the Acqusition Links they will contain. "I want only DRM-free Mobi files," the client says. The server limits the Publication Collection.

Using the Accept Header has the advantage of being normal. Using query parameters allows a URI to be saved and sent around. (This is a normal tension.)

Keith and Hadrien will research URI-Templates and whether Accept & Headers in general would work.

## Components of publications ##

Roger notes that OPDS doesn't express the subdivision (chapters, lessons) of consolidated publications (book).

Keith believes that this is something that is (very generically) supported in the current stuff. He's concerned pragmatically about expanding the current spec too much.

Roger wonders whether Publication Collections will need to be filtered using this type of constraint.

Hadrien discusses Feedbook's implementation of component discovery (via TOC) and download. He doesn't believe it will be "much of a problem." Perhaps this will be something that Hierarchical Collections help support.

## Consensus on markup for intermediated acquisition links ##

Not covered.

## Client requirements for buy, borrow, and subscribe acquisitions ##

Not covered.

# Future #

  * Keith and Hadrien will research URI-Templates and whether Accept and Headers will work.
  * Roger would like a future agenda to include:
  * What are the provisions for adding metadata from external sources?
  * Global identifiers and associating Entries with identifiers
  * Keith to try to start mailing list discussion of: Consensus on markup for intermediated acquisition links
  * Keith to try to start mailing list discussion of: Client requirements for buy, borrow, and subscribe acquisitions