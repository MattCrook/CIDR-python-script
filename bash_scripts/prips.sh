#!/bin/bash

prips() {
  local cidr=$1 ; local lo hi a b c d e f g h
  # range is bounded by network (-n) & broadcast (-b) addresses.
  lo=$(ipcalc -n "$cidr" | cut -f2 -d=)
  hi=$(ipcalc -b "$cidr" | cut -f2 -d=)
  IFS=. read -r a b c d <<< "$lo"
  IFS=. read -r e f g h <<< "$hi"
  eval "echo {$a..$e}.{$b..$f}.{$c..$g}.{$d..$h}"
}
