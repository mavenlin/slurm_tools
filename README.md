# Slurm Tools

## Prerequisites

As for now these are hard coded.

Make sure you have the following directories on the cluster
- `~/project/run/tar`
- `~/project/run/untar`
- `~/project/run/tensorboard`

Make sure you have the python virtualenv set up at `~/tf2` on the cluster

## Install

```bash
pip install git+https://github.com/mavenlin/slurm_tools.git@master#egg=slurm_tools
```

## Config

Copy `slurm_config` file to your local `~/.slurm_config`, modify it accordingly with your username and add your clusters.
The five columns means `name`, `local_port`, `hostname`, `remote_port`, `username` respectively. `remote_port` is the sshd port (usually 22) for the access node of the cluster.
The scripts will open a connection in the background using
```bash
ssh -p remote_port -L local_port:localhost:remote_port username@hostname
```
Once the connection is established, the rest of the scripts will connect through `localhost:local_port`

## Commands

To activate the commands, run
```bash
source slurm_tools
```
This will create alias to commands with the cluster name in your `slurm_config` file.


To submit a job from local (replace beluga with the cluster name listed in `~/.slurm_config`)
```bash
beluga submit --job-name "job_name" --mem 16G --other-slurm-options program_to_run --program-options
```
What happens behind the scene is the `slurm_pack` script will pack the current repo under which you run the command into a tarball. Convert the options into a sbatch script and pack together into the tarball, unpack remotely and submit a job.

To grep the jobs
```bash
beluga grep "job_name_pattern"
```
Specify `job_name_pattern` as you would do with `grep` command


To run tensorboard on the jobs, pipe the greped job to the `tb` command,
it will gather by softlinking all the folders to one place and launch the tensorboard.
It will also setup all the port forwardings necessary and open the link in your browser.
Sending `Ctrl-C` will kill the remote tensorboard processes/jobs
```bash
beluga grep "job_name_pattern" | beluga tb "cluster_name"
```

To clean up the tensorboard softlinks
```bash
beluga clear_tb
```
