#!/bin/bash

source /cvmfs/lhcb.cern.ch/group_login.sh
/cvmfs/lhcb.cern.ch/lib/lhcb/LBSCRIPTS/LBSCRIPTS_v7r10p4/InstallArea/scripts/SetupProject.sh DaVinci
SetupProject.sh DaVinci

RAPIDFITROOT=/Home/gcowan1/software/RapidFit/trunk
RAPIDFITROOTTMP=/Home/gcowan1/software/tmp/trunk
BC=/Home/gcowan1/lhcb/lhcb/b2cc/analysis/phi_s/3fb/toy/angle_time_correlation
CONFIG1=$BC/untagged_gen.xml
CONFIG2=$BC/untagged_fit.xml

myID=`hostid`_$RANDOM
workdir=/tmp/${myID}
mkdir -p $workdir
echo "Workdir "$workdir
cd $workdir

$RAPIDFITROOTTMP/bin/fitting -f $CONFIG1 --saveOneDataSet test.root --useUUID
$RAPIDFITROOT/bin/fitting -f $CONFIG2 --doPulls pulls.root --OutputLevel 1

datadir=$BC/data/
mkdir -p $datadir
cd $datadir

cp -f  $workdir/pulls.root ${myID}_pulls.root
#rm -rf $workdir
