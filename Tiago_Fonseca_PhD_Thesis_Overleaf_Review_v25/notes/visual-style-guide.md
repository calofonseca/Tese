# Visual Style and Evidence Guide

The thesis should use visuals as part of the argument, not as decoration.

## Diagram families

- **Architecture/context diagrams:** stable layers, boundaries, responsibilities, and contracts; avoid class-level implementation detail in the main chapters.
- **Sequence/timeline diagrams:** show order, actors, failure points, manual approvals, and recovery; use these for lifecycle and operational evidence.
- **Formal/method diagrams:** notation must match equations exactly; separate deterministic mechanisms from learned mechanisms.
- **Experimental-design diagrams:** show manipulated variables, controls, baselines, seeds, and evidence levels before presenting results.
- **Result plots:** one claim per panel; include uncertainty and relevant baselines; identify oracle/perfect-information methods explicitly.
- **Photographs/screenshots:** use only to prove physical integration or operator/runtime behaviour. Pair screenshots with underlying data and describe what the image proves.

## Recommended production format

- Conceptual diagrams: TikZ, draw.io, Inkscape, or vector PDF/SVG exported with embedded fonts.
- Plots: scripted generation from archived CSV/Parquet/JSON results; save both vector PDF and the source script/data manifest.
- Photos: high-resolution JPEG/PNG with metadata/permission record; crop only for relevance and do not reveal personal or confidential information.
- UI screenshots: capture at consistent resolution, anonymise identifiers, add callouts sparingly, and keep the full underlying log/result in the repository.
