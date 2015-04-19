# Agenda #

  * Librivox catalog
  * Facets
  * Indirect acquisition


# Attending #

Hadrien Gardeur, Patrick Thompson, Tim Jones


# Discussion #

> ## Librivox catalog ##

Patrick and Hadrien both agreed that the creation of a new non-ebook catalog for Librivox (audiobooks) was a success and demonstrated that OPDS can easily be adapted to other media with minimal work (mostly new metadata).

> ## Facets ##

Aside from the example available at Feedbooks, and the two potential semantics provided on the mailing list, Tim also mentioned that Bluefire Reader is already using facets on the Books-A-Million OPDS catalog (Tim will provide an example on the mailing list).

All these examples are very similar, which means that we'll probably be able to move forward easily on this new feature.

Feedbooks, Books-A-Million and Libri should be the first three catalogs to support faceted search & browsing. The IA catalog is another potential candidate.

Patrick asked if facets would also support advanced search in catalogs. Hadrien explained how these two features are different, and support for advanced search using Open Search will also be added to the OPDS 1.1 requirements.

> ## Indirect Acquisition ##

Hadrien explained why all the previous discussions and potential solutions failed to solve this problem.

According to Tim, Bluefire Reader uses elements in its own namespace to solve this problem. They use an element to indicate the mimetype and another one to indicate the nature of the DRM.

A potential solution was discussed: a new element in the OPDS namespace with two attributes (type & size). This element could support multiple levels of indirection.

Hadrien will provide an example on the mailing list.

# Conclusion #

Advanced search will be added to the OPDS 1.1 requirements.

Based on existing examples and discussions during the conference call, potential solutions for facets and indirect acquisition will be posted on the mailing list.

_End_