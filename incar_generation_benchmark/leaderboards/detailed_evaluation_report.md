# Detailed Evaluation Report

- Generated at: `2026-07-01T08:29:05Z`
- Benchmark root: `/Users/alexander/Workspace/incarbench-skill/incar_generation_benchmark`
- Models covered: `2`
- Models are ranked primarily by `average_scores.must_match` from the summary JSON.
- `Minimum Task-Runnable Rate` is reported as a supplementary case-level feasibility metric and does not change the ranking order.
- Dimension table cells are shown as `must_match_semantic / must_match_policy / must_match`.

## Contents

- [Overall Ranking](#overall-ranking)
- [By Difficulty](#by-difficulty)
- [By Task Type](#by-task-type)
- [By Task Family](#by-task-family)
- [By Material Family](#by-material-family)
- [By Challenge Type](#by-challenge-type)
- [Case Details](#case-details)

## Overall Ranking

| Model | Avg Must Match | Avg Semantic | Avg Policy | Minimum Task-Runnable Rate | Perfect Case Rate | Graded | Missing |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-4o-no-skill | 37.62 | 36.84 | 38.41 | 23.03% | 2.42% | 165/192 | 27 |
| gpt-4o-vasp.skill | - | - | - | - | - | 0/192 | 192 |

## By Difficulty

| Group | Cases | gpt-4o-no-skill | gpt-4o-vasp.skill | Best Model |
| --- | --- | --- | --- | --- |
| L1 | 17 | 77.78 / 78.33 / 78.06 | - | gpt-4o-no-skill (78.06) |
| L2 | 65 | 58.19 / 55.10 / 56.64 | - | gpt-4o-no-skill (56.64) |
| L3 | 110 | 17.15 / 21.74 / 19.45 | - | gpt-4o-no-skill (19.45) |

## By Task Type

| Group | Cases | gpt-4o-no-skill | gpt-4o-vasp.skill | Best Model |
| --- | --- | --- | --- | --- |
| dos_nscf | 48 | 5.94 / 12.06 / 9.00 | - | gpt-4o-no-skill (9.00) |
| geometry_relax | 48 | 85.37 / 61.83 / 73.60 | - | gpt-4o-no-skill (73.60) |
| line_mode_bands | 48 | 6.20 / 13.58 / 9.89 | - | gpt-4o-no-skill (9.89) |
| static_scf | 48 | 50.61 / 66.81 / 58.71 | - | gpt-4o-no-skill (58.71) |

## By Task Family

| Group | Cases | gpt-4o-no-skill | gpt-4o-vasp.skill | Best Model |
| --- | --- | --- | --- | --- |
| dos_nscf | 48 | 5.94 / 12.06 / 9.00 | - | gpt-4o-no-skill (9.00) |
| geometry_relax | 48 | 85.37 / 61.83 / 73.60 | - | gpt-4o-no-skill (73.60) |
| line_mode_bands | 48 | 6.20 / 13.58 / 9.89 | - | gpt-4o-no-skill (9.89) |
| static_scf | 48 | 50.61 / 66.81 / 58.71 | - | gpt-4o-no-skill (58.71) |

## By Material Family

| Group | Cases | gpt-4o-no-skill | gpt-4o-vasp.skill | Best Model |
| --- | --- | --- | --- | --- |
| battery_material | 8 | - | - | - |
| binary_compound | 12 | 47.92 / 52.92 / 50.42 | - | gpt-4o-no-skill (50.42) |
| chalcogenide | 12 | 44.72 / 59.17 / 51.94 | - | gpt-4o-no-skill (51.94) |
| complex_low_symmetry | 8 | 0.00 / 0.00 / 0.00 | - | gpt-4o-no-skill (0.00) |
| correlated_oxide | 10 | 28.69 / 35.86 / 32.27 | - | gpt-4o-no-skill (32.27) |
| elemental | 12 | 30.42 / 31.39 / 30.90 | - | gpt-4o-no-skill (30.90) |
| heavy_element_semiconductor | 12 | 26.67 / 27.08 / 26.88 | - | gpt-4o-no-skill (26.88) |
| ionic_insulator | 12 | 43.75 / 45.00 / 44.38 | - | gpt-4o-no-skill (44.38) |
| layered_anisotropic | 12 | 43.06 / 57.78 / 50.42 | - | gpt-4o-no-skill (50.42) |
| layered_material | 12 | 33.33 / 27.08 / 30.21 | - | gpt-4o-no-skill (30.21) |
| magnetic_metal | 12 | 40.56 / 37.64 / 39.10 | - | gpt-4o-no-skill (39.10) |
| metal | 12 | 31.25 / 29.17 / 30.21 | - | gpt-4o-no-skill (30.21) |
| oxide | 12 | 29.17 / 35.00 / 32.08 | - | gpt-4o-no-skill (32.08) |
| perovskite_multinary_oxide | 12 | - | - | - |
| semiconductor | 24 | 42.71 / 36.25 / 39.48 | - | gpt-4o-no-skill (39.48) |
| transition_metal_oxide | 10 | 31.67 / 28.24 / 29.95 | - | gpt-4o-no-skill (29.95) |

## By Challenge Type

| Group | Cases | gpt-4o-no-skill | gpt-4o-vasp.skill | Best Model |
| --- | --- | --- | --- | --- |
| dftu_semantics | 27 | 15.14 / 26.02 / 20.58 | - | gpt-4o-no-skill (20.58) |
| magnetic_initialization | 12 | 81.48 / 47.78 / 64.63 | - | gpt-4o-no-skill (64.63) |
| metal_smearing | 8 | 50.00 / 56.25 / 53.12 | - | gpt-4o-no-skill (53.12) |
| nscf_workflow | 55 | 6.13 / 12.89 / 9.51 | - | gpt-4o-no-skill (9.51) |
| relax_semantics | 25 | 86.96 / 64.35 / 75.65 | - | gpt-4o-no-skill (75.65) |
| semiconductor_smearing | 18 | 73.53 / 77.94 / 75.74 | - | gpt-4o-no-skill (75.74) |
| soc_semantics | 18 | 5.00 / 20.10 / 12.55 | - | gpt-4o-no-skill (12.55) |
| spin_semantics | 11 | 26.06 / 44.70 / 35.38 | - | gpt-4o-no-skill (35.38) |
| symmetry_sensitive | 8 | 5.00 / 33.33 / 19.17 | - | gpt-4o-no-skill (19.17) |
| vdw_semantics | 10 | 85.19 / 69.44 / 77.31 | - | gpt-4o-no-skill (77.31) |

## Case Details

Each row shows which semantic and policy keys were missed, which optional keys were not matched, and whether unsupported extra keys were added.

### gpt-4o-no-skill

| Case | Task | Material | Challenge | Minimum Runnable | Runnable Failure Reasons | Imputed Defaults | Missing Semantic | Missing Policy | Optional Miss | Extra Keys | Semantic | Policy | Must | Perfect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01_Si_Static_SCF | static_scf | semiconductor | semiconductor_smearing | False | semantic:IBRION | - | IBRION | - | ALGO, LREAL | ALGO, ISTART, NBANDS | 50.00 | 100.00 | 75.00 | False |
| P02_GaAs_Line_Mode_Bands | line_mode_bands | semiconductor | nscf_workflow | False | semantic:ISYM, semantic:IBRION, semantic:NSW | - | IBRION, ISYM, NSW | - | PREC, ALGO, LREAL | ALGO, ISTART | 25.00 | 100.00 | 62.50 | False |
| P03_Fe_Static_Magnetic | static_scf | magnetic_metal | spin_semantics | False | semantic:IBRION | - | IBRION | - | MAGMOM, ALGO | ALGO, ISTART, NELMIN | 66.67 | 100.00 | 83.33 | False |
| P04_LiF_Geometry_Relax | geometry_relax | ionic_insulator | relax_semantics | True | - | - | - | ENCUT | ALGO | ALGO | 100.00 | 80.00 | 90.00 | False |
| P05_AlN_Geometry_Relax | geometry_relax | semiconductor | relax_semantics | True | - | - | - | EDIFFG, ENCUT | SIGMA, ALGO | ALGO | 100.00 | 60.00 | 80.00 | False |
| P06_Si_Line_Mode_Bands | line_mode_bands | semiconductor | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | SIGMA, LREAL, ALGO | ALGO, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P07_GaAs_DOS_NSCF | dos_nscf | semiconductor | nscf_workflow | False | semantic:ISYM, semantic:IBRION, policy:ISMEAR | - | IBRION, ISYM | ISMEAR, SIGMA | ENCUT, EDIFF, LREAL | ISTART, LORBIT, NELMIN | 50.00 | 0.00 | 25.00 | False |
| P08_TiO2_Static_DFTU | static_scf | oxide | dftu_semantics | False | semantic:LDAU | - | LDAU | LASPH, LMAXMIX | ALGO, LREAL | ALGO, LORBIT, LVHAR, NELMIN | 0.00 | 60.00 | 30.00 | False |
| P09_FeO_Static_DFTU_Spin | static_scf | correlated_oxide | dftu_semantics | False | semantic:LDAUL, policy:LDAUU, policy:LDAUJ, policy:ISMEAR | - | LDAUL | ISMEAR, LASPH, LDAUJ, LDAUU, LMAXMIX | MAGMOM, ALGO | ALGO, ISTART | 75.00 | 28.57 | 51.79 | False |
| P100_Bi2WO6_DOS_NSCF | dos_nscf | complex_low_symmetry | soc_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LSORBIT, policy:ISMEAR | - | IBRION, ICHARG, ISYM, LSORBIT, NSW | ISMEAR, SAXIS, SIGMA | PREC, ALGO | ALGO, ISTART, LOPTICS, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P101_NiO_Static_SCF | static_scf | correlated_oxide | dftu_semantics | False | semantic:LDAU, semantic:LDAUTYPE, semantic:LDAUL, semantic:LDAUU, semantic:LDAUJ | - | LDAU, LDAUJ, LDAUL, LDAUTYPE, LDAUU | LASPH, LMAXMIX | MAGMOM, ALGO | ALGO, NCORE | 16.67 | 60.00 | 38.33 | False |
| P102_NiO_Geometry_Relax | geometry_relax | correlated_oxide | magnetic_initialization | False | semantic:ISPIN, policy:LDAU, policy:LDAUU, policy:LDAUJ | - | ISPIN | LASPH, LDAU, LDAUJ, LDAUU, LMAXMIX | SIGMA, MAGMOM, ALGO | ALGO | 66.67 | 50.00 | 58.33 | False |
| P103_NiO_Line_Mode_Bands | line_mode_bands | correlated_oxide | dftu_semantics | False | semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LDAU, semantic:LDAUTYPE, semantic:LDAUL, policy:LDAUU, policy:LDAUJ, policy:ISMEAR | - | IBRION, ISYM, LDAU, LDAUL, LDAUTYPE, NSW | ISMEAR, LDAUJ, LDAUU | MAGMOM, LASPH, ALGO, LREAL | ALGO, ISTART, LORBIT | 14.29 | 40.00 | 27.14 | False |
| P104_NiO_DOS_NSCF | dos_nscf | correlated_oxide | dftu_semantics | False | semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LDAU, semantic:LDAUTYPE, semantic:LDAUL, policy:LDAUU, policy:LDAUJ | - | IBRION, ISYM, LDAU, LDAUL, LDAUTYPE, NSW | LDAUJ, LDAUU | MAGMOM, LASPH, PREC, ALGO | ALGO, ISTART, LORBIT | 14.29 | 50.00 | 32.14 | False |
| P105_Bi2Te3_Static_SCF | static_scf | heavy_element_semiconductor | soc_semantics | False | semantic:LSORBIT, semantic:ISYM | - | ISYM, LSORBIT | SAXIS | ALGO, LREAL | ALGO | 0.00 | 75.00 | 37.50 | False |
| P106_Bi2Te3_Geometry_Relax | geometry_relax | heavy_element_semiconductor | vdw_semantics | True | - | - | - | EDIFFG, NSW | - | ADDGRID, MAXMIX | 100.00 | 60.00 | 80.00 | False |
| P107_Bi2Te3_Line_Mode_Bands | line_mode_bands | heavy_element_semiconductor | soc_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LSORBIT, policy:ISMEAR | - | IBRION, ICHARG, ISYM, LSORBIT, NSW | EDIFF, ENCUT, ISMEAR, SAXIS | PREC, ALGO, LREAL | ALGO, ISTART, KPOINTS, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P108_Bi2Te3_DOS_NSCF | dos_nscf | heavy_element_semiconductor | soc_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LSORBIT, policy:ISMEAR | - | IBRION, ICHARG, ISYM, LSORBIT, NSW | ISMEAR, SAXIS, SIGMA | PREC, ALGO | ALGO, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P109_NaCl_Static_SCF | static_scf | ionic_insulator | semiconductor_smearing | True | - | - | - | - | LREAL | LVTOT | 100.00 | 100.00 | 100.00 | False |
| P10_MoS2_Relax_vdW | geometry_relax | layered_material | vdw_semantics | True | - | - | - | NSW | ALGO | ALGO, ISTART, KSPACING | 100.00 | 75.00 | 87.50 | False |
| P110_NaCl_Geometry_Relax | geometry_relax | ionic_insulator | relax_semantics | True | - | - | - | EDIFFG | ALGO | ALGO | 100.00 | 80.00 | 90.00 | False |
| P111_NaCl_Line_Mode_Bands | line_mode_bands | ionic_insulator | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, LREAL | ISTART | 0.00 | 0.00 | 0.00 | False |
| P112_NaCl_DOS_NSCF | dos_nscf | ionic_insulator | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC, ALGO | ALGO, ISTART, LOPTICS | 0.00 | 0.00 | 0.00 | False |
| P113_C_Static_SCF | static_scf | layered_material | metal_smearing | False | semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, NSW | EDIFF, ENCUT, ISMEAR, SIGMA | PREC, ALGO, LREAL | ALGO, ISTART, NBANDS, NELMIN | 0.00 | 0.00 | 0.00 | False |
| P114_C_Geometry_Relax | geometry_relax | layered_material | vdw_semantics | True | - | - | - | EDIFFG, NSW | ALGO | ALGO | 100.00 | 50.00 | 75.00 | False |
| P115_C_Line_Mode_Bands | line_mode_bands | layered_material | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, KPOINTS, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P116_C_DOS_NSCF | dos_nscf | layered_material | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC | EMAX, EMIN, ISTART, LOPTICS | 0.00 | 0.00 | 0.00 | False |
| P117_Co_Static_SCF | static_scf | magnetic_metal | spin_semantics | False | semantic:IBRION | - | IBRION | SIGMA | MAGMOM, PREC, ALGO | ALGO, ISTART | 66.67 | 75.00 | 70.83 | False |
| P118_Co_Geometry_Relax | geometry_relax | magnetic_metal | magnetic_initialization | False | policy:ISMEAR | - | - | EDIFF, EDIFFG, ISMEAR | SIGMA, MAGMOM, ALGO | ALGO, ISTART | 100.00 | 40.00 | 70.00 | False |
| P119_Co_Line_Mode_Bands | line_mode_bands | magnetic_metal | spin_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:ISPIN, policy:ISMEAR | - | IBRION, ICHARG, ISPIN, ISYM, NSW | EDIFF, ENCUT, ISMEAR | MAGMOM, PREC, LREAL | ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P11_InSb_Static_SOC | static_scf | heavy_element_semiconductor | soc_semantics | False | semantic:LSORBIT, semantic:ISYM | - | ISYM, LSORBIT | ENCUT, SAXIS | ALGO, LREAL | ALGO | 0.00 | 50.00 | 25.00 | False |
| P120_Co_DOS_NSCF | dos_nscf | magnetic_metal | spin_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:ISPIN, policy:ISMEAR | - | IBRION, ICHARG, ISPIN, ISYM, NSW | ISMEAR, SIGMA | MAGMOM, PREC | ICHARGE, ISTART, LORBIT, NPAR | 0.00 | 0.00 | 0.00 | False |
| P121_Au_Static_SCF | static_scf | metal | metal_smearing | False | semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, NSW | EDIFF, ENCUT, ISMEAR, SIGMA | PREC, ALGO, LREAL | ALGO, ISTART | 0.00 | 0.00 | 0.00 | False |
| P122_Au_Geometry_Relax | geometry_relax | metal | relax_semantics | False | workflow:IBRION, workflow:NSW, semantic:IBRION, semantic:ISIF, policy:ISMEAR | - | IBRION, ISIF | EDIFF, EDIFFG, ENCUT, ISMEAR, NSW | SIGMA, PREC | LOPTICS, NCORE | 0.00 | 0.00 | 0.00 | False |
| P123_Au_Line_Mode_Bands | line_mode_bands | metal | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P124_Au_DOS_NSCF | dos_nscf | metal | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC, ALGO | ALGO, ISTART, NPAR | 0.00 | 0.00 | 0.00 | False |
| P125_ZrO2_Static_SCF | static_scf | oxide | semiconductor_smearing | True | - | - | - | - | ALGO, LREAL | ALGO, LOPTICS, SYMPREC | 100.00 | 100.00 | 100.00 | False |
| P126_ZrO2_Geometry_Relax | geometry_relax | oxide | relax_semantics | False | workflow:IBRION, workflow:NSW, semantic:IBRION, semantic:ISIF, policy:ISMEAR | - | IBRION, ISIF | EDIFF, EDIFFG, ENCUT, ISMEAR, NSW | SIGMA, PREC | - | 0.00 | 0.00 | 0.00 | False |
| P127_ZrO2_Line_Mode_Bands | line_mode_bands | oxide | symmetry_sensitive | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P128_ZrO2_DOS_NSCF | dos_nscf | oxide | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC, ALGO | ALGO, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P129_InP_Static_SCF | static_scf | semiconductor | semiconductor_smearing | False | semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, NSW | EDIFF, ENCUT, ISMEAR, SIGMA | PREC, ALGO, LREAL | ALGO, ISTART, KSPACING | 0.00 | 0.00 | 0.00 | False |
| P12_VO2_Static_Symmetry | static_scf | correlated_oxide | symmetry_sensitive | False | semantic:ISPIN, semantic:ISYM | - | ISPIN, ISYM | - | MAGMOM, ALGO, LREAL | ALGO, GGA, NELMIN | 0.00 | 100.00 | 50.00 | False |
| P130_InP_Geometry_Relax | geometry_relax | semiconductor | relax_semantics | True | - | - | - | EDIFFG, NSW | - | ISTART | 100.00 | 60.00 | 80.00 | False |
| P131_InP_Line_Mode_Bands | line_mode_bands | semiconductor | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, LOPTICS | 0.00 | 0.00 | 0.00 | False |
| P132_InP_DOS_NSCF | dos_nscf | semiconductor | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC | EMAX, EMIN, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P13_Cu_Static_SCF | static_scf | elemental | metal_smearing | True | - | - | - | - | ALGO, LREAL | ALGO, NELMIN | 100.00 | 100.00 | 100.00 | False |
| P14_Cu_Geometry_Relax | geometry_relax | elemental | relax_semantics | True | - | - | - | - | SIGMA | - | 100.00 | 100.00 | 100.00 | True |
| P15_Cu_Line_Mode_Bands | line_mode_bands | elemental | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, LREAL | ISTART, LOPTICS | 0.00 | 0.00 | 0.00 | False |
| P16_Cu_DOS_NSCF | dos_nscf | elemental | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC | EMAX, EMIN, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P17_W_Static_SCF | static_scf | elemental | metal_smearing | False | semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, NSW | EDIFF, ENCUT, ISMEAR, SIGMA | PREC, ALGO, LREAL | ALGO, ISTART | 0.00 | 0.00 | 0.00 | False |
| P18_W_Geometry_Relax | geometry_relax | elemental | relax_semantics | False | workflow:IBRION, workflow:NSW, semantic:IBRION, semantic:ISIF, policy:ISMEAR | - | IBRION, ISIF | EDIFF, EDIFFG, ENCUT, ISMEAR, NSW | SIGMA, PREC, ALGO | ALGO, ISTART | 0.00 | 0.00 | 0.00 | False |
| P19_W_Line_Mode_Bands | line_mode_bands | elemental | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, LREAL | ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P206_FeO_Geometry_Relax | geometry_relax | correlated_oxide | magnetic_initialization | False | policy:LDAU, policy:LDAUU, policy:LDAUJ, policy:ISMEAR | - | - | EDIFFG, ISMEAR, LASPH, LDAU, LDAUJ, LDAUU, LMAXMIX | SIGMA, MAGMOM, ALGO | ALGO | 100.00 | 30.00 | 65.00 | False |
| P20_W_DOS_NSCF | dos_nscf | elemental | nscf_workflow | False | semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ISYM, NSW | ISMEAR | PREC | ISTART, LORBIT | 25.00 | 50.00 | 37.50 | False |
| P210_VO2_Geometry_Relax | geometry_relax | correlated_oxide | magnetic_initialization | False | workflow:IBRION, workflow:NSW, semantic:ISPIN, semantic:IBRION, semantic:ISIF, policy:LDAU, policy:LDAUU, policy:LDAUJ, policy:ISMEAR | - | IBRION, ISIF, ISPIN | EDIFF, EDIFFG, ENCUT, ISMEAR, LASPH, LDAU, LDAUJ, LDAUU, LMAXMIX, NSW | SIGMA, MAGMOM, PREC | GGA, ISTART, NPAR | 0.00 | 0.00 | 0.00 | False |
| P211_VO2_Line_Mode_Bands | line_mode_bands | correlated_oxide | dftu_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LDAU, semantic:LDAUTYPE, semantic:LDAUL, policy:LDAUU, policy:LDAUJ, policy:ISMEAR | - | IBRION, ICHARG, ISYM, LDAU, LDAUL, LDAUTYPE, NSW | EDIFF, ENCUT, ISMEAR, LDAUJ, LDAUU | MAGMOM, LASPH, PREC, ALGO, LREAL | ALGO, ISTART | 0.00 | 0.00 | 0.00 | False |
| P212_VO2_DOS_NSCF | dos_nscf | correlated_oxide | dftu_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LDAU, semantic:LDAUTYPE, semantic:LDAUL, policy:ISMEAR, policy:LDAUU, policy:LDAUJ | - | IBRION, ICHARG, ISYM, LDAU, LDAUL, LDAUTYPE, NSW | ISMEAR, LDAUJ, LDAUU, SIGMA | MAGMOM, LASPH, PREC | EMAX, EMIN, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P214_InSb_Geometry_Relax | geometry_relax | heavy_element_semiconductor | relax_semantics | True | - | - | - | EDIFFG, ENCUT | SIGMA, ALGO | ADDGRID, ALGO, NELMIN | 100.00 | 60.00 | 80.00 | False |
| P215_InSb_Line_Mode_Bands | line_mode_bands | heavy_element_semiconductor | soc_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LSORBIT, policy:ISMEAR | - | IBRION, ICHARG, ISYM, LSORBIT, NSW | EDIFF, ENCUT, ISMEAR, SAXIS | PREC, LREAL | ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P216_InSb_DOS_NSCF | dos_nscf | heavy_element_semiconductor | soc_semantics | False | semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LSORBIT, policy:ISMEAR | - | IBRION, ISYM, LSORBIT, NSW | ISMEAR, SAXIS, SIGMA | - | EMAX, EMIN | 20.00 | 0.00 | 10.00 | False |
| P21_Te_Static_SCF | static_scf | elemental | soc_semantics | False | semantic:IBRION, semantic:NSW, semantic:LSORBIT, semantic:ISYM, policy:ISMEAR | - | IBRION, ISYM, LSORBIT, NSW | EDIFF, ENCUT, ISMEAR, SAXIS, SIGMA | PREC, ALGO, LREAL | ALGO | 0.00 | 0.00 | 0.00 | False |
| P221_PbSe_Static_SCF | static_scf | heavy_element_semiconductor | soc_semantics | False | semantic:LSORBIT, semantic:ISYM, policy:ISMEAR | - | ISYM, LSORBIT | EDIFF, ENCUT, ISMEAR, SAXIS | PREC, ALGO, LREAL | ALGO, KSPACING, NELMIN | 0.00 | 0.00 | 0.00 | False |
| P222_PbSe_Geometry_Relax | geometry_relax | heavy_element_semiconductor | relax_semantics | True | - | - | - | NSW | ALGO | ALGO, ISTART, POTIM | 100.00 | 80.00 | 90.00 | False |
| P223_PbSe_Line_Mode_Bands | line_mode_bands | heavy_element_semiconductor | soc_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LSORBIT, policy:ISMEAR | - | IBRION, ICHARG, ISYM, LSORBIT, NSW | EDIFF, ENCUT, ISMEAR, SAXIS | PREC, LREAL | ISTART, NELMIN | 0.00 | 0.00 | 0.00 | False |
| P224_PbSe_DOS_NSCF | dos_nscf | heavy_element_semiconductor | soc_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LSORBIT, policy:ISMEAR | - | IBRION, ICHARG, ISYM, LSORBIT, NSW | ISMEAR, SAXIS, SIGMA | PREC | ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P225_LiF_Static_SCF | static_scf | ionic_insulator | semiconductor_smearing | False | semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, NSW | EDIFF, ENCUT, ISMEAR, SIGMA | PREC, ALGO, LREAL | ALGO, NELMEND, NELMIN | 0.00 | 0.00 | 0.00 | False |
| P227_LiF_Line_Mode_Bands | line_mode_bands | ionic_insulator | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, LREAL | ISTART, KPAR, LOPTICS, SYMPREC | 0.00 | 0.00 | 0.00 | False |
| P228_LiF_DOS_NSCF | dos_nscf | ionic_insulator | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC | ISTART, LORBIT, NPAR | 0.00 | 0.00 | 0.00 | False |
| P22_Te_Geometry_Relax | geometry_relax | elemental | relax_semantics | True | - | - | - | EDIFF, NSW | ALGO | ALGO, ISTART | 100.00 | 60.00 | 80.00 | False |
| P233_KCl_Static_SCF | static_scf | ionic_insulator | semiconductor_smearing | True | - | - | - | - | LREAL | - | 100.00 | 100.00 | 100.00 | True |
| P234_KCl_Geometry_Relax | geometry_relax | ionic_insulator | relax_semantics | True | - | - | - | EDIFF | ALGO | ALGO, ISTART, NPAR | 100.00 | 80.00 | 90.00 | False |
| P235_KCl_Line_Mode_Bands | line_mode_bands | ionic_insulator | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, GGA, ISTART, LOPTICS, LORBIT, NCORE | 0.00 | 0.00 | 0.00 | False |
| P236_KCl_DOS_NSCF | dos_nscf | ionic_insulator | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION | - | IBRION, ICHARG, ISYM | - | PREC, ALGO | ALGO, IALGO, NBANDS | 25.00 | 100.00 | 62.50 | False |
| P237_MoS2_Static_SCF | static_scf | layered_material | semiconductor_smearing | True | - | - | - | - | ALGO, LREAL | ALGO, ISTART, KSPACING, NPAR | 100.00 | 100.00 | 100.00 | False |
| P239_MoS2_Line_Mode_Bands | line_mode_bands | layered_material | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P23_Te_Line_Mode_Bands | line_mode_bands | elemental | soc_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LSORBIT, policy:ISMEAR | - | IBRION, ICHARG, ISYM, LSORBIT, NSW | EDIFF, ENCUT, ISMEAR, SAXIS | PREC, ALGO, LREAL | ALGO, ISTART, KPAR, LORBIT, NCORE | 0.00 | 0.00 | 0.00 | False |
| P240_MoS2_DOS_NSCF | dos_nscf | layered_material | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC | ISTART, KPAR, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P245_BN_Static_SCF | static_scf | layered_material | semiconductor_smearing | True | - | - | - | - | LREAL | - | 100.00 | 100.00 | 100.00 | True |
| P246_BN_Geometry_Relax | geometry_relax | layered_material | vdw_semantics | False | workflow:IBRION, workflow:NSW, semantic:IBRION, semantic:ISIF, policy:ISMEAR | - | IBRION, ISIF | EDIFFG, ENCUT, ISMEAR, NSW | SIGMA, PREC | LVDW, NPAR | 0.00 | 0.00 | 0.00 | False |
| P247_BN_Line_Mode_Bands | line_mode_bands | layered_material | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, KSPACING, LOPTICS, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P248_BN_DOS_NSCF | dos_nscf | layered_material | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC, ALGO | ALGO, EMAX, EMIN, ISTART | 0.00 | 0.00 | 0.00 | False |
| P24_Te_DOS_NSCF | dos_nscf | elemental | soc_semantics | False | semantic:ISYM, semantic:IBRION, semantic:LSORBIT | - | IBRION, ISYM, LSORBIT | SAXIS | - | ISTART, LORBIT | 40.00 | 66.67 | 53.33 | False |
| P250_Fe_Geometry_Relax | geometry_relax | magnetic_metal | magnetic_initialization | False | policy:ISMEAR | - | - | EDIFF, ISMEAR, NSW | SIGMA, MAGMOM, ALGO | ALGO, ISTART | 100.00 | 40.00 | 70.00 | False |
| P251_Fe_Line_Mode_Bands | line_mode_bands | magnetic_metal | spin_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:ISPIN, policy:ISMEAR | - | IBRION, ICHARG, ISPIN, ISYM, NSW | EDIFF, ENCUT, ISMEAR | MAGMOM, PREC, ALGO, LREAL | ALGO, ISTART, KPAR, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P252_Fe_DOS_NSCF | dos_nscf | magnetic_metal | spin_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:ISPIN, policy:ISMEAR | - | IBRION, ICHARG, ISPIN, ISYM, NSW | ISMEAR, SIGMA | MAGMOM, PREC | ISTART, LORBIT, NPAR | 0.00 | 0.00 | 0.00 | False |
| P257_Ni_Static_SCF | static_scf | magnetic_metal | spin_semantics | False | semantic:IBRION, policy:ISMEAR | - | IBRION | ISMEAR, SIGMA | MAGMOM, PREC, ALGO | ALGO | 66.67 | 50.00 | 58.33 | False |
| P258_Ni_Geometry_Relax | geometry_relax | magnetic_metal | magnetic_initialization | False | semantic:ISPIN, policy:ISMEAR | - | ISPIN | ISMEAR | SIGMA, MAGMOM, ALGO | ALGO | 66.67 | 80.00 | 73.33 | False |
| P259_Ni_Line_Mode_Bands | line_mode_bands | magnetic_metal | spin_semantics | False | semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:ISPIN | - | IBRION, ISPIN, ISYM, NSW | EDIFF | MAGMOM, ALGO, LREAL | ALGO, KPOINTS, LORBIT | 20.00 | 66.67 | 43.33 | False |
| P25_BP_Static_SCF | static_scf | binary_compound | semiconductor_smearing | True | - | - | - | - | ALGO, LREAL | ALGO | 100.00 | 100.00 | 100.00 | False |
| P260_Ni_DOS_NSCF | dos_nscf | magnetic_metal | spin_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:ISPIN, policy:ISMEAR | - | IBRION, ICHARG, ISPIN, ISYM, NSW | ISMEAR, SIGMA | MAGMOM, PREC | ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P261_Al_Static_SCF | static_scf | metal | metal_smearing | False | policy:ISMEAR | - | - | ISMEAR, SIGMA | LREAL | ISTART, NELMIN | 100.00 | 50.00 | 75.00 | False |
| P262_Al_Geometry_Relax | geometry_relax | metal | relax_semantics | False | policy:ISMEAR | - | - | ISMEAR | SIGMA, ALGO | ALGO | 100.00 | 80.00 | 90.00 | False |
| P263_Al_Line_Mode_Bands | line_mode_bands | metal | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P264_Al_DOS_NSCF | dos_nscf | metal | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC | ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P269_Pt_Static_SCF | static_scf | metal | metal_smearing | False | semantic:IBRION | - | IBRION | - | ALGO, LREAL | ALGO, ISTART | 50.00 | 100.00 | 75.00 | False |
| P26_BP_Geometry_Relax | geometry_relax | binary_compound | relax_semantics | True | - | - | - | - | ALGO | ALGO, NPAR | 100.00 | 100.00 | 100.00 | False |
| P270_Pt_Geometry_Relax | geometry_relax | metal | relax_semantics | False | policy:ISMEAR | - | - | EDIFFG, ENCUT, ISMEAR, NSW | SIGMA, ALGO | ALGO, NCORE, POTIM | 100.00 | 20.00 | 60.00 | False |
| P271_Pt_Line_Mode_Bands | line_mode_bands | metal | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, LOPTICS, LORBIT, NELMIN | 0.00 | 0.00 | 0.00 | False |
| P272_Pt_DOS_NSCF | dos_nscf | metal | nscf_workflow | False | semantic:ISYM, semantic:IBRION, semantic:NSW | - | IBRION, ISYM, NSW | - | ALGO | ALGO, ISTART, LORBIT, NBANDS | 25.00 | 100.00 | 62.50 | False |
| P274_TiO2_Geometry_Relax | geometry_relax | oxide | relax_semantics | True | - | - | - | NSW | ALGO | ADDGRID, ALGO, ISTART | 100.00 | 80.00 | 90.00 | False |
| P275_TiO2_Line_Mode_Bands | line_mode_bands | oxide | symmetry_sensitive | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, LOPTICS, TYPE | 0.00 | 0.00 | 0.00 | False |
| P276_TiO2_DOS_NSCF | dos_nscf | oxide | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC | ISTART, LOPTICS | 0.00 | 0.00 | 0.00 | False |
| P27_BP_Line_Mode_Bands | line_mode_bands | binary_compound | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, LOPTICS, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P281_HfO2_Static_SCF | static_scf | oxide | semiconductor_smearing | False | semantic:IBRION | - | IBRION | - | ALGO, LREAL | ADDGRID, ALGO, ISTART, KSPACING, NELMIN | 50.00 | 100.00 | 75.00 | False |
| P282_HfO2_Geometry_Relax | geometry_relax | oxide | relax_semantics | True | - | - | - | NSW | ALGO | ALGO, GGA, NPAR | 100.00 | 80.00 | 90.00 | False |
| P283_HfO2_Line_Mode_Bands | line_mode_bands | oxide | symmetry_sensitive | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P284_HfO2_DOS_NSCF | dos_nscf | oxide | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC | ISTART, LOPTICS, NPAR | 0.00 | 0.00 | 0.00 | False |
| P289_GaP_Static_SCF | static_scf | semiconductor | semiconductor_smearing | True | - | - | - | - | ALGO, LREAL | ALGO | 100.00 | 100.00 | 100.00 | False |
| P28_BP_DOS_NSCF | dos_nscf | binary_compound | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC, ALGO | ALGO, EMAX, EMIN, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P290_GaP_Geometry_Relax | geometry_relax | semiconductor | relax_semantics | False | policy:ISMEAR | - | - | EDIFF, ISMEAR, NSW | SIGMA, ALGO | ALGO, ISTART, NELMIN | 100.00 | 40.00 | 70.00 | False |
| P291_GaP_Line_Mode_Bands | line_mode_bands | semiconductor | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, LOPTICS | 0.00 | 0.00 | 0.00 | False |
| P292_GaP_DOS_NSCF | dos_nscf | semiconductor | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC, ALGO | ALGO, LORBIT, NELMIN | 0.00 | 0.00 | 0.00 | False |
| P293_CdTe_Static_SCF | static_scf | semiconductor | semiconductor_smearing | True | - | - | - | - | ALGO, LREAL | ALGO, ISTART | 100.00 | 100.00 | 100.00 | False |
| P294_CdTe_Geometry_Relax | geometry_relax | semiconductor | relax_semantics | True | - | - | - | - | ALGO | ALGO | 100.00 | 100.00 | 100.00 | False |
| P295_CdTe_Line_Mode_Bands | line_mode_bands | semiconductor | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, LREAL | ISTART, KSPACING, LOPTICS | 0.00 | 0.00 | 0.00 | False |
| P296_CdTe_DOS_NSCF | dos_nscf | semiconductor | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC, ALGO | ALGO, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P297_Si_Geometry_Relax | geometry_relax | semiconductor | relax_semantics | True | - | - | - | - | ALGO | ALGO, ISTART | 100.00 | 100.00 | 100.00 | False |
| P298_Si_DOS_NSCF | dos_nscf | semiconductor | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC, ALGO | ALGO, ISTART | 0.00 | 0.00 | 0.00 | False |
| P299_AlN_Static_SCF | static_scf | semiconductor | semiconductor_smearing | False | semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, NSW | EDIFF, ENCUT, ISMEAR, SIGMA | PREC, ALGO, LREAL | ALGO | 0.00 | 0.00 | 0.00 | False |
| P29_ZnSe_Static_SCF | static_scf | binary_compound | semiconductor_smearing | True | - | - | - | ENCUT | ALGO, LREAL | ALGO, ISTART, KSPACING, NELMIN | 100.00 | 75.00 | 87.50 | False |
| P300_AlN_Line_Mode_Bands | line_mode_bands | semiconductor | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, LREAL | ISTART, KSPACING, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P301_AlN_DOS_NSCF | dos_nscf | semiconductor | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC | ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P302_GaAs_Static_SCF | static_scf | semiconductor | semiconductor_smearing | True | - | - | - | ENCUT, SIGMA | ALGO, LREAL | ALGO, LOPTICS | 100.00 | 50.00 | 75.00 | False |
| P303_GaAs_Geometry_Relax | geometry_relax | semiconductor | relax_semantics | True | - | - | - | ENCUT, NSW | SIGMA, ALGO | ALGO, ISTART | 100.00 | 60.00 | 80.00 | False |
| P30_ZnSe_Geometry_Relax | geometry_relax | binary_compound | relax_semantics | True | - | - | - | EDIFFG, NSW | ALGO | ALGO, ISTART, MAXMIX, NPAR | 100.00 | 60.00 | 80.00 | False |
| P31_ZnSe_Line_Mode_Bands | line_mode_bands | binary_compound | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P32_ZnSe_DOS_NSCF | dos_nscf | binary_compound | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC, ALGO | ALGO, ISTART, LOPTICS, LORBIT, NPAR | 0.00 | 0.00 | 0.00 | False |
| P33_TiN_Static_SCF | static_scf | binary_compound | metal_smearing | False | semantic:IBRION | - | IBRION | - | ALGO, LREAL | ALGO, ISTART | 50.00 | 100.00 | 75.00 | False |
| P34_TiN_Geometry_Relax | geometry_relax | binary_compound | relax_semantics | True | - | - | - | - | - | ISTART, NPAR | 100.00 | 100.00 | 100.00 | False |
| P35_TiN_Line_Mode_Bands | line_mode_bands | binary_compound | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, ALGO, LREAL | ALGO, LOPTICS | 0.00 | 0.00 | 0.00 | False |
| P36_TiN_DOS_NSCF | dos_nscf | binary_compound | nscf_workflow | False | semantic:ISYM, semantic:IBRION, semantic:NSW | - | IBRION, ISYM, NSW | - | PREC, ALGO | ALGO, EMAX, EMIN, ISTART, LORBIT, NBANDS | 25.00 | 100.00 | 62.50 | False |
| P37_CoO_Static_SCF | static_scf | transition_metal_oxide | dftu_semantics | False | semantic:IBRION, semantic:NSW, semantic:LDAU, semantic:LDAUTYPE, semantic:LDAUL, policy:LDAUU, policy:LDAUJ | - | IBRION, LDAU, LDAUL, LDAUTYPE, NSW | LASPH, LDAUJ, LDAUU, LMAXMIX | MAGMOM, ALGO, LREAL | ALGO, ISTART, NBANDS, NWRITE | 16.67 | 42.86 | 29.76 | False |
| P38_CoO_Geometry_Relax | geometry_relax | transition_metal_oxide | magnetic_initialization | False | policy:LDAU, policy:LDAUU, policy:LDAUJ | - | - | EDIFFG, LASPH, LDAU, LDAUJ, LDAUU, LMAXMIX, NSW | MAGMOM | ADDGRID, IALGO, KSPACING, NELMIN | 100.00 | 30.00 | 65.00 | False |
| P39_CoO_Line_Mode_Bands | line_mode_bands | transition_metal_oxide | dftu_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LDAU, semantic:LDAUTYPE, semantic:LDAUL, policy:LDAUU, policy:LDAUJ, policy:ISMEAR | - | IBRION, ICHARG, ISYM, LDAU, LDAUL, LDAUTYPE, NSW | EDIFF, ENCUT, ISMEAR, LDAUJ, LDAUU | LASPH, MAGMOM, PREC, LREAL | ISTART | 0.00 | 0.00 | 0.00 | False |
| P40_CoO_DOS_NSCF | dos_nscf | transition_metal_oxide | dftu_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR, policy:LDAU, policy:LDAUU, policy:LDAUJ | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, LDAU, LDAUJ, LDAUU, SIGMA | LASPH, MAGMOM, PREC | AIJ, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P43_FeO_Line_Mode_Bands | line_mode_bands | transition_metal_oxide | dftu_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LDAU, semantic:LDAUTYPE, semantic:LDAUL, policy:LDAUU, policy:LDAUJ, policy:ISMEAR | - | IBRION, ICHARG, ISYM, LDAU, LDAUL, LDAUTYPE, NSW | EDIFF, ENCUT, ISMEAR, LDAUJ, LDAUU | MAGMOM, LASPH, PREC, LREAL | ISTART, LOPTICS, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P44_FeO_DOS_NSCF | dos_nscf | transition_metal_oxide | dftu_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LDAU, semantic:LDAUTYPE, semantic:LDAUL, policy:ISMEAR, policy:LDAUU, policy:LDAUJ | - | IBRION, ICHARG, ISYM, LDAU, LDAUL, LDAUTYPE, NSW | ISMEAR, LDAUJ, LDAUU, SIGMA | MAGMOM, LASPH, PREC, ALGO | ALGO, ISTART, LORBIT, NPAR | 0.00 | 0.00 | 0.00 | False |
| P45_Cr2O3_Static_SCF | static_scf | transition_metal_oxide | dftu_semantics | False | semantic:LDAU, semantic:LDAUTYPE, semantic:LDAUL, policy:LDAUU, policy:LDAUJ | - | LDAU, LDAUL, LDAUTYPE | LASPH, LDAUJ, LDAUU, LMAXMIX | MAGMOM, LREAL | - | 50.00 | 42.86 | 46.43 | False |
| P46_Cr2O3_Geometry_Relax | geometry_relax | transition_metal_oxide | magnetic_initialization | False | policy:LDAU, policy:LDAUU, policy:LDAUJ | - | - | LDAU, LDAUJ, LDAUU, LMAXMIX | MAGMOM, ALGO | ADDGRID, ALGO, GGA, NELMIN | 100.00 | 60.00 | 80.00 | False |
| P47_Cr2O3_Line_Mode_Bands | line_mode_bands | transition_metal_oxide | symmetry_sensitive | False | semantic:ISYM, semantic:IBRION, semantic:NSW | - | IBRION, ISYM, NSW | EDIFF | LASPH, MAGMOM, ALGO, LREAL | ALGO, ISTART, LOPTICS | 25.00 | 66.67 | 45.83 | False |
| P48_Cr2O3_DOS_NSCF | dos_nscf | transition_metal_oxide | dftu_semantics | False | semantic:ISYM, semantic:IBRION, semantic:NSW, policy:LDAU, policy:LDAUU, policy:LDAUJ | - | IBRION, ISYM, NSW | LDAU, LDAUJ, LDAUU | LASPH, MAGMOM, ALGO | ALGO, EMAX, EMIN, ISTART, KPAR, LORBIT, NBANDS | 25.00 | 40.00 | 32.50 | False |
| P49_FeSe_Static_SCF | static_scf | chalcogenide | spin_semantics | False | semantic:ISPIN | - | ISPIN | - | MAGMOM, ALGO, LREAL | ALGO, MAXMIX, NELMIN | 66.67 | 100.00 | 83.33 | False |
| P50_FeSe_Geometry_Relax | geometry_relax | chalcogenide | magnetic_initialization | True | - | - | - | - | MAGMOM, ALGO | ADDGRID, ALGO, NELMIN | 100.00 | 100.00 | 100.00 | False |
| P51_FeSe_Line_Mode_Bands | line_mode_bands | chalcogenide | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | MAGMOM, PREC, LREAL | ISTART, KSPACING, LOPTICS | 0.00 | 0.00 | 0.00 | False |
| P52_FeSe_DOS_NSCF | dos_nscf | chalcogenide | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | MAGMOM, PREC, ALGO | ALGO, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P53_SnSe2_Static_SCF | static_scf | chalcogenide | semiconductor_smearing | True | - | - | - | - | LREAL | - | 100.00 | 100.00 | 100.00 | True |
| P54_SnSe2_Geometry_Relax | geometry_relax | chalcogenide | vdw_semantics | True | - | - | - | - | ALGO | ALGO, KPAR | 100.00 | 100.00 | 100.00 | False |
| P55_SnSe2_Line_Mode_Bands | line_mode_bands | chalcogenide | nscf_workflow | False | semantic:ISYM, semantic:NSW | - | ISYM, NSW | - | ALGO, LREAL | ALGO, ISTART, LORBIT, NEDOS | 50.00 | 100.00 | 75.00 | False |
| P56_SnSe2_DOS_NSCF | dos_nscf | chalcogenide | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC, ALGO | ALGO, ISTART | 0.00 | 0.00 | 0.00 | False |
| P57_Bi2Se3_Static_SCF | static_scf | chalcogenide | soc_semantics | False | semantic:IBRION, semantic:NSW, semantic:LSORBIT, semantic:ISYM | - | IBRION, ISYM, LSORBIT, NSW | SAXIS | ALGO, LREAL | ALGO, ISTART, NBANDS | 0.00 | 80.00 | 40.00 | False |
| P58_Bi2Se3_Geometry_Relax | geometry_relax | chalcogenide | vdw_semantics | True | - | - | - | NSW | ALGO | ALGO, INIWAV, ISTART, KSPACING | 100.00 | 80.00 | 90.00 | False |
| P59_Bi2Se3_Line_Mode_Bands | line_mode_bands | chalcogenide | soc_semantics | False | semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LSORBIT | - | IBRION, ISYM, LSORBIT, NSW | ENCUT, SAXIS | LREAL | ISTART, LOPTICS, NEDOS | 20.00 | 50.00 | 35.00 | False |
| P60_Bi2Se3_DOS_NSCF | dos_nscf | chalcogenide | soc_semantics | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, semantic:LSORBIT, policy:ISMEAR | - | IBRION, ICHARG, ISYM, LSORBIT, NSW | ISMEAR, SAXIS, SIGMA | PREC | ISTART, LORBIT, NBANDS | 0.00 | 0.00 | 0.00 | False |
| P61_WSe2_Static_SCF | static_scf | layered_anisotropic | semiconductor_smearing | False | semantic:IBRION | - | IBRION | - | ALGO, LREAL | ALGO, ISTART | 50.00 | 100.00 | 75.00 | False |
| P62_WSe2_Geometry_Relax | geometry_relax | layered_anisotropic | vdw_semantics | True | - | - | - | NSW | ALGO | ALGO, ISTART, NPAR | 100.00 | 80.00 | 90.00 | False |
| P63_WSe2_Line_Mode_Bands | line_mode_bands | layered_anisotropic | nscf_workflow | False | semantic:ISYM, semantic:IBRION, semantic:NSW | - | IBRION, ISYM, NSW | - | ALGO, LREAL | ALGO, LORBIT, NWRITE | 25.00 | 100.00 | 62.50 | False |
| P64_WSe2_DOS_NSCF | dos_nscf | layered_anisotropic | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC, ALGO | ALGO, ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P65_TiS2_Static_SCF | static_scf | layered_anisotropic | metal_smearing | True | - | - | - | - | ALGO, LREAL | ALGO, STATIC | 100.00 | 100.00 | 100.00 | False |
| P66_TiS2_Geometry_Relax | geometry_relax | layered_anisotropic | vdw_semantics | True | - | - | - | NSW | ALGO | ALGO, ISTART, KPAR, NPAR, POTIM | 100.00 | 80.00 | 90.00 | False |
| P67_TiS2_Line_Mode_Bands | line_mode_bands | layered_anisotropic | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | EDIFF, ENCUT, ISMEAR | PREC, LREAL | ISTART, LORBIT | 0.00 | 0.00 | 0.00 | False |
| P68_TiS2_DOS_NSCF | dos_nscf | layered_anisotropic | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | PREC, ALGO | ALGO, ISTART, LOPTICS | 0.00 | 0.00 | 0.00 | False |
| P69_NbSe2_Static_SCF | static_scf | layered_anisotropic | spin_semantics | False | semantic:ISPIN, semantic:IBRION, semantic:NSW | - | IBRION, ISPIN, NSW | - | MAGMOM, ALGO, LREAL | ALGO | 0.00 | 100.00 | 50.00 | False |
| P70_NbSe2_Geometry_Relax | geometry_relax | layered_anisotropic | vdw_semantics | False | semantic:ISPIN | - | ISPIN | - | MAGMOM, ALGO | ALGO | 66.67 | 100.00 | 83.33 | False |
| P71_NbSe2_Line_Mode_Bands | line_mode_bands | layered_anisotropic | nscf_workflow | False | semantic:ISYM, policy:ISMEAR | - | ISYM | EDIFF, ISMEAR | MAGMOM, ALGO, LREAL | ALGO, LOPTICS, LORBIT | 75.00 | 33.33 | 54.17 | False |
| P72_NbSe2_DOS_NSCF | dos_nscf | layered_anisotropic | nscf_workflow | False | workflow:ICHARG, semantic:ICHARG, semantic:ISYM, semantic:IBRION, semantic:NSW, policy:ISMEAR | - | IBRION, ICHARG, ISYM, NSW | ISMEAR, SIGMA | MAGMOM, PREC, ALGO | ALGO, ISTART, LOPTICS | 0.00 | 0.00 | 0.00 | False |
| P73_SrTiO3_Static_SCF | static_scf | perovskite_multinary_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P74_SrTiO3_Geometry_Relax | geometry_relax | perovskite_multinary_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P75_SrTiO3_Line_Mode_Bands | line_mode_bands | perovskite_multinary_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P76_SrTiO3_DOS_NSCF | dos_nscf | perovskite_multinary_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P77_LaMnO3_Static_SCF | static_scf | perovskite_multinary_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P78_LaMnO3_Geometry_Relax | geometry_relax | perovskite_multinary_oxide | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P79_LaMnO3_Line_Mode_Bands | line_mode_bands | perovskite_multinary_oxide | symmetry_sensitive | None | - | - | - | - | - | - | - | - | - | None |
| P80_LaMnO3_DOS_NSCF | dos_nscf | perovskite_multinary_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P81_BaZrO3_Static_SCF | static_scf | perovskite_multinary_oxide | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P82_BaZrO3_Geometry_Relax | geometry_relax | perovskite_multinary_oxide | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P83_BaZrO3_Line_Mode_Bands | line_mode_bands | perovskite_multinary_oxide | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P84_BaZrO3_DOS_NSCF | dos_nscf | perovskite_multinary_oxide | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P85_LiFePO4_Static_SCF | static_scf | battery_material | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P86_LiFePO4_Geometry_Relax | geometry_relax | battery_material | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P87_LiFePO4_Line_Mode_Bands | line_mode_bands | battery_material | symmetry_sensitive | None | - | - | - | - | - | - | - | - | - | None |
| P88_LiFePO4_DOS_NSCF | dos_nscf | battery_material | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P89_LiCoO2_Static_SCF | static_scf | battery_material | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P90_LiCoO2_Geometry_Relax | geometry_relax | battery_material | vdw_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P91_LiCoO2_Line_Mode_Bands | line_mode_bands | battery_material | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P92_LiCoO2_DOS_NSCF | dos_nscf | battery_material | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P93_YMn2O5_Static_SCF | static_scf | complex_low_symmetry | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P94_YMn2O5_Geometry_Relax | geometry_relax | complex_low_symmetry | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P95_YMn2O5_Line_Mode_Bands | line_mode_bands | complex_low_symmetry | symmetry_sensitive | None | - | - | - | - | - | - | - | - | - | None |
| P96_YMn2O5_DOS_NSCF | dos_nscf | complex_low_symmetry | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P97_Bi2WO6_Static_SCF | static_scf | complex_low_symmetry | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P98_Bi2WO6_Geometry_Relax | geometry_relax | complex_low_symmetry | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P99_Bi2WO6_Line_Mode_Bands | line_mode_bands | complex_low_symmetry | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |

### gpt-4o-vasp.skill

| Case | Task | Material | Challenge | Minimum Runnable | Runnable Failure Reasons | Imputed Defaults | Missing Semantic | Missing Policy | Optional Miss | Extra Keys | Semantic | Policy | Must | Perfect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01_Si_Static_SCF | static_scf | semiconductor | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P02_GaAs_Line_Mode_Bands | line_mode_bands | semiconductor | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P03_Fe_Static_Magnetic | static_scf | magnetic_metal | spin_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P04_LiF_Geometry_Relax | geometry_relax | ionic_insulator | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P05_AlN_Geometry_Relax | geometry_relax | semiconductor | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P06_Si_Line_Mode_Bands | line_mode_bands | semiconductor | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P07_GaAs_DOS_NSCF | dos_nscf | semiconductor | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P08_TiO2_Static_DFTU | static_scf | oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P09_FeO_Static_DFTU_Spin | static_scf | correlated_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P100_Bi2WO6_DOS_NSCF | dos_nscf | complex_low_symmetry | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P101_NiO_Static_SCF | static_scf | correlated_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P102_NiO_Geometry_Relax | geometry_relax | correlated_oxide | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P103_NiO_Line_Mode_Bands | line_mode_bands | correlated_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P104_NiO_DOS_NSCF | dos_nscf | correlated_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P105_Bi2Te3_Static_SCF | static_scf | heavy_element_semiconductor | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P106_Bi2Te3_Geometry_Relax | geometry_relax | heavy_element_semiconductor | vdw_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P107_Bi2Te3_Line_Mode_Bands | line_mode_bands | heavy_element_semiconductor | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P108_Bi2Te3_DOS_NSCF | dos_nscf | heavy_element_semiconductor | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P109_NaCl_Static_SCF | static_scf | ionic_insulator | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P10_MoS2_Relax_vdW | geometry_relax | layered_material | vdw_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P110_NaCl_Geometry_Relax | geometry_relax | ionic_insulator | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P111_NaCl_Line_Mode_Bands | line_mode_bands | ionic_insulator | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P112_NaCl_DOS_NSCF | dos_nscf | ionic_insulator | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P113_C_Static_SCF | static_scf | layered_material | metal_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P114_C_Geometry_Relax | geometry_relax | layered_material | vdw_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P115_C_Line_Mode_Bands | line_mode_bands | layered_material | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P116_C_DOS_NSCF | dos_nscf | layered_material | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P117_Co_Static_SCF | static_scf | magnetic_metal | spin_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P118_Co_Geometry_Relax | geometry_relax | magnetic_metal | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P119_Co_Line_Mode_Bands | line_mode_bands | magnetic_metal | spin_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P11_InSb_Static_SOC | static_scf | heavy_element_semiconductor | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P120_Co_DOS_NSCF | dos_nscf | magnetic_metal | spin_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P121_Au_Static_SCF | static_scf | metal | metal_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P122_Au_Geometry_Relax | geometry_relax | metal | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P123_Au_Line_Mode_Bands | line_mode_bands | metal | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P124_Au_DOS_NSCF | dos_nscf | metal | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P125_ZrO2_Static_SCF | static_scf | oxide | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P126_ZrO2_Geometry_Relax | geometry_relax | oxide | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P127_ZrO2_Line_Mode_Bands | line_mode_bands | oxide | symmetry_sensitive | None | - | - | - | - | - | - | - | - | - | None |
| P128_ZrO2_DOS_NSCF | dos_nscf | oxide | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P129_InP_Static_SCF | static_scf | semiconductor | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P12_VO2_Static_Symmetry | static_scf | correlated_oxide | symmetry_sensitive | None | - | - | - | - | - | - | - | - | - | None |
| P130_InP_Geometry_Relax | geometry_relax | semiconductor | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P131_InP_Line_Mode_Bands | line_mode_bands | semiconductor | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P132_InP_DOS_NSCF | dos_nscf | semiconductor | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P13_Cu_Static_SCF | static_scf | elemental | metal_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P14_Cu_Geometry_Relax | geometry_relax | elemental | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P15_Cu_Line_Mode_Bands | line_mode_bands | elemental | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P16_Cu_DOS_NSCF | dos_nscf | elemental | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P17_W_Static_SCF | static_scf | elemental | metal_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P18_W_Geometry_Relax | geometry_relax | elemental | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P19_W_Line_Mode_Bands | line_mode_bands | elemental | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P206_FeO_Geometry_Relax | geometry_relax | correlated_oxide | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P20_W_DOS_NSCF | dos_nscf | elemental | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P210_VO2_Geometry_Relax | geometry_relax | correlated_oxide | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P211_VO2_Line_Mode_Bands | line_mode_bands | correlated_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P212_VO2_DOS_NSCF | dos_nscf | correlated_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P214_InSb_Geometry_Relax | geometry_relax | heavy_element_semiconductor | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P215_InSb_Line_Mode_Bands | line_mode_bands | heavy_element_semiconductor | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P216_InSb_DOS_NSCF | dos_nscf | heavy_element_semiconductor | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P21_Te_Static_SCF | static_scf | elemental | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P221_PbSe_Static_SCF | static_scf | heavy_element_semiconductor | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P222_PbSe_Geometry_Relax | geometry_relax | heavy_element_semiconductor | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P223_PbSe_Line_Mode_Bands | line_mode_bands | heavy_element_semiconductor | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P224_PbSe_DOS_NSCF | dos_nscf | heavy_element_semiconductor | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P225_LiF_Static_SCF | static_scf | ionic_insulator | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P227_LiF_Line_Mode_Bands | line_mode_bands | ionic_insulator | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P228_LiF_DOS_NSCF | dos_nscf | ionic_insulator | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P22_Te_Geometry_Relax | geometry_relax | elemental | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P233_KCl_Static_SCF | static_scf | ionic_insulator | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P234_KCl_Geometry_Relax | geometry_relax | ionic_insulator | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P235_KCl_Line_Mode_Bands | line_mode_bands | ionic_insulator | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P236_KCl_DOS_NSCF | dos_nscf | ionic_insulator | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P237_MoS2_Static_SCF | static_scf | layered_material | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P239_MoS2_Line_Mode_Bands | line_mode_bands | layered_material | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P23_Te_Line_Mode_Bands | line_mode_bands | elemental | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P240_MoS2_DOS_NSCF | dos_nscf | layered_material | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P245_BN_Static_SCF | static_scf | layered_material | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P246_BN_Geometry_Relax | geometry_relax | layered_material | vdw_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P247_BN_Line_Mode_Bands | line_mode_bands | layered_material | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P248_BN_DOS_NSCF | dos_nscf | layered_material | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P24_Te_DOS_NSCF | dos_nscf | elemental | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P250_Fe_Geometry_Relax | geometry_relax | magnetic_metal | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P251_Fe_Line_Mode_Bands | line_mode_bands | magnetic_metal | spin_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P252_Fe_DOS_NSCF | dos_nscf | magnetic_metal | spin_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P257_Ni_Static_SCF | static_scf | magnetic_metal | spin_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P258_Ni_Geometry_Relax | geometry_relax | magnetic_metal | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P259_Ni_Line_Mode_Bands | line_mode_bands | magnetic_metal | spin_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P25_BP_Static_SCF | static_scf | binary_compound | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P260_Ni_DOS_NSCF | dos_nscf | magnetic_metal | spin_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P261_Al_Static_SCF | static_scf | metal | metal_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P262_Al_Geometry_Relax | geometry_relax | metal | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P263_Al_Line_Mode_Bands | line_mode_bands | metal | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P264_Al_DOS_NSCF | dos_nscf | metal | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P269_Pt_Static_SCF | static_scf | metal | metal_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P26_BP_Geometry_Relax | geometry_relax | binary_compound | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P270_Pt_Geometry_Relax | geometry_relax | metal | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P271_Pt_Line_Mode_Bands | line_mode_bands | metal | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P272_Pt_DOS_NSCF | dos_nscf | metal | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P274_TiO2_Geometry_Relax | geometry_relax | oxide | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P275_TiO2_Line_Mode_Bands | line_mode_bands | oxide | symmetry_sensitive | None | - | - | - | - | - | - | - | - | - | None |
| P276_TiO2_DOS_NSCF | dos_nscf | oxide | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P27_BP_Line_Mode_Bands | line_mode_bands | binary_compound | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P281_HfO2_Static_SCF | static_scf | oxide | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P282_HfO2_Geometry_Relax | geometry_relax | oxide | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P283_HfO2_Line_Mode_Bands | line_mode_bands | oxide | symmetry_sensitive | None | - | - | - | - | - | - | - | - | - | None |
| P284_HfO2_DOS_NSCF | dos_nscf | oxide | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P289_GaP_Static_SCF | static_scf | semiconductor | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P28_BP_DOS_NSCF | dos_nscf | binary_compound | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P290_GaP_Geometry_Relax | geometry_relax | semiconductor | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P291_GaP_Line_Mode_Bands | line_mode_bands | semiconductor | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P292_GaP_DOS_NSCF | dos_nscf | semiconductor | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P293_CdTe_Static_SCF | static_scf | semiconductor | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P294_CdTe_Geometry_Relax | geometry_relax | semiconductor | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P295_CdTe_Line_Mode_Bands | line_mode_bands | semiconductor | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P296_CdTe_DOS_NSCF | dos_nscf | semiconductor | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P297_Si_Geometry_Relax | geometry_relax | semiconductor | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P298_Si_DOS_NSCF | dos_nscf | semiconductor | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P299_AlN_Static_SCF | static_scf | semiconductor | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P29_ZnSe_Static_SCF | static_scf | binary_compound | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P300_AlN_Line_Mode_Bands | line_mode_bands | semiconductor | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P301_AlN_DOS_NSCF | dos_nscf | semiconductor | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P302_GaAs_Static_SCF | static_scf | semiconductor | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P303_GaAs_Geometry_Relax | geometry_relax | semiconductor | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P30_ZnSe_Geometry_Relax | geometry_relax | binary_compound | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P31_ZnSe_Line_Mode_Bands | line_mode_bands | binary_compound | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P32_ZnSe_DOS_NSCF | dos_nscf | binary_compound | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P33_TiN_Static_SCF | static_scf | binary_compound | metal_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P34_TiN_Geometry_Relax | geometry_relax | binary_compound | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P35_TiN_Line_Mode_Bands | line_mode_bands | binary_compound | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P36_TiN_DOS_NSCF | dos_nscf | binary_compound | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P37_CoO_Static_SCF | static_scf | transition_metal_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P38_CoO_Geometry_Relax | geometry_relax | transition_metal_oxide | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P39_CoO_Line_Mode_Bands | line_mode_bands | transition_metal_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P40_CoO_DOS_NSCF | dos_nscf | transition_metal_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P43_FeO_Line_Mode_Bands | line_mode_bands | transition_metal_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P44_FeO_DOS_NSCF | dos_nscf | transition_metal_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P45_Cr2O3_Static_SCF | static_scf | transition_metal_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P46_Cr2O3_Geometry_Relax | geometry_relax | transition_metal_oxide | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P47_Cr2O3_Line_Mode_Bands | line_mode_bands | transition_metal_oxide | symmetry_sensitive | None | - | - | - | - | - | - | - | - | - | None |
| P48_Cr2O3_DOS_NSCF | dos_nscf | transition_metal_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P49_FeSe_Static_SCF | static_scf | chalcogenide | spin_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P50_FeSe_Geometry_Relax | geometry_relax | chalcogenide | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P51_FeSe_Line_Mode_Bands | line_mode_bands | chalcogenide | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P52_FeSe_DOS_NSCF | dos_nscf | chalcogenide | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P53_SnSe2_Static_SCF | static_scf | chalcogenide | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P54_SnSe2_Geometry_Relax | geometry_relax | chalcogenide | vdw_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P55_SnSe2_Line_Mode_Bands | line_mode_bands | chalcogenide | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P56_SnSe2_DOS_NSCF | dos_nscf | chalcogenide | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P57_Bi2Se3_Static_SCF | static_scf | chalcogenide | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P58_Bi2Se3_Geometry_Relax | geometry_relax | chalcogenide | vdw_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P59_Bi2Se3_Line_Mode_Bands | line_mode_bands | chalcogenide | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P60_Bi2Se3_DOS_NSCF | dos_nscf | chalcogenide | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P61_WSe2_Static_SCF | static_scf | layered_anisotropic | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P62_WSe2_Geometry_Relax | geometry_relax | layered_anisotropic | vdw_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P63_WSe2_Line_Mode_Bands | line_mode_bands | layered_anisotropic | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P64_WSe2_DOS_NSCF | dos_nscf | layered_anisotropic | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P65_TiS2_Static_SCF | static_scf | layered_anisotropic | metal_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P66_TiS2_Geometry_Relax | geometry_relax | layered_anisotropic | vdw_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P67_TiS2_Line_Mode_Bands | line_mode_bands | layered_anisotropic | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P68_TiS2_DOS_NSCF | dos_nscf | layered_anisotropic | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P69_NbSe2_Static_SCF | static_scf | layered_anisotropic | spin_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P70_NbSe2_Geometry_Relax | geometry_relax | layered_anisotropic | vdw_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P71_NbSe2_Line_Mode_Bands | line_mode_bands | layered_anisotropic | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P72_NbSe2_DOS_NSCF | dos_nscf | layered_anisotropic | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P73_SrTiO3_Static_SCF | static_scf | perovskite_multinary_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P74_SrTiO3_Geometry_Relax | geometry_relax | perovskite_multinary_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P75_SrTiO3_Line_Mode_Bands | line_mode_bands | perovskite_multinary_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P76_SrTiO3_DOS_NSCF | dos_nscf | perovskite_multinary_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P77_LaMnO3_Static_SCF | static_scf | perovskite_multinary_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P78_LaMnO3_Geometry_Relax | geometry_relax | perovskite_multinary_oxide | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P79_LaMnO3_Line_Mode_Bands | line_mode_bands | perovskite_multinary_oxide | symmetry_sensitive | None | - | - | - | - | - | - | - | - | - | None |
| P80_LaMnO3_DOS_NSCF | dos_nscf | perovskite_multinary_oxide | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P81_BaZrO3_Static_SCF | static_scf | perovskite_multinary_oxide | semiconductor_smearing | None | - | - | - | - | - | - | - | - | - | None |
| P82_BaZrO3_Geometry_Relax | geometry_relax | perovskite_multinary_oxide | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P83_BaZrO3_Line_Mode_Bands | line_mode_bands | perovskite_multinary_oxide | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P84_BaZrO3_DOS_NSCF | dos_nscf | perovskite_multinary_oxide | nscf_workflow | None | - | - | - | - | - | - | - | - | - | None |
| P85_LiFePO4_Static_SCF | static_scf | battery_material | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P86_LiFePO4_Geometry_Relax | geometry_relax | battery_material | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P87_LiFePO4_Line_Mode_Bands | line_mode_bands | battery_material | symmetry_sensitive | None | - | - | - | - | - | - | - | - | - | None |
| P88_LiFePO4_DOS_NSCF | dos_nscf | battery_material | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P89_LiCoO2_Static_SCF | static_scf | battery_material | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P90_LiCoO2_Geometry_Relax | geometry_relax | battery_material | vdw_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P91_LiCoO2_Line_Mode_Bands | line_mode_bands | battery_material | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P92_LiCoO2_DOS_NSCF | dos_nscf | battery_material | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P93_YMn2O5_Static_SCF | static_scf | complex_low_symmetry | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P94_YMn2O5_Geometry_Relax | geometry_relax | complex_low_symmetry | magnetic_initialization | None | - | - | - | - | - | - | - | - | - | None |
| P95_YMn2O5_Line_Mode_Bands | line_mode_bands | complex_low_symmetry | symmetry_sensitive | None | - | - | - | - | - | - | - | - | - | None |
| P96_YMn2O5_DOS_NSCF | dos_nscf | complex_low_symmetry | dftu_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P97_Bi2WO6_Static_SCF | static_scf | complex_low_symmetry | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P98_Bi2WO6_Geometry_Relax | geometry_relax | complex_low_symmetry | relax_semantics | None | - | - | - | - | - | - | - | - | - | None |
| P99_Bi2WO6_Line_Mode_Bands | line_mode_bands | complex_low_symmetry | soc_semantics | None | - | - | - | - | - | - | - | - | - | None |
