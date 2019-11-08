# Slurm Tools

## Prerequisites

As for now these are hard coded.

Make sure you have the following directories on the cluster
- `~/project/run/tar`
- `~/project/run/untar`
- `~/project/run/tensorboard`

Make sure you have the python virtualenv set up at `~/tf2` on the cluster

## Commands

To submit a job from local
```bash
slurm submit "cluster_name" --job-name "job_name" --mem 16G --other-slurm-options program_to_run --program-options
```
What happens behind the scene is the `slurm_pack` script will pack the current repo under which you run the command into a tarball. Convert the options into a sbatch script and pack together into the tarball, unpack remotely and submit a job.

To grep the jobs
```bash
slurm grep "cluster_name" "job_name_pattern"
```

To run tensorboard on the jobs, pipe the greped job to the `tb` command, 
it will gather by softlinking all the folders to one place and launch the tensorboard. 
It will also setup all the port forwardings necessary and open the link in your browser.
Sending `Ctrl-C` will kill the remote tensorboard processes/jobs
```bash
slurm grep "cluster_name" "job_name_pattern" | tb "cluster_name"
```

To clean up the tensorboard softlinks
```bash
clear_tb "cluster_name"
```

To config the clusters, edit `slurm_config` file, the four columns means
`name`, `local_port`, `hostname`, `remote_port` respectively. `remote_port` is the sshd port (usually 22) for the access node of the cluster.
The scripts will open a connection in the background using
```bash
ssh -L local_port:localhost:remote_port hostname
```
Once the connection is established, the rest of the scripts will connect through `localhost:local_port`

