#summary Meeting notes from the March 24, 2010 call

# Roll call #

Present: Roger S, Raj K, Eric H, Keith F, Cart R

Regrets: Peter B, Liza D, Ed S

# Agenda #

  * OPDS and Audiobooks
  * Spec development
  * New Catalogs
  * Terminology & Partial Entries
  * Update on validation tools
  * Profile parameter


# Discussion #

## OPDS and Audiobooks ##

Eric has joined the call to learn more about the current state of OPDS. He is hoping to use OPDS in the context of audiobooks.

## Spec development ##

Keith has been doing a little bit of writing in between other work. He hopes this will continue at the end of this week and into the next.

You are all encouraged to comment on any issues assigned to you or to take any open issue to help move the drafting along more quickly.

## New Catalogs ##

The Pragmatic Programmer's PragProg magazine is now available as an OPDS Catalog: http://pragprog.com/magazines.opds

Keith has learned that there has been interest and discussion from some much larger US players. They had some legitimate reservations. He is trying to learn more.

The Internet Archive has launched a new view of the Open Library at http://upstream.openlibrary.org/.  Raj is planning on publishing these pages as OPDS Catalogs (and there are an awful lot of them).

## Terminology & Partial Entries ##

This is http://code.google.com/p/openpub/issues/detail?id=14

Hadrien believes that we should do a better job of defining the difference between Partial and Complete OPDS Catalog Entries.

Keith goes on a long discussion of the reasons why Partial and Complete Entries are desirable. A story:

  1. An ebook system provides a link to a publisher's Root OPDS Catalog Document (you should always link to the Root)
  1. The user clicks on the link; the ebook system does an HTTP GET and recieves a Hierarchical Collection
  1. The ebook system displays the first layer of the Hierarchical Collection represented in the Root OPDS Catalog Document easily because the atom:feed is short and simple
  1. The user clicks on 'Alphabetical'
  1. The ebook system does another HTTP GET and recieves another Hierarchical Collection
  1. The user clicks on 'A'
  1. The ebook system does another HTTP GET and recieves the first page of a multipage Publication Collection (it can tell because there are Acqusition Links in this atom:feed)
  1. The ebook system displays a simple set of metadata for each title and a link to learn more. This Publication Collection that the ebook system has received only contains "Partial OPDS Catalog Entries". These entries are limited in size by the Catalog producer to ensure that bandwidth- and processing-limited devices can consume them. Each Partial OPDS Catalog Entry SHOULD contain a core set of metadata to ensure that a basic display of information about the publication can be presented to the user.
  1. The user clicks on a title for more information
  1. The ebook system does an HTTP GET on the link for the Complete OPDS Catalog Entry (if it is present) and displays the more rich set of data about the title to the user.

By allowing Catalog producers to embed any sort of arbitrary information in the Complete OPDS Catalog Entry (reviews, cataloging information, stuff we've never thought of), we now have a reasonable extensibility mechanism (or at least that is the goal).







## Update on validation tools ##

This is http://code.google.com/p/openpub/issues/detail?id=13

Ed is having problems getting the test suite to pass. Keith needs to revisit the testing tools to ensure that they're working properly and are reasonably robust.

Roger will continue evaluating whether XSD 1.1 would be a better alternative. The only validator we're aware of at this time is Saxon Enterprise edition.

Roger notes that the `XMLBlueprint` http://www.xmlblueprint.com/ XML editor may support embedded Schematron in RelaxNG.

## Profile parameter ##

Keith is not entirely comfortable with the Profile Media Type Parameter Draft at http://buzzword.org.uk/2009/draft-inkster-profile-parameter-00.html

He is most concerned that the slashes we would encode, `profile=http://opds-spec.org/something`, are not allowed by the Media Type RFCs.

He proposes we move to this `@type`:

```
<link rel="self"  href="/opds-catalogs/root.xml" type="application/atom+xml;type=feed;profile=opds-catalog"/>
```
