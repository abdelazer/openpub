# Conference Call Meeting Notes: 16 July 2009 #

## Attendees: ##
  * Steph (chair)
  * Liza (scribe)
  * Keith
  * Hugh
  * Patrick (Bluefire)
  * Paul Norton (Adobe)
  * Peter Brantley
  * Peter Sorotokin (Adobe)
  * Marc Prud'hommeaux (Lexcycle)
  * Hadrien (Feedbooks)
  * Matt Supko (ABA/Indiebound)
  * Raj Kumar (IA)

**Bold** indicates an action item for someone.

## Introduction to OPDS/Bookserver ##

Peter introduced the October deadline and its background in the annual Internet Archive
[IA](IA.md) meeting.

  * "Bookserver" is both the name of the internal IA project and the overall ecosystem
  * The "Noah's Ark" project is the goal to have at least two components in the ecosystem:
two reading systems, two catalog providers, etc. These will have working implementations
by October.
  * This call will focus exclusively on the OPDS piece of Bookserver.

## Use Cases ##

Keith began the discussion of whether we should start with approving the use cases.

  * It was agreed that we should.
  * Hadrien cautioned that we should avoid producing an exhaustive list and that changes could be accommodate later via extensions or revisions to the specification.

**Keith agreed and will post by Friday July 24, 2009:**
  * **A confirmation of all the existing use cases**
  * **A statement describing the change process for adding additional use cases.**

Keith asked whether it would be sufficient to approve/change use cases via online discussion.

  * It was agreed that we would have discussion online and move to calls if there were significant disagreement.

## Issue Tracking ##

Steph asked if we should use the Google Code tracker to manage issues and responsibilities.

  * Hadrien was concerned that discussion could move to the tracker
  * It was agreed that we will discourage discussion on the tracker but refer to the tracker IDs in discussions via mailing list subject headings. This will allow people who find issues via the tracker to follow them on the mailing list.

**Keith will update the template for the issue tracker to mention this convention.**

Steph asked if there are issues which already need to be put in the tracker.

  * There are open issues already for OpenSearch and autodiscovery.
  * **Hadrien mentioned a metadata discussion. He will (?) create an issue for that.**

Steph asked about how we should use the ownership field in the tracker.

  * Hadrien was concerned that often the person who raises an issue will not be the one who resolves it.
  * It was decided that whoever raised the issue will be responsible for getting it assigned to someone who will resolve it.
  * Keith changed the settings on the project to email all issue updates to the mailing list. This will be revisited if it is too verbose.

## Updating the Existing Specification ##

Hadrien asked if we should update the existing draft spec with changes that are already (informally) finalized.

  * Keith preferred to leave the existing spec as-is since it describes some systems which are already in place, and to start a new spec.

**Keith will write the first revision for each update and others can make changes as
necessary.**

## OPDS Roadmap ##

Steph reviewed the existing roadmap on the Wiki. There were no major questions.

Keith suggested that OPDS implementers attempt to schedule an interop session in late
August.

**Steph will update the roadmap to reflect any changes.**

## Specification Language ##

Steph asked whether we should clarify some of the terms being used in writing up the
specification, such as "acquisition" (this may be either getting a free title, or be
part of a purchase workflow).

  * Hadrien recommended that whenever possible we use IETF language ("MUST", "SHOULD"). -
Keith agreed that the final specification should follow IETF guidelines such that it
could easily be submitted to a standards body, if we so choose.

**Steph will develop a preliminary glossary of terms that can be updated as the draft is refined.**

**Peter B. will locate the IETF style guide.**

Steph asked if the specification should be written to be testable, as some W3C guidelines are.

**Steph will find pointers to the W3C standard here and follow up.**

Hadrien asked if we will be submitting OPDS to IETF.

  * Peter S. suggested that this would be difficult because it is not a rubber-stamp
organization and would also have to go through committee discussion.
  * Hadrien thought it should be drafted as an RFC as other Atom-derived formats have.

## Future Calls ##

Steph asked if future calls should be scheduled or ad hoc based on issues to be addressed.

  * Matt prefers to resolve tricky issues by phone.
  * Peter B. & Keith prefer scheduled calls.
  * Hadrien was concerned about accommodating European timezones.
  * The next call will be scheduled via Tungle and will start much earlier (~7am US Pacific time).

**Steph will follow up with finding the best day through the mailing list followed by a Tungle invite.**


## Roles and Responsibilities ##

Hadrien requested that stakeholders indicate in the wiki which part of the ecosystem they are interested in.

  * It was agreed this was a good idea.
  * Keith cautioned that some interests will need to be represented by others, such as publishers who do not have technical resources.

**Peter will draw up a list of the participant types that will be in the Noah's Ark project (e.g. "reading systems", "catalog providers", etc.)**

**Stakeholders will self-identify with those categories.**