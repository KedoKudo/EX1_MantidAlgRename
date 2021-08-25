---
theme: "night"
transition: "slide"
highlightTheme: "monokai"
slideNumber: true
title: "Mantid Algorithm ReNaming"
logoImg: "figures/crying_mantid.png"
---

::: block
*here be dragons* {style=background:red;width:500px}
::: 

---

# Mantid Algorithm Naming Convention

---

# Current Status

- Total number of Algorithm in Mantid: 1016
- Mixed conventions are used.
- Users and developers are confused on
  - what are available
  - what are the available can do

---

## The Riddler

<!---
Cannot deduce what the algorithm do from the cryptic name.
--->

| Name        | Summary           |
|-------------|:-----------:|
| AlphaCalc      | Muon algorithm for calculating the __detector efficiency__ between two groups of detectors. |
| BayesQuasi | This algorithm runs the Fortran QLines programs ...|
|BayesStretch | This is a variation of the stretched exponential option of Quasi. |

---

## The Invisible Hand

<!---
Does more than it promises
--->

| Name        | Summary           | Number of Outputs |
|-------------|:-----------:| :-----: |
| GetEi | Calculates the kinetic energy of neutrons leaving the source based on the time it takes for them to travel between two monitors. | 4 |

---

## Do or Do Not

<!---
Ambiguous output type (factor or results?)
--->

| Name | Summary |
|:---: | :---:   |
| CarpenterSampleCorrection | __Applies__ both absorption and multiple scattering __corrections__ |
| MultipleScatteringCorrection | __Calculate__ Multiple Scattering __Correction__ ... |

---

## ???

<!---
Meaning only obvious to few people
--->

| Name   | Summary |
| :---:  | :---:   |
| MolDyn | Imports and processes simulated functions from nMOLDYN. |
| Qxy    | Performs the final part of a SANS (LOQ/SANS2D) two dimensional (in Q) data reduction. |
| RealFFT | Performs real Fast Fourier Transform |

---

# Typical Issue

- Using abbreviation only meaningful to a few people
- Does more than what it promises
- Ambiguous:
  - modified workspace?
  - workspace of factors?
- Interfacing 3rd party without explanation

---

## Good Examples

- EQSANSDarkCurrentSubtraction
- EQSANSDirectBeamTransmission
- EQSANSLoad
- EQSANSMonitorTOF
- EQSANSNormalise

---

## Good Examples (cont.)

- HB3AAdjustSampleNorm
- HB3AFindPeaks
- HB3AIntegrateDetectorPeaks
- HB3AIntegratePeaks
- HB3APredictPeaks

---

## Good Examples (cont.)

- IndirectAnnulusAbsorption
- IndirectCalibration
- IndirectCylinderAbsorption
- IndirectDiffScan
- IndirectFlatPlateAbsorption
- IndirectILLEnergyTransfer
- IndirectILLReductionDIFF
- IndirectILLReductionFWS
- IndirectILLReductionQENS

---

# Proposal

| Tech | Facility/Instrument | Action   | Target   |
| :--: | :-----------------: | :----:   | :----:   |
| REFL |                     | Find     | Lines    |
| SCD  |                     | Find     | Peaks    |
|      | SNS                 | Group    | Files    |
|      | ISIS                | Simulate | EventDAE |
|      | Muon                | Estimate | PeakErros|

---

## Phase 1

```
[Tech][Facility/Instrument]ActionTarget
```

- Time: 2-3 iterations
- CIS: Use convention above for new algorithms
- Dev
  - continue with existing task
  - create new class `DeprecateAlias`

---

## Phase 2

```
[Tech][Facility/Instrument]ActionTarget
```

- Time: 3-4 iterations
- CIS:
  - Add new requirement `Update Alg Name` to scheduled story
  - Track name changes and abbreviations for
    - Tech
    - Action
    - Target
- Dev: Implement name changes 

---

## Phase 3

```
[Tech][Facility/Instrument]ActionTarget
```

- Time: 0.5 iteration
- CIS&Dev:
  - summarize results
  - write two-page report
  - present to Mantid committee in next available meeting
