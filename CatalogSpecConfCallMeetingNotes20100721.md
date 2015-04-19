﻿#summary Meeting notes from the 21 July 2010 call

# Roll call #

Present: Roger, Keith, Benoit, Liza, Patrick K, Patrick T, Tim, Peter B, Hadrien

# Agenda #

  * Revising schedule for 1.0
  * Removing Indirect Acquisition
  * Removing Publication Metadata
  * Images
  * Reviewing Spec Changes
  * Clarifying Role Values
  * Pure HTTP Acquisition
  * Currencycode attributes
  * Schema updates
  * Describing Regional Availablity

# Discussion #

## Revising schedule for 1.0 ##

  * Hadrien wonders whether we need a defined schedule for the Informational Documents
  * Keith agrees, but asks that the focus stay on 1.0 and then we switch
  * Roger is concerned that the schedule is too agressive, but Keith clarifies that the scope for 1.0 is fairly limited, but we'll relax it as necessary

## Removing Indirect Acquisition ##

  * Hadrien has removed the section on Indirect Acquisition
  * Patrick K feels that the specification should make stronger suggestions on Indirect Acquisition, but wonders why Hadrien omitted it.
  * Hadrien clarified that it was removed because we never reached good consensus on the specifics for these techniques.
  * Keith suggests that we've been working on specifying this for 9 months, so he'd rather wait for a while and see if there is outside experimentation, implementation, and consensus
  * Hadrien wants more feedback from the direct users of Indirect Acquisition

## Removing Publication-Specific Metadata ##

  * Hadrien would like the description of Publication-Specific Metadata to happen in more updatable places like the wiki
  * Hadrien wants to make sure that Catalog creators for other domains not be forced to use Dublin Core
  * Keith wonders what the downside of including the Relationship Between Atom and Dublin Core Metadata in the spec
  * Peter clarifies that Dublin Core is used outside of ebooks (libraries, some sectors of music)
  * Peter would like to simply state that we're trying to do wider multimedia
  * Compromise: Include text that DC isn't **required**; keep list of suggested elements in ID; move Relationship Between Atom and Dublin Core Metadata back into Spec

## Images ##

  * Hadrien updated the /covers and /thumbnail rel values to be more generic.
  * Keith suggests this needs more review

## Reviewing Spec Changes ##

  * You can svn log http://openpub.googlecode.com/svn/trunk/wiki
  * Or you can use the diff interface from the Source->Browse tab: http://code.google.com/p/openpub/source/diff?spec=svn296&r=296&format=side&path=/wiki/CatalogSpecDraft.wiki&old_path=/wiki/CatalogSpecDraft.wiki&old=295

## Clarifying Role Values ##

  * Hadrien is concerned that we're duplicating too many link rels from other registries. We should only include the ones that we absolutely need to clarify.
  * Keith agrees.

## Pure HTTP Acquisition ##

  * Keith will review this more formally.
  * Hadrien wants to keep the technique as simple as possible. The biggest addition to well-defined HTTP properties is a new HTTP Header, although the use of Location in 402 is atypical.
  * Does the document need to list more error conditions?
  * Hadrien clarifies that the he believes this will be best used for associating existing accounts rather than registering new accounts (and potentially new credit cards, etc).

## Currencycode attributes ##

  * Roger would like the specification to allow either the numeric or alphabetic codes from ISO4217.
  * ISO4217 documents both numeric and alphabetic codes, so if we're referencing ISO4217, we need to accept both.
  * The list is not that long, so it's not to big of an implementation burden.
  * There is no voiced objection to adding the numeric codes to the text and schema.

## Schema updates ##

  * Roger suggests that we include optional patterns for suggested metadata (dcWhatever). This will make it easier for local customization.
  * Roger has been doing research on specifying exact enumerations. Others suggests that including enumerations in the non-normative schema ("informative") makes sense.
  * Keith updates the Spec to make the inclusion of the RNC informative.

## Describing Regional Availablity ##

  * Tim wonders about specifiying the regional availability of publications in OPDS Catalogs.
  * Keith suggests that they throw up their suggested solution (ONIX 3.0 snippet embedded in atom:entry?) on the wiki as something labled an Informational Document and then collect feedback, clarification, and support (perhaps implementations). If there is consensus and independent implementation, it would certainly be something to consider adding to the core specification in the future.

## Action Items ##

  * Keith to implement compromise: Include text that DC isn't **required**; keep list of suggested elements in ID; move Relationship Between Atom and Dublin Core Metadata back into Spec
  * Keith will make sure that the MUST/SHOULD/MUST NOTs are updated.