# Stakeholder's call, August 12, 2009 #

## Attending ##

  * Stephanie Troeth (discussion leader)
  * Keith Fahlgren
  * Liza Daly (notes)
  * Peter Brantley
  * Hadrien Gardeur
  * Paul Norton
  * Tim Jones
  * Raj Kumar
  * Cart Reed

## Use Case status ##

  * 25 use cases have been approved

## Open Search ##

Open Search was discussed with two goals:

  1. The ability for catalogs to be browsed by facets described declaratively in the catalog.
  1. The ability to perform simple search on query terms in the feed and its contents.

Keith felt that these use cases were important however it remains critical to keep OPDS simple enough for small catalog providers to use without supporting any kind of search or browse.

Peter indicated that it is extremely important to support this for very large catalogs like the Internet Archive's.

Keith stated that Stanza's solution of encouraging hierarchical catalogs was not scalable and that we should not imitate this solution.

Hadrien:

  1. The declarative syntax implied by Open Search for browsing is immature and has no existing implementations.
  1. However Open Search for simple text searching _is_ easily implemented.

Steph suggested that we draw up a list of Use Cases for the most common kinds of browse that should be supported.

  * Hadrien will implement Open Search on the Feedbooks OPDS catalog by end of day August 12, 2009.

  * Raj will implement Open Search on the IA OPDS catalog within 1 week of August 12, 2009.

## Lending models ##

IA is proceeding with Adobe CS4 implementation for lending.  They will update the mailing list with their progress.

Liza stressed that any use of DRM or acquisition terms should be disclosed in the feed.  Hadrien suggested the use of Atom types there.  IA will provide an initial implementation and vocabulary. [?] suggested that the Prism lending terms be revisited on the list as a method to describe this.

## Acquisiton/purchase ##

Keith will begin describing common acquisition types and begin to add suggested semantics that could be used to express them.  This will be posted within one week from August 12, 2009.

## OPDS spec development ##

Keith will begin to post work from converting the existing Stanza specification to OPDS by the end of the week of August 10, 2009.

## Noah's Ark implementers ##

A number of "possible" or interested implementers have been identified.  Liza will propose some methods to begin to formalize the group and include some possibly non-public contributors.

# Action items #

  * Keith agreed to look into outlining use cases for advanced search/browse.(This will be out of implementation scope for v1.) He had begun to outline facets like: 25 most popular titles, titles by this author, new releases, etc.

  * Hadrien will implement basic Open Search on the Feedbooks OPDS catalog by end of day August 12, 2009.

  * Raj will implement basic Open Search on the IA OPDS catalog within 1 week of August 12, 2009.

  * Liza to describe what basic search functionalities are required from a reading system perspective relative to Hadrien and Raj's implementations (in response to those)

  * IA will implement a lending model using Adobe CS4 and provide the list with their implementation, including the file type and usage rights.

  * Keith will begin describing common acquisition types and begin to add suggested semantics that could be used to express them.  This will be posted within one week from August 12, 2009. Hadrien will review/comment.

  * Keith will begin to post work from converting the existing Stanza specification to OPDS by the end of the week of August 10, 2009.

  * Liza will begin organizing the Noah's Ark implementers mailing list and procedure.

  * We will review implementers' list in two weeks, commit to some deadlines and also at that point address any implementation risks.