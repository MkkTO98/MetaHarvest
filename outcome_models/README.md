# Outcome Models

Outcome models explain how ArchitectureHarvest converts adoption history into future recommendation weight.

They do not use opaque scores. Each recommendation must distinguish:

- generic recommendation based on external/project evidence
- ecosystem-weighted recommendation based on ProjectForge/MacroForge/generated-project outcomes

Patterns that repeatedly succeed locally gain weight. Patterns that repeatedly fail, create excessive maintenance, or add complexity lose weight and may produce rejection or retirement records.
