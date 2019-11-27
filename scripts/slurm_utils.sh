#!/bin/bash

function ssh_nocheck {
    ssh -o 'StrictHostKeyChecking=no' -o 'UserKnownHostsFile=/dev/null' "$@"
}

function find_port {
    awk -v LOOKUPVAL=$1 '$1 == LOOKUPVAL { print $2 }' < ~/.slurm_config
}

function find_user {
    awk -v LOOKUPVAL=$1 '$1 == LOOKUPVAL { print $5 }' < ~/.slurm_config
}

function find_all {
    awk -v LOOKUPVAL=$1 '$1 == LOOKUPVAL { print $2 " " $3 " " $4 " " $5 }' < ~/.slurm_config
}
