# Agenda #

Review the draft, vote for the OPDS 1.1 review period.

Discussion about OPDS spec reorganization.

Documentation, tools and implementations for OPDS 1.1.


# Attending #

Hadrien Gardeur, Tim Jones, Aaron Miller, Peter Brantley, Chris Rowan


# Discussion #

## Indirect Acquisition Spec Review ##

After a short review of the spec language, Aaron started a long discussion about ACS4: what happens when a catalog doesn't provide another indirect acquisition element to indicate if the file that you acquire through an .acsm is a PDF or an EPUB.

Hadrien said that it's entirely up to the clients to figure that part and decide if the catalog provides enough information or not to consider the acquisition link valid.

Tim said something similar and mentioned that in Bluefire Reader's case, they strictly use links with enough information.

Following this first discussion, another discussion about callbacks started. What happens after a user is redirected to the browser, how does the client open the file at the end of the acquisition ?

Hadrien replied that it depends on the platform:
  * for a web app, the best thing to do is to check the user's bookshelf in that case and download the new files
  * on Android/iOS you can also associate the mimetype to a client
  * if the transaction is handles in the web view, it's easy to get the file
  * and some client can also use their own URL scheme

Tim said that for Bluefire Reader their preferred method is their own scheme, although on iOS they also associate with the mimetype. Tim mentioned a specific problem on Android 3.x where you can't add a mimetype handler on .acsm because they're considered plain text files.
Hadrien replied that even with this bug, it's still possible to use a web view for Android 3.x.

Tim also mentioned that while the spec language & examples look good, that it would be useful to have more examples. Hadrien replied that he will work on a blog post about acquisition with more examples extracted from the mailing list.

## Review for the rest of the spec ##

The review for the rest went fine and the group votes for a review period before a final version of the spec is posted.

## Spec reorganization ##

Hadrien explained that while we should publish the spec as soon as the review period is over, he'd like to see a reorganized version of the spec released in August with more focus on Acquisition/Navigation rather than Feed/Entry.

Fairly long discussion between Tim, Aaron & Hadrien about the value of preparing the spec to be more serialization agnostic and the various upsides/downsides.

Agreement that it would be a good thing anyway, and that this might be a good step towards OPDS 2.0.

Aaron also mentioned that for annotations, JSON will make more sense than Atom even though the discussions about annotations are not about serialization yet.

_End_