#!/bin/bash
# build_fractals.sh
# Automates the generation and compilation of fractals for The Visibilities

set -e

# Default settings
RES=300
MODE="smooth"
SCALE=1.0

echo "=== The Visibilities: Fractal Compilation Suite ==="

# 1. Generate Heptabrot
echo "Generating Heptabrot (power 7)..."
texlua generate_fractal.lua -p 7 -o heptabrot.mp -r $RES -m $MODE -s $SCALE

# 2. Generate Octabrot
echo "Generating Octabrot (power 8)..."
texlua generate_fractal.lua -p 8 -o octabrot.mp -r $RES -m $MODE -s $SCALE

# 3. Compile with MetaPost
echo "Compiling MetaPost files..."
mpost heptabrot.mp
mpost octabrot.mp

# 4. Convert to PDF
echo "Converting to PDF format..."
mptopdf heptabrot.mps
mptopdf octabrot.mps
cp heptabrot-mps.pdf heptabrot.pdf
cp octabrot-mps.pdf octabrot.pdf

echo "=== Compilation Complete! ==="
echo "Generated files:"
echo "  - heptabrot.pdf (Heptabrot figure)"
echo "  - octabrot.pdf (Octabrot figure)"
