# Introduction #

We've had a number of interest discussions about different techniques for representing Publications that use DRM and how they might be acquired. This page serves as a common place where people can add suggestions for markup and provide alternative suggestions.

Right now, our alternative offering of Direct Acqusition (with media type in the atom:link) and Indirect Acqusition (with the media type in the dc:format child of the atom:link), fails to represent all three of the possible components of a DRM'd transaction:

  * Where the DRM'd content may be acquired (potentially via some HTML stuff)?
  * What is the underlying format of the Publication (if it had no DRM)?
  * What specific DRM solution does the Publication use?

# Goals #

  * Allow an OPDS Catalog client to unambiguously filter between Publications without DRM and Publications using DRM.
  * Avoid unnecessary or redundant markup, following our "open standards and conventions, with a priority on simplicity."
  * Support DRM solutions including but not limited to what Adobe ACS4 currently supports.
  * Allow the combination of an HTML shopping cart and a DRM'd Publication that requires
  * Represent an encrypted DAISY Publication, which uses a key from the U.S. LoC's NLS that would be paired with a matching private key associated with a device held by a certified user

# Open Questions #

  * Should we be able to represent password-protected Publications?

# One DRM Negotiation #

The negotiation between a client and the server(s) to actually get a user a DRM-protected Publication can be complex. Here's a brief and probably incorrect outline of the process for acquiring ACS4-protected content simply to give the background on one current DRM technique.

  1. The user does something that allows them access to the Publication (not specified here, but could be complex)
  1. The client requests a application/vnd.adobe.adept+xml document from the ACS4 server
  1. The server returns a application/vnd.adobe.adept+xml document with metadata about how the content may be acquired
  1. The client initiates a number of requests, following the specifics outlined in the application/vnd.adobe.adept+xml, to the server to authenticate the user and request the content
  1. The server sends an specially-prepared ePub file for the user specifically to the client for reading

Note:
```
"""
One (more common) [specific DRM technique] is based on a server-based identity, such as AdobeID, with a limit on
the number of machines you can activate. Another flavor (used by B&N) is purely client-based 
using name and private (e.g. credit card #) password with no need for [server-based] activation. More 
[types of DRM] may be added in the future as there is demand for both more relaxed (e.g. pure 
tracking with no encryption) and more draconian (e.g. very hard to remove) flavors
"""
```

# Markup Alternatives #

## DRM media type parameter (KHF) ##

Proposal:
```
If the Publication is available in a format with DRM, a
drm parameter is added to the type attribute:

 <link type="application/pdf;drm=ns.adobe.com#adept"
```

Criticism:
  * Doesn't accurately represent the negotiation over the "application/vnd.adobe.adept+xml" metadata between the client and the provider, which is the actual content type that the client requests.
  * Doesn't encode the specifics of the exact type of DRM (server-side activation?, client-side, encrypted?)

Status: Rejected by author

## Adept+XML Type (MT) ##

Proposal:
```
An OPDS provider would very rarely serve ACS4 DRM-wrapped epub files directly; the much more
common scenario would be for the OPDS provider to generate and serve an acsm file (which the 
client is then free to use to acquire the 'final' epub file).

This appears very much to be another example of indirect acquisition, where doing an HTTP GET 
on the link URI supplied by the OPDS provider does not result in the actual bytes of the publication 
to be returned, but rather gives the client an intermediate resource that can then be used to acquire 
the actual publication.

<link type="application/vnd.adobe.adept+xml" 
          rel="http://opds-spec.org/acquisition"
          href="/product/9781449381806">
      <dc:format>application/epub+zip</dc:format> 
</link> 
```

Criticism:
  * Cannot be used if the Publication requires Indirect Acquisition (HTML shopping cart) in addition to DRM, which is probably the most common case.
  * Doesn't encode the specifics of the exact type of DRM (server-side activation?, client-side, encrypted?)

## Enclosed Parameter (HG) ##

Proposal:
```
Direct Acquisition

<link type="application/vnd.adobe.adept+xml;enclosed=epub" 
          rel="http://opds-spec.org/acquisition"
          href="/product/9781449381806">
</link> 

Indirect Acquisition

<link type="text/html" 
          rel="http://opds-spec.org/acquisition"
          href="/product/9781449381806">
      <dc:format>application/vnd.adobe.adept+xml;enclosed=pdf</dc:format> 
</link> 

The "enclosed" media parameter might not be the best name for this media parameter
but you get the idea. With this solution:
  * a file using DRM has a different mimetype
  * for ACS4, since several file types can use the same DRM, we identify different formats with a media type
  * both direct and indirect acquisition still work as previously defined
```

Criticism:
  * Some view this as a violation of Dublin Core. Semantics of Dublin Core elements is supposed to be resource description, not description of the the network protocol used to acquire it
  * Introducing new parameters is disliked by some, in part because it makes dispatching Publications based on media type into the proper processor break (in some contexts).
  * Doesn't encode the specifics of the exact type of DRM (server-side activation?, client-side, encrypted?)

Status: rejected by author, see new proposal

## Rights-Management Element (PS) ##

Proposal:
```
Type attribute and dc:format element solve the problem for direct acquisition. 
For indirect acquisition, another metadata element parallel to dc:format is required, I think, to solve your use case.

<link type="text/html"
         rel="http://opds-spec.org/acquisition"
         href="/product/9781449381806">
     <dc:format>application/epub+zip</dc:format>
     <opds:rights-management>http://ns.adobe.com/adept#passhash</opds:rights-management>
</link>
 
vs.
 
<link type="text/html"
         rel="http://opds-spec.org/acquisition"
         href="/product/9781449381806">
     <dc:format>application/epub+zip</dc:format>
     <opds:rights-management>none</opds:rights-management>
</link>
```

Criticism:
  * New elements come at a high cost, but may be justified.
  * Harder to filter out than only relying on type/dc:format
  * OPDS namespace SHOULD NOT be about DRM information: if we add opds:rights-management, we'll also need other fields

## Vendor types + Proprietary Rights-Management Element (HG) ##

Proposal:

Based on all the above propositions, I believe that we should support the following things:
  * atom:link@type should point to a different mimetype than the unencrypted file types (for example, application/epub+zip should be strictly for DRM-free files). For ADEPT, it would be "application/vnd.adobe.adept+xml"
  * instead of creating DRM elements in the OPDS namespace, the full responsability for DRM metadata would be on the party providing the DRM solution. ADEPT has different limitations, types of enclosed files and type of encryption than another DRM solution, and we can't define those in the OPDS namespace.

```
<link type="application/vnd.adobe.adept+xml" 
          rel="http://opds-spec.org/acquisition"
          href="/product/9781449381806">
      <adept:enclose>application/epub+zip</adept:enclose>
      <adept:encryption>password</adept:encryption>
</link> 
```

Criticism:
  * It's up to the DRM-vendors to define elements in their own namespace

## General element to represent required features/DRMs/extensions etc. (PS) ##

Proposal:

Let's not even talk about DRM per se. Look at the DRM system as a required reader feature or an EPUB extension of sorts. Let's invent an element that would provide a way to mark a link as requiring a particular feature/extension (identified by a URN) and add:

  * processing rule that all links which require features which are not understood or not supported should be ignored
  * an authoring rule that all content requiring a partucular EPUB extension or a DRM scheme explicitly states that requirement using the new element.

Example:

```
<link type="text/html" 
          rel="http://opds-spec.org/acquisition"
          href="/product/9781449381806">
      <opds:requiredFeature>http://ns.adobe.com/adept</opds:requiredFeature>
      <dc:format>application/epub+zip</dc:format>
</link> 
```