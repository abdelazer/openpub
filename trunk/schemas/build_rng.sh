#!/bin/sh
for RNC in opds_*.rnc; do
  RNG=`basename "$RNC" .rnc`.rng
  echo "Converting $RNC to $RNG"
  trang -I rnc -O rng "$RNC" "$RNG"
done
