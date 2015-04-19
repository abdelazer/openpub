#summary Meeting notes from the 14 July 2010 call

# Roll call #

Present: Keith, Hadrien, Peter B, Benoit, Roger, Liza
Regrets:

# Agenda #

  * MARC Relators for atom:author and atom:contributor
  * DRM Goals & Next Steps
  * Indirect Acquisition
  * Open Access Acquisition Links
  * rel Values for Images
  * Schema Updates
  * Revising Schedule for 1.0

# Discussion #

## MARC Relators for atom:author and atom:contributor ##

  * Why not use ONIX?
  * Hadrien feels that following the EPUB model and using MARC Relators in an opds-namespaced attribute would be the most attractive.
  * Keith likes that the MARC Relator codes are actively updated, available on the web, and well-documented: http://www.loc.gov/marc/relators/relaterm.html.
  * Peter reports that his recent trip to Japan exposed the fact that ONIX is not well-known in Asia.
  * Roger notes that opening the pandora's box of including data from other domains will immediately raise questions like FRBR and ONIX
  * Hadrien will add a bit to the CatalogSpecDraft
  * Roger asks Liza to keep us informed of updates from the EPUB 2.1 Metadata Subgroup

## DRM Goals & Next Steps ##

  * Liza and Keith wonder why we're bothering to solve a DRM problem when the DRM-providers are not providing their own recommendations to solve "their" own problem.
  * Hadrien clarifies that his recent discussions with Peter S have produced two agreements:
  * Many of the details of ADEPT metadata could be included in an Adobe-namedspaced set of elements
  * The mimetype of the ADEPT file could be the atom:link/@type
  * Hadrien's recommendation is to **not** include any DRM-specific text in the spec, but to reinforce the idea that a DRM'd resource is a different @type.

## Indirect Acquisition ##

  * Some providers need more details about what exactly is available in each particular version (format) of the title.
  * Hadrien wonders whether inlining RDF or atom:link/atom:link is more attractive.
  * Keith asks if this MUST be in 1.0.
  * Hadrien believes is would be more attractive _outside_ of 1.0.
  * Hadrien will create a Ticket in the Issue Tracker with a new `InformationalDocument` milestone

## Open Access Acquisition Links ##

  * Hadrien believes this is straightforward.
  * Our generic "acquisition" rel is not as specific as Open Access.
  * This is http://code.google.com/p/openpub/issues/detail?id=36.

## rel Values for Images ##

  * This was a suggestion from Benoit and is http://code.google.com/p/openpub/issues/detail?id=31.

## Schema Updates ##

  * Roger believes that the 1.0 specification document must include the schema itself.
  * Roger has discussed this issue with John Cowan.
  * Roger has suggested two changes to the schema in his email & Keith will include them.

## Revising Schedule for 1.0 ##

  * The old deadline for 1.0 was 26 July 2010, but Keith feels that deadline is no longer viable.
  * Peter talks about 1.0, he suggests that it'll be done "by the end of the Summer"
  * Keith and Liza are concerned that we haven't seen much feedback from content creators with commerical content. What are our goals in this directions?
  * Peter continues to find interest from much larger organizations internationally. Domestically, conversations continue between the Internet Archive and other parties, but they're evolving slowly (which is typical).
  * Peter sees OPDS adoption breaking into two distinct groups:
  * B2B IA-Distrubtors, Kobo (internally)
  * Reading applications & Feedbooks
  * Peter notes that we need to be patient when speaking with players in the book supply chain which haven't ever done this sort of distribution.
  * Keith suggests that we:
  * Publish OPDS 1.0 promptly to encourage adoption and allow tooling to be developed.
  * Ask OPDS contributors to work on tooling and understanding of 1.0 (rather than spec revisions)
  * Wait until new contributors with new problems appear to solve their problems in later revisions.
  * Hadrien feels that most of the technological pieces are available in OPDS 1.0 and should be available between FB and multiple reading systems soon.
  * Benoit and Hadrien will publish an informational document for pure HTTP acquisition of commercial content.
  * Hadrien suggests that the biggest missing piece is support for subscriptions.
  * Hadrien encourages us to make sure that we continue to keep 1.0 **very** generic.
  * Peter & Roger agree.
  * Keith will prepare a new OPDS 1.0 timeline for the meeting next