
default:
  just --list

start_datasites nsites="3":
    for i in {1..{{nsites}}}; do echo $i; done