# Introduction #

A number of book vendors possess a books which they have less than worldwide rights to.  How do we present this information in the OPDS feed in such a manner that OPDS Clients can determine saleability before displaying invalid entries to their user.

# Goals #

  * Avoid unnecessary or redundant markup, following our "open standards and conventions, with a priority on simplicity."
  * Support current vendor needs.
  * Enable representation that is as robust as necessary to represent all possible territory rights for ebooks.

# Markup Alternatives #

## Onix-Style Declaration (TJ) ##

Proposal:

> Similar to the Onix specification for regional rights, a feed may represent its rights as a series of allowable and  disallowable regions and territories.  If an `<included>` block is included in the link specification, then only those countries or territories listed within may acquire the book from the OPDS catalog provider.  In any case, all territories  and countries in the excluded block are excluded from acquiring the book from the OPDS catalog provider.

```
<rights>
	<included>
		<country>us</country>
	</included>
	<excluded>
		<territory>US-TX</territory>
	</excluded>
</rights>
```

> Country elements would deliniated as 2 character custom codes according to ISO 3166-1 alpha 2 (http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

> Territory codes would match ONIX code list 49 which reads:


|AU-CT|Australian Capital Territory|
|:----|:---------------------------|
|AU-NS|New South Wales|
|AU-NT|Northern Territory|
|AU-QL|Queensland|
|AU-SA|South Australia|
|AU-TS|Tasmania|
|AU-VI|Victoria|
|AU-WA|Western Australia|
|CA-AB|Alberta|
|CA-BC|British Columbia|
|CA-MB|Manitoba|
|CA-NB|New Brunswick|
|CA-NL|Newfoundland and Labrador|
|CA-NS|Nova Scotia|
|CA-NT|Northwest Territories|
|CA-NU|Nunavut|
|CA-ON|Ontario|
|CA-PE|Prince Edward Island|
|CA-QC|Quebec|
|CA-SK|Saskatchewan|
|CA-YT|Yukon Territory|
|ES-CN|Canary Islands|
|GB-AIR|UK airside|Airside outlets at UK international airports only|
|GB-APS|UK airports|All UK airports, including both airside and other outlets|
|GB-CHA|Channel Islands|
|GB-ENG|England|
|GB-EWS|England, Wales, Scotland|UK excluding Northern Ireland|
|GB-IOM|Isle of Man|
|GB-NIR|Northern Ireland|
|GB-SCT|Scotland|
|GB-WLS|Wales|
|US-AK |Alaska|
|US-AL |Alabama|
|US-AR |Arkansas |
|US-AZ |Arizona |
|US-CA |California |
|US-CO |Colorado |
|US-CT |Connecticut |
|US-DC |District of Columbia |
|US-DE |Delaware |
|US-FL |Florida |
|US-GA |Georgia |
|US-HI |Hawaii |
|US-IA |Iowa |
|US-ID |Idaho |
|US-IL |Illinois |
|US-IN |Indiana |
|US-KS |Kansas |
|US-KY |Kentucky |
|US-LA |Louisiana |
|US-MA |Massachusetts |
|US-MD |Maryland |
|US-ME |Maine |
|US-MI |Michigan |
|US-MN |Minnesota |
|US-MO |Missouri |
|US-MS |Mississippi |
|US-MT |Montana |
|US-NC |North Carolina |
|US-ND |North Dakota |
|US-NE |Nebraska |
|US-NH |New Hampshire |
|US-NJ |New Jersey |
|US-NM |New Mexico |
|US-NV |Nevada |
|US-NY |New York |
|US-OH |Ohio |
|US-OK |Oklahoma |
|US-OR |Oregon |
|US-PA |Pennsylvania |
|US-RI |Rhode Island |
|US-SC |South Carolina |
|US-SD |South Dakota |
|US-TN |Tennessee |
|US-TX |Texas |
|US-UT |Utah |
|US-VA |Virginia |
|US-VT |Vermont |
|US-WA |Washington |
|US-WI |Wisconsin |
|US-WV |West Virginia |
|US-WY |Wyoming |
|ROW|Rest of world|World except as otherwise specified|
|WORLD|World|