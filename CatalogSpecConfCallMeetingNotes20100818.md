﻿#summary Meeting notes from the 18 August 2010 call

# Roll call #

Present: Keith, Roger, Hadrien, Peter, Tim, Benoît

# Agenda #

  * Open 1.0 Tickets
  * Feedback from Benoît
  * Feedback from Dave Thomas

# Discussion #

## Open 1.0 Tickets ##


**MUST/SHOULD/MAY an Acquisition Feed use a sorting relation? (http://code.google.com/p/openpub/issues/detail?id=44): Fixed (no further comments)** subheading for definition of "start" and "subsection" (http://code.google.com/p/openpub/issues/detail?id=46): WontFix


### Sorting Relations ###

This is from the ticket: explanation of sorting relations (http://code.google.com/p/openpub/issues/detail?id=45)

Hadrien believes that the Sorting Relations are not too tightly defined. They may be used in a variety of client UXes, including the presentation of supplementary displays or interleaved aggregation.

There is consensus that the three relations we define in this section are typically subsets. "featured" may not impose an order and is based on arbitrary criteria, "new" is typically sorted by the publication date of the Publication and the latest dates are first, "popular" is typically sorted based on some numerical ranking criteria and the most popular are first.

Roger notes that many publishers would feature titles for each imprint and/or genre.

Roger wonders what OPDS Catalog providers should do when trying to present Navigation Feeds with relations that are not formally defined. Keith will write something up in the ticket for further comment. Tim adds that the driving force for establishing new conventions around relations may be the OPDS Catalog clients (rather than providers).

Keith notes the inherent, acceptable tension between providers, who want to define a hierarchy, and clients, who want to control the UI/UX.

Peter suggests that publishers have to accept a certain amount of loss of control when publishing OPDS Catalogs, especially when their content is aggregated.

Tim is concerned about not defining an order for "featured" but putting it under "Sorting." Keith will try to resolve this issue.

## Feedback from Benoît ##

We agree that we should strike this sentence: The maximum size of the longest dimension of http://opds-spec.org/image/thumbnail images SHOULD be 120 pixels.
Instead, we'll simply say that these thumbnails "SHOULD be suitable for presentation at a small size."

Benoît wonders whether Acquisition Feeds that use sorting should self-identify:

```
<feed xmlns="http://www.w3.org/2005/Atom">
  <link rel="self"    
        href="/opds-catalogs/popular.xml"
        type="application/atom+xml;profile=opds-catalog"/>
  <link rel="featured"   
        href="/opds-catalogs/popular.xml"
        type="application/atom+xml;profile=opds-catalog"/>
```

We agree that this would be swell, but that we cannot impose that requirement.

## Feedback from Dave Thomas ##

Hadrien discusses the feedback and points to his response on the mailing list. He disagrees with many of the points. Keith would like to more formally review and discuss Dave's points about better support for commercial transactions following the publication of 1.0.

Keith requests that we pull out actionable items from Dave's email for the 1.0 draft.

Hadrien notes that Dave and others are not clear on the requirements for atom:summary and atom:content.

Keith quotes the spec, which imposes some new requirements on Atom (atom:summary MUST only be type="text") but also uses Atom verbatim (like atom:content/@src). This has caused confusion.

Keith will create a ticket on Dave's behalf and try to work out clearer spec text around the issue.

Roger thinks restricting atom:summary to text-only is a mistake. Keith notes that no comments have been recieved on this issue.