# Recommended metadata #

Partial Catalog Entries SHOULD include the following metadata elements, if available:

  * dc:extent
  * dc:identifier
  * dc:issued
  * dc:language
  * dc:publisher

See the section "Relationship Between Atom and Dublin Core Metadata" in the OPDS Catalog 1.0 specification itself for more detail on when to use elements from the Atom vocabulary and when to use Dublin Core elements.

# Relations #

OPDS Catalog providers are encouraged to use relations from `[DRAFT-Web-Linking]` inside OPDS Catalogs. Some of the Relations that have been defined elsewhere but have been useful in real-world OPDS Catalogs are described below.

## OPDS Catalog Relations ##

OPDS Catalog Feed Documents uses relations to link to other available Acquisition and Navigation Feeds and other related Resources to encourage independent navigation. Here are some potentially-useful relations from `[DRAFT-Web-Linking]` with some clarification on how exactly they might be used in an OPDS Catalog context. These clarifications are incomplete, so please see `[DRAFT-Web-Linking]` for the real definitions.

  * "alternate": This OPDS Catalog in another format.
  * "first": The initial page in a paginated Acquisition Feed.
  * "help": A Resource that describes how the OPDS Catalog or Publications may be used.
  * "last": The final page in a paginated Acquisition Feed.
  * "license": The license under which this OPDS Catalog is released.
  * "next": The following page in a paginated Acquisition Feed.
  * "previous": The previous page in a paginated Acquisition Feed.
  * "related": A related or suggested Acquisition Feed. An example would be a "related" link from the newest releases in a category to the most popular in a category.
  * "self": This Atom Feed.
  * "start": The OPDS Catalog Root.
  * "subsection": A Navigation Feed not better described by a more specific relation.
  * "up": The parent Navigation Feed of this Navigation Feed.

These relations MAY be used by clients to provide additional or alternative navigation, both in a Navigation Feed or an Acquisition Feed.

## Entry Relations ##

OPDS Catalog Entry Documents uses relations to link to other Resources related to the Entry and publication. Here are some potentially-useful relations from `[DRAFT-Web-Linking]` with some clarification on how exactly they might be used in an OPDS Catalog Entry context. These clarifications are incomplete, so please see `[DRAFT-Web-Linking]` for the real definitions.

  * "alternate": Identifies a Resource that describes this Publication in another format.
  * "copyright": Refers to a copyright statement that applies to this OPDS Catalog Entry.
  * "latest-version": Refers to a more recent version of the Publication described by this OPDS Catalog Entry.
  * "license": Refers to a license associated with this OPDS Catalog Entry.
  * "related": Refers to a similar OPDS Catalog Entry.
  * "replies ": Refers to a comment on or discussion of this OPDS Catalog Entry.

# References #

  * [DRAFT-Web-Linking] Nottingham, M., "Web Linking", draft-nottingham-http-link-header-10, May 2010, http://tools.ietf.org/html/draft-nottingham-http-link-header.