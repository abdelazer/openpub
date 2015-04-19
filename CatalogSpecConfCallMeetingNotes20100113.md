# Roll call #

Minh, Cart, Keith, Liza, Bill, Peter B, Ed. Hadrien

# Agenda: #

  * New OPDS Catalog generators
  * Need for explicit list of delivery formats
  * Semantic model for borrow and subscribe acquisition types
  * Client requirements for buy, borrow, and subscribe acquisitions
  * Discovering OPDS Catalogs
  * Authentication and authorization use cases and requirements
  * Explicit specification of OPDS Catalog search techniques

# New OPDS Catalog generators #

  * Trook (Nook add-on) http://code.google.com/p/nookapps/
  * Lucicat
  * calibre2opds

## Other consumers ##

  * Bookshelf (iPhone)  Don't allow adding of new catalogs
  * FBReader (desktop version)
  * KNFBReader (Blio?) reader - Basic implementation of catalog browsing


# Need for explicit list of delivery formats #

Don't feel there's a need to limit the type of formats that can be
transmitted by OPDS.  Should we limit that?

Hadrien: It might be useful to enumerate which formats a given catalog
feed has.  Use Accept headers?  Will make this an action item to
determine the best way to do this to filter whole catalogs.

# Semantic model for borrow and subscribe acquisition types #

IA hasn't been able to do further work on borrowing to date.

ILL (interlibrary loan) is one possible use for OPDS/borrowing.

Various implementations have been done in different library software.

Prior art NCIP:
http://www.oclc.org/support/documentation/firstsearch/getting_started/ncipweb/default.htm

Ingram also has some work here that they are offering to work with the
IA on.

What the minimal constraints? Length of the loan

DRM constraints (but may not be exposed in the transaction stream)
> Is printing enabled?
> Can the work be further lent?

## Subscriptions ##

Hadrien has some support for Subscription in the feeds, but it is not
yet possible to subscribe to a particular item using OPDS.  Published a document about a subscription scenario at Make Books Apparent.

There isn't strong support yet for subscription implementations so
this should be deferred.  Good to have the @rel value ready, but that
is all we'll specify at this point.

# Client requirements for buy, borrow, and subscribe acquisitions #

When a client sees an OPDS catalog entry, if the acquisition link is
"bare", it's assumed that the publication will be delivered using a
standard HTTP link.

Hadrien described his HTTP-level scenario for transactions between
Aldiko and Feedbooks.

Hadrien thinks that the acquisition link should be type XHTML for
HTML-based shopping carts, and include child links that list the types
of documents that can be purchased.

# Discovering OPDS Catalogs #

Autodiscovery from HTML (though there may be other discovery
scenarios):

application/atom+xml;type=feed;profile=http://opds-spec.org/2010/catalog

Expect that a @rel would be expressed in the same way as an Atom feed
('alternate', often).  It is an Atom feed, it happens to be a
specialized one.

Example:
<link rel="alternate" type="application/atom+xml" title="Atom"
href="http://feeds.feedburner.com/oreilly/radar/atom" />

("Alternate" may not always be the correct relationship.)

# Explicit specification of OPDS Catalog search techniques #

What needs to be critically included in the main spec in terms of
search?

Just reference opensearch and reference it using an OpenSearch  description document.

# Authentication and authorization use cases and requirements #

(missed this)


# Additional notes #

Keith is actively working on the spec draft as well as the RNG OPDS
schema.

# Action items #

**Further develop method to query an OPDS catalog about which publication formats it supports.**

**Continue work on OPDS spec (Keith)**.