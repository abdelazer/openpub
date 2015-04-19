# Status of this Draft #

This document specifies the first draft of the OPDS Callback specification.



# License #

This document is licensed under [Creative Commons Attribution-Share Alike](http://creativecommons.org/licenses/by-sa/3.0/).

# Abstract #

The Open Publication Distribution System (OPDS) Callback specification is based on the `[OPDS-Catalog]` format.
It provides an easy way for any Publication provider to redirect a user to a native or a Web application in order to consume a publication.

# Introduction #

Through an OPDS Catalog, a client can browse and acquire publications. But in some cases, the user must finalize the acquisition outside of the OPDS client, for example in order to pay for a book or subscribe to a magazine.
In the end, the publication is usually delivered to the client, without any method to open the publication in the client where the acquisition started.

This specification introduces two new Callbacks, to redirect the user to a client where the publication can be consumed.

These Callbacks MAY be used independently from an OPDS Catalog, although they require the Publication provider to produce OPDS Callback Entry Documents.

# Notational Conventions #

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in `[RFC2119]`.

# Terminology #

This specification uses the same terminology found in the Terminology section of the `[OPDS-Catalog]` format.
Additionally, the following terms are also introduced:

  * Application Callback -- URI provided by an OPDS Client to consume an OPDS Callback Link.
  * Callback -- A method to redirect a user to a client where a publication can be consumed.
  * OPDS Callback Entry Document -- An OPDS Catalog Entry Document provided by the Publication provider to the client in order to acquire a Publication.
  * OPDS Callback Link -- An URI that points to an OPDS Callback Entry Document.
  * OPDS URI Scheme -- An URI scheme that starts with "opds" and points to a resource that is either an OPDS Catalog Entry Document or an OPDS Catalog Feed Document.

# OPDS Callback Entry Document #

In the `[OPDS-Catalog]` format, OPDS Catalog Entry Documents describe Publications. Each entry provides:
  * Metadata about the Publication
  * At least one Acquisition link where the client can acquire the Publication
  * Additional links either for navigation or service discovery purposes

Acquisition Links in `[OPDS-Catalog]` can be separated into three main groups:
  * those that MAY require a transaction or authentication of some kind (buy, borrow, subscribe, sample)
  * those that MUST NOT require any transaction or authentication (open-access)
  * and a generic link (acquisition)

Each type of link is identified by a relationship value as defined in the Acquisition Relations section of `[OPDS-Catalog]`.

An OPDS Callback Entry Document is an OPDS Catalog Entry Document with one additional condition. An OPDS Callback Entry Document MUST have at least one generic Acquisition Link.

This generic Acquisition Link MUST NOT require any subsequent authentication and MUST link directly to the publication and not an intermediate resource.

OPDS Callback providers MAY make these Acquisition Links time-sensitive in order to secure the access to these Publications. While this specification doesn't recommend a duration for such time-sensitive links, OPDS Callback providers SHOULD make this duration comfortable enough for clients that may download these Publications from a slow connection (such as mobile devices).

## OPDS Callback Entry Document Example ##

```
<entry xmlns="http://www.w3.org/2005/Atom" 
       xmlns:opds="http://opds-spec.org/2010/catalog" 
       xmlns:dc="http://purl.org/dc/terms/">
  <title>Bob, Son of Bob</title>
  <id>urn:uuid:6409a00b-7bf2-405e-826c-3fdff0fd0734</id>
  <updated>2010-01-10T10:01:11Z</updated>

  <author>
    <name>Bob the Recursive</name>
    <uri>http://opds-spec.org/authors/1285</uri>
  </author>
  <dc:language>en</dc:language>
  <dc:issued>1989</dc:issued>
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

  <link rel="http://opds-spec.org/acquisition" 
        href="/content/4561.epub?hash=3580979e2de35fe8e42a3ee20ebb0301"
        type="application/epub+zip"/>

  <link rel="http://opds-spec.org/shelf" 
        href="/shelf.atom" 
        type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>
</entry>
```

## Service Discovery ##

Aside from a generic Acquisition Link, an OPDS Callback Entry Document MAY contain additional links.

It is RECOMMENDED to use such links in order to enable service discovery through the identification by the client of certain relationship and media type combination.

### Service Discovery Examples ###

An OPDS Callback provider with a full OPDS Catalog available could provide a link to the OPDS Catalog Root:
```
<link rel="start" 
      href="/opds-catalog/root.xml" 
      type="application/atom+xml;profile=opds-catalog;kind=navigation"/>
```

If the Callback is for a Publication that the user just bought, a link to the bookshelf could be useful:
```
<link rel="http://opds-spec.org/shelf" 
      href="/shelf.atom" 
      type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>
```

If the user just subscribed to a Publication, the Callback could also include a link to all of the user's subscriptions:
```
<link rel="http://opds-spec.org/subscriptions" 
      href="/subscriptions" 
      type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>
```

# OPDS Callback Link #

A Publication provider MUST provide an OPDS Callback Link in order to send the OPDS Callback Entry Document to a client.

An OPDS Callback Link can either use:
  * An OPDS URI Scheme, which is more suited for Native Applications that can register the OPDS URI Scheme
  * An Application Callback URI, which is more suited for Web Applications

An OPDS Callback Link MUST NOT require additional authentication to access the OPDS Callback Entry Document referenced.

OPDS Callback providers MAY make these OPDS Callback Links time-sensitive in order to secure the access to these Publications. While this specification doesn't recommend a duration for such time-sensitive links, OPDS Callback providers SHOULD make this duration comfortable enough for clients that may download these Publications from a slow connection (such as mobile devices).

## OPDS URI Scheme ##

The OPDS URI Scheme is a URI Scheme as defined in `[RFC3986]` and in the OPDS URI Scheme section of `[OPDS-Catalog]`.

In an `[OPDS-Catalog]`, this scheme uses "opds" and the path MUST point strictly to either an OPDS Catalog Entry Document or an OPDS Catalog Feed Document.

An OPDS Callback Link using the OPDS URI Scheme MUST point to an OPDS Callback Entry Document and MUST NOT point to an OPDS Catalog Feed Document.

Any application MAY register this URI Scheme to detect an OPDS Callback Link, open the associated OPDS Callback Entry Document and download the Publication.

### OPDS URI Scheme Example ###

An OPDS Callback Link to "opds-example.org/example.opds?hash=2c8b6d72435c8664c1cf383971f8e244" would be:

```
<a href="opds://opds-example.org/example.opds?hash=2c8b6d72435c8664c1cf383971f8e244">
  Open this Publication
</a>
```

## Application Callback URI ##

An Application Callback URI is an URI to an application that can consume an OPDS Callback Entry Document.

These Application Callback URIs can be either:
  * Registered at a Publication provider
  * Added to an Indirect Acquisition Link by the application using a well-known parameter: "opds-callback"

The Publication provider MUST append to this Application Callback URI an escaped URI pointing to the OPDS Callback Entry Document.

### The "opds-callback" parameter ###

The "opds-callback" parameter is a well-known URI parameter in OPDS Callback and MUST be a well-formed URI parameter as defined in `[RFC3986]`.

Its value MUST be an URL encoded Application Callback URI.

A Publication provider MAY white-list these "opds-callback" values in order to secure a Callback.

### Application Callback URI Example ###

The application provided the following Application Callback URI: "http://opds-reader.com/?callback="

At the end of the transaction, the Publication provider wants to points the user to an OPDS Callback Entry Document at: "opds-example.org/example.opds?hash=2c8b6d72435c8664c1cf383971f8e244"

The following OPDS Callback Link is displayed:
```
<a href="http://opds-reader.com/?callback=http%3a%2f%2fopds-example.org%2fexample.opds%3fhash%3d2c8b6d72435c8664c1cf383971f8e244">
  Open this Publication
</a>
```

# Acquiring Publications #

The client MUST identify at least one Acquisition Link in the OPDS Callback Entry Document. The client MAY download directly the link as soon as the entry is parsed, or it MAY provide alternate options to the user.

An OPDS Callback Entry Document MAY contain more than a single generic Acquisition Link that the client can follow. In this case, it is up to the client to decide which Acquisition Link should be followed, or to implement more complex scenarios where the user may select the right link.

# Callback Examples #

## OPDS URI Scheme ##

A user just bought "Bob, Son of Bob", and finalized the transaction through a Web page. In the HTML page, the Callback provider includes a time-sensitive callback using the OPDS URI Scheme:
```
<a href="opds://opds-example.org/example.opds?hash=2c8b6d72435c8664c1cf383971f8e244">
  Open this Publication
</a>
```

The native application detects the OPDS URI Scheme and opens the resource associated to the link at "opds-example.org/example.opds?hash=2c8b6d72435c8664c1cf383971f8e244":

```
<entry xmlns="http://www.w3.org/2005/Atom" 
       xmlns:opds="http://opds-spec.org/2010/catalog" 
       xmlns:dc="http://purl.org/dc/terms/">
  <title>Bob, Son of Bob</title>
  <id>urn:uuid:6409a00b-7bf2-405e-826c-3fdff0fd0734</id>
  <updated>2010-01-10T10:01:11Z</updated>

  <author>
    <name>Bob the Recursive</name>
    <uri>http://opds-spec.org/authors/1285</uri>
  </author>
  <dc:language>en</dc:language>
  <dc:issued>1989</dc:issued>
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

  <link rel="http://opds-spec.org/acquisition" 
        href="/content/4561.epub?hash=a4592f10dab48f60dc7b256d25ccc243"
        type="application/epub+zip"/>

  <link rel="http://opds-spec.org/shelf" 
        href="/shelf.atom" 
        type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>
</entry>
```

The client parses the OPDS Callback Entry Document, detects the Acquisition Link and downloads the Publication.

The Publication is added to the user's local shelf and then opened.

## Application Callback URI ##

The user is browsing an OPDS Catalog using a Web Application and selects "Bob, Son of Bob":

```
<entry xmlns="http://www.w3.org/2005/Atom" 
       xmlns:opds="http://opds-spec.org/2010/catalog" 
       xmlns:dc="http://purl.org/dc/terms/">
  <title>Bob, Son of Bob</title>
  <id>urn:uuid:6409a00b-7bf2-405e-826c-3fdff0fd0734</id>
  <updated>2010-01-10T10:01:11Z</updated>

  <author>
    <name>Bob the Recursive</name>
    <uri>http://opds-spec.org/authors/1285</uri>
  </author>
  <dc:language>en</dc:language>
  <dc:issued>1989</dc:issued>
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

  <link rel="http://opds-spec.org/acquisition/buy" 
        href="http://opds-example.org/content/4561/buy"
        type="application/epub+zip">
    <opds:price currencycode="USD">7.99</opds:price>
  </link>
</entry>
```

The user decides to click on the "Buy for 7.99 USD" link displayed.
The client redirects the user to the Acquisition Link at "http://opds-example.org/content/4561/buy" and adds an "opds-callback" parameter with its own Application Callback: "http://opds-reader.com/?callback=".

The full URL where the user is redirected is:
```
http://opds-example.org/content/4561/buy?opds-callback=http%3a%2f%2fopds-reader.com%2f%3fcallback%3d
```

The Publication provider checks if the Application Callback is authorized in its settings and walks the user through the steps necessary to finalize the transaction.

At the end of the transaction, the Publication provider displays the following link:
```
<a href="http://opds-reader.com/?callback=http%3a%2f%2fopds-example.org%2fexample.opds%3fhash%3d2c8b6d72435c8664c1cf383971f8e244">
  Open this Publication
</a>
```

The user is redirected to the initial Web client.
In the background, the client opens and parses the OPDS Callback Entry Document:

```
<entry xmlns="http://www.w3.org/2005/Atom" 
       xmlns:opds="http://opds-spec.org/2010/catalog" 
       xmlns:dc="http://purl.org/dc/terms/">
  <title>Bob, Son of Bob</title>
  <id>urn:uuid:6409a00b-7bf2-405e-826c-3fdff0fd0734</id>
  <updated>2010-01-10T10:01:11Z</updated>

  <author>
    <name>Bob the Recursive</name>
    <uri>http://opds-spec.org/authors/1285</uri>
  </author>
  <dc:language>en</dc:language>
  <dc:issued>1989</dc:issued>
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

  <link rel="http://opds-spec.org/acquisition" 
        href="/content/4561.epub?hash=a4592f10dab48f60dc7b256d25ccc243"
        type="application/epub+zip"/>

  <link rel="http://opds-spec.org/shelf" 
        href="/shelf.atom" 
        type="application/atom+xml;profile=opds-catalog;kind=acquisition"/>
</entry>
```

The client finds the Acquisition Link and downloads the Publication.

The Publication is displayed to the user.

# Security Considerations #

OPDS Callback Entry Documents are OPDS Catalog Entry Documentsthus subject to the security considerations found in `[OPDS-Catalog]`.

# References #

## Normative References ##

  * `[OPDS-Catalog]` The openpub community, "Open Publication Distribution System", June 2011, http://opds-spec.org/specs/opds-catalog-1-1.
  * `[RFC2119]` Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
  * `[RFC3986]` Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.