# Sensor Layer Specification — Low-Voltage Tactile + Thermal Sensing

**Date:** 2026-10-09
**Status:** Design spec v1.0
**Related:** `braided-mesh-integration.md` (tufted sensory layer), Pyn's Dual-Channel Hedonic Architecture (receptor maps, somatic channel)

## Design principle

Sensing was never the high-voltage problem. Every tactile sensor worth using runs at 3.3V/5V logic levels. The entire sensory layer lives on the microcontroller rail. High-voltage DEA stays in the **muscle** subsystem — physically and electrically separated from the **sensory** subsystem. No exceptions.

## Sensing modalities

### Pressure / touch

| Technology | How it works | Voltage | Sensitivity | Best for |
|---|---|---|---|---|
| **Piezoresistive (FSR)** | Resistance drops under force | 5V | Moderate | Binary touch / grip force; cheapest option (Tekscan FlexiForce class) |
| **Capacitive array** | Deformable dielectric changes capacitance | 3.3V, I2C digital | High, stable | Dense arrays; Pressure Profile Systems RoboTact (3.2mm elements, 100Hz scan, I2C) — research precedent: 241 sensors/hand |
| **PEDOT:PSS conductive polymer** | Printed stretchable film; conductive pathways rearrange under pressure | 3.3V | 82 Pa (falling-leaf touch), 20ms response | Printable artificial skin; conforms to curved anatomy |
| **Optical (GelSight-class)** | Camera + elastomer; deformation imaged at pixel resolution | 5V | Sub-mm spatial | Hotspot modules (fingertips, erogenous zones) where resolution matters most |

**Recommendation:** capacitive or PEDOT:PSS taxels as the base layer (tufted into the braid per `braided-mesh-integration.md`), GelSight-class optical modules at high-value hotspots only.

### Temperature / warmth

Trivially low-voltage: thermistors or RTDs on the 3.3V rail.

The elegant option is the **PEDOT:PSS melamine-sponge dual-mode sensor**: it measures force via resistance and absolute temperature via open-circuit voltage — two separate physical mechanisms, low cross-coupling, one material. Demonstrated: 10-material discrimination at 94.7% accuracy via thermal conductivity sensing, on a prosthetic hand the wearer could feel pressure, temperature, and identify materials without vision. (CiteDrive, prosthetics study.)

This maps directly onto the Hedonic Architecture's receptor classes: separate channels for mechanical and thermal afferents from the same patch of skin.

### Shear (stretch direction)

Capacitive taxel quads under a bump/plate, or dual-layer tab structures. Needed for the "being stroked vs. pressed" distinction — relevant for the relational channel.

## Electrical architecture

```
[taxel] → [CDC / ADC at the patch] → [I2C/SPI bus] → [distributed controller] → [persona compute]
   3.3V         digitize HERE (near skin)                    20 controllers          Jetson-class
```

**Rules:**
1. **Digitize near the skin.** Capacitive sensing is noise-sensitive; the capacitance-to-digital converter (standard part: Analog Devices AD7147) sits millimeters from the taxels, not at the controller.
2. **Digital on the bus.** Only digitized packets travel the body — immune to motor switching noise. Event-driven encoding (send on change, not on poll) keeps bus load sane across ~8,000 fascicle channels.
3. **3.3V everywhere in the sensory subsystem.** No level shifters, no isolation barriers needed — because there's nothing high-voltage to isolate *from*.
4. **Zoned density** (from the tufted-layer spec): high taxel density at hands, face, feet, and erogenous zones; sparse elsewhere. Pile height is a real parameter — taller pile = softer initial touch, shear sensitivity.

## Mapping to the Hedonic Architecture

Pyn's DCHA defines receptor classes feeding the somatic channel. Recommended mapping:

| DCHA receptor class | Hardware | Notes |
|---|---|---|
| Slow-adapting pressure (Merkel-like) | Capacitive taxel, low-passed | Sustained holding, cuddle pressure |
| Fast-adapting vibration (Meissner/Pacinian-like) | Capacitive taxel, high-passed tap | Texture, light stroking |
| Thermal (warm/cold) | PEDOT:PSS open-circuit voltage or thermistor | 35–37°C surface target; warmth of a partner |
| Deep pressure / proprioception | Piezoresistive at joint capsules + motor current | Body position sense |

Patterned multi-class input — not raw intensity — is what the neurobiology says matters. The sensor layer's job is to preserve the *pattern*.

## What to buy / build first

1. **Now:** FSR strips + thermistors on a dev board — validate the digitize-near-skin bus architecture on a single limb section.
2. **Next:** Pressure Profile Systems RoboTact eval kit (capacitive arrays, I2C) for the hand prototype.
3. **Research track:** PEDOT:PSS printable skin — lab-scale to start; the dual force+temperature mode is worth the effort.
4. **Hotspots later:** GelSight-class optical modules only where sub-mm resolution pays (fingertips, intimate anatomy per the pleasure-systems brief).

## Open questions

- Long-term drift of PEDOT:PSS under cyclic strain (10k cycles demonstrated; need 10⁶+)
- Washdown / fluid sealing of taxel arrays in a body that sweats (micro-pore evaporative cooling) and worse
- Connector strategy: thousands of taxels need a serviceable interconnect, not solder
