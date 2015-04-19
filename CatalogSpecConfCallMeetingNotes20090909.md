# Attendees #

  * Tim Jones (Bluefire)
  * Paul Norton (Adobe)
  * Cart Reed (Ingram Digital)
  * Roger Sperberg
  * Raj Kumar (Internet Archive)
  * Keith Fahlgren (O'Reilly)
  * Stephanie (Book Oven) - chair/notetaker

**Apologies:** Liza Daly, Peter Brantley, Hadrien Gardeur

# Action items summary #

  * Cart will begin a discussion on mailing list on relevance of RssCloud and pubsubhubbub.
  * Roger to find reference on XML WG and how they split up use cases to different non-normative content (posted on list, will also add to draft spec outline before end of week).
  * **Everyone to add to/revise**<a href='https://docs.google.com/Doc?docid=0Aa_ib7wwqmSXZGRzY2ZxdmRfMzdoaHp0MndjdA&hl=en'>spec outline</a> by end of Monday September 14*** Keith & Cart will set up a call to discuss outline on Friday and will recommend the best way for people to prioritise items.
  * Steph will communicate we may need an additional call to arrive at consensus.
  * Steph to ping Peter re remote participations**

# Important dates #

  * September 14: All revisions to spec outline done.
  * September 17: Prioritization for items to be included/written in first draft of spec completed.
  * September 23: Stakeholders' call. First draft of prioritized items on spec draft completed.
  * September 30: Additional stakeholders' call (to be confirmed)
  * October 8: Final stakeholders' call (phase 1)

# Meeting Notes #

## Search ##

  * Cart is unsure why we're using OpenSearch, may be worth investigating options with RSS Cloud and pubsubhubbub.
  * Tim: Google's implementation of search protocol uses Open Search.

**Cart will begin a discussion on mailing list on relevance of RssCloud and pubsubhubbub.**

## Acquisition ##

  * Roger: Price needs to discussed better, this will be useful everywhere.
  * Cart: was Peter taking care of rental acquisition?
  * Raj: we're still taking care of loaning scenario, using adobe content server, adobe DRM/SDK
  * Cart: RssCloud and pubsubhubbub support this scenario without using adobe.
  * Raj: we don't want to deal with the DRM issue right now, going with the industry standard. Would prefer going with social DRM structure.
  * Roger mentioned XML schema spec, non-normative like use cases and tutorials are placed in separate documents. This might be the approach we want to take.

**Roger to find reference from XML schema, and add this to the spec draft as a reference, as an example appendices. References to how that group handled multiple release of documents - by the end of the week. Already sent to mailing list.**

## Spec outline ##

**Everyone to add to/revise spec outline by end of Monday September 14**

  * Keith would like everyone to attend in SF to be able to have interoperable implementation. Would like this group to be representative of consensus. Would love for the first version of draft to be done by Oct 17.
  * Steph suggests that we prioritise different sections by some we know which will be consensus or not. E.g. we know already "acquisition" and "search" will not be ready.
  * Keith: personal vote would be seeing if we're lagging in a week or so. Would like Cart to offer wisdom on structure and how the spec should be organised.
  * Keith commits to write more text.
  * Steph suggests contacting people for direct contributions.
  * Everyone to revise by Sept 14.
  * Keith will chase up muscle for writing based on important items.
  * Steph asks for a way to get everyone to put in their prioritisation.

**Keith & Cart will set up a call to discuss outline on Friday and will recommend the best way for people to prioritise items.**

  * Steph asks for approximate 1st draft deadline.
  * Keith: assuming someone is willing to have a section assigned to them. Assume sections can be written within 5 working days.
  * Steph: Set September 17th for prioritization complete deadline.
  * Steph: This may be that draft may not be ready until around Sep 23.
  * Roger: There will be back and forth on email, but we may not have consensus and october, we may need to have one additional meeting schedule.
  * Keith: not at all opposed to be having more meetings.

**Steph will communicate we may need an additional call to arrive at consensus.**

## Noah's Ark implementers list ##

  * Steph: Thanks Raj for setting this up. Currently no communications?
  * Keith: Dormant until such time we have interop issues to discuss.

## October 19/20 meeting ##

  * Steph: schedule for October is complete. A couple of free slots for breakout session, Peter is the main contact.
  * Keith: Should ask Peter if we can have it set up so we can have contributions from people not at SF. e.g. participation from IRC

**Steph to ping Peter re remote participations -- done**


## Feeds for aggregation ##

  * Raj asks for valid OPDS feeds to aggregate, and if all feeds from Stanza are valid OPDS?
  * Tim: not valid opds. you can find them at catalog.lexcycle.com
  * Raj: An OPDS feed is available at bookserver.archive.org
  * Keith: Stanza's should be pretty close. Hadrien's feed is probably the closest to be conformant. There will be an O'Reilly Catalog ready by Oct 19.
  * Raj: since there aren't any feeds out there, would it make sense for me to start aggregating Atom feeds as well?
  * Keith: that would be the pragmatic way of doing it.
  * Keith: stanza's are not valid Atom feeds. We want to be more rigorous. Chicken & egg problem re spec not yet written, therefore no "valid" feeds yet.