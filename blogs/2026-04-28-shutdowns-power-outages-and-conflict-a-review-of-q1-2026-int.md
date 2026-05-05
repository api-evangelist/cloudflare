---
title: "Shutdowns, power outages, and conflict: a review of Q1 2026 Internet disruptions"
url: "https://blog.cloudflare.com/q1-2026-internet-disruption-summary/"
date: "Tue, 28 Apr 2026 13:00:00 GMT"
author: "David Belson"
feed_url: "https://blog.cloudflare.com/rss"
---
<p>In the first quarter of 2026, <a href="#government-directed-shutdowns"><u>government-directed shutdowns</u></a> figured prominently, with prolonged Internet blackouts in both Uganda and Iran, a stark contrast to the lack of observed government-directed shutdowns in the same quarter a year prior. This quarter, we also observed a number of Internet disruptions caused by <a href="#power-outages"><u>power outages</u></a>, including three separate collapses of Cuba's national electrical grid. <a href="#military-action"><u>Military action</u></a> continued to disrupt connectivity in Ukraine and also impacted hyperscaler cloud infrastructure in the Middle East. <a href="#severe-weather"><u>Severe weather</u></a> knocked out Internet connectivity in Portugal, while <a href="#cable-damage"><u>cable damage</u></a> disrupted connectivity in the Republic of Congo. A <a href="#technical-problems"><u>technical problem</u></a> hit Verizon Wireless in the United States, and <a href="#unknown-cause"><u>unknown issues</u></a> briefly disrupted connectivity for customers of providers in Guinea and the United Kingdom.</p><p>This post is intended as a summary overview of observed and confirmed disruptions and is not an exhaustive or complete list of issues that have occurred during the quarter. A larger list of detected traffic anomalies is available in the <a href="https://radar.cloudflare.com/outage-center#traffic-anomalies"><u>Cloudflare Radar Outage Center</u></a>. Note that both bytes-based and request-based traffic graphs are used within this post to illustrate the impact of the observed disruptions, with the choice of metric generally made based on which better illustrates the impact of the disruption.</p>
    <div>
      <h2>Government-directed shutdowns</h2>
      <a href="#government-directed-shutdowns">
        
      </a>
    </div>
    
    <div>
      <h3>Uganda</h3>
      <a href="#uganda">
        
      </a>
    </div>
    <p>In advance of the January 15 presidential election, <a href="https://radar.cloudflare.com/ug"><u>Ugandan</u></a> authorities ordered a nationwide Internet shutdown. The Uganda Communications Commission (UCC) <a href="https://www.monitor.co.ug/uganda/news/national/ucc-orders-mobile-network-operators-to-suspend-public-internet-access-5325326"><u>instructed mobile network operators</u></a> to suspend public Internet access, effective 18:00 local time (15:00 UTC) on January 13. The UCC <a href="https://www.aljazeera.com/news/2026/1/13/uganda-cuts-internet-days-before-presidential-election"><u>reportedly</u></a> defended the shutdown as necessary to "curb misinformation, disinformation, electoral fraud and related risks." Domestic traffic at the Uganda Internet Exchange Point (UIXP) <a href="https://x.com/kyleville/status/2011376912804024813"><u>dropped from approximately 72 Gbps to 1 Gbps</u></a> as a result of the action taken.</p><p>Similarly, Cloudflare data shows a near-complete loss of traffic from <a href="https://radar.cloudflare.com/ug"><u>Uganda</u></a> coincident with the start of the shutdown, with traffic remaining effectively at zero through 23:00 local time (20:00 UTC) on January 17, when Internet connectivity <a href="https://www.reuters.com/sustainability/society-equity/uganda-partially-restores-internet-after-ageing-president-wins-seventh-term-2026-01-18/"><u>was partially restored</u></a> after incumbent President Yoweri Museveni was declared winner of his seventh term. </p><p>Full Internet restoration was <a href="https://www.monitor.co.ug/uganda/news/national/uganda-announces-full-internet-restoration--5338692"><u>announced by the UCC on January 26</u></a>, with mobile network operators <a href="https://x.com/mtnug/status/2015685730534604850"><u>MTN Uganda</u></a> and <a href="https://x.com/Airtel_Ug/status/2015709863167332584"><u>Airtel Uganda</u></a> both confirming on social media that restrictions had been lifted. The shutdown prompted <a href="https://ntv.co.ug/news/ucc-telecom-companies-sued-over-internet-shutdown"><u>lawsuits against UCC and the telecoms companies</u></a> and drew criticism from digital rights organizations including <a href="https://cipesa.org/2026/01/navigating-the-aftermath-of-ugandas-internet-shutdown/"><u>CIPESA</u></a>.</p><p>Uganda also <a href="https://www.apc.org/en/news/uganda-2021-general-elections-internet-shutdown-and-its-ripple-effects"><u>blocked Internet access</u></a> during its 2021 election. Authorities had repeatedly promised this time would be different, <a href="https://www.aljazeera.com/news/2026/1/13/uganda-cuts-internet-days-before-presidential-election"><u>stating</u></a> as recently as January 5 that "claims suggesting otherwise are false, misleading."</p>
    <div>
      <h3>Iran</h3>
      <a href="#iran">
        
      </a>
    </div>
    <p>Iranian citizens spent a large part of Q1 2026 offline, or with severely limited connectivity, due to two nationwide Internet shutdowns. The first began around 20:00 local time (16:30 UTC) on January 8, and we explored the impact seen over the first few days in our <a href="https://blog.cloudflare.com/iran-protests-internet-shutdown/"><i><u>What we know about Iran’s Internet shutdown</u></i></a> blog post. Traffic from Iran remained near zero until January 21, when a small amount of traffic returned, only to disappear a little over 24 hours later. A similar brief restoration also occurred on January 25, before traffic recovered more aggressively starting on January 27.</p><p>A near-complete loss of announced IPv6 address space started several hours before the drop in traffic took place on January 8. <a href="https://radar.cloudflare.com/as43754"><u>Asiatech (AS43754)</u></a> was by far the single largest contributor, losing 4.46 million /48-equivalents, accounting for ~9.4% of Iran's entire IPv6 space loss on its own. <a href="https://radar.cloudflare.com/as31549"><u>RASANA (AS31549)</u></a> was the second-largest, losing 4.19 million /48-equivalents (~8.8% of the country total). As would be expected, this resulted in the share of IPv6 traffic in Iran going to zero. Given the gap in timing between this change and the loss of traffic across the country, this may have been a leading indicator of what was about to happen, but likely not a direct cause of it. Some nominal shifts in announced IPv4 address space are visible during the shutdown, but levels remained fairly consistent during the shutdown period. These observations suggest that the shutdown was implemented by other means, such as filtering.</p> <p>Cloudflare Radar social media posts (<a href="https://x.com/search?q=iran%20(from%3Acloudflareradar)%20until%3A2026-02-05%20since%3A2026-01-07&amp;src=recent_search_click&amp;f=live"><u>X</u></a>, <a href="https://bsky.app/search?q=iran+from%3Aradar.cloudflare.com+since%3A2026-01-07+until%3A2026-02-05"><u>Bluesky</u></a>, <a href="https://mastodon.social/deck/search?q=iran+from%3A%40cloudflareradar%40noc.social+after%3A2026-01-07+before%3A2026-02-05&amp;type=statuses"><u>Mastodon</u></a>) throughout January and into early February documented our observations about the state of connectivity in Iran over the course of that month.
</p><p>On February 28, as military strikes on Iran escalated, a second nationwide Internet shutdown began. <a href="https://x.com/CloudflareRadar/status/2027709437981450502"><u>Cloudflare Radar observed</u></a> a sharp drop in traffic from <a href="https://radar.cloudflare.com/ir"><u>Iran</u></a> beginning around 10:30 local time (07:00 UTC). Traffic levels fell to well under 1% of previous levels, with only <a href="https://x.com/CloudflareRadar/status/2028457567840583735"><u>small amounts of Web and DNS traffic</u></a> egressing the country.</p><p>No significant shifts in announced IP address space were observed around the onset of this shutdown. IPv4 space remained fairly consistent, and IPv6 space remained consistently volatile, suggesting that route withdrawals were not the cause of this second shutdown.</p><p>The continued announcement of IP address space, and the presence of traffic from the country, even if just a small amount, supports reports that the shutdown was effectively achieved through aggressive filtering, with so-called <a href="https://www.iranintl.com/en/202603106004"><u>“whitelists” and “white SIM cards”</u></a> restricting access to only approved Internet sites by selected users.</p><p>Iran remained effectively offline through the end of the quarter. As of late April, this shutdown remains largely in place, making it one of the longest sustained Internet disruptions observed in recent years.</p>
    <div>
      <h3>Republic of Congo</h3>
      <a href="#republic-of-congo">
        
      </a>
    </div>
    <p>On March 15, as the <a href="https://radar.cloudflare.com/cg"><u>Republic of Congo</u></a> held a presidential election <a href="https://www.aljazeera.com/news/2026/3/15/republic-of-congo-votes-in-election-that-could-extend-sassous-42-year-rule"><u>expected to extend President Denis Sassou Nguesso's 42-year rule</u></a>, a <a href="https://bsky.app/profile/radar.cloudflare.com/post/3mh3kcl5zwn2y"><u>near-complete shutdown of Internet connectivity</u></a> was observed in the country. Traffic from the country dropped precipitously around 06:30 local time (05:30 UTC), falling to near zero for approximately 60 hours through the election period and its immediate aftermath. Traffic began recovering around March 17 at 18:20 local time (17:20 UTC), rapidly returning to pre-shutdown levels. While Congolese authorities provided no official explanation for the drop in traffic, <a href="https://www.accessnow.org/campaign/2026-elections-and-internet-shutdowns-watch/#Congo"><u>similar shutdowns were put into place</u></a> during the 2021 and 2016 elections.</p>
    <div>
      <h2>Military action</h2>
      <a href="#military-action">
        
      </a>
    </div>
    
    <div>
      <h3>Ukraine (Dnipropetrovsk)</h3>
      <a href="#ukraine-dnipropetrovsk">
        
      </a>
    </div>
    <p>On January 7-8, <a href="https://kyivindependent.com/dnipro-reportedly-without-electricity-and-water-following-power-plant-explosion/"><u>Russian attacks on energy infrastructure</u></a> in <a href="https://radar.cloudflare.com/ua"><u>Ukraine</u></a> caused power outages that disrupted Internet connectivity in <a href="https://radar.cloudflare.com/traffic/709929"><u>Dnipropetrovsk</u></a> and surrounding regions. <a href="https://x.com/CloudflareRadar/status/2009205930047775078"><u>Cloudflare Radar observed</u></a> a significant drop in traffic from the region, reaching nearly 50% below the prior week’s levels, starting around 22:45 local time (20:45 UTC) on January 7. Recovery began approximately 06:00 local time (04:00 UTC) on January 8.</p>
    <div>
      <h3>Ukraine (Kharkiv)</h3>
      <a href="#ukraine-kharkiv">
        
      </a>
    </div>
    <p>On January 26, Russia launched a drone and missile attack <a href="https://gwaramedia.com/en/russia-attacks-kharkiv-with-25-shahed-drones-injuring-31-including-2-children-photo/"><u>targeting energy infrastructure</u></a> in <a href="https://radar.cloudflare.com/traffic/706482"><u>Kharkiv</u></a>. <a href="https://x.com/CloudflareRadar/status/2015919533408534533"><u>Cloudflare Radar observed</u></a> an approximately 50% drop in traffic from the region beginning around 19:15 local time (17:15 UTC). Recovery progressed through January 27 as power was gradually restored.</p>
    <div>
      <h3>Amazon Web Services Middle East (United Arab Emirates and Bahrain)</h3>
      <a href="#amazon-web-services-middle-east-united-arab-emirates-and-bahrain">
        
      </a>
    </div>
    <p>One of the most unusual disruptions of the quarter was the physical damage inflicted on <a href="https://radar.cloudflare.com/cloud-observatory/amazon"><u>Amazon Web Services</u></a> data centers in the Middle East by drone strikes tied to the ongoing regional conflict. On the morning of March 1 (UTC), Amazon <a href="https://www.reuters.com/world/middle-east/amazons-cloud-unit-reports-fire-after-objects-hit-uae-data-center-2026-03-01/"><u>reported</u></a> a fire started after objects hit a UAE data center. The following day, the company <a href="https://www.cnbc.com/2026/03/02/amazon-says-drone-strikes-damaged-3-facilities-in-uae-and-bahrain.html"><u>confirmed</u></a> that two of its facilities in the United Arab Emirates (<a href="https://radar.cloudflare.com/cloud-observatory/amazon/me-central-1"><u>me-central-1</u></a> region) were "directly struck" by drones and that a facility in Bahrain (<a href="https://radar.cloudflare.com/cloud-observatory/amazon/me-south-1"><u>me-south-1</u></a> region) was also taken offline after being damaged by a nearby strike.</p><p>Cloudflare's <a href="https://radar.cloudflare.com/cloud-observatory/amazon/me-central-1"><u>Cloud Observatory</u></a> data showed elevated connection failure rates for the <a href="https://radar.cloudflare.com/cloud-observatory/amazon/me-central-1?dateStart=2026-02-28&amp;dateEnd=2026-03-06#connection-metrics"><u>me-central-1</u></a> and <a href="https://radar.cloudflare.com/cloud-observatory/amazon/me-south-1?dateStart=2026-02-28&amp;dateEnd=2026-03-06#connection-metrics"><u>me-south-1</u></a> regions beginning March 1-2 and remaining higher for multiple days. Connection failures occur when Cloudflare fails to successfully connect to an origin server when attempting to retrieve uncacheable content, or content not in/expired from cache. These graphs illustrate the increased rate of failures experienced when attempting to connect to servers in these impacted regions.</p><p>In a <a href="https://health.aws.amazon.com/health/status?eventID=arn:aws:health:me-central-1::event/MULTIPLE_SERVICES/AWS_MULTIPLE_SERVICES_OPERATIONAL_ISSUE/AWS_MULTIPLE_SERVICES_OPERATIONAL_ISSUE_5E6B8_EF2498889B5"><u>status post</u></a> on the AWS Health Dashboard, Amazon acknowledged: "These strikes have caused structural damage, disrupted power delivery to our infrastructure, and in some cases required fire suppression activities that resulted in additional water damage." The company warned that instability was likely to continue in the Middle East, making operations "unpredictable," and urged customers with workloads in the affected regions to back up their data or migrate to other AWS regions.</p><p><a href="https://www.aljazeera.com/news/2026/3/24/amazon-says-aws-bahrain-region-disrupted-following-drone-activity"><u>The AWS me-south-1 region in Bahrain suffered an additional disruption</u></a> on March 23, following further drone activity.</p>
    <div>
      <h2>Power outages</h2>
      <a href="#power-outages">
        
      </a>
    </div>
    
    <div>
      <h3>Argentina (Buenos Aires)</h3>
      <a href="#argentina-buenos-aires">
        
      </a>
    </div>
    <p>On January 15, a <a href="https://www.batimes.com.ar/news/argentina/massive-power-cut-in-buenos-aires-city-and-suburbs-hits-800000-users.phtml"><u>power outage struck Buenos Aires</u></a> during a summer heat wave. The outage caused nominal disruptions in Internet connectivity for customers of multiple providers in the <a href="https://radar.cloudflare.com/traffic/3433955"><u>Buenos Aires</u></a> area, including <a href="https://radar.cloudflare.com/as7303"><u>Telecom Argentina (AS7303)</u></a>, <a href="https://radar.cloudflare.com/as27747"><u>Telecentro (AS27747)</u></a>, and <a href="https://radar.cloudflare.com/as16814"><u>IPLAN (AS16814)</u></a>, with traffic from these networks dropping between 17:30 and 19:30 local time (20:30 - 22:30 UTC). Traffic returned to expected levels approximately two hours after the outage began.</p>
    <div>
      <h3>Moldova and Ukraine</h3>
      <a href="#moldova-and-ukraine">
        
      </a>
    </div>
    <p>An emergency power cut on <a href="https://radar.cloudflare.com/ua"><u>Ukraine's</u></a> electricity grid on January 31 caused widespread power outages affecting <a href="https://radar.cloudflare.com/md"><u>Moldova</u></a> and several Ukrainian regions including <a href="https://radar.cloudflare.com/traffic/703447"><u>Kyiv</u></a> and <a href="https://radar.cloudflare.com/traffic/706482"><u>Kharkiv</u></a>. Moldova was <a href="https://www.reuters.com/world/moldova-hit-by-widespread-power-cuts-amid-ukraine-grid-problems-2026-01-31/"><u>reportedly</u></a> hit by widespread power cuts amid the Ukrainian grid problems, and the Ukrainian Energy Minister <a href="https://www.dw.com/en/ukraine-moldova-kyiv-kharkiv-massive-power-outage/a-75738787"><u>explained</u></a> the cross-border impact, noting “Today at 10:42 a.m. (08:42 GMT), a technical malfunction occurred, causing a simultaneous shutdown of the 400 kilovolt line between the power grids of Romania and Moldova and the 750 kilovolt line between western and central Ukraine.” Traffic from Moldova, Kyiv, and Kharkiv began falling around 10:42 local time (08:42 UTC), <a href="https://x.com/CloudflareRadar/status/2017591854762545196"><u>reaching as much as 46% below the prior week</u></a>, with recovery occurring around 14:00 local time (12:00 UTC).</p>
    <div>
      <h3>Paraguay</h3>
      <a href="#paraguay">
        
      </a>
    </div>
    <p>On February 18, widespread power outages struck <a href="https://radar.cloudflare.com/py"><u>Paraguay</u></a> after key transmission lines went out of service. <a href="https://x.com/ANDEOficial/status/2024197363925926251"><u>The National Electricity Administration (ANDE)</u></a> posted a series of updates on X documenting the incident and efforts to restore power. Internet traffic from <a href="https://radar.cloudflare.com/py"><u>Paraguay</u></a> <a href="https://x.com/CloudflareRadar/status/2024221341948198980"><u>dropped as much as 72%</u></a> compared to the prior week beginning around 15:15 local time (18:15 UTC), and the disruption lasted nearly three hours, with recovery occurring by approximately 18:30 local time (21:30 UTC).</p>
    <div>
      <h3>Dominican Republic</h3>
      <a href="#dominican-republic">
        
      </a>
    </div>
    <p>A <a href="https://x.com/ETED_RD/status/2025971028141433113"><u>major failure in the Interconnected National Electric System (SENI)</u></a> of the <a href="https://radar.cloudflare.com/do"><u>Dominican Republic</u></a> caused a widespread power outage on February 23. The state-owned electric company <a href="https://x.com/ETED_RD/status/2025971028141433113"><u>Empresa de Transmisión Eléctrica Dominicana (ETED)</u></a> posted updates on X documenting the failure and the recovery effort. Internet traffic from the country dropped sharply beginning around 10:50 local time (14:50 UTC), and recovered around midnight local time (04:00 UTC) on February 24, in line with a <a href="https://x.com/ETED_RD/status/2026170873145675975"><u>confirmation</u></a> posted by ETED that “The authorities of the electric sector reported that the Interconnected National Electric System (SENI) was fully restored to 100% at 11:53 p.m. on this Monday…”.</p>
    <div>
      <h3>Cuba</h3>
      <a href="#cuba">
        
      </a>
    </div>
    <p><a href="https://radar.cloudflare.com/cu"><u>Cuba</u></a> experienced three separate collapses of its <a href="https://www.ecured.cu/Sistema_El%C3%A9ctrico_Nacional"><u>National Electric System (SEN)</u></a> during March, each causing widespread Internet disruption, reflecting the severe deterioration of the country's electrical infrastructure. (Power outages also disrupted Internet connectivity in Cuba during <a href="https://blog.cloudflare.com/q3-2025-internet-disruption-summary/#cuba"><u>September</u></a> and <a href="https://blog.cloudflare.com/q1-2025-internet-disruption-summary/#cuba"><u>March</u></a> 2025, and <a href="https://blog.cloudflare.com/q4-2024-internet-disruption-summary/#cuba"><u>October</u></a> 2024.) </p><p>The first collapse occurred on March 4, when a disconnection of Cuba's National Electroenergy System cascaded from Camagüey to Pinar del Río, cutting power to the western half of the island, including Havana. <a href="https://x.com/OSDE_UNE/status/2029253573666656431"><u>OSDE/UNE (Cuba's Electric Union)</u></a> confirmed the failure on social media. Cloudflare Radar data showed <a href="https://x.com/CloudflareRadar/status/2029279905700028768?s=20"><u>traffic from the island dropping by nearly half</u></a> beginning around 12:15 local time (17:15 UTC), with <a href="https://bsky.app/profile/radar.cloudflare.com/post/3mgazlklonk2p"><u>traffic recovering</u></a> by approximately 05:01 local time (10:01 UTC) on March 5.</p><p>The <a href="https://www.reuters.com/business/energy/cubas-national-electric-grid-collapses-says-grid-operator-2026-03-16/"><u>second collapse</u></a> occurred on March 16, when Cuba's entire National Electric Power System was disconnected. <a href="https://x.com/EnergiaMinasCub/status/2033602468827779169"><u>EnergíaMinas Cuba</u></a> posted updates on the situation on X. Cloudflare Radar data again shows a significant loss of traffic from Cuba beginning around 13:35 local time (17:35 UTC) on March 16, <a href="https://x.com/CloudflareRadar/status/2033606366393200845?s=20"><u>dropping approximately 65%</u></a>. Traffic returned to expected levels by approximately 20:00 local time on March 17 (00:00 UTC on March 18), with the disruption lasting over 30 hours.</p><p>The <a href="https://www.reuters.com/business/energy/cuba-begins-recovery-efforts-after-second-grid-collapse-week-2026-03-22/"><u>third collapse</u></a> (the second in just a week) happened just days later, on March 21-22. <a href="https://x.com/EnergiaMinasCub/status/2035487928378413423"><u>EnergíaMinas Cuba</u></a> and <a href="https://x.com/OSDE_UNE/status/2035520912297013393"><u>OSDE/UNE</u></a> again provided situation updates via X. Cloudflare Radar data shows another <a href="https://x.com/CloudflareRadar/status/2035818794644377926"><u>significant loss of traffic from Cuba</u></a> beginning around 18:30 local time (22:30 UTC) on March 21, falling as much as 77% compared to the previous week. Traffic recovered around 21:39 local time on March 22 (01:39 UTC on March 23).</p>
    <div>
      <h3>U.S. Virgin Islands</h3>
      <a href="#u-s-virgin-islands">
        
      </a>
    </div>
    <p>According to a <a href="https://www.facebook.com/USVIWAPA/posts/pfbid02eMvKKSQxc9VUjQCCKAEVd56rhn2oCxej8eetUX965QHrozHS854iXK6MnzQkPuMgl"><u>Facebook post</u></a> from the Virgin Islands Water and Power Authority (WAPA) on March 24, a loss of generation at the Richmond Power Plant combined with damage to an underground cable caused a power outage affecting <a href="https://radar.cloudflare.com/traffic/7267902"><u>St. Croix</u></a> and <a href="https://radar.cloudflare.com/traffic/7267904"><u>St. Thomas</u></a> in the <a href="https://radar.cloudflare.com/vi"><u>U.S. Virgin Islands</u></a>. Cloudflare Radar data shows traffic from local provider <a href="https://radar.cloudflare.com/as14434"><u>VI Powernet (AS14434)</u></a>, the primary ISP for the U.S. Virgin Islands, dropping to near zero beginning around 12:15 local time (16:15 UTC), with recovery occurring by approximately 14:45 local time (18:45 UTC). Although VI Powernet experienced a near-complete outage, traffic from St. Thomas only fell by around 60%, and approximately 40% from St. Croix due to the presence of other providers.</p>
    <div>
      <h2>Severe weather</h2>
      <a href="#severe-weather">
        
      </a>
    </div>
    
    <div>
      <h3>Portugal</h3>
      <a href="#portugal">
        
      </a>
    </div>
    <p>Storm Kristin made landfall in Portugal on January 28, causing widespread damage and power outages across the country. Approximately 1,500 <a href="https://www.theportugalnews.com/news/2026-01-28/storm-kristin-causes-1500-incidents-in-portugal/951235"><u>incidents were registered</u></a> by Civil Protection between midnight and 08:00 local time (00:00 - 08:00 UTC), with the hardest-hit areas being the districts of Leiria and Coimbra. Significant infrastructure damage was reported, and by 07:00 local time (07:00 UTC), over 850,000 E-Redes customers were without electricity.</p><p>The associated power outages disrupted Internet connectivity across Portugal, which <a href="https://x.com/CloudflareRadar/status/2016455596552130895"><u>Cloudflare Radar observed</u></a> primarily in the regions of <a href="https://radar.cloudflare.com/traffic/2267094"><u>Leiria</u></a>, <a href="https://radar.cloudflare.com/traffic/2263478"><u>Santarém</u></a>, and <a href="https://radar.cloudflare.com/traffic/2740636"><u>Coimbra</u></a> beginning around 04:10 local time (04:10 UTC) on January 28. Internet traffic dropped as much as 70% in Leiria, and 52% in Coimbra.</p><p>Recovery was slow: <a href="https://sicnoticias.pt/pais/2026-01-30-mais-de-290-mil-clientes-da-e-redes-continuam-sem-energia-a83ff827"><u>over 290,000 customers</u></a> remained without power as late as January 30, and Cloudflare continued tracking <a href="https://x.com/CloudflareRadar/status/2020903675657347237?s=20"><u>gradual recovery of regional traffic</u></a> over the following weeks. (Coimbra returned to expected levels within the first several days after the storm.) More than three weeks after the storm, over 6,000 customers in Leiria <a href="https://cnnportugal.iol.pt/chas/silvino-santos/leiria-ha-mais-de-tres-semanas-sem-luz-silvino-sente-a-solidao-a-apertar/20260220/69983bd1d34e6a48f446c42b"><u>reportedly</u></a> remained without electricity.</p>
    <div>
      <h2>Cable damage</h2>
      <a href="#cable-damage">
        
      </a>
    </div>
    
    <div>
      <h3>Republic of Congo</h3>
      <a href="#republic-of-congo">
        
      </a>
    </div>
    <p>Just after the New Year, Internet connectivity in the <a href="https://radar.cloudflare.com/CG"><u>Republic of Congo</u></a> was disrupted by an incident on the <a href="https://www.submarinecablemap.com/submarine-cable/west-africa-cable-system-wacs"><u>WACS (West Africa Cable System)</u></a> submarine cable. <a href="https://radar.cloudflare.com/as37451"><u>Congo Telecom (AS37451)</u></a> <a href="https://x.com/CongoOfficiel/status/2007015235308372035"><u>posted on X</u></a> announcing "an international incident on the WACS cable" was causing Internet disruptions, and stating that backup solutions had been activated. <a href="https://x.com/CloudflareRadar/status/2007121965954535842"><u>Cloudflare Radar observed</u></a> a significant drop in traffic from <a href="https://radar.cloudflare.com/cg"><u>Congo</u></a> beginning around 00:00 local time on January 2 (23:00 UTC on January 1), falling to 82% below expected levels. A <a href="https://x.com/CongoOfficiel/status/2007481102672232641"><u>follow-up post from Congo Telecom</u></a> confirmed that repairs were ongoing, with users potentially experiencing slowdowns during peak hours. Traffic returned to expected levels by approximately 15:00 local time (14:00 UTC) on January 4.</p>
    <div>
      <h2>Technical problems</h2>
      <a href="#technical-problems">
        
      </a>
    </div>
    
    <div>
      <h3>Verizon Wireless (United States)</h3>
      <a href="#verizon-wireless-united-states">
        
      </a>
    </div>
    <p>On January 14, a <a href="https://www.datacenterdynamics.com/en/news/verizon-outage-last-week-down-to-software-issue/"><u>software issue</u></a> impacted voice and data services for customers of <a href="https://radar.cloudflare.com/as6167"><u>Verizon Wireless (AS6167)</u></a> across the <a href="https://radar.cloudflare.com/us"><u>United States</u></a>. Verizon <a href="https://www.verizon.com/about/news/update-network-outage"><u>published an official statement</u></a> acknowledging that the outage began January 14 and that by 22:15 ET (03:15 UTC on January 15) the issue had been resolved. <a href="https://x.com/VerizonNews/status/2011517297572380929"><u>Multiple updates on X from @VerizonNews</u></a> kept subscribers informed throughout the evening. Cloudflare Radar data shows a minor drop in traffic beginning around 12:30 ET (17:30 UTC) on January 14, consistent with the reported onset of the outage.</p>
    <div>
      <h3>Grenada</h3>
      <a href="#grenada">
        
      </a>
    </div>
    <p>On February 9-10, customers of <a href="https://radar.cloudflare.com/as46650"><u>Flow Grenada (AS46650)</u></a> – the primary Internet provider serving <a href="https://radar.cloudflare.com/gd"><u>Grenada</u></a> – experienced an island-wide service disruption lasting approximately 12 hours. The provider <a href="https://www.facebook.com/HelloFlowGrenada/posts/pfbid02Qt4Wtc5sEWwiCSyLnCk2Hv54vy31BRwFavApbboF3eYg3iRsuU4xRuFJdGNRwcsol"><u>posted on Facebook</u></a> acknowledging a service disruption, though no details about the root cause were provided. Cloudflare Radar data shows traffic from the network initially dropping around 11:30 local time (15:30) UTC on February 9, disappearing completely around 20:00 local time (midnight UTC on February 10), and recovering by approximately 23:30 local time (03:30 UTC on February 10). Routing data shows a complete loss of announced IPv4 space at the same time traffic dropped to zero. <a href="https://radar.cloudflare.com/routing/as46650?dateStart=2026-02-09&amp;dateEnd=2026-02-10#bgp-announcements"><u>Major spikes in BGP announcements</u></a> around the time the disruption initially started, and bookending the complete outage, suggest that the whole event may have been routing-related.</p>
    <div>
      <h2>Unknown cause</h2>
      <a href="#unknown-cause">
        
      </a>
    </div>
    
    <div>
      <h3>Orange Guinée (Guinea)</h3>
      <a href="#orange-guinee-guinea">
        
      </a>
    </div>
    <p>Customers of <a href="https://radar.cloudflare.com/as37461"><u>Orange Guinée (AS37461)</u></a> in <a href="https://radar.cloudflare.com/gn"><u>Guinea</u></a> were <a href="https://www.guinee360.com/06/01/2026/appels-impossibles-en-guinee-les-citoyens-face-au-mutisme-des-operateurs-et-des-autorites/"><u>unable to make phone calls or access the Internet</u></a> starting around 10:45 local time (10:45 UTC) on January 6. Orange Guinée <a href="https://www.africaguinee.com/coupure-de-linternet-et-des-appels-orange-guinee-evoque-une-panne-exceptionnelle/"><u>subsequently confirmed</u></a> an "exceptional breakdown" affecting mobile phone and Internet services due to a technical incident, with teams mobilized to restore service. Service was restored by approximately 14:00 local time (14:00 UTC) that same day. No further details on the root cause of the incident were publicly disclosed.</p>
    <div>
      <h3>TalkTalk (United Kingdom)</h3>
      <a href="#talktalk-united-kingdom">
        
      </a>
    </div>
    <p>On March 25, customers of UK broadband provider <a href="https://radar.cloudflare.com/as13285"><u>TalkTalk (AS13285)</u></a> <a href="https://www.ispreview.co.uk/index.php/2026/03/customers-of-uk-broadband-isp-talktalk-report-major-service-outage.html"><u>reported</u></a> widespread service disruptions. <a href="https://x.com/TalkTalk/status/2036740766576377995"><u>TalkTalk acknowledged the issues on X</u></a> but did not publicly disclose a root cause. <a href="https://x.com/CloudflareRadar/status/2036774076413362592"><u>Cloudflare Radar observed</u></a> traffic from the provider drop nearly 50% as compared to the previous week beginning around 07:00 local time (07:00 UTC), with service restored by approximately 08:15 local time (08:15 UTC).</p>
    <div>
      <h2>A quarter marked by major disruptions</h2>
      <a href="#a-quarter-marked-by-major-disruptions">
        
      </a>
    </div>
    <p>The first quarter of 2026 was marked by an unusually high number of severe and prolonged Internet disruptions. The major government-directed shutdowns, particularly the extended blackouts in Uganda and Iran, underscore how Internet access continues to be weaponized as a tool of political control. Cuba's three separate national grid collapses in a single month paint a troubling picture of infrastructure fragility with direct consequences for connectivity. And the drone strikes on AWS data centers in the Middle East represent an unprecedented escalation as active military conflict directly and physically damaged major cloud infrastructure, with disastrous consequences for the websites and applications hosted there.</p><p>The Cloudflare Radar team is constantly monitoring for Internet disruptions, sharing our observations on the <a href="https://radar.cloudflare.com/outage-center"><u>Cloudflare Radar Outage Center</u></a>, via social media, and in posts on <a href="https://blog.cloudflare.com/tag/cloudflare-radar/"><u>blog.cloudflare.com</u></a>. Follow us on social media at <a href="https://twitter.com/CloudflareRadar"><u>@CloudflareRadar</u></a>(X), <a href="https://noc.social/@cloudflareradar"><u>noc.social/@cloudflareradar</u></a> (Mastodon), and <a href="https://bsky.app/profile/radar.cloudflare.com"><u>radar.cloudflare.com</u></a> (Bluesky), or contact us via <a href="#"><u>email</u></a>.</p>
