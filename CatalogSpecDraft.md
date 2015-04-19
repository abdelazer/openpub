﻿#summary Draft of version 1.2 of the OPDS Catalog specification. Version 1.1 has been published: http://opds-spec.org/specs/opds-catalog-1-1
#labels Featured,Phase-Design

# Status of this Draft #

This document specifies the 1.2 draft of the OPDS Catalog specification.



# License #

This document is licensed under [Creative Commons Attribution-Share Alike](http://creativecommons.org/licenses/by-sa/3.0/).

# Abstract #

The Open Publication Distribution System (OPDS) Catalog format is a syndication format for electronic publications based on Atom and HTTP. OPDS Catalogs enable the aggregation, distribution, discovery, and acquisition of electronic publications. OPDS Catalogs use existing or emergent open standards and conventions, with a priority on simplicity.

# Introduction #

The Open Publication Distribution System (OPDS) Catalog format is a syndication format for electronic publications based on Atom `[RFC4287]` and HTTP `[RFC2616]`. OPDS Catalogs enable available electronic publications to be:

  * discovered, using optional search or a range of optional browsing techniques
  * acquired, using direct downloads, lending, or vending

An OPDS Catalog is a set of one or more Atom Feeds, which are themselves listings of Atom Entries. The Atom Feeds that make up all OPDS Catalogs can be divided into two groups: Navigation Feeds, which create a hierarchy for browsing, and Acquisition Feeds, which list available electronic publications. Each Atom Entry in an Acquisition Feed includes basic metadata about the publication, the publication's format, and how the publication can be acquired. These included Atom Entries may be minimal subsets of the complete metadata, with a link to a more extensive, standalone representation URI (see the Section Listing Acquisition Feeds for more).

OPDS Catalogs may be aggregated and combined into larger OPDS Catalogs.

# Notational Conventions #

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in `[RFC2119]`.

# XML-Related Conventions #

## Referring to Information Items ##

The OPDS Catalog format is specified in terms of the XML Information Set `[REC-xml-infoset]`, serialized as XML 1.0 `[REC-xml]`.

The Infoset terms "Element Information Item" and "Attribute Information Item" are shortened to "element" and "attribute" respectively. Therefore, when this specification uses the term "element", it is referring to an Element Information Item, and when it uses the term "attribute", it is referring to an Attribute Information Item.

# RELAX NG Schema #

Some sections of this specification are illustrated with fragments of a non-normative RELAX NG Compact schema `[RNC]`. However, the text of this specification provides the definition of conformance. Complete schemas appear in Appendix B.

# Terminology #

The following terminology is used by this specification:

  * Acquisition Feed -- An Atom Feed whose Atom Entries are exclusively OPDS Catalog Entries.
  * Acquisition Link -- An atom:link element with a relation that begins with "http://opds-spec.org/acquisition" and refers to the Resource which holds the content of the described Publication or the Resource through which it may be acquired for any OPDS Catalog Entry. See the Sections Acquisition Relations and Acquiring Publications. They are serialized as OPDS Catalog Feed Documents.
  * Complete Catalog Entry -- An OPDS Catalog Entry that includes all known metadata about the described Publication and is referenced by a Partial Catalog Entry.
  * Facet -- A subset or an alternate order for an Acquisition Feed. In an OPDS Catalog, a Facet is represented as an atom:link in an Acquisition Feed.
  * IRI -- An Internationalized Resource Identifier as defined in `[RFC3987]`.
  * Navigation Feed -- An Atom Feed whose Atom Entries are not OPDS Catalog Entries but instead links to other Navigation Feeds, Acquisition Feeds, or other Resources to establish a hierarchical, browsable presentation of the OPDS Catalog.
  * OPDS Catalog -- All of the Atom Feeds (Acquisition and Navigation) and Entries (Partial and Complete) following this specification published together to describe a consolidated group of available Publications.
  * OPDS Catalog Entry -- An Atom Entry that provides a representation of an available Publication and includes an Acquisition Link. They are serialized as OPDS Catalog Entry Documents.
  * OPDS Catalog Entry Document -- The formal name for the XML documents that are a refinement of an "atom:entry" from the Atom Syndication Format `[RFC4287]` that this specification defines.
  * OPDS Catalog Feed Document -- The formal name for XML documents that are a refinement of an "atom:feed" from the Atom Syndication Format `[RFC4287]` that this specification defines.
  * OPDS Catalog Root -- The Atom Feed that represents either the complete OPDS Catalog (a single Acquisition Feed) or the Atom Feed that starts a set of Navigation Feeds. External links to the OPDS Catalog SHOULD reference the OPDS Catalog Root Resource.
  * Partial Catalog Entry --- An OPDS Catalog Entry that includes the minimal required metadata about the described Publication but no other metadata and links to the Complete Catalog Entry.
  * Publication - An electronic document, typically available as a single file. OPDS Catalogs are agnostic about the particular format of Publications.
  * relation (or "relation of") -- Refers to the "rel" attribute value of an atom:link element.
  * Representation -- An entity included with a request or response as defined in `[RFC2616]`.
  * Resource -- A network-accessible data object or service identified by an IRI, as defined in `[RFC2616]`. See `[REC-webarch]` for further discussion on Resources.
  * URI -- A Uniform Resource Identifier as defined in `[RFC3986]`. In this specification, the phrase "the URI of a document" is shorthand for "a URI which, when dereferenced, is expected to produce that document as a representation".

# Document Types #

This specification defines two kinds of documents -- OPDS Catalog Feed Documents and OPDS Catalog Entry Documents.

An OPDS Catalog Feed Document is a refinement of an "atom:feed" from the Atom Syndication Format `[RFC4287]`.

An OPDS Catalog Entry Document is a refinement of an "atom:entry" from the Atom Syndication Format `[RFC4287]`.

The namespace name `[REC-xml-names]` for elements defined in this specification and used in OPDS Catalog Feed Documents and OPDS Catalog Entry Documents is:

http://opds-spec.org/2010/catalog

OPDS Catalog Feed Documents and OPDS Catalog Entry Documents MUST be "namespace-well-formed" as specified in Section 7 of `[REC-xml-names]`.

This specification uses the prefix "opds:" for the namespace name. The prefix "atom:" is used for "http://www.w3.org/2005/Atom ", the namespace name of the Atom Syndication Format `[RFC4287]`. The prefix "dc:" is used for"http://purl.org/dc/terms/", the namespace name of Dublin Core Metadata Initiative (DCMI) Metadata Terms `[DCTERMS]`. These namespace prefixes are not semantically significant.

Producers of OPDS Catalogs SHOULD produce OPDS Catalog Feed Documents and OPDS Catalog Entry Documents that are conformant to both Atom and the OPDS Catalog RELAX NG schemas.

## Document Extensibility ##

Unrecognized markup in any Atom Feed or Atom Entry in an OPDS Catalog is considered "foreign markup" as defined in Section 6 of the Atom Syndication Format `[RFC4287]`. Foreign markup can be used anywhere within an OPDS Catalog unless it is explicitly forbidden. Processors that encounter foreign markup MUST NOT stop processing and MUST NOT signal an error. Clients SHOULD preserve foreign markup when transmitting or aggregating such documents.

The namespace name "http://opds-spec.org/2010/catalog" is reserved for forward-compatible revisions of the OPDS Catalog format. This does not exclude the addition of elements and attributes that might not be recognized by processors conformant to this specification. Such unrecognized markup from the "http://opds-spec.org/2010/catalog" namespace MUST be treated as foreign markup.

# Media Type Considerations #

## The Atom Format Type Parameter ##

The Atom Publishing Protocol `[RFC5023]` defines the Atom Format Type Parameter.

Publishers of OPDS Catalogs SHOULD use the "type" parameter to help clients distinguish between relations to OPDS Catalog Entries and OPDS Catalog Feeds.

## The OPDS Catalog Profile Parameter ##

Relations to OPDS Catalog Feed Document and OPDS Catalog Entry Document Resources SHOULD use a "profile" parameter following Section 4.3 of `[RFC4288]` with the value "opds-catalog". This profile parameter provides clients with an advisory hint that the Resource should be a component of an OPDS Catalog.

The complete media type for a relation to an OPDS Catalog Entry Document Resource SHOULD be:

```
application/atom+xml;type=entry;profile=opds-catalog
```

The complete media type for a relation to an OPDS Catalog Feed Document Resource SHOULD be:

```
application/atom+xml;profile=opds-catalog
```

## The OPDS Kind Parameter ##

In addition to the new "profile" parameter, this specification also introduces a new "kind" parameter following Section 4.3 of `[RFC4288]` with the value "acquisition" or "navigation". This "kind" parameter provides clients with an advisory hint whether the Resource should be an  Acquisition Feed or a Navigation Feed.

This value is intended to make it easier for OPDS clients to display basic contextual information about the feed without requiring that those clients dereference, parse, and analyze linked resources.
That said, the client MUST NOT assume this parameter to provide completely accurate information about the nature of the feed. Feed publishers SHOULD make an effort to ensure that this value is accurate.

The complete media type for a relation to an Acquisition Feed SHOULD be:

```
application/atom+xml;profile=opds-catalog;kind=acquisition
```

The complete media type for a relation to a Navigation Feed SHOULD be:

```
application/atom+xml;profile=opds-catalog;kind=navigation
```

# OPDS Catalog Feed Documents #

OPDS Catalog Feed Documents are Atom `[RFC4287]` Feeds. They serve two purposes:

  * To create a browsable hierarchy of other OPDS Catalog Feed Documents and other Resources. These OPDS Catalog Feed Documents are referred to as Navigation Feeds.
  * To collect a set of OPDS Catalog Entries. These OPDS Catalog Feed Documents are referred to as Acquisition Feeds.

While Navigation Feeds do provide a suggested hierarchy from the OPDS Catalog publisher, OPDS Catalog Feed Documents MAY contain other relations that allow for other methods of consumption and display. See the Section OPDS Catalog Relations for more detail.

Every OPDS Catalog Feed Document MUST either be an Acquisition Feed or a Navigation Feed. An Acquisition Feed can be identified by the presence of Acquisition Links in each Atom Entry.

## OPDS Catalog Root ##

The OPDS Catalog Root is the top-level OPDS Catalog Feed Document. It is either a single Acquisition Feed in the simple case or the start of a set of Navigation Feeds. Every OPDS Catalog MUST have one and only one OPDS Catalog Root.

External links to the OPDS Catalog Resource SHOULD use the IRI of the OPDS Catalog Root.

Each OPDS Catalog Feed Document SHOULD contain an atom:link element with a link relation of "start", which references the OPDS Catalog Root Resource.

## Element Definitions ##

### The "atom:feed" Element ###

The "atom:feed" element is the document (i.e., top-level) element of an OPDS Catalog Feed Document, acting as a container for metadata, hierarchy, and Publications associated with the OPDS Catalog. Its element children consist of metadata elements followed by zero or more atom:entry child elements.

The following child elements are refined by this specification:

  * OPDS Catalog Feed Documents SHOULD contain one atom:link element with a "rel" attribute value of "self". This is the preferred URI for retrieving the atom:feed representing this OPDS Catalog Feed Document.

# Navigation Feeds #

A Navigation Feed is an OPDS Catalog Feed Document whose Atom Entries serve to create a suggested hierarchy for presentation and browsing. A Navigation Feed MUST NOT contain OPDS Catalog Entries but instead contains Atom Entries that link to other Navigation or Acquisition Feeds or other Resources. Each Atom Entry's "atom:content" element SHOULD include a brief description of the linked Resource.

Links to Navigation Feeds SHOULD use the "type" attribute "application/atom+xml;profile=opds-catalog;kind=navigation". OPDS Catalog providers SHOULD choose the best relation for each Navigation Feed based on the relations in the section OPDS Catalog Relations. The relation "subsection" SHOULD be used if no other relation is more appropriate.

## Navigation Feed Example ##

An OPDS Catalog Root that is the top of a set of Navigation Feeds references three Acquisition Feeds using atom:links:
```
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <id>urn:uuid:2853dacf-ed79-42f5-8e8a-a7bb3d1ae6a2</id>
  <link rel="self"  
        href="/opds-catalogs/root.xml" 
        type="application/atom+xml;profile=opds-catalog;kind=navigation"/>
  <link rel="start" 
        href="/opds-catalogs/root.xml" 
        type="application/atom+xml;profile=opds-catalog;kind=navigation"/>
  <title>OPDS Catalog Root Example</title>
  <updated>2010-01-10T10:03:10Z</updated>
  <author>
    <name>Spec Writer</name>
    <uri>http://opds-spec.org</uri>
  </author>

  <entry>
    <title>Popular Publications</title>
    <link rel="http://opds-spec.org/sort/popular" 
          href="/opds-catalogs/popular.xml"
          type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>
    <updated>2010-01-10T10:01:01Z</updated>
    <id>urn:uuid:d49e8018-a0e0-499e-9423-7c175fa0c56e</id>
    <content type="text">Popular publications from this catalog based on downloads.</content>
  </entry>
  <entry>
    <title>New Publications</title>
    <link rel="http://opds-spec.org/sort/new" 
          href="/opds-catalogs/new.xml"
          type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>
    <updated>2010-01-10T10:02:00Z</updated>
    <id>urn:uuid:d49e8018-a0e0-499e-9423-7c175fa0c56c</id>
    <content type="text">Recent publications from this catalog.</content>
  </entry>
  <entry>
    <title>Unpopular Publications</title>
    <link rel="subsection" 
          href="/opds-catalogs/unpopular.xml"
          type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>
    <updated>2010-01-10T10:01:00Z</updated>
    <id>urn:uuid:d49e8018-a0e0-499e-9423-7c175fa0c56d</id>
    <content type="text">Publications that could use some love.</content>
  </entry>
</feed>
```

# Acquisition Feeds #

An Acquisition Feed is an OPDS Catalog Feed Document that collects OPDS Catalog Entries into a single, ordered set. The simplest complete OPDS Catalog would be a single Acquisition Feed listing all of the available OPDS Catalog Entries from that provider. In more complex OPDS Catalogs, Acquisition Feeds are used to present and organize sets of related OPDS Catalog Entries for browsing and discovery by clients and aggregators.

Links to Acquisition Feeds SHOULD use the "type" attribute "application/atom+xml;profile=opds-catalog;kind=acquisition".

For further details on limiting the size of Acquisition Feeds through pagination, Partial Catalog Entries, and compression, see the Section Listing Acquisition Feeds.

## OPDS Catalog Entry Documents ##

OPDS Catalog Entry Documents are Atom `[RFC4287]` Entry documents that provide a complete representation of the metadata and data associated with an available Publication.

Each OPDS Catalog Entry Document MUST include at least one Acquisition Link, which is an atom:link element with a relation that begins "http://opds-spec.org/acquisition". This link refers to the Resource which is the content of the Resource described by the OPDS Catalog Entry in a particular media type. Acquisition Links use one of the relations described in the Section Acquisition Relations.

### Relationship Between Atom and Dublin Core Metadata ###

OPDS Catalog providers are encouraged to include metadata from the Dublin Core Metadata Initiative (DCMI) Metadata Terms `[DCTERMS]` whenever appropriate. However, these elements are not required. Some of the elements defined in `[DCTERMS]` overlap in meaning with similar elements defined by Atom in `[RFC4287]`. In general, OPDS Catalog Entries prefer the Atom elements over the `[DCTERMS]` elements and the following rules should be used by OPDS Catalog providers when choosing elements:

  * OPDS Catalog Entries MUST be identified by an "atom:id". One or more "dc:identifier" elements SHOULD be used to identify the represented Publication, if appropriate metadata is available, and MUST NOT identify the OPDS Catalog Entry.
  * OPDS Catalog Entries MUST include an "atom:updated" element indicating when the OPDS Catalog Entry was last updated. A "dc:issued" element SHOULD be used to indicate the first publication date of the Publication and MUST NOT represent any date related to the OPDS Catalog Entry.
  * OPDS Catalog Entries MUST include an "atom:title" representing the Publication's title and MUST NOT use "dc:title".
  * OPDS Catalog Entries SHOULD use "atom:author" to represent the Publication's creators and SHOULD NOT use "dc:creator".
  * OPDS Catalog Entries SHOULD use "atom:category" to represent the Publication's category, keywords, key phrases, or classification codes and SHOULD NOT use "dc:subject".
  * OPDS Catalog Entries SHOULD use "atom:rights" to represent rights held in and over the Publication and SHOULD NOT use "dc:rights".
  * OPDS Catalog Entries SHOULD use "atom:summary" and/or "atom:content" to describe the Publication SHOULD NOT use "dc:description" or "dc:abstract".
  * OPDS Catalog Entries MAY use "atom:contributor" to represent contributors to the Publication beside its creators.
  * OPDS Catalog Entries MAY use "atom:published" to indicate when the OPDS Catalog Entry was first accessible.

All metadata elements required by Atom are required in OPDS Catalog Entries and Feeds.

Following Atom `[RFC4287]` Section 4.2.6, the content of an "atom:id" identifying an OPDS Catalog Entry MUST NOT change when the OPDS Catalog Entry is "relocated, migrated, syndicated, republished, exported, or imported" and "MUST be created in a way that assures uniqueness."

### Partial and Complete Catalog Entries ###

An OPDS Catalog Entry may be represented as either a Partial or Complete Catalog Entry. Partial Catalog Entries include only critical metadata elements to reduce the size of OPDS Catalog documents for bandwidth- and resource-limited clients and link to their alternate representation as a Complete Catalog Entries, which include all metadata elements.

A Partial Catalog Entry MUST include an "alternate" link relation referencing the Complete Catalog Entry Resource and that atom:link MUST use the "type" attribute "application/atom+xml;type=entry;profile=opds-catalog".

Any OPDS Catalog Entry without a link to a Complete Catalog Entry MUST include all metadata elements.

Partial Catalog Entries SHOULD include the following metadata elements, if available:

  * atom:category
  * atom:contributor
  * atom:rights
  * opds:price

OPDS Catalog providers are strongly encouraged to limit metadata elements not required by Atom, OPDS, or listed above from Partial Catalog Entries to help facilitate the efficient transmission and consumption of OPDS Catalog documents. Implementers are encouraged to include metadata elements from other vocabularies in Complete Catalog Entries.


### Summary and Content ###

OPDS Catalog Entries use "atom:content" and "atom:summary" elements to describe a Publication. This is a distinction from Atom `[RFC4287]`, which uses "atom:content" for the "content of the entry." Instead, OPDS Catalog Entries reference an electronic document with the Publication's content using Acquisition Links. OPDS Catalog Entries SHOULD include either "atom:summary" or "atom:content" elements or both to provide a description, summary, abstract, or excerpt of the Publication.

An "atom:summary" element in an OPDS Catalog Entry MUST use a "type" attribute of "text" and the content MUST NOT contain child elements. The content of an "atom:summary" element SHOULD NOT duplicate the content of "atom:title" or "atom:content". Such text is intended to be presented to humans in a readable fashion. The restriction of the content of "atom:summary" and the "type" attribute is a restriction of Atom `[RFC4287]`.

An "atom:content" element in an OPDS Catalog Entry either contains or links to a description, summary, abstract, or excerpt of the Publication. The behavior or "atomOutOfLineContent" and the "src" attribute is defined in Section 4.1.3 of `[RFC4287]`.

If an OPDS Catalog Entry includes both "atom:content" and "atom:summary", the "atom:content" SHOULD NOT be included in the Partial Catalog Entry. Both elements SHOULD be included in the Complete Catalog Entry.

```
atomSummary = 
  element atom:summary {
    atomCommonAttributes,
    attribute type { "text" }?,
    text
}
```

### Entry Relations ###

OPDS Catalog Entry Documents SHOULD include links to related Resources. This specification defines new relations for linking from OPDS Catalog Entry Documents. They are defined in the Sections Acquisition Relations and Artwork Relations.

OPDS Catalog providers are encouraged to use relations from `[RFC5988]` inside OPDS Catalog Entry Documents where appropriate.

#### Acquisition Relations ####

Acquisition relations describe the extent of the content referred to by an Acquisition Link or the manner in which that Resource may be acquired. This specification defines six Acquisition Relations, which all begin with "http://opds-spec.org/acquisition":

  * "http://opds-spec.org/acquisition": A generic relation that indicates that the complete representation of the content Resource may be retrieved.
  * "http://opds-spec.org/acquisition/open-access": Indicates that the complete representation of the Resource can be retrieved without any requirement, which includes payment and registration.
  * "http://opds-spec.org/acquisition/borrow": Indicates that the complete representation of the content Resource may be retrieved as part of a lending transaction.
  * "http://opds-spec.org/acquisition/buy": Indicates that the complete representation of the content Resource may be retrieved as part of a purchase.
  * "http://opds-spec.org/acquisition/sample": Indicates that a subset of the content Resource may be retrieved.
  * "http://opds-spec.org/acquisition/subscribe": Indicates that the complete representation of the content Resource may be retrieved as part of a subscription.

#### Artwork Relations ####

OPDS Catalog Entries MAY include atom:links to images that provide a visual representation of the Publication. For many Publications, these images will be the Publication's artwork. This specification defines two Artwork Relations, which begin with "http://opds-spec.org/image":

  * "http://opds-spec.org/image": a graphical Resource associated to the OPDS Catalog Entry
  * "http://opds-spec.org/image/thumbnail": a reduced-size version of a graphical Resource associated to the OPS Catalog Entry

Image resources related by http://opds-spec.org/image/thumbnail SHOULD be suitable for presentation at a small size.

The atom:links with these relations SHOULD include at least one link with a type attribute of "image/gif", "image/jpeg", or "image/png" and the image Resources MUST be in GIF, JPEG, or PNG format.

Additional atom:links MAY also include additional resources using a vector-based format.

While either image Resource is optional and may be included independently, OPDS Catalog providers are encouraged to provide both these relations and Resources whenever possible.

Some OPDS Catalog providers MAY choose to provide http://opds-spec.org/image/thumbnail image Resources using the "data" URL scheme from `[RFC2397]`. OPDS Catalog clients SHOULD support the "data" URL scheme if they support Artwork relations.

### Entry Examples ###

An example of a Partial Catalog Entry (as would appear in an Acquisition Feed) for a Publication available in two formats:
```
  <entry>
    <title>Bob, Son of Bob</title>
    <id>urn:uuid:6409a00b-7bf2-405e-826c-3fdff0fd0734</id>
    <updated>2010-01-10T10:01:11Z</updated>
    <author>
      <name>Bob the Recursive</name>
      <uri>http://opds-spec.org/authors/1285</uri>
    </author>
    <dc:language>en</dc:language>
    <dc:issued>1917</dc:issued>
    <category scheme="http://www.bisg.org/standards/bisac_subject/index.html"
              term="FIC020000"
              label="FICTION / Men's Adventure"/>
    <summary type="text">The story of the son of the Bob and the gallant part he played in
      the lives of a man and a woman.</summary>
    <link rel="http://opds-spec.org/image"     
          href="/covers/4561.lrg.png"
          type="image/png"/> 
    <link rel="http://opds-spec.org/image/thumbnail" 
          href="/covers/4561.thmb.gif"
          type="image/gif"/>

    <link rel="alternate"
          href="/opds-catalogs/entries/4571.complete.xml"
          type="application/atom+xml;type=entry;profile=opds-catalog" 
          title="Complete Catalog Entry for Bob, Son of Bob"/>

    <link rel="http://opds-spec.org/acquisition" 
          href="/content/free/4561.epub"
          type="application/epub+zip"/>
    <link rel="http://opds-spec.org/acquisition" 
          href="/content/free/4561.mobi"
          type="application/x-mobipocket-ebook"/>
 </entry>
```

The Complete Catalog Entry for the same Publication:
```
  <entry>
    <title>Bob, Son of Bob</title>
    <id>urn:uuid:6409a00b-7bf2-405e-826c-3fdff0fd0734</id>
    <updated>2010-01-10T10:01:11Z</updated>

    <author>
      <name>Bob the Recursive</name>
      <uri>http://opds-spec.org/authors/1285</uri>
    </author>
    <dc:language>en</dc:language>
    <dc:issued>1917</dc:issued>
    <category scheme="http://www.bisg.org/standards/bisac_subject/index.html"
              term="FIC020000"
              label="FICTION / Men's Adventure"/>

    <summary type="text">The story of the son of the Bob and the gallant part he played in
      the lives of a man and a woman.</summary>
    <content type="text">The story of the son of the Bob and the gallant part
      he played in the lives of a man and a woman. Bob begins his humble life
      under the wandering eye of his senile mother, but quickly learns how to
      escape into the wilder world. Follow Bob as he uncovers his father's past
      and uses those lessons to improve the lives of others.</content>

    <link rel="http://opds-spec.org/image"     
          href="/covers/4561.lrg.png"
          type="image/png"/> 
    <link rel="http://opds-spec.org/image/thumbnail" 
          href="/covers/4561.thmb.gif"
          type="image/gif"/>

    <link rel="self"
          href="/opds-catalogs/entries/4571.complete.xml"
          type="application/atom+xml;type=entry;profile=opds-catalog"/>

    <link rel="http://opds-spec.org/acquisition" 
          href="/content/free/4561.epub"
          type="application/epub+zip"/>
    <link rel="http://opds-spec.org/acquisition" 
          href="/content/free/4561.mobi"
          type="application/x-mobipocket-ebook"/>
 </entry>
```

### Element Definitions ###

#### The "atom:entry" Element ####

The "atom:entry" element is the document (i.e., top-level) element of an OPDS Catalog Entry Document, acting as a container for metadata and data associated with an available Publication.

The following child elements are refined by this specification:

  * OPDS Catalog Entry Documents MUST contain at least one Acquisition Link, an atom:link element with a rel attribute that begins with "http://opds-spec.org/acquisition".

#### The "atom:link" Element ####

The "atom:link" element defines a reference from an Atom Entry or Atom Feed to a Resource.

```
atomLink =
  element atom:link {
    atomCommonAttributes ,
    attribute href { atomUri },
    attribute type { atomMediaType }? ,
    attribute hreflang { atomLanguageTag }? ,
    attribute title { text }? ,
    attribute length { text }? ,
  ((attribute rel { "http://opds-spec.org/facet" }, (attribute opds:facetGroup { text }? & attribute opds:activeFacet { "true" }? ))
    |
   (attribute rel { "http://opds-spec.org/acquisition/buy" }, opdsPrice+ )
   |
   (attribute rel { OPDSUrisExceptBuy }, opdsPrice*)
   |
   (attribute rel { atomNCName | ( atomUriExceptOPDS ) } ))? ,
    (opdsIndirectAcquisition |
    anyOPDSForeignElement |
    text)*
  }

  # Here is where OPDS Catalogs use John Cowan's pragmatic evaluation of an
  # IRI. This modifies xsd:anyURI in XSD 1.0 to exclude ASCII characters not
  # valid in 1.1 or IRI's without being escaped. This matches the OPDS and Atom
  # specs, but not the non-normative atom.rnc.
  atomUri = xsd:anyURI - xsd:string {pattern = '.*[ <>{}|^`"\\\n\r\t].*'}
```

The following child elements are defined by this specification:

  * atom:link elements with a rel attribute value of "http://opds-spec.org/acquisition/buy" MUST contain at least one opds:price element.
  * atom:link elements with a rel attribute of "http://opds-spec.org/acquisition/borrow", "http://opds-spec.org/acquisition/subscribe", or "http://opds-spec.org/acquisition/sample" MAY contain one or more opds:price elements.

#### The "opds:price" Element ####

The "opds:price" element represents the acquisition price in a particular currency of an individual Publication in a particular format from a particular provider. This element can appear as a child of the atom:link element (in OPDS Catalog Entry Documents).

The content of opds:price is text describing a currency value. A currency sign MUST NOT be included.

```
opdsPrice = 
  element opds:price {
    atomCommonAttributes,
    attribute currencycode { opdsPriceCurrencyCode },
    xsd:decimal { minInclusive="0.0" } 
  }
```

##### The "currencycode" Attribute #####

On the opds:price element, the value of the "currencycode" attribute MUST be an active code from `[ISO4217]` representing a currency. It defines the currency used for the content of the opds:price element.

#### The "opds:indirectAcquisition" Element ####

In some cases, the OPDS Catalog provider MAY require the client to acquire an intermediate Resource before acquiring the final Publication.
This can be the case for example with containers (archive formats, multimedia containers for various formats) or when a payment is required (need to go through a series of HTML pages to handle the transaction).

The "opds:indirectAcquisition" element represents these secondary media types `[MIMEREG]` that the client can expect to acquire if they follow the Acquisition Link.

These "opds:indirectAcquisition" elements CAN be arbitrarily nested to represent several levels of indirection.

```
opdsIndirectAcquisition = 
  element opds:indirectAcquisition {
    atomCommonAttributes,
    attribute type { atomMediaType },
    (  anyOPDSForeignElement | 
      opdsIndirectAcquisition) *
  }
```

## Acquiring Publications ##

The goal of OPDS Catalogs is to make Publications both discoverable and straightforward to acquire on a range of devices and platforms. To support that goal, this specification strives to provide a framework for describing how a Publication may be acquired while not attempting to constrain this very complex topic. Commonly-used acquisition scenarios may be specified in an update to this specification.

All Acquisition Links MUST include a "type" attribute that advises clients on the media type of the representation that is expected to be returned when the value of the href attribute is dereferenced. As with Atom, the value of the type attribute MUST conform to the syntax of a MIME media type `[MIMEREG]`.

Publications in a format using Digital Rights Management SHOULD use a different value for the type attribute of the Acquisition Link than the same format without Digital Rights Management.

OPDS Catalog clients may only support a subset of all possible Publication media types. These clients will need to filter both the type attribute of Acquisition Links.

OPDS Catalogs may only provide certain Publications through an Indirect Acquisition, either through a container or a different Acquisition workflow.
In such cases, it is up to the clients to filter these publications based on both the "opds:indirectAcquisition" and "atom:link" type attributes.

### Acquisition Examples ###

The simplest case is a Publication available in one format:

```
<link rel="http://opds-spec.org/acquisition" 
      type="video/mp4v-es" 
      href="/content/free/4561.mp4"/>
```

If the Publication was available in multiple formats as unique Resources, they would simply be listed:

```
<link rel="http://opds-spec.org/acquisition/borrow" 
      href="/content/borrow/4561.mobi"
      type="application/x-mobipocket-ebook" />

<link rel="http://opds-spec.org/acquisition/borrow" 
      href="/content/borrow/4561.epub"
      type="application/epub+zip" />
```

If the Publication requires payment, at least one "opds:price" element is required:

```
<link rel="http://opds-spec.org/acquisition/buy"
      href="/product/song1.mp3"
      type="audio/mpeg">
  <opds:price currencycode="USD">1.99</opds:price> 
</link> 
```

If the same Publication requires a payment through an HTML page, then an "opds:indirectAcquisition" element is required to
describe the content type of the final Publication Representation:

```
<link rel="http://opds-spec.org/acquisition/buy"
      href="/product/1"
      type="text/html">
  <opds:price currencycode="USD">1.99</opds:price>
  <opds:indirectAcquisition type="audio/mpeg" />
</link> 
```

Multiple "opds:indirectAcquisition" elements can also be used as child elements of an Acquisition Link or another "opds:indirectAcquisition" when this is necessary (a bundle would be a good example):

```
<link type="text/html" rel="http://opds-spec.org/acquisition/buy" href="/item/1111/buy/">
  <opds:price currencycode="EUR">10.99</opds:price>
  <opds:indirectAcquisition type="application/zip">
    <opds:indirectAcquisition type="application/epub+zip" />
    <opds:indirectAcquisition type="application/pdf" />
    <opds:indirectAcquisition type="application/x-mobipocket-ebook" />
  </opds:indirectAcquisition>
</link>
```

## Acquisition Feed Relations ##

### Facets ###

An Acquisition Feed MAY offer multiple links to reorder the Publications listed in the feed or limit them to a subset. This specification defines one new relation to identify such links as Facets:
  * "http://opds-spec.org/facet": An Acquisition Feed with a subset or an alternate order of the Publications listed.

Links using this relation MUST only appear in Acquisition Feeds.

#### The "opds:facetGroup" Attribute ####

Facets CAN be grouped together by the OPDS Catalog provider using an "opds:facetGroup" attribute. The value of this attribute is the name of the group.

A Facet MUST NOT appear in more than a single group.

#### The "opds:activeFacet" Attribute ####

A Facet is considered active, if the attribute associated to the Facet is already being used to filter Publications in the current Acquisition Feed.

The OPDS Catalog provider SHOULD indicate that a Facet is active using the "opds:activeFacet" attribute set to "true".

If the Facet is not active, the "opds:activeFacet" attribute SHOULD NOT appear in the link.

In a group of Facets, an OPDS Catalog provider MUST NOT mark more than one Facet as active.


#### The "thr:count" Attribute ####

The OPDS Catalog provider MAY provide an additional hint about the number of items expected in the Acquisition Feed, if an OPDS client follows a link.

The "thr:count" attribute, extracted from `[RFC4685]` MAY be added to a Facet in order to provide this information.

#### Example of Facets ####

```
<link rel="http://opds-spec.org/facet" 
      href="/sci-fi" 
      title="Science-Fiction" 
      opds:facetGroup="Categories" 
      opds:activeFacet="true" />

<link rel="http://opds-spec.org/facet" 
      href="/romance" 
      title="Romance"  
      opds:facetGroup="Categories" 
      thr:count="600" />

<link rel="http://opds-spec.org/facet" 
      href="/thrillers" 
      title="Thrillers"  
      opds:facetGroup="Categories" 
      thr:count="1200" />

<link rel="http://opds-spec.org/facet" 
      href="/sci-fi/english" 
      title="English" 
      opds:facetGroup="Language" 
      opds:activeFacet="true" />

<link rel="http://opds-spec.org/facet" 
      href="/sci-fi/french" 
      title="French"  
      opds:facetGroup="Language" 
      thr:count="40" />
```

## Acquisition Feed Example ##

An Acquisition Feed listing OPDS Catalog Entries from the "Unpopular Publications" Entry provided in the Navigation Feed Example:
```
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:dc="http://purl.org/dc/terms/"
      xmlns:opds="http://opds-spec.org/2010/catalog">
  <id>urn:uuid:433a5d6a-0b8c-4933-af65-4ca4f02763eb</id>

  <link rel="related" 
        href="/opds-catalogs/vampire.farming.xml" 
        type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>
  <link rel="self"    
        href="/opds-catalogs/unpopular.xml"
        type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>
  <link rel="start"   
        href="/opds-catalogs/root.xml"
        type="application/atom+xml;profile=opds-catalog;kind=navigation"/>
  <link rel="up"      
        href="/opds-catalogs/root.xml"
        type="application/atom+xml;profile=opds-catalog;kind=navigation"/>

  <title>Unpopular Publications</title>
  <updated>2010-01-10T10:01:11Z</updated>
  <author>
    <name>Spec Writer</name>
    <uri>http://opds-spec.org</uri>
  </author>

  <entry>
    <title>Bob, Son of Bob</title>
    <id>urn:uuid:6409a00b-7bf2-405e-826c-3fdff0fd0734</id>
    <updated>2010-01-10T10:01:11Z</updated>
    <author>
      <name>Bob the Recursive</name>
      <uri>http://opds-spec.org/authors/1285</uri>
    </author>
    <dc:language>en</dc:language>
    <dc:issued>1917</dc:issued>
    <category scheme="http://www.bisg.org/standards/bisac_subject/index.html"
              term="FIC020000"
              label="FICTION / Men's Adventure"/>
    <summary>The story of the son of the Bob and the gallant part he played in
      the lives of a man and a woman.</summary>
    <link rel="http://opds-spec.org/image"     
          href="/covers/4561.lrg.png"
          type="image/png"/> 
    <link rel="http://opds-spec.org/image/thumbnail" 
          href="/covers/4561.thmb.gif"
          type="image/gif"/>

    <link rel="alternate"
          href="/opds-catalogs/entries/4571.complete.xml"
          type="application/atom+xml;type=entry;profile=opds-catalog" 
          title="Complete Catalog Entry for Bob, Son of Bob"/>

    <link rel="http://opds-spec.org/acquisition" 
          href="/content/free/4561.epub"
          type="application/epub+zip"/>
    <link rel="http://opds-spec.org/acquisition" 
          href="/content/free/4561.mobi"
          type="application/x-mobipocket-ebook"/>
 </entry>

 <entry>
    <title>Modern Online Philately</title>
    <id>urn:uuid:7b595b0c-e15c-4755-bf9a-b7019f5c1dab</id>
    <author>
      <name>Stampy McGee</name>
      <uri>http://opds-spec.org/authors/21285</uri>
    </author>
    <author>
      <name>Alice McGee</name>
      <uri>http://opds-spec.org/authors/21284</uri>
    </author>
    <author>
      <name>Harold McGee</name>
      <uri>http://opds-spec.org/authors/21283</uri>
    </author>
    <updated>2010-01-10T10:01:10Z</updated>
    <rights>Copyright (c) 2009, Stampy McGee</rights>
    <dc:identifier>urn:isbn:978029536341X</dc:identifier>
    <dc:publisher>StampMeOnline, Inc.</dc:publisher>
    <dc:language>en</dc:language>
    <dc:issued>2009-10-01</dc:issued>
    <content type="text">The definitive reference for the web-curious
      philatelist.</content>
    <link rel="http://opds-spec.org/image"     
          href="/covers/11241.lrg.jpg"
          type="image/jpeg"/> 

    <link rel="http://opds-spec.org/acquisition/buy" 
          href="/content/buy/11241.epub"
          type="application/epub+zip">
      <opds:price currencycode="USD">18.99</opds:price>
      <opds:price currencycode="GBP">11.99</opds:price>
    </link>
 </entry>
</feed>
```

# Search #

An OPDS Catalog MAY provide a search facility through an `[OpenSearch]` description document. Links to `[OpenSearch]` description documents MUST use the "search" relation value and the "application/opensearchdescription+xml" media type as defined in the "Autodiscovery" section of the `[OpenSearch]` specification.

```
<link rel="search" 
      href="search.xml" 
      type="application/opensearchdescription+xml"/>
```

In an `[OpenSearch]` description document, the search interface SHOULD use the media type associated to OPDS Catalogs:
```
<Url type="application/atom+xml;profile=opds-catalog"
     template="http://example.com/search?q={searchTerms}" />
```

An OPDS Catalog MAY also provide more advanced possibilities for its search endpoint, using one or more fully qualified parameters from the Atom namespace such as:
  * atom:author
  * atom:contributor
  * atom:title

OPDS Catalog Feed Documents MAY include elements from the `[OpenSearch]` namespace such as "opensearch:totalResults" or "opensearch:itemsPerPage" in `[OpenSearch]` responses.

## Search Example ##

In order to provide a search endpoint that supports both basic (keyword based) and advanced search, an OPDS Catalog could provide the following template in its `[OpenSearch]` Description document:

```
<Url type="application/atom+xml;profile=opds-catalog"
     xmlns:atom="http://www.w3.org/2005/Atom"
     template="http://example.com/search?q={searchTerms}&author={atom:author}&contributor={atom:contributor}&title={atom:title}" />
```

With such a template, an OPDS Client could for example support the following search queries:
  * http://example.com/search?q=gardening
  * http://example.com/search?q=gardening&author=smith
  * http://example.com/search?author=drucker
  * http://example.com/search?author=ferriss&title=four


# OPDS Catalog Relations #

OPDS Catalog Feed Documents SHOULD include links to other available Acquisition and Navigation Feeds and other related Resources to encourage independent navigation.

These relations MAY be used by clients to provide additional or alternative navigation, both in a Navigation Feed or an Acquisition Feed.

The following relations are derived from `[RFC5988]`, with some clarification:

  * "start": The OPDS Catalog Root.
  * "subsection": A Navigation Feed not better described by a more specific relation.

When creating an OPDS Catalog with Navigation and Acquisition Feeds, OPDS Catalog providers are encouraged to use the relations defined in this specification and `[RFC5988]`. If no appropriate relation is found, the Feeds SHOULD use a descriptive "atom:title" element and the "atom:link"s SHOULD use a descriptive "title" attribute.

## Sorting Relations ##

This specification defines two new relations, which begin with "http://opds-spec.org/sort", to describe how an Acquisition Feed is sorted. These relations SHOULD be used when creating Navigation Feeds and the OPDS Catalog Root, if applicable.

  * "http://opds-spec.org/sort/new": An Acquisition Feed with newly released OPDS Catalog Entries. These Acquisition Feeds typically contain a subset of the OPDS Catalog Entries in an OPDS Catalog based on the publication date of the Publication.
  * "http://opds-spec.org/sort/popular": An Acquisition Feed with popular OPDS Catalog Entries. These Acquisition Feeds typically contain a subset of the OPDS Catalog Entries in an OPDS Catalog based on a numerical ranking criteria.

Acquisition Feeds using the "http://opds-spec.org/sort/new" relation SHOULD be ordered with the most recent items first. Acquisition Feeds using the "http://opds-spec.org/sort/popular" relation SHOULD be ordered with the most popular items first.

## Featured Relation ##

This specification also defines a relation to describe an Acquisition Feed of featured items. This relation SHOULD be used when creating Navigation Feeds and the OPDS Catalog Root, if applicable.

  * "http://opds-spec.org/featured": An Acquisition Feed with featured OPDS Catalog Entries. These Acquisition Feeds typically contain a subset of the OPDS Catalog Entries in an OPDS Catalog that have been selected for promotion by the OPDS Catalog provider. No order is implied.

## Recommendations ##

This specification also defines a relation to describe an Acquisition Feed of recommended items. Since recommendations can be customized for the user, such feed may require some kind of prior authentication. This relation SHOULD be used when creating Navigation Feeds and the OPDS Catalog Root, if applicable.

  * "http://opds-spec.org/recommended": An Acquisition Feed with recommended OPDS Catalog Entries. These Acquisition Feeds typically contain a subset of the OPDS Catalog Entries in an OPDS Catalog that have been selected specifically for the user. Acquisition Feeds using the "http://opds-spec.org/recommended" relation SHOULD be ordered with the most recommended items first.

## Relations for Previously Acquired Content ##

An OPDS catalog MAY track content that was previously acquired by the user. This specification defines two new relations to identify Acquisition Feeds listing such resources:

  * "http://opds-spec.org/shelf": A Resource that includes a user's existing set of Acquired Content, which MAY be represented as an OPDS Catalog.
  * "http://opds-spec.org/subscriptions": A Resource that includes a user's set of subscriptions, which MAY be represented as an OPDS Catalog.

An OPDS client MAY use these links to automatically sync content to the user's local shelf or check for periodical content updates.


## Crawlable Feed Relation ##

For aggregation or crawling purposes, an OPDS Catalog MAY link to an optimized Acquisition Feed. This specification defines one new relation for this goal: "http://opds-spec.org/crawlable".

See Complete Acquisition Feeds for more information about this feed.

# Feed Handling #

## Listing Acquisition Feeds ##

OPDS Catalog Feed Documents, especially Acquisition Feeds, may contain large numbers of Atom Entries.

A client such as a web spider or web browser might be overwhelmed if the response to a GET contained every Atom Entry in an Acquisition Feed -- in turn the server might also waste bandwidth and processing time on generating a response that cannot be handled. For this reason, servers MAY respond to Acquisition Feed GET requests with a paginated response: an OPDS Catalog Feed Document containing a partial list of the Acquisition Feed's member Atom Entries and a link to the next partial Acquisition Feed, if it exists, as defined in Section 3 of `[RFC5005]`.

OPDS Catalog providers SHOULD use Partial Catalog Entries in all Acquisition Feeds except Complete Acquisition Feeds, which are intended for crawling and are referenced using the http://opds-spec.org/crawlable relation.

Clients MUST NOT assume that an OPDS Catalog Entry returned in the Acquisition Feed is a full representation of an OPDS Catalog Entry Resource, as described in the Section Partial and Complete Entries.

## Complete Acquisition Feeds ##

An OPDS Catalog provider MAY provide a single, consolidated Acquisition Feed that includes the complete representation of every unique OPDS Catalog Entry Document in an OPDS Catalog in an atom:feed to facilitate crawling and aggregation. Complete Acquisition Feeds SHOULD NOT be paginated unless they are extremely large.

This representation is called a Complete Acquisition Feed and each OPDS Catalog Entry MUST be ordered by atom:updated, with the most recently updated Atom Entries coming first in the document order.

If available, each OPDS Catalog Feed Document in the OPDS Catalog SHOULD contain an atom:link element with a relation of "http://opds-spec.org/crawlable" that references the Complete Acquisition Feed Resource.

A Complete Acquisition Feed MUST include a fh:complete element from `[RFC5005]` unless pagination is required. See Section 2 of `[RFC5005]` for the specification of the fh:complete element.

OPDS Catalog providers SHOULD use a compressed Content-Encoding when transmitting Complete Acquisition Feeds over HTTP. See Section 14.11 of `[RFC2616]` for more on compression.

OPDS Catalog providers MUST include Complete Catalog Entries when serializing a Complete Acquisition Feed.

# Aggregating OPDS Catalogs #

OPDS Catalogs may be aggregated using the same techniques as Atom Feeds. Aggregators SHOULD use the atom:source element from Section 4.2.11 of `[RFC4287]` to include information about the original OPDS Catalog.

# Discovering OPDS Catalogs #

OPDS Catalogs may be referenced in HTML/XHTML pages, HTTP headers, or using other techniques. These links may reference both OPDS Catalog Entries or Feeds.

Links to OPDS Catalog Entry Document Resources MUST use a type attribute of "application/atom+xml;type=entry;profile=opds-catalog". Links to OPDS Catalog Feed Document Resources MUST use a type attribute of "application/atom+xml;profile=opds-catalog".

The most common mechanism for encouraging the auto-discovery of OPDS Catalogs is to link from an HTML document to the OPDS Catalog Root Resource, using the auto-discovery pattern popularized by the syndicated feed community `[AUTODISCOVERY]`.

Multiple links to OPDS Catalog Resources MAY be expressed in a single HTML document.

An example of two links inside an HTML page about the same Publication:
```
<link rel="related"   
      href="/opds-catalogs/root" 
      type="application/atom+xml;profile=opds-catalog"  
      title="Example OPDS Catalog" /> 

<link rel="alternate" 
      href="/entry/1"
      type="application/atom+xml;type=entry;profile=opds-catalog" 
      title="Example OPDS Entry" /> 
```

Auto-discovery links MAY also be expressed using HTTP headers as defined in `[RFC5988]`.

# OPDS URI Scheme #

In order to link directly to an OPDS Catalog Feed or an OPDS Catalog Entry Document, this specification introduces a new URI scheme as defined in Section 3.1 of `[RFC3986]`.

This scheme SHOULD only be used when none of the other discovery methods are available.

The full details are available under the "IANA Registration of opds URI Scheme" section of this specification.

# Securing OPDS Catalogs #

OPDS Catalogs are delivered over HTTP. Authentication requirements for HTTP are covered in Section 11 of `[RFC2616]`.

The type of authentication required for any OPDS Catalog is a decision to be made by the OPDS Catalog provider. OPDS Catalog clients are likely to face authentication schemes that vary across OPDS Catalogs. At a minimum, client and server implementations MUST be capable of being configured to use HTTP Basic Authentication `[RFC2617]` in conjunction with a connection made with TLS 1.0 `[RFC2246]` or a subsequent standards-track version of TLS supporting the conventions for using HTTP over TLS described in `[RFC2818]`. It is RECOMMENDED that OPDS Catalog clients be implemented in such a way that new authentication schemes can be deployed.

Because this protocol uses HTTP response status codes as the primary means of reporting the result of a request, OPDS Catalog providers are advised to respond to unauthorized or unauthenticated requests using an appropriate 4xx HTTP response code (e.g., 401 "Unauthorized" or 403 "Forbidden") in accordance with `[RFC2617]`.

# Bandwidth and Processing Considerations #

Many OPDS Catalog clients operate in mobile environments, which may impose strict limitations on bandwidth and processing resources. OPDS Catalog publishers are strongly encouraged to publish their OPDS Catalogs using compression and caching techniques and the partial feeds described in the Section Listing Acquisition Feeds. Implementers are encouraged to investigate and use alternative mechanisms regarded as equivalently good or better at the time of deployment. See `[CACHING]` for more on caching techniques.


# Security Considerations #

OPDS Catalogs are Atom documents delivered over HTTP and thus subject to the security considerations found in Section 15 of `[RFC2616]` and Section 5 of `[RFC4287]`.

## Linked Resources ##

OPDS Catalogs can contain XML External Entities as defined in Section 4.2.2 of `[REC-xml]`. OPDS Catalog implementations are not required to load external entities. External entities are subject to the same security concerns as any network operation and can alter the semantics of an OPDS Catalog Feed Document or OPDS Catalog Entry Document. The same issues exist for Resources linked to by elements such as atom:link and atom:content.

## URIs and IRIs ##

OPDS Catalog implementations handle URIs and IRIs. See Section 7 of `[RFC3986]` and Section 8 of `[RFC3987]` for security considerations related to their handling and use.

## Code Injection and Cross Site Scripting ##

OPDS Catalogs can contain a broad range of content types including code that might be executable in some contexts. Malicious publishers could attempt to attack servers or other clients by injecting code into OPDS Catalog Feed Documents or OPDS Catalog Entry Documents or Media Resources.

Server implementations are strongly encouraged to verify that external content is safe prior to aggregating, processing, or publishing it. In the case of HTML, experience indicates that verification based on a white list of acceptable content is more effective than a black list of forbidden content.

Additional information about XHTML and HTML content safety can be found in Section 8.1 of `[RFC4287]`.

# IANA Registration of opds URI Scheme #

In accordance with `[RFC4395]`, this section provides the information required to register the opds URI scheme.

## URI Scheme Name ##

opds

## Status ##

permanent

## URI Scheme Syntax ##

The 'opds' URI takes the form of the opds-uri rule below as specified using ABNF from `[RFC5234]`:

```
opds-uri = "opds://" absolute-URI
```

## URI Scheme Semantics ##

The opds URI Scheme identifies Open Publication Distribution System (OPDS) resources that can be consumed by dedicated clients, and provides the location to these resources.

Each application implementing the 'opds' URI scheme is permitted to choose how to handle the OPDS Document associated to the URI.
The current practice is to either display the information available in the OPDS Document or to start the acquisition of the resource if a link is provided.

This scheme is associated to either OPDS Feed Documents (identified by the "application/atom+xml;profile=opds-catalog" media type) or OPDS Entry Documents (identified by the "application/atom+xml;profile=opds-catalog;type=entry" media type).

## Encoding Considerations ##

There are no encoding considerations for 'opds' URIs other than those discussed in `[RFC3986]`.

## Applications/Protocols That Use This URI Scheme Name ##

The opds URI scheme is intended to be used by OPDS clients.

## Interoperability Considerations ##

There are no known interoperability concerns related to use of the opds URI scheme.

## Security Considerations ##

See the Security Considerations section of this document.

## Contact ##

... [mailto:xxx@yyy](mailto:xxx@yyy)

## Author/Change Controller ##

... [mailto:xxx@yyy](mailto:xxx@yyy)

# References #

## Normative References ##

  * `[DCTERMS]` DCMI Usage Board, "DCMI Metadata Terms", January 2008, http://dublincore.org/documents/dcmi-terms/.
  * `[ISO4217]` "ISO 4217 currency and funds name and code elements", International Standard ISO 4217, http://www.iso.org/iso/en/prods-services/popstds/currencycodeslist.html.
  * `[MIMEREG]` Freed, N. and J. Klensin, "Media Type Specifications and Registration Procedures", BCP 13, RFC 4288, December 2005.
  * `[OpenSearch]` Clinton D., "Open Search 1.1 Draft 4", http://www.opensearch.org/Specifications/OpenSearch/1.1.
  * `[REC-xml]` Yergeau, F., Paoli, J., Bray, T., Sperberg-McQueen, C., and E. Maler, "Extensible Markup Language (XML) 1.0 (Fourth Edition)", World Wide Web Consortium Recommendation REC-xml-20060816, August 2006, http://www.w3.org/TR/2006/REC-xml-20060816.
  * `[REC-xml-infoset]` Cowan, J. and R. Tobin, "XML Information Set (Second Edition)", World Wide Web Consortium Recommendation REC-xml-infoset-20040204, February 2004, http://www.w3.org/TR/2004/REC-xml-infoset-20040204.
  * `[REC-xml-names]` Hollander, D., Bray, T., Tobin, R., and A. Layman, "Namespaces in XML 1.0 (Second Edition)", World Wide Web Consortium Recommendation REC-xml-names-20060816, August 2006, http://www.w3.org/TR/2006/REC-xml-names-20060816.
  * `[RFC2119]` Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
  * `[RFC2246]` Dierks, T. and C. Allen, "The TLS Protocol Version 1.0", RFC 2246, January 1999.
  * `[RFC2397]` Masinter, L., "The 'data' URL scheme", RFC 2397, August 1998.
  * `[RFC2616]` Fielding, R., Gettys, J., Mogul, J., Frystyk, H., Masinter, L., Leach, P., and T. Berners-Lee, "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2616, June 1999.
  * `[RFC2617]` Franks, J., Hallam-Baker, P., Hostetler, J., Lawrence, S., Leach, P., Luotonen, A., and L. Stewart, "HTTP Authentication: Basic and Digest Access Authentication", RFC 2617, June 1999.
  * `[RFC2818]` Rescorla, E., "HTTP Over TLS", RFC 2818, May 2000.
  * `[RFC3986]` Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
  * `[RFC3987]` Duerst, M. and M. Suignard, "Internationalized Resource Identifiers (IRIs)", RFC 3987, January 2005.
  * `[RFC4287]` Nottingham, M. and R. Sayre, "The Atom Syndication Format", RFC 4287, December 2005.
  * `[RFC4288]` Freed, N. and J. Klensin, "Media Type Specifications and Registration Procedures", RFC 4288, December 2005.
  * `[RFC4685]` Snell, J., "Atom Threading Extensions", RFC 4685, September 2006.
  * `[RFC5005]` Nottingham, M., "Feed Paging and Archiving", RFC 5005, September 2007.
  * `[RFC5988]` Nottingham, M., "Web Linking", RFC5988, October 2010.

## Informative References ##

  * `[AUTODISCOVERY]` Cadenhead, R., Holderness, J., Morin, R., "RSS Autodiscovery", November 2006, http://www.rssboard.org/rss-autodiscovery.
  * `[CACHING]` Nottingham, M., "Caching Tutorial", 1998, http://www.mnot.net/cache_docs/.
  * `[REC-webarch]` Walsh, N. and I. Jacobs, "Architecture of the World Wide Web, Volume One", W3C REC REC-webarch-20041215, December 2004, http://www.w3.org/TR/2004/REC-webarch-20041215.
  * `[RNC]` Clark, J., "RELAX NG Compact Syntax", December 2001, http://www.oasis-open.org/committees/relax-ng/compact-20021121.html.

# Appendix A. Contributors #

The content and concepts within this specification are a product of the openpub community.

# Appendix B. RELAX NG Compact Schema #

This appendix is informative.

The RELAX NG schema explicitly excludes elements in the OPDS Catalog namespace that are not defined in this revision of the specification. Requirements for Atom Protocol processors encountering such markup are given in Sections 6.2 and 6.3 of `[RFC4287]`.

The Schema for OPDS Catalog Feed & Entry Documents:
```
# -*- rnc -*- 
# RELAX NG Compact Syntax Grammar for OPDS Catalog Feed & Entry Documents
# Version 2010-08-18
namespace atom = "http://www.w3.org/2005/Atom"
namespace opds = "http://opds-spec.org/2010/catalog"
namespace local = ""

# The OPDS Catalog spec extends Atom (RFC4287), and the additions require some
# patterns not used in the Atom schema. The first is atomUriExceptOPDS, which
# is used to describe an atomLink whose rel value is an atomNCName (no-colon
# name) or any URI other than these from OPDS Catalogs. In these cases, no
# opds:price element should appear.
atomUriExceptOPDS = string - ( string "http://opds-spec.org/acquisition/buy"
                             | string "http://opds-spec.org/acquisition/borrow"
                             | string "http://opds-spec.org/acquisition/subscribe"
                             | string "http://opds-spec.org/acquisition/sample" )

# Next is OPDSUrisExceptBuy, which is used to describe an atomLink whose
# rel value is from OPDS Catalogs but is not ".../acquisition/buy". In such
# cases, an opds:price element is optional.
OPDSUrisExceptBuy = string "http://opds-spec.org/acquisition/borrow"
                  | string "http://opds-spec.org/acquisition/subscribe"
                  | string "http://opds-spec.org/acquisition/sample"

# To simplify OPDS Catalog validation, we do not use Schematron to assert that
# any atom:link with a rel value of ".../acquisition/buy" must be accompanied
# by one or more opds:price elements.
# Instead we rely on Relax NG to describe one of three situations:
# - the rel value is ".../acquisition/buy" and at least one opds:price element
#   is required
# - the rel value is ".../acquisition/borrow" or ".../acquisition/subscribe" or
#   ".../acquisition/sample", in case opds:price elements may be
#   included; or
# - the value of the rel attribute is any other URI or an Atom-defined no-colon
#   name, and no opds:price element is permitted

# Note that this OPDS Catalog schema includes atom.rnc, so that schema must be
# present for validation.
# 
# Note also that atom.rnc defines atomUri as text and not as xsd:anyURI, and so
# wherever the Atom spec requires an IRI, the schema will not check the value
# against any URI pattern or logic. The OPDS Catalog schema overrides atom.rnc
# to provide a relatively accurate test. With the approval of XSD 1.1, the
# schema definition should change to xsd:anyURI to match what the spec text
# says.
include "atom.rnc" {

undefinedAttribute =
  attribute * - (xml:base | xml:lang | local:*| opds:* ) { text }

  atomLink =
    element atom:link {
      atomCommonAttributes ,
      attribute href { atomUri },
      attribute type { atomMediaType }? ,
      attribute hreflang { atomLanguageTag }? ,
      attribute title { text }? ,
      attribute length { text }? ,
    ((attribute rel { "http://opds-spec.org/facet" }, (attribute
       opds:facetGroup { text }? & attribute opds:activeFacet { "true" }? ))
     |
     (attribute rel { "http://opds-spec.org/acquisition/buy" }, opdsPrice+ )
     |
     (attribute rel { OPDSUrisExceptBuy }, opdsPrice*)
     |
     (attribute rel { atomNCName | ( atomUriExceptOPDS ) } ))? ,
      (opdsIndirectAcquisition |
      anyOPDSForeignElement |
      text)*
    }

    # Here is where OPDS Catalogs use John Cowan's pragmatic evaluation of an
    # IRI. This modifies xsd:anyURI in XSD 1.0 to exclude ASCII characters not
    # valid in 1.1 or IRI's without being escaped. This matches the OPDS and Atom
    # specs, but not the non-normative atom.rnc.
    atomUri = xsd:anyURI - xsd:string {pattern = '.*[ <>{}|^`"\\\n\r\t].*'}

    # Here we override Atom to account for HTML abuse in the summary element,
    # restricting it in OPDS Catalog to text:
    atomSummary = 
      element atom:summary {
        atomCommonAttributes,
        attribute type { "text" }?,
        text
    }
}


anyOPDSForeignElement =
  element * - ( atom:* | opds:* ) {
      ( attribute * { text }
      | text
      | anyElement )*
  } 


# An opds:indirectAcquisition should use strictly MIME media type for
#its type attribute
opdsIndirectAcquisition = 
  element opds:indirectAcquisition {
    atomCommonAttributes,
    attribute type { atomMediaType },
    (  anyOPDSForeignElement | 
      opdsIndirectAcquisition) *
  }


# An opds:price element should not contain a currency symbol; it is
# restricted to non-negative decimal numbers.
opdsPrice = 
  element opds:price {
    atomCommonAttributes,
    attribute currencycode { opdsPriceCurrencyCode },
    xsd:decimal { minInclusive="0.0" } 
  }


# Instead of allowing every possible 3-letter or 3-digit combination as a
# currency code, here the permissible codes (as identified in ISO4217 as of
# 2010-08-25) are enumerated. In 2012 or so, that standard may add, remove or
# change some currency codes, thus requiring this schema to be updated. Note
# that codes for metals and funds are not included.
opdsPriceCurrencyCode =  (   
  "AED" | "AFN" | "ALL" | "AMD" | "ANG" | "AOA" | "ARS" | "AUD" | "AWG" | "AZN" | "BAM" | "BBD" | "BDT" | 
  "BGN" | "BHD" | "BIF" | "BMD" | "BND" | "BOB" | "BOV" | "BRL" | "BSD" | "BTN" | "BWP" | "BYR" | "BZD" | 
  "CAD" | "CDF" | "CHE" | "CHF" | "CHW" | "CLF" | "CLP" | "CNY" | "COP" | "COU" | "CRC" | "CUC" | "CUP" | 
  "CVE" | "CZK" | "DJF" | "DKK" | "DOP" | "DZD" | "EEK" | "EGP" | "ERN" | "ETB" | "EUR" | "FJD" | "FKP" | 
  "GBP" | "GEL" | "GHS" | "GIP" | "GMD" | "GNF" | "GTQ" | "GYD" | "HKD" | "HNL" | "HRK" | "HTG" | "HUF" | 
  "IDR" | "ILS" | "INR" | "IQD" | "IRR" | "ISK" | "JMD" | "JOD" | "JPY" | "KES" | "KGS" | "KHR" | "KMF" | 
  "KPW" | "KRW" | "KWD" | "KYD" | "KZT" | "LAK" | "LBP" | "LKR" | "LRD" | "LSL" | "LTL" | "LVL" | "LYD" | 
  "MAD" | "MDL" | "MGA" | "MKD" | "MMK" | "MNT" | "MOP" | "MRO" | "MUR" | "MVR" | "MWK" | "MXN" | "MXV" | 
  "MYR" | "MZN" | "NAD" | "NGN" | "NIO" | "NOK" | "NPR" | "NZD" | "OMR" | "PAB" | "PEN" | "PGK" | "PHP" | 
  "PKR" | "PLN" | "PYG" | "QAR" | "RON" | "RSD" | "RUB" | "RWF" | "SAR" | "SBD" | "SCR" | "SDG" | "SEK" | 
  "SGD" | "SHP" | "SLL" | "SOS" | "SRD" | "STD" | "SVC" | "SYP" | "SZL" | "THB" | "TJS" | "TMT" | "TND" | 
  "TOP" | "TRY" | "TTD" | "TWD" | "TZS" | "UAH" | "UGX" | "USD" | "USN" | "USS" | "UYI" | "UYU" | "UZS" | 
  "VEF" | "VND" | "VUV" | "WST" | "XAF" | "XAG" | "XAU" | "XBA" | "XBB" | "XBC" | "XBD" | "XCD" | "XDR" | 
  "XFU" | "XOF" | "XPD" | "XPF" | "XPT" | "XTS" | "XXX" | "YER" | "ZAR" | "ZMK" | "ZWL" | "008" | "012" | 
  "032" | "036" | "044" | "048" | "050" | "051" | "052" | "060" | "064" | "068" | "072" | "084" | "090" | 
  "096" | "104" | "108" | "116" | "124" | "132" | "136" | "144" | "152" | "156" | "170" | "174" | "188" | 
  "191" | "192" | "203" | "208" | "214" | "222" | "230" | "232" | "233" | "238" | "242" | "262" | "270" | 
  "292" | "320" | "324" | "328" | "332" | "340" | "344" | "348" | "352" | "356" | "360" | "364" | "368" | 
  "376" | "388" | "392" | "398" | "400" | "404" | "408" | "410" | "414" | "417" | "418" | "422" | "426" | 
  "428" | "430" | "434" | "440" | "446" | "454" | "458" | "462" | "478" | "480" | "484" | "496" | "498" | 
  "504" | "512" | "516" | "524" | "532" | "533" | "548" | "554" | "558" | "566" | "578" | "586" | "590" | 
  "598" | "600" | "604" | "608" | "634" | "643" | "646" | "654" | "678" | "682" | "690" | "694" | "702" | 
  "704" | "706" | "710" | "748" | "752" | "756" | "760" | "764" | "776" | "780" | "784" | "788" | "800" | 
  "807" | "818" | "826" | "834" | "840" | "858" | "860" | "882" | "886" | "894" | "901" | "931" | "932" | 
  "934" | "936" | "937" | "938" | "940" | "941" | "943" | "944" | "946" | "947" | "948" | "949" | "950" | 
  "951" | "952" | "953" | "955" | "956" | "957" | "958" | "959" | "960" | "961" | "962" | "963" | "964" | 
  "968" | "969" | "970" | "971" | "972" | "973" | "974" | "975" | "976" | "977" | "978" | "979" | "980" | 
  "981" | "984" | "985" | "986" | "990" | "997" | "998" | "999"
)
```

This schema is also maintained in version control: http://openpub.googlecode.com/svn/trunk/schemas/opds_catalog.rnc