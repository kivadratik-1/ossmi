# OSSMI — Open Source Small Mount Interface

**An open mechanical interface for mounting and arranging small devices, modules, components, and everyday objects.**  
**Small devices. One open interface.**  
**The interface is open. The ecosystem is a market.**

| Document | Value |
|---|---|
| Identifier | `OSSMI-STD-0001` |
| Version | **0.1.3 — Public Draft (expanded applications)** |
| Date | 2026-11-05 |
| Status | Proposal / prototype-backed; **not yet a ratified standard; reference hardware licensing policy adopted** |
| Project | Open Source Small Mount Interface (OSSMI) |
| Scope | Passive mechanical connection, mounting and arrangement of small devices, components and everyday objects |
| First reference application | Rugged modular tablet frame (Lenovo Y700) |
| Repository | <https://github.com/kivadratik-1/ossmi> |
| Governance / licensing | **CERN-OHL-W-2.0 adopted for OSSMI reference hardware sources**, subject to explicit file notices; see §12 |

> **We standardized how small devices exchange data. We never standardized how they stay together.**

---

# Part I — The OSSMI Manifesto

## 1. The missing interface

Modern electronics have learned to talk to one another. USB carries data. USB-C provides a common physical connection for many devices. Wireless protocols make communication less dependent on cables. Yet the mechanical relationship between small devices remains an improvised problem.

An SSD is attached to a tablet with tape. A card reader hangs from its cable. A modem rides in a pocket. A sensor needs a new enclosure, a new bracket, and a new screw pattern. A TV streaming box or external power brick dangles behind a display. A portable solar panel and power bank need an improvised way to stay together. A small sensor or telemetry unit needs yet another custom mount on a DIY drone or robot. The same everyday problem is re-solved, by thousands of people, thousands of times.

We have made electronic devices modular in **information**, but not sufficiently modular in **space**.

OSSMI exists to close that gap.

We propose a minimal, documented mechanical interface for mounting, connecting and arranging small devices, components and everyday objects. Electronics are the starting point, **not the boundary of the idea**. Makers should be able to print it, designers to integrate it, companies to adopt it, and ordinary users to adapt it without joining a closed accessory ecosystem.

We do not need a new proprietary connector for every small device. We need a common foundation on which many different products can coexist.

## 2. The proposition

**OSSMI — Open Source Small Mount Interface** is a proposal for a small-scale, open, passive mechanical interface. It defines the **mating relationship between parts**, not the overall geometry, electronics, purpose, or load rating of products connected through it.

Its first implementation combines:

- An **8.0 mm nominal orthogonal grid** derived from widely available LEGO System-compatible stud geometry.
- A **receiving/underside interface on the host** (the tablet frame, electronics enclosure, mounting plate, or other carrier).
- A **studded interface on the detachable accessory**, achievable with an ordinary compatible plate or a custom printed part.
- **Tool-free engagement** for modules whose weight, geometry, and conditions permit friction-based retention.
- **Optional M3 threaded anchoring** at selected host positions for accessories that need additional security, using a compatible purpose-designed adapter.

**Host = receiving sockets. Accessory = studs.** This orientation is intentional and defines the v0.1 reference architecture. Reversing it changes the user experience and must not be represented as the OSSMI v0.1 default.

The system is meant to be useful at its simplest. A maker should be able to attach a low-profile studded plate to an existing card reader and use the same mounting surface as someone who designs a complete parametric enclosure.

OSSMI does not require the user to purchase a unique vendor-specific latch. It should work both for **device-to-accessory** arrangements and, through suitable adapters or brackets, for **device-to-device** and **device-to-surface** mounting. A custom bracket can have whatever length or shape a maker needs; only its OSSMI mating features need follow the interface.

## 3. What we believe

### 3.1 An interface should outlive a product

A mount must not become useless because its manufacturer stops selling a phone case, changes a generation, or discontinues a proprietary adapter. A published interface gives users and independent makers the ability to maintain compatibility.

### 3.2 Compatibility is infrastructure, not captivity

A common mounting interface is valuable precisely because nobody needs to control every accessory made for it. Producers compete through quality, design, service, durability, and applications—not by preventing devices from attaching to one another.

### 3.3 Ordinary people should be able to participate

An OSSMI implementation should be approachable using consumer 3D printers, readily available mounting plates, standard fasteners, and common workshop tools. Advanced CNC, molding, and engineering materials may improve results, but must not be prerequisites for participation.

### 3.4 Mechanical simplicity matters

Fewer special parts means fewer points of failure. For many small devices, a well-designed friction interface is sufficient. Where friction alone is inappropriate, the same mounting architecture should offer deliberate mechanical fastening.

### 3.5 Open source means modifiable source, not only downloadable meshes

An STL is useful for printing. A parametric model is useful for learning, adapting, repairing, and evolving the interface. OSSMI encourages editable CAD, dimensional drawings, tolerance documentation, and transparent design decisions.

### 3.6 The standard must be bigger than its first product

The original tablet frame is a proof of concept, not the definition of OSSMI. The same interface should be adaptable to Raspberry Pi enclosures, microcontroller cases, phone cases, compact tablet covers, laptop mounting pads, TV accessory mounts, desktop equipment, robotics, UAV research modules, portable solar equipment and peripherals not yet imagined. A mounting surface can be part of a device, an enclosure, an adhesive plate, a bracket or a standalone carrier.

### 3.7 Claims must follow measurements

A securely fitting prototype is evidence of feasibility, **not** evidence of universal impact resistance, safety-rated retention, verified cycling durability, or compatibility with every printer and material. OSSMI should publish methods, results, and limits rather than unearned ratings.

### 3.8 Interoperability must remain voluntary and fair

No maker or manufacturer should need permission from a single vendor merely to build a dimensionally interoperable design, subject to applicable law and the **licenses actually published for the relevant OSSMI materials**. Describing a product as compatible must be truthful; permission to use the OSSMI name or logo for branding may be governed by separate, fair trademark rules. No contributor should be required to assign ownership of unrelated inventions merely to participate.

### 3.9 Open hardware can support profitable businesses

An open interface does not mean that every product must be free of charge, manufactured by volunteers, or sold without a margin. Makers may share designs; factories may invest in tooling and manufacturing; accessory brands may build distinctive products; distributors may provide logistics, stock, local support, and customer service. They should be able to profit from solving real problems **without owning the shared interface**.

### 3.10 Adoption matters more than centralized control

OSSMI succeeds when independently manufactured parts work together and buyers can choose between alternatives. A single factory producing ten thousand identical items would be useful evidence of manufacturing readiness—but **interoperability across independent producers** is the stronger proof of an ecosystem.

## 4. The ambition

We imagine a world where a small battery, SSD, sensor, radio, card reader, camera accessory, or controller can be attached to a compatible surface as naturally as a cable can be plugged into a port.

The person building a weather station should be able to reuse mounting ideas from the person building a photo rig. A photographer should be able to borrow an adapter from a robotics project. An accessory designed for one host should be usable on another, where dimensions and load capacity allow.

That is how open interfaces become ecosystems: not because a company declares a standard, but because **independent people build compatible things without coordinating with one another**.

OSSMI begins with a familiar plastic construction geometry, a simple screw thread, and one working tablet prototype. Its value will be proven only when others design, print, test, and improve independent implementations.

> **A connector should not be a business model. An interface should be a shared foundation.**

> **Build the device you need. Attach it to the world you already have.**

## 4A. Commercial adoption and ecosystem charter (non-normative proposal)

**The interface is open. The ecosystem is a market.**

OSSMI is intended to enable a market of interoperable products, not to turn a published mounting geometry into a proprietary tollbooth. Its contributors should make it practical for independent manufacturers, brands, and distributors to participate while preserving the ability of users to reproduce, repair, and adapt compatible equipment.

### 4A.1 Participants and their value

| Participant | What they contribute | How they may benefit |
|---|---|---|
| Individual makers | Tested adapters, printable models, measurements, tutorials | Recognition, improved tools, optional sales and services |
| Manufacturers and factories | Repeatable processes, tooling, quality assurance, materials | Revenue from manufactured parts and assembly services |
| Device and accessory brands | OSSMI-compatible cases, mounts, SSD holders, reader adapters | Product differentiation and cross-product compatibility |
| Distributors and retailers | Availability, local inventory, fulfillment, returns | Margins on hardware, kits and accessories |
| Integrators and designers | Custom mechanical integration for specific devices | Paid engineering, customization and support |
| End users | Real-world use cases, feedback and independent validation | Less lock-in, replaceable parts, broader choice |

### 4A.2 Principles for manufacturer participation

1. **No exclusive control of the base interface.** A launch partner funding molds, stock, marketing, or distribution does not thereby acquire exclusive rights to the published OSSMI interface or the right to block dimensionally compatible alternatives. Any rights in a specific partner-designed product, tooling, logo, or independently developed improvement must be addressed separately.
2. **Commercial manufacturing is welcome.** The intended licensing approach should permit lawful production, sales and modification of released reference designs without per-unit royalty payments to the project for using those designs. **For covered reference hardware, those permissions follow from CERN-OHL-W-2.0 and its notices; for future assets, permissions depend on their actual published licenses**; the actual license files and third-party rights determine permissions.
3. **Quality claims need evidence.** A supplier should publish which OSSMI revision, reference gauge or coupon, materials, and tests its products support. No company may claim OSSMI certification until a certification process exists.
4. **Interoperability is not branding permission.** Compatibility statements, factual attribution, and use of an OSSMI logo or official partner mark are separate matters. Future trademark rules should be objective, non-discriminatory and not used to suppress independent technical compatibility.
5. **The standard should stay usable without any one supplier.** Users should retain access to the normative published geometry, reference files and testing methods needed for independent implementation, subject to the published licenses and law.

### 4A.3 Launch partnerships without platform capture

Early market formation may require coordination among a reference-design maintainer, a manufacturing partner, a distribution channel and real users. A practical pilot could include an adhesive laptop/SSD mounting kit or a field-photography tablet/card-reader kit, subject to safety, fit, adhesive and retention validation.

A partner may negotiate priority manufacturing access, a time-limited sales arrangement for **its own specific SKU**, preorders, co-marketing, or a regional distribution agreement. Such agreements should **not** create exclusivity over the underlying OSSMI interface, prevent other parties from making compatible equipment, or suppress publication of interface information needed for interoperability. Commercial contract terms are outside the normative v0.1 specification and require independent legal review.

Do not manufacture a speculative large batch on the strength of the manifesto alone. A prudent industrial pilot should connect prototype evidence, estimated landed cost, expected selling price, test requirements, channel interest, and staged minimum order quantities before committing to expensive tooling.

### 4A.4 Independence and stewardship

The initial repository may be personally maintained. Public contribution processes should allow independent implementers to propose changes; manufacturers should have a voice without purchasing control of the technical definition. A future organization or foundation is an **option**, not a prerequisite for first release. Material compatibility changes should require published rationale, tests and versioning rather than private agreement with a favored supplier.

### 4A.5 Measures of ecosystem progress

Project success is not measured by revenue, impressions or GitHub stars alone. More meaningful signals include: an independent compatible host, an independently designed accessory, verified cross-vendor mating, public reproduction of a reference coupon, documented field durability, and at least one third-party supplier willing to invest its own resources. Sales and distribution strengthen that network but are not substitutes for interoperability.

### 4A.6 What OSSMI does not promise

This charter does not promise a market, buyers, investment returns, certification, guaranteed engineering performance, or patent/trademark freedom to operate. Licensing rights are provided through the actual CERN-OHL-W-2.0 notice on covered hardware sources, not by an invitation alone. Practical production claims still require actual CAD, tests and, where necessary, professional advice.

---

## 4B. One connection, many arrangements (non-normative vision)

The smallest useful OSSMI part may be an adhesive-backed receiving patch, a printable studded plate or an adapter between two otherwise unrelated objects. The standard does not need to prescribe the bracket between those ends.

### 4B.1 Connection patterns

| Pattern | Example | What OSSMI standardizes |
|---|---|---|
| **Device → accessory** | Tablet → removable card reader or SSD | The mating geometry, not the peripheral |
| **Device → device** | Portable solar panel → power bank through an adapter | The interfaces on the joining adapter or carrier, not the charging circuit |
| **Device → surface** | TV → streaming box, external power supply or cable organizer | The interface between the mounted object and the mounting patch or bracket |
| **Device → bracket → device** | Tablet → arm → controller; robot → bracket → sensor | Repeatable OSSMI ends; bracket shape, length and stiffness remain application-specific |
| **Device → enclosure / carrier** | DIY drone frame → removable sensor enclosure; 3D printer → camera mount | The docking interface, not the host machine's performance or safety certification |

**The interface connects. The surrounding product decides what the assembly can safely do.**

### 4B.2 Illustrative application families

- **Home and desk:** streaming boxes and small external power supplies behind TVs or monitors; USB hubs, cables and compact electronics under desks. Keep ventilation, service access, electrical insulation and cable strain relief unobstructed.
- **Mobile and photographic rigs:** phones, tablets, SSDs, readers, modems, controllers and power banks, with printable or ready-made attachment patches. Magnetic-system adapters may bridge other ecosystems rather than replace them.
- **Off-grid and portable solar:** lightweight portable or folding solar panels, compatible power banks, charge controllers and cable holders. The mechanical link does not imply electrical compatibility; charging regulation, battery temperatures, panel flex and sunlight exposure require independent design.
- **Robotics and UAV prototyping:** modular sensors, GPS and telemetry housings, cameras, small payload enclosures and ground-test fixtures. OSSMI-Q may suit bench configuration and noncritical modules; airborne use needs separately engineered and validated retention, typically with a positive mechanical fastener or secondary restraint.
- **Maker tools and 3D printers:** camera arms, lights, switches, tool holders, filament accessories and auxiliary sensors mounted to custom brackets. Never obstruct moving axes, cooling or emergency controls.

These are **potential applications**, not claims that such products have been built, tested, certified or commercialized by the OSSMI project.

### 4B.3 Quick and secured modes are choices, not promises

OSSMI-Q prioritizes tool-free repositioning. OSSMI-S adds optional M3 fastening for an application that needs more deliberate retention. A captive or spring-loaded M3 screw can ease assembly and prevent screw loss, but **being spring-loaded does not itself guarantee resistance to loosening under vibration**. Joint preload, fastener locking, host material, insert strength, fatigue and actual test conditions matter. Neither mode carries a universal shock, flight, crash or load rating.

OSSMI does not set the design objective of retaining every accessory during a drop or collision. Controlled disengagement may be acceptable or useful in some configurations; ordinary handling performance and safety of a specific product remain the responsibility of its designer. Aircraft-borne and moving-machine assemblies require additional, use-specific validation and must not rely on the draft interface alone.

# Part II — Proposed OSSMI v0.1 Interface Specification

## 5. Status, terminology, and scope

This document contains both a manifesto (non-normative) and a **draft technical specification**. It is not an ISO, IEC, DIN, or other formally ratified standard. References to *compatible* in this document describe design intent, not third-party certification.

The capitalized terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** express intended requirements within this **draft**. They are not evidence of external certification.

**Terminology**

- **Host:** the underlying device, frame, enclosure, or mounting surface carrying the receiver.
- **Receiver:** socket-side LEGO-compatible contact geometry, including the necessary walls, tubes, and other clutch surfaces.
- **Accessory:** the removable payload, including card readers, SSDs, modems, power packs, sensors, etc.
- **Studded adapter:** the accessory-side interface with outward studs.
- **Clutch:** retention produced by the engagement and elastic deformation of mating features.
- **M3 anchor:** an optional threaded attachment point integrated in the receiver region.
- **Secured adapter:** an accessory adapter designed to use both OSSMI clutch alignment and an M3 fastener.
- **Reference implementation:** an example design illustrating the specification; it is not the only valid implementation.
- **Mounting bridge / bracket:** a freely shaped mechanical part that connects two or more OSSMI mating interfaces or adapts a device to a host surface.
- **Host role:** the receiver-bearing side of a particular connection; one physical device may act as a host in one connection and an accessory in another through separate adapters.

**In scope for v0.1:** passive placement, alignment, mechanical attachment, detachable modules, optional threaded retention, adapters linking devices and surfaces, geometry documentation, reproducible test methods.

**Out of scope for v0.1:** electrical or data contacts; wireless communications; cable specifications; solar charge-control and battery safety; watertightness; structural or life-safety attachment; attachment to a human body for protection; fall arrest; motorcycle/high-speed mounting; rated vibration/impact performance; medical or aircraft use. UAV examples are research and prototyping concepts only, not a flight-use qualification.

## 6. Interface architecture

### 6.1 Two complementary retention modes

| Designation | Engagement | Intended purpose | Tool |
|---|---|---|---|
| **OSSMI-Q** (quick) | Studded adapter ↔ receiver clutch | Frequent repositioning of suitable lightweight accessories | None |
| **OSSMI-S** (secured) | OSSMI-Q geometry **plus** one or more M3 fasteners | Optional higher-retention / more permanent installation, if tested for the use case | Appropriate screwdriver |

These designations are **proposed names**, not certified load classes. **OSSMI-S does not automatically imply a particular force or shock rating.**

### 6.2 Orientation

In the v0.1 reference convention:

1. The host carries **female/underside LEGO-compatible receiving geometry**.
2. The removable accessory carries **male/studded LEGO-compatible geometry**.
3. Selected host cells MAY contain threaded M3 anchor points.
4. A standard studded adapter MUST NOT be assumed to accept a securing screw without an appropriate hole and load-bearing structure.

The presence of holes alone does not create a functioning receiver. Retention depends on the correct relationship of studs, contact walls/tubes, polymer response, and assembly depth.

### 6.3 Grid and coordinate system

The nominal XY pitch between adjacent stud centers is **8.00 mm**. Host and adapter designers SHOULD use a consistent orthogonal grid and document the origin, cell coordinates, grid orientation, and active cells. The absolute outline of a host is unconstrained.

A local coordinate convention is proposed: X and Y follow grid axes; +Z points outward from the host receiver surface toward the accessory. Mating dimensions should be documented in this frame.

### 6.4 Core nominal dimensions

The following values describe **commonly reported LEGO System-style proportions**. They are **starting geometry**, not an official LEGO manufacturing drawing, and MUST NOT be interpreted as a fully tolerance-specified standard:

| Feature | Initial nominal reference | Caution |
|---|---:|---|
| Grid pitch, X/Y | **8.00 mm** | Primary reference dimension |
| Accessory stud outer diameter | **≈4.80 mm** | Shape, rounding and fit matter |
| Accessory stud height | **≈1.80 mm** | Measured from its supporting face |
| Standard plate body height | **≈3.20 mm** | Excludes protruding stud, by this convention |
| Brick-style underside tube outer diameter | **≈6.50 mm** | May not apply identically to every plate or cell design |
| M3 fastener thread | **M3 × 0.5** | Metal insert dimensions depend on supplier |

**Important correction:** Ø6.5 mm refers to the **outer diameter of a representative underside clutch tube**, not to the diameter of a stud. The nominal stud is approximately Ø4.8 mm.

Geometry and interfaces vary among full bricks, thin plates, tiles and specialist parts. Therefore v0.1 does **not** claim a definitive tube inner diameter, wall thickness, interference fit, clearance, or tolerance for every mating situation. Those remain subjects for reference CAD, calibrated drawings, and empirical fit testing.

A typical external footprint of an N-stud-wide legacy-style rectangular part can be approximated by `8 × N − 0.2 mm`, but this is illustrative only and does not define the receiving clutch geometry.

### 6.5 Receiver design rules

A receiver implementation SHOULD:

- Reproduce **functional** underside contact features, not merely a pattern of empty drilled holes.
- Support unobstructed placement and removal of ordinary compatible studded plates in the declared active zone.
- Provide enough body material to resist splitting under the intended load and insertion force.
- Avoid sharp edges that can abrade cables, hands, or adapters.
- Leave enough finger access for intentional removal, including edge-peel where appropriate.
- Avoid interference with device cooling, cameras, buttons, radio antennas, ports, or screens.
- Document local geometry differences caused by mounting screws, reinforcing ribs, or embedded inserts.

### 6.6 Accessory-side design rules

An accessory adapter SHOULD:

- Present compatible stud geometry on the **surface facing the host**.
- Use multiple contact points for larger or eccentric loads rather than relying on a single stud.
- Have a sufficiently rigid load path between the accessory and studded plate.
- Disclose the attachment method between the adapter and accessory (adhesive, screws, integrated enclosure, etc.).
- Route cables so cable snags do not act as a lever detaching the payload or damaging the host port.

Pre-existing construction-brick plates can serve as accessories, but material, geometry, and manufacturing variations SHOULD be tested rather than assumed interchangeable at every load.

### 6.7 Adapters, bridges and multiple host roles

A bracket MAY include multiple OSSMI mating zones for arranging separate objects. In each individual joint, the **receiver side remains the host** and the **stud side remains the detachable accessory or adapter** under v0.1. Combining two receiver-equipped devices requires a separately designed bridge with suitable studs at its mating ends; it does not reverse the reference convention.

The OSSMI specification does not prescribe bridge shape, extension length, cable routing, overall enclosure, operating temperature or allowable loads. Those are product-level engineering decisions. A shared 8 mm pitch alone does not demonstrate that independently produced profiles fit; actual clutch geometry and documented tolerances still matter.

## 7. Optional M3 anchoring

OSSMI-S adds a selective fastener without requiring every adapter to use screws.

### 7.1 Intent

The M3 system is an **optional mechanical security feature**, not a replacement for the base OSSMI-Q interface. A host can support the quick mode everywhere and offer secured positions in selected cells.

### 7.2 Host-side guidance

- Selected receiving cells MAY contain **brass heat-set M3 threaded inserts** or other reliable M3 threads.
- The insert SHOULD be recessed below relevant mating faces so an ordinary studded adapter can still attach.
- The heat-set pocket diameter, bore depth, interference, minimum wall, and installation temperature MUST be specified **per actual insert part number** and host material.
- Local reinforcement SHOULD preserve both the insertion strength of the M3 feature and the OSSMI clutch function.
- Installers MUST ensure the screw cannot reach or damage the electronics behind the host panel.
- Two spaced anchors SHOULD be considered where significant rotational moments are expected, subject to measured strength.

### 7.3 Accessory-side guidance

- Secured adapters MUST provide proper screw clearance or captive-fastener features; standard LEGO pieces should not be drilled or stressed blindly.
- Screw length MUST account for washer, adapter thickness, thread engagement, and remaining available depth.
- A manufacturer SHOULD publish tightening guidance based on its chosen insert and printed material. **No universal torque value is specified in v0.1.**
- Thread-locking compounds and adhesives may attack certain plastics; compatibility must be checked.

### 7.4 Failure considerations

Relevant failures include stripped inserts, plastic creep, cracked receiver tubes, deformation from heat-setting, screw bottoming-out, and excessive loading transferred directly to a fragile host device. Secured mode reduces some accidental release risks but may create other failure modes; it is not inherently safety-rated.

## 8. Fabrication and interoperability

### 8.1 Intended manufacturing methods

OSSMI is manufacturing-process agnostic. Implementations MAY be 3D-printed, machined, molded, or manufactured by other methods, provided the actual interface operates as documented.

### 8.2 FDM guidance

- **PETG** is a practical initial prototyping material; **ABS/ASA** and other engineering polymers MAY be explored for their thermal and UV characteristics.
- Printed clutch dimensions depend on nozzle, extrusion, flow, material, orientation, cooling, and slicer settings.
- A small calibration coupon SHOULD be printed before committing to a full device housing.
- Tolerance variants SHOULD be documented with actual measured dimensions, not a universal guessed fit offset.
- Repeated forceful insertion SHOULD be checked for layer separation and wear.
- Heat-set inserts SHOULD be installed using a controlled process and adequate surrounding plastic.

### 8.3 Adhesive-mounted accessories

A studded plate MAY be attached to a small device using adhesive or suitable mounting tape. This is a critical part of the accessibility of OSSMI: the maker need not redesign the electronic device.

However, compatibility depends on case material, surface finish, coatings, temperature, preparation, and load. Cyanoacrylate (“superglue”) does not work reliably on all polymers, especially certain low-surface-energy plastics. Avoid blocking cooling, batteries, ventilation, labels, buttons, or service access. Adhesive performance MUST be evaluated separately from clutch performance.

### 8.4 Non-endorsement

“LEGO-compatible” in this document is **descriptive**. OSSMI is independent of, and is not endorsed by, affiliated with, or certified by the LEGO Group. Official LEGO trademarks and logos are not part of this standard.

## 9. Reference products and ecosystem

The interface is separate from the products used to demonstrate it.

| Working reference family | Purpose | Status at v0.1 |
|---|---|---|
| **OSSMI Tablet** | Rugged tablet frame with receiving zones | **Physical prototype demonstrated**, Lenovo Y700-based |
| **OSSMI Pi** | Raspberry Pi enclosure with receiver matrix | Concept/CAD prototype; physical fit and connector clearances not validated |
| **OSSMI Arduino** | Modular microcontroller enclosure | Concept only |
| **OSSMI Mobile** | Smartphone enclosure with selected receiver zones | Concept only; device-specific model/fit TBD |
| **OSSMI Mini Tablet** | Compact iPad mini enclosure | Concept only; device-specific model/fit TBD |
| **OSSMI Adhesive Plate** | Add-on receiver zone for e.g. laptop covers | Concept only; laptop finish/load/thermal safety not validated |
| **OSSMI Adapters** | Studded plates, M3-secured brackets, custom device modules | Generic family; implementations to be published |
| **OSSMI Home / Display** | TV or monitor mounting patches for streaming boxes and small external power supplies | Concept only; thermal, electrical and adhesive fit not validated |
| **OSSMI Solar / Field** | Portable solar-panel carrier for a power bank or controller | Concept only; charging, weather, flex and temperature suitability not validated |
| **OSSMI Robotics / UAV** | Sensor, camera and telemetry-module brackets | Concept only; vibration and flight retention not validated |
| **OSSMI Maker / Printer** | Removable mounts for lights, cameras or sensors on maker equipment | Concept only; moving-part and thermal clearances not validated |

Illustrations and AI visualizations SHOULD be labeled **concept render** unless produced from verified engineering CAD. Claims of fit to specific iPhone, iPad, MacBook, Raspberry Pi, or Arduino models MUST be supported by dimensional and physical validation.

### 9.1 First proof: modular tablet frame

The first OSSMI precursor is an FDM-printed perimeter frame with two separated receiver regions on the back of a Lenovo Y700 tablet. A card reader and portable SSD are **reported by the creator** to have been mounted simultaneously using LEGO-compatible plates. The creator reports firm engagement during ordinary handling. A revised test piece is **reported** to incorporate M3 brass inserts within selected receiving features for optional screw retention. These observations are not accompanied by a standardized independent test report in this draft.

This supports **feasibility**, not a verified force specification. No certified weight, impact, cycling, or temperature limit has been established.

### 9.2 Why these examples matter

A proposed open interface gains credibility when different independent host products use the *same mating geometry*. The goal is not five incompatible products wearing the same logo. The goal is one interface demonstrated across at least five device classes.

## 10. Validation and conformance roadmap

### 10.1 Tests required before performance claims

1. **Dimensional metrology:** document as-built pitch, tube and stud dimensions, feature heights, and flatness.
2. **Genuine-part compatibility:** test multiple ordinary construction-brick plates against each printed receiver coupon.
3. **Pull-off force:** measure axial separation force at defined adapter sizes and insertion states.
4. **Peel / moment resistance:** record release from an edge-loaded, offset-mass arrangement.
5. **Insertion/removal cycling:** measure force and wear over repeatable cycles (e.g. 100, 500, 1,000); numbers are proposed test points, not requirements.
6. **Vibration and shocks:** test dummy masses before exposing valuable electronics to risk.
7. **Adhesive retention:** measure bond durability, including edge peel and environmental aging.
8. **M3 insert pull-out / torque:** test by insert supplier, host geometry and material.
9. **Thermal and environmental:** characterize heat, UV exposure where relevant, humidity, and low temperatures.
10. **Electronics integration:** confirm clearance, cooling, antenna performance where applicable, and cable strain relief.

### 10.2 Reporting template

Each public test report SHOULD include: host revision; adapter dimensions and number of engaged studs; material and printer/process; layer orientation; environmental condition; insertion method; number of cycles; applied load geometry; instrument or method; raw measurements; failure mode; and photos/video.

### 10.3 Compatibility vocabulary

Until a reference gauge and tolerances are ratified:

- **“OSSMI-inspired”** MAY describe experimental designs inspired by the approach.
- **“OSSMI v0.1 prototype-compatible”** SHOULD be used only where actual mating to the published reference coupon is documented.
- **“OSSMI-certified”** MUST NOT be used: **no certification process exists**.

### 10.4 Reserved load classes

No numeric mass or load classes are defined in v0.1. Future versions MAY add load classes based on measured failure modes and safety factors. A nominal class should never be extrapolated from the performance of one PETG print.

## 11. Safety, responsibility, and limitations

- **Do not use an untested OSSMI connection for fall arrest, personal safety equipment, automotive crash restraints, moving vehicle mounts, flight-critical or overhead load-bearing installations, or medical devices.**
- For UAVs and robots, an OSSMI-compatible geometry is not evidence of flight or vibration qualification. A product designer must validate positive retention, fastening, vibration, clearance and consequences of release for the intended use.
- For solar panels and power banks, do not cover solar cells, thermal vents or batteries; assess direct-sun heat, flexible-panel bending, cable routing and proper electrical charging separately.
- For televisions and monitors, avoid exhaust vents, hot surfaces, high-voltage sections, wall-mount fasteners and unsafe strain on power cords.
- OSSMI-Q clutch retention may fail under impact, vibration, temperature changes, material fatigue, or cable snags.
- Larger accessories generate torque even at small masses; test the real lever arm.
- Avoid mounting devices in ways that obstruct ventilation or create battery overheating hazards.
- A securing screw can damage internal electronics if too long; it can also crack thin polymer features when overtightened.
- Adhesive bonds on painted or coated devices can fail or cause finish damage; a manufacturer or device owner should decide whether an adhesive installation is acceptable.
- Exposed mounts can collect dirt and debris; surface care and inspection should be considered.
- Compatible geometry is **not** a guarantee of safe retention or suitability for any given purpose.

## 12. Open source, intellectual property, and names

### 12.1 Publication objective

OSSMI intends to publish the interface specification, editable parametric reference CAD, useful exports (STEP/STL), calibration coupons, test protocols, and implementation examples so third parties can independently reproduce them.

### 12.2 Licensing policy — reciprocal open hardware

**OSSMI reference hardware designs are licensed under the CERN Open Hardware Licence Version 2 — Weakly Reciprocal (`CERN-OHL-W-2.0`).** This decision applies to original OSSMI hardware design source files that the copyright holder publishes with an explicit CERN-OHL-W-2.0 notice, including reference CAD and associated manufacturing drawings. The authoritative, unmodified license text **must be added** to the repository root `LICENSE` file before the hardware release. SPDX identifier: `CERN-OHL-W-2.0`. Official license reference: <https://spdx.org/licenses/CERN-OHL-W-2.0.html>.

**Principle: Build commercially. Improve openly. Compete on products, not compatibility lock-in.**

Under CERN-OHL-W-2.0, anyone may make, modify, distribute, and commercially sell products based on covered hardware source, without per-unit licensing royalties to OSSMI, provided they satisfy the license. In particular:

1. **Covered improvements stay open when distributed.** Those who distribute modified covered source must supply the required notices, identify changes, and license the modified covered source under CERN-OHL-W-2.0 (or another version where explicitly allowed by that license).
2. **Shipping hardware carries source obligations.** Those who distribute products based on covered source must give recipients the Complete Source or notify them of its Source Location as specified by section 4.1. This includes applicable covered modifications and the information necessary to make the product, subject to the license's rules for Available Components and External Material.
3. **Independent devices remain independently licensed.** Unrelated hardware that interacts with the OSSMI implementation solely through the documented interface may qualify as *External Material*, whose source need not be released solely on account of that interaction. This depends on the legal definition and the actual design, not simply on naming a part "external".
4. **No mandatory upstream contribution.** The license does not require manufacturers to submit pull requests, assign copyright, or transfer improvements to OSSMI maintainers. It requires the source availability and notices described in the license when their triggering conditions apply.
5. **No obligation for independently authored implementations solely from interoperability.** Reproducing the documented mechanical interface without copying or deriving from covered source does not, by itself, impose CERN-OHL-W-2.0 terms on independently authored files. Patent, design-right, and trademark questions remain separate.
6. **Factory partnerships do not privatize the core.** Early manufacturing partners may own their tooling, fund product development, negotiate commercial terms, and sell finished OSSMI products. Such arrangements must not remove rights already granted to the public for covered source or grant exclusive control over the published mechanical interface.

**Licensing scope within the repository:**

| Material | License / treatment |
|---|---|
| Original OSSMI reference CAD, mechanical source, design drawings, fabrication source, and expressly designated hardware sources | **CERN-OHL-W-2.0**, with explicit file or directory-level copyright/license notices |
| Generated STEP/STL exports of covered OSSMI hardware designs | Treat and distribute consistently with the underlying licensed source; include provenance and notices; exports alone do not replace editable source |
| CAD-generation scripts and general-purpose software tools | **MIT** proposed; select and include the full license when the first such code is published |
| Manifesto, explanatory prose, and normative written specification | **CC BY 4.0** proposed for separately identifiable original text; finalize and publish corresponding notices before claiming these texts are CC-licensed |
| Third-party photographs, examples, logos, trademarks and other material | Original rights and explicit individual permissions govern; **not** automatically covered by CERN-OHL-W-2.0 |

**Implementation note:** The mere presence of a `LICENSE` file does not automatically settle rights in third-party assets, mixed-license files, or copyright held by outside contributors. Add copyright, SPDX and source-location notices to hardware files, and define contribution rules before accepting substantial third-party patches. Existing rights under published license grants cannot simply be withdrawn for earlier recipients by changing the project's license in a later version.

For example, a hardware design source file may carry the notice:

```text
SPDX-License-Identifier: CERN-OHL-W-2.0
Copyright (c) 2026 <copyright holder>
Source Location: https://github.com/<owner>/ossmi
```

Replace placeholders with the actual copyright holder and repository URL before publication. The full CERN-OHL-W-2.0 license text must be left unmodified. Neither this manifesto nor the license guarantees freedom from third-party patents, industrial design rights, or trademarks.

### 12.3 OSSMI name and marks

OSSMI stands for **Open Source Small Mount Interface**. `OSSMI` is the proposed community name; availability and trademark clearance across jurisdictions are **not established by this document**. Project governance SHOULD separately publish naming, attribution, and compatibility-mark rules. The open interface must not depend on mandatory purchase of trademark licenses.

### 12.4 Patents and prior art

LEGO-compatible geometry, embedded threaded inserts, quick-release mounts, and modular hardware are established concepts. OSSMI does **not** assert invention of these underlying mechanisms or guarantee global freedom to operate. Before commercial production, implementers should consider professional patent and trademark searches relevant to their countries and product categories.

## 13. Community governance and change process

OSSMI aims to be **community-maintained** rather than centrally gatekept, but the exact governance structure is not yet ratified. The project may begin in the creator's personal GitHub repository; this does not prevent public issues, pull requests or independent implementations. It should not falsely present itself as an established foundation or standards body.

Proposed process:

1. **Public issue / discussion:** identify a compatibility, safety, fabrication, or usability problem.
2. **OSSMI Improvement Proposal (OIP):** submit a concise proposal with motivation, geometry, migration impact, examples, and test evidence.
3. **Open review:** obtain input from multiple independent implementers, particularly on existing compatibility.
4. **Reference implementation and tests:** attach CAD, gauge models, and data where changes affect the mechanical interface.
5. **Versioned publication:** record the decision and release a tagged spec with a changelog.

**Compatibility principle:** a future revision SHOULD preserve interoperability with v0.1 where practical. Breaking changes MUST be explicit, accompanied by migration guidance, and given a distinct version designation.

No future maintainer should be able to silently redefine the interface while calling incompatible hardware equivalent.

## 14. Reference repository layout

A single repository named `ossmi` is proposed for the initial personal-account release. It can be transferred to an organization later if governance needs change.

```text
ossmi/
├── README.md
├── MANIFESTO.md
├── SPECIFICATION.md
├── LICENSE                  # add full unmodified CERN-OHL-W-2.0 text
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── docs/
│   ├── terminology.md
│   ├── interface-dimensions.md
│   ├── tolerances-and-fits.md
│   ├── m3-anchors.md
│   ├── compatibility.md
│   ├── safety.md
│   ├── prior-art-and-trademarks.md
│   ├── governance.md
│   └── commercial-adoption.md
├── cad/
│   ├── receiver-reference/
│   ├── adapter-reference/
│   ├── test-coupons/
│   └── gauges/
├── exports/
│   ├── step/
│   └── stl/
├── tests/
│   ├── protocols/
│   └── results/
├── examples/
│   ├── tablet/
│   ├── raspberry-pi/
│   ├── arduino/
│   ├── mobile/
│   └── adhesive-receiver/
└── media/
    ├── prototypes/
    └── concepts/
```

The normative OSSMI geometry should stay independent of any particular model of tablet, phone, SBC, printer, or slicer.

## 15. Open questions for v0.2

The following items must not be silently treated as settled:

- Which underside receiver architecture(s) should be canonical: brick-like tubes, plate-like features, or multiple profiles?
- What exact tolerances produce compatible and repeatable clutch performance across molding, FDM, and other manufacturing methods?
- What minimum receiver thickness, tube wall, edge margin, and support geometry should reference designs require?
- How will M3 insert locations be indexed on an 8 mm grid, and what clearance rules protect stud mating?
- Will the interface define a standard test gauge and go/no-go fit protocol?
- How will retaining force, moment resistance, fatigue, and thermal performance be graded?
- Should adapter peel-release ergonomics be included in the standard or left to implementation?
- How will names, logo use, contributor licensing, and compatibility assertions be governed?
- Which device reference models are physically tested, and which remain concept only?
- Which third-party construction-brick geometry sources and existing standards are suitable references under their respective licenses?
- What documented adapter geometry allows two receiver-bearing devices to be linked without reversing the host/accessory convention?
- Which separate test profiles, if any, should be developed for stationary mounts, outdoor solar carriers and UAV/robotics applications without implying universal safety certification?

## 16. Release roadmap

- [x] Build a physical receiver-grid tablet frame prototype.
- [x] Mount real card-reader and SSD peripherals on the prototype.
- [x] Prototype optional M3 heat-set inserts in selected receiver cells.
- [x] Articulate OSSMI as a device-independent open mounting proposal.
- [x] **Adopt hardware licensing policy:** CERN-OHL-W-2.0 for original reference designs.
- [ ] Add the full unmodified CERN-OHL-W-2.0 text to `LICENSE` and add file-level notices before publishing covered CAD.
- [ ] Finish trademark/name due diligence for OSSMI, separately from checking domain availability.
- [ ] Publish parametric canonical receiver and studded adapter CAD, including the exact receiving profile and stated revision.
- [ ] Publish precise 2D dimensioned drawings and measurement conventions.
- [ ] Publish a small multi-tolerance calibration coupon and test gauge.
- [ ] Measure strength and repeated connection cycles with documented fixtures.
- [ ] Independently reproduce the interface on another printer and in another material.
- [ ] Fabricate and test at least one second device class (e.g. Raspberry Pi housing).
- [ ] Publish a device-to-device bridge and a device-to-surface mounting example using the same OSSMI mating geometry.
- [ ] Build and document a stationary home/desk mount or portable solar carrier as a distinct application proof.
- [ ] Prototype a robotics/UAV sensor bracket for non-flight or controlled laboratory validation, with explicit limits and test notes.
- [ ] Establish OSSMI improvement proposal and compatibility versioning process.
- [ ] Publish manufacturer participation guidance and factual compatibility-claim rules.
- [ ] Validate a simple commercially manufacturable starter kit and collect supplier/channel feedback before committing to molds or large production.
- [ ] Release v0.2 after collecting public data and independent feedback.

---

# Part III — Invitation

OSSMI is an invitation, not a claim of ownership over the way small devices attach.

If you print a compatible receiver, publish your settings. If you develop an adapter for an odd-shaped gadget, share the source when you can. If the attachment is weaker than expected, show the failure. If the geometry can be improved, propose a measured change.

**To manufacturers:** build reliable, affordable, interoperable products. Invest in tools, processes, materials, and product quality—not exclusive control over the basic mounting interface.  
**To distributors and retailers:** help people obtain ready-to-use parts instead of requiring everyone to own a printer.  
**To independent makers:** explore the geometry, adapt it, challenge weak assumptions, and publish reproducible evidence.  
**To device brands:** consider OSSMI as an optional attachment vocabulary that customers can reuse across devices.

If you build a commercial product, be truthful about interoperability and the safety limits you have validated. The project should welcome profitable compatible products without confusing commercial endorsement with independent conformance.

OSSMI also welcomes a maker who solves a tiny everyday problem: mounting a streaming box behind a TV, keeping a power bank with a foldable solar panel, or building a reusable sensor mount for a robot. The scale of a use case should not determine whether its contribution matters.

The most meaningful milestone for OSSMI will not be a logo, a launch post, or a large number of downloads. It will be the first independently designed module, made by somebody who never contacted the original inventor, that fits a receiver made by somebody else.

That is when an idea becomes an interface.

**Small devices. One open interface.**  
**The interface is open. The ecosystem is a market.**

**OSSMI — Open Source Small Mount Interface.**

---

## Appendix A — Provenance and factual boundaries

This draft incorporates the earlier *Open Small Mount / Open Modular Tablet Rig* design notes and the inventor's reported prototype observations. It distinguishes observed results from proposals.

- **Observed:** a 3D-printed Lenovo Y700 frame, receiver zones, mounted card reader and SSD, reported strong qualitative hold, and a revised receiving test piece integrating M3 inserts.
- **Nominal reference geometry:** 8 mm stud pitch, approximately 4.8 mm stud diameter, 1.8 mm stud height, approximately 6.5 mm underside tube outer diameter, M3 × 0.5 thread.
- **Not yet established:** standard drawing tolerances, universal plate compatibility, mass ratings, impact resistance, adhesive life, production economics, independent compatibility verification, and legal protection of the OSSMI name.

## Appendix B — Design constraints for any public visualizations

1. Receiver/socket-side geometry appears on the **host**. Studs appear on the **removable accessory**.
2. Do not visually mistake Ø6.5 mm receiver tubes for Ø4.8 mm accessory studs.
3. Depict an 8 mm center-to-center grid with physically plausible device scale.
4. Show M3 inserts only in specifically selected positions, not automatically in every socket.
5. Mark unbuilt products as *concept*, and never claim exact device fit from an AI-generated rendering.

## Appendix C — One-paragraph explanation for README / press

**OSSMI (Open Source Small Mount Interface)** is a proposed open mechanical mounting interface for small devices, components and everyday objects, designed to be reproduced by 3D printing, machining, or molding. It uses an 8 mm LEGO-compatible stud-and-socket grid, with receiving sockets on a host device and studded plates on removable accessories, plus optional M3 threaded securing points. Inspired by a working rugged tablet-frame prototype carrying a card reader and portable SSD, OSSMI aims to let makers and manufacturers build interoperable accessories, device-to-device bridges, and device-to-surface mounts for applications ranging from photography and home electronics to portable solar rigs and robotics research around one reusable mechanical interface. The project welcomes independent commercial products and distribution while resisting exclusive ownership of the shared interface. OSSMI v0.1 is a draft proposal, not a certified safety or industry standard; reference hardware is designated for CERN-OHL-W-2.0, while definitive tolerance profiles remain to be published.

---

*End of OSSMI-STD-0001, v0.1.3 (Public Draft).*
