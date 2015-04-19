Like in AtomPub, an entry in an OPDS feed SHOULD NOT be considered to be a full entry.
Partial entries, MAY have a full entry identified by link@rel="alternate" and the "application/atom+xml;type=entry" mimetype.

# Metadata #

Metadata in OPDS can be:
  * required in the partial entry
  * allowed in the partial entry, and MUST be in the partial entry if they're used
  * strictly allowed in the full entry
If a property is in the partial entry, it MUST be in the full entry too.

## Required in partial entry ##

  * atom:title
  * atom:author
  * atom:id
  * atom:updated _(Corresponds to the latest update of the Atom entry, NOT the publication)_
  * atom:link with an acquisition link relation

## If present, must be in partial entry ##

  * atom:summary
  * atom:category _(Should use a scheme and a label)_
  * atom:rights
  * dcterms:language
  * dcterms:publisher
  * dcterms:issued _(publicaton date)_
  * prism:issue
  * prism:volume
  * opds:price with three-letter [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) currencycode attribute
  * opds:paymentgateway _(e.g. https://www.paypal.com/us/ or http://checkout.google.com )_
  * dc:identifier with ISBN _(e.g._

&lt;dc:identifier&gt;

urn:isbn:9780596806712

&lt;/dc:identifier&gt;

)_* dcterms:SizeOrDuration with Number of Pages, if available.
## Full entry ##_

All of the elements above and anything else.
Anything in the partial entry MUST be in the full entry too (aside from the link to the full entry). It is recommended that OPDS feed publishers use the dcterms: namespace for additional metadata.

# Link Relations #

Aside from common link relations (as defined in the [Link Header draft](http://tools.ietf.org/html/draft-nottingham-http-link-header-06) rather than the current [IANA link registry](http://www.iana.org/assignments/link-relations/link-relations.xhtml)), several OPDS-specific link relations are created.

## Feed-level (defined in the OPDS specs) ##

  * http://opds-spec.org/bookshelf
  * http://opds-spec.org/subscriptions
  * http://opds-spec.org/crawlable _(a non-hierarchical feed paginated with many entries, easy for crawlers to consume)_

**Sorting publications**

  * http://opds-spec.org/sort/new
  * http://opds-spec.org/sort/popular
  * http://opds-spec.org/sort/featured

## Feed-level (from the link header draft) ##

  * search _(not actually defined in the draft, which is something that we should consider)_
  * next _(pagination)_
  * previous _(pagination)_
  * first _(pagination)_
  * last _(pagination)_
  * start _(points to the main OPDS catalog)_
  * alternate
  * self
  * related _(best way to suggest related OPDS collection feeds. For example while browsing new release in romance, a related link could suggest the most popular publications in romance)_
  * help

## Entry-level (defined in the OPDS specs) ##

**Acquisition Links**

  * http://opds-spec.org/acquisition
  * http://opds-spec.org/acquisition/buy
  * http://opds-spec.org/acquisition/borrow
  * http://opds-spec.org/acquisition/subscribe
  * http://opds-spec.org/acquisition/sample

**Other**

  * http://opds-spec.org/cover
  * http://opds-spec.org/thumbnail

## Entry-level (from the link header draft) ##
  * alternate
  * related
  * copyright
  * license
  * replies _(for comments)_