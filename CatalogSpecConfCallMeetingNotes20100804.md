#summary Meeting notes from the 4 August 2010 call

# Roll call #

Present: Roger, Keith, Tim, Hadrien, Peter B

# Agenda #

  * Schedule for 1.0
  * Artwork
  * Required spec changes
  * Multi-formats and PragDave
  * Regional availability

# Discussion #

## Schedule for 1.0 ##

Stable draft: 4 August

Public call for comment: 4 August-17 August

Schema finalized & embedded in spec: 11 August

Change review call: 18 August

Consensus call for final: 25 August

1.0 published: 27 August

## Artwork ##

  * Keith wants to remove "More than one atom:link with either relation SHOULD NOT be provided for a single OPDS Catalog Entry."
  * Keith wants to change this to SHOULD "The atom:links with these relations MUST include at least one link with a type attribute of "image/gif", "image/jpeg", or "image/png" and the image Resources MUST be in GIF, JPEG, or PNG format."
  * Keith wonders if we should move toward saying things "start with": http://opds-spec.org/image
> > - "This specification defines two Artwork Relations, which both begin with "http://opds-spec.org/image":
  * Roger suggests some editorial improvements, which are accepted.
  * Hadrien wonders if "/artwork" is better. We decide "/image" is fine.

## Required spec changes ##

  * We need to review all of the open issues tagged 1.0: http://code.google.com/p/openpub/issues/list?can=2&q=milestone=Release1.0
  * Roger wonders if OPDS is still the best name, given our movement toward generic resources rather than publications.
  * Hadrien thinks the name is becoming stale, but there's a lot of knowledge of the OPDS name.
  * Peter wants to stay with OPDS & publish, but as a _verb_ rather than as a noun.
  * Roger suggests a change to Open Publishing Distribution System
  * Keith believes that we have finished: http://code.google.com/p/openpub/issues/detail?id=32 (he closed it as Done)
  * Hadrien wonders if we need to define an alphabetical sort per http://code.google.com/p/openpub/issues/detail?id=33
> > - Keith doesn't feel this has been justified by actual users to date. We'll close and then listen.
  * Hadrien wonders if we even need the three "/sort" OPDS Catalog Relations?
> > - Keith asserts that the three we've define.
  * Hadrien asks that we close http://code.google.com/p/openpub/issues/detail?id=37
> > - Keith closes WontFix
  * We have added the open-access relation to resolve http://code.google.com/p/openpub/issues/detail?id=38
  * We need to review this Voss stuff: http://code.google.com/p/openpub/issues/detail?id=36
  * Hadrien asks Keith to remove all of the OPDS Catalog Relations save "start" and "subsection"
  * Hadrien asks Keith to remove the Entry Relations-clarifications list from the Spec.
  * Hadrien has changed some of the examples to include more formats.
  * Hadrien feels that we should group the OPDS Catalog Relations more meaningfully.

## Multi-formats and PragDave ##

## Regional availability ##

## Action Items ##

  * Keith to Remove "More than one atom:link with either relation SHOULD NOT be provided for a single OPDS Catalog Entry." ; DONE
  * Keith to change this to SHOULD "The atom:links with these relations MUST include at least one link with a type attribute of "image/gif", "image/jpeg", or "image/png" and the image Resources MUST be in GIF, JPEG, or PNG format."; DONE
  * """This specification defines two Artwork Relations, which begin with "http://opds-spec.org/image""""; DONE
  * Keith to try to move toward "content" where possible and "publish" as a verb.
  * All: We need to review this Voss stuff: http://code.google.com/p/openpub/issues/detail?id=36
  * Keith to remove all of the OPDS Catalog Relations save "start" and "subsection"; DONE
  * Hadrien to move the current Entry Relations & Catalog Relations clarifications out of the spec and into some other document.; DONE
  * Keith to remove the Entry Relations-clarifications list from the Spec and note that DRAFT-Web-Linking relations are swell.; DONE
  * Discuss Open Publishing Distribution System name change next time.
  * Hadrien will update the spec to group the OPDS Catalog Relations more meaningfully.; DONE