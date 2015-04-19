﻿#summary Meeting notes from the February 10, 2010 call

# Roll call #

Raj K, Keith F, Roger S, Bill K, Ed S, Liza D, Tim J, Hadrien G, Peter B


# Agenda #

  * Developing the spec draft
  * Addition of dc:format to Acquisition Links
  * What are the provisions for adding metadata from external sources?
  * Global identifiers and associating Entries with identifiers

# Discussion #

## Developing the spec draft ##

Keith continues to be concerned about the development of the spec document and schema. He continues to ask for suggestions about how to get it moving faster.

Roger raises concerns about the Document Extensibility and the reservation of the opds: prefix and the OPDS namespace name. The group confirms that the namespace prefix is not significant and that the http://opds-spec.org domain is owned by IA for the use of the Openpub community.

## Addition of dc:format to Acquisition Links ##

Keith summarizes the discussion on the mailing list from the thread 'Semantics for acquisition links with an HTML cart OPDS.' He wonders whether dc:format should be required on **every** Acquisition Link.

Hadrien thinks that requiring dc:format inside all Acquisition Links is redundant and unnecessary. He'd like to encourage implementors to use HTTP-based acquisition methods. Keith asserts that providing the dc:format in every entry is a big win if we want consistency.

The group discusses two goals:
  * Allow clients to filter OPDS Catalog Entries by the available content types
  * Allow clients to filter OPDS Catalog Entries based on the whether the Acqusition Link requires a web browser

Ed notes that the dc:format solution feels like a bit of a hack. He'd prefer seeing the Acquisition Link point to the eventual location the ePub resource rather than the Shopping Cart entry point.

## What are the provisions for adding metadata from external sources? ##

Our hope is that "Processors that encounter foreign markup MUST NOT stop processing and MUST NOT signal an error. Clients SHOULD preserve foreign markup when transmitting such documents." We encourage foreign metadata to be added into the complete OPDS Catalog Entry representations (and discourage too much foreign metadata in partial Collections).

Hadrien likes the approach to metadata & extensibility that XMPP used. They wrote a simple first document but then wrote more specifications in the future to describe more advanced features.

## Global identifiers and associating Entries with identifiers ##

Keith discusses growth of ISTC

Hadrien suggests we encourage Catalog producers to include **multiple** identifiers, as that's the only pragmatic solution. Whenever possible, **all** identifiers should be included in every representation of a Catalog Entry.

Roger notes that consumers are demanding more effective consolidation of different editions and different formats of the same work.

There doesn't seem to be clear consensus on the benefit of marking certain identifiers (or metadata) as untrusted.


# Future #