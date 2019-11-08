#!/bin/bash

function ssh_nocheck {
    ssh -o 'StrictHostKeyChecking=no' -o 'UserKnownHostsFile=/dev/null' "$@"
}

function find_port {
    awk -vLOOKUPVAL=$1 '$1 == LOOKUPVAL { print $2 }' < $(dirname "$0")/slurm_config
}

function find_all {
    awk -vLOOKUPVAL=$1 '$1 == LOOKUPVAL { print $2 " " $3 " " $4 }' < $(dirname "$0")/slurm_config
}
