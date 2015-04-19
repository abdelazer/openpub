﻿#summary Meeting notes from the 12 May 2010 call

# Roll call #

Present: Ed S, Keith, Peter, Hadrien, Patrick, Liza
Regrets: Roger

# Agenda #

  * OPDS 0.9 Draft Review
  * Coordinating call for comments

# Discussion #

## OPDS 0.9 Draft Review ##

  * Some of the direct acquisition examples should be cleaned up to not include the redundant dc:format (as per [Issue #19](https://code.google.com/p/openpub/issues/detail?id=#19)).
  * Keith will consolidate the vocab around Hadrien's suggestions, although it's still unclear how we should split Catalog and Feed. We need to introduce some specific terminology for our domain but need to make them as easy as possible to understand, because we cannot (by definition) point people to external references (like atom:feed).
  * We'll probably use any new vocab in any documents that are intended for normal humans to read (but they won't refer to RFCs).
  * Keith will clarify which elements from other namespaces (like prism: and dc:) should be used.
  * Keith will go through [Issue #19](https://code.google.com/p/openpub/issues/detail?id=#19) and the spec text and
  * Hadrien and Ed will consolidate their comments about discovery. Ed includes more background but Hadrien included more discovery types (local network and HTTP headers). We'd probably try to keep the door open for future discovery techniques. All discovery techniques are based around the mimetype (and parameters). Some other techniques
  * Hadrien notes that the Link Header draft doesn't include "search", but we'll wait and see what the call for comments generate.
  * Patrick wonders if we should use atom:summary or atom:content? We should clarify when atom:content makes sense, what restrictions exist on atom:summary, and outline what the branches are for clients (all from Atom). JHadrien suggests that the ideal is probably feeds with partial entries that include textual (short) summaries and alternate links to compelte entries that have summaries and longer content (potentially XHTML). Keith agrees. Patrick is concerned that many current catalogs repeat metadata available elsewhere (author, title) in the HTML atom:content and that including both will look silly. Keith agrees but suggests that Catalog authors will realize their error. Patrick will make a ticket.
  * Hadrien will make a ticket for Keith requesting text on Cache Control and including some stronger text about targeting bandwidth- and resource-limited clients.

## Coordinating call for comments ##

  * Keith will write to atom-syntax and atom-protocol, epub-community & Norm Walsh, DeWitt Clinton, [people at big company](undisclosed.md), O'Reilly people (Tim?) and I'll write to the openpub Google Group.
  * Ed will write to code4lib.
  * Hadrien will write to Mark Nottingham, the French OPDS community, and post to MobileRead.
  * Peter will reach out to some other folks, DLF, and Read-20l.
  * Liza will write to Jon Orwant.
  * People should create new tickets or post comments to the Google Group by Wednesday 19 May 2010.
  * Make sure to point to examples of people using it now. Feedbooks (2M+/month), Ibis Reader, Prags. http://catalog.oreilly.com/aldiko/main.xml