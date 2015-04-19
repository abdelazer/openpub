﻿#summary Meeting notes from the 19 May 2010 call

# Roll call #

Present: Hadrien, Patrick, Keith, Liza, Peter
Regrets: Ed S, Roger

# Agenda #

  * Hadrien's Draft for [Issue #6](https://code.google.com/p/openpub/issues/detail?id=#6): Relationship between OPDS and DC/PRISM
  * Update on Discovery Mechanisms
  * Review of Comments
  * Review Open Issues
  * Discuss Timeline

# Discussion #

## Discuss Timeline ##

  * Keith will incorporate all outstanding notes from open and recently closed tickets into the CatalogSpecDraft tommorrow (Thur 20 May) by EOD
  * Keith will notify the mailing list when he has no further outstanding edits
  * Everyone should incorporate all outstanding edits they've been hoping to make by EOD tommorrow (Thur 20 May)
  * Everyone is encourage to do an end-to-end review of the draft before Monday (Hadrien and another engineer will review it; other committments welcomed)
  * On Monday, 24 May 2010, we will have a brief (30 minute max) yes/no meeting. Send proxy votes to Peter B privately. "No" votes must include justification & comments.

## Hadrien's Draft for [Issue #6](https://code.google.com/p/openpub/issues/detail?id=#6): Relationship between OPDS and DC/PRISM ##

  * Gavin C, Karen Coyle, and Dave Thomas all had questions about this issue, clarifying its importance
  * Keith will add some text clarifying the role of atom:contributor (in full entries and not partial) and atom:published (encouraged but not required, describes the OPDS Catalog Entry and not the Publication)
  * Keith is concerned about MUST NOT dc:subject. Keith will comment in the ticket about MUST NOTs that he'd like to change to SHOULD NOT.
  * Keith will add some text to the spec to point to Dublin Core and PRISM explicitly (perhaps in the previous section).
  * Hadrien notes that we should be very explicit: All of the required metadata elements for Atom are required in OPDS Catalog Entries and Feeds.
  * Keith notes that we should include a comment about keeping atom:ids for OPDS Catalog Entries stable.

## Update on Discovery Mechanisms ##

  * HTTP Headers subsection added
  * Hadrien mentioned that links can point to both OPDS Catalog Entries and OPDS Catalog Feeds

## Review of Comments ##

  * More than 0 comments, which is nice.
  * Comment period will formally close at the EOD today, Wednesday 19 May.

## Review Open Issues ##

  * DRM: Can we reach consensus on this issue before EOD Thursday? If not, it'll be dropped. Keith and Hadrien prefer the media type parameter approach.
  * Hadrien suggests changing the stance on DRM to only: "Publications using Digital Rights Management MUST use a different media type than the same format without Digital Rights Management."
  * Hadrien will provide some examples of his idea in the open thread.