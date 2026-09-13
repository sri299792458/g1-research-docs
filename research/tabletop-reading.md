# Tabletop and prototype source reading

Source: `g1-dex3-tabletop/running_notes.md`, 7,403 lines, SHA-256
`9b159c235fd6fdb086249d9025c3083f439292fe3a884c6f6ae4ffcfddcc3d91`.
Reading began 2026-09-13. This records source-reported evidence; no hardware
experiments are being repeated. Later calibration-ledger corrections govern.

## Coverage

- Complete: lines 1–7,403 read sequentially on 2026-09-13.
- Prototype lines 2–1,864 are byte-identical to tabletop lines 359–2,221;
  reading that shared block covers the complete prototype log except its title.
  These are one history, not independent experiments.

## Findings through line 2,290

- The log is not chronological: August 13/16 work precedes inherited August
  1–12 prototype material. Distinguish dates from file order.
- The prototype grew explicit measured-state acquisition, bounded joint replay,
  stationary capture, immutable raw sessions, corner-level residuals, grouped
  holdouts, and hash-bound route approvals. Early zero-weight emergency release
  and 50 ms immediate faults were subsequently replaced; do not use them as the
  current recovery procedure.
- Reuse of Unitree XR meant an attributed, narrow adapter, not instantiating its
  eager zero-target publisher. G1Pilot Cartesian OpenSoT was deliberately kept
  out of the discrete calibration runtime.
- Actual Ready FSM is 4, not an assumed 500; vendor mode 5 does not itself say
  that the physical waist is free. Image pairing uses measured joints, never
  commanded target vectors. Rectified pixels require P, not raw K.
- Manual GUIDE/HOLD teaching has supported/held seven-frame bursts. The
  operator's hand must be removed only after HOLD is active. This is a
  historical commissioned route, not a promise of certified freedrive.
- Printed rounded 40 mm AprilCube provenance: July 14, 3 mm perimeter radius,
  six 30 mm 4x4_100 markers IDs 0–5. Sharp/rounded tag coordinates identical.
  Early rigid dummy-palm tape choices were revised to test the already purchased
  foam tape using repeated anchors; do not prescribe an abandoned clamshell.
- Calibration detector uses only decoded current-frame corners. Tracking,
  optical flow, recovered quads, or filtered poses cannot silently enter fits.
- manual_run_001: 39 observations/273 frames; native extrinsics 8.205 px,
  shoulder-roll effective correction +4.346 degrees gives 4.875 px; all offsets
  4.363 px. Capture 028 was user-confirmed stream lag, not proof of compliance.
  Its omission barely changes the shoulder correction. Physical cause unproven.
- Torso ChArUco fixture went through several CAD designs, none established here
  as a physically qualified torso calibration standard. Final v4: one H2D
  multicolor carrier plus four arms, 5x5_50, 6x9 squares 30/22 mm. Old 4x4 PDF
  and v0 obstructed screw-access design are superseded. Root fit, engagement,
  flatness and reinstall repeatability were still release gates.
- Dex3 dorsal marker final revision 2: 50x60x4 mm carrier, 40 mm 6x6_50 marker,
  right ID4 / left ID5, 15 mm M3 hole spacing, M3x8, third support corrected
  after actual first-print flex. Left dorsal is +palm-Y, right -palm-Y; copying
  right transform made left targets invisible. Preserve proper rotations.
- August 12 bilateral middle-close commissioning physically passed, 22.5 mm
  minimum modeled clearance. Failed candidate_0627 exposed omitted shoulder/
  torso collision pairs; old 100-target plan unusable. Finite 80-target plans
  replaced repeated backup sorties. Rejections are retained, not erased.
- PNG/JSON/fsync moved to a prewarmed writer process after scheduler interference.
  Later independent 51 ms pause showed writer isolation alone cannot promise
  real-time Linux. Fixed 4 ms motion increments prevent catch-up jumps; local
  250 ms hard fault plus independent 500 ms PC2 heartbeat replaced 50 ms rule.
- Right 62-primary marker fit: CAD-fixed 23.045 px holdout vs free 9.737 px;
  effective 13.638 mm/4.621 degree correction is not a mount measurement.
- Focused tabletop repo separates Python ROS/control from GPU CuRobo worker.
  Seven active arm joints + 42 locked coordinates; return paths must connect.
  Batching 1,544 IK candidates in groups of 128 avoided GPU OOM. Named mapping
  fixes DDS versus CuRobo hand order. Planning model is not identified physics.
- A resting cube defines a support plane, not the finite table's registered
  footprint. Right wrist/hand/payload plane checks plus self collision cannot
  certify unobserved elbow/table-edge clearance.
- CUDA failure despite nvidia-smi was cuInit999 and /dev/nvidia-uvm EIO;
  reboot restored the existing environment. No package reinstall was justified.
- Seated takeover starts at all 29 measured joints, with independent PC2
  watchdog and gravity feedforward; restoration 0→1→3 physically verified.
- August 16 cushion vs rigid seat trials completed five lift pairs per arm.
  Rigid measurements ~5.3 mm/0.7–0.8 degrees vs cushion ~10.5 mm/1.4–1.7;
  posture and route differed, so this is not a controlled estimate of cushion
  effect. Rigid seating became the practical baseline.
- Offline hybrid pelvis/waist FK/torso IMU reduces settled apparent drift to
  ~1–1.2 mm on rigid trials; contact-origin assumption is local, not global
  odometry. Producer clocks must map independently to MCAP time. Depth plane
  adds height/tilt but cannot observe in-plane translation/yaw. Continuous
  replay with visual resets is distinct from a deployed estimator.
- GraspGen-X/Quest/HERO discussions are upstream audits, not completed local
  teleoperation or learned-FK deployments. GraspGen-X's exact G1 calibration is
  unpublished; fiducials visible in a video do not establish their algorithm.

## Findings from lines 2,291–4,940

- Runtime object contract changed from mismatched 45 mm AprilTag cube to the
  actual 40 mm rounded 4x4_100 cube; poses were regenerated, not rescaled.
  Later 60 mm R3 profiles have 45 mm markers IDs10–15 and IDs20–25. All bind
  mesh, detection geometry and shortlist hashes. Cube symmetry permits any
  face up via canonicalization; an old tag132-up requirement is obsolete.
- Initial 15/3,178 grasps were free-object PhysX-qualified but relied on cube
  motion during closing. Physical run190430 reached the intended grasp within
  3.61 mm/2.99 degrees, then stalled against an inappropriate simulated joint
  endpoint. Descriptor close is a fixed command; achieved simulated q is evidence.
  Stationary fixed-close requalification admitted five40mm and 5760mm grasps.
- Left/right canonical grasp geometry agrees under exact handedness adaptation;
  mechanical motor names still require signed mapping/index-middle exchange.
- Selected-arm finite table patch helps optimization; infinite-plane validation
  remains independent. Collision proxy overlap led to temporary exceptions,
  subsequently ALL selected-shoulder start recovery removed: live start must be
  strict-clear. Don't document the abandoned negative buffer/monotonic escape.
- Finite IK branch preservation, independent seeds per candidate, immutable
  per-attempt state fixed false 'unreachable' diagnoses. CuRobo mutates input
  JointState. Float32 anchoring fixes only numerical roundoff, not real joins.
- GPU native strict collision checks reproduced decisions and bit-identical
  paths while reducing one task295.81→39.05s. Pools reuse compatible topology
  and refold measured locked state. Cold/warm timing isn't full hardware time.
- Raw MCAP writer isolates control from encoding. Synthetic9trials maxgap<10ms
  not physical safety proof. ROS topic names omit Unitree DDS rt partition.
  Subscribed-to-all and metadata types/nonempty checks prevent camera-only bags.
  Start recording before ownership, stop after all recovery; incomplete remains.
- Teardown ROS/planner only after verified external takeover; early teardown
  starved local callbacks~209ms despite healthy independent LowState stream.
- Correct perception uses largest well-resolved face, generic planar IPPE two
  branches/positive depth/lowest residual, then LM. Rawgray beat CLAHE on326
  retainedframes; do not turn a13px corner error into alleged object motion.
- 5mm physical table margin replaced submillimetre accepted routes after real
  strike. Reobserve fixedcube at liftedclearance to account for~5.3mm body shift.
  Capture synchronized anchor before planning can evict it from4096samplebuffer.
  At pregrasp propagate hybrid camera estimate and replan samegrasp remainder.
  Every boundary has already-frozen exact reverse even if newplan fails.
- First physical complete lift/replacement Aug17T230114 failed later due omitted
  return_to_pregrasp leg. Do not call its full lifecycle completed.
- Contact policy evolved materially: exactpostPhysX q→singlejointstall→opposed
  pressure→commissioned empty-close opposed joint shortfall. Current withinthis
  range requires thumb AND opposingclosingjoint >=.05radshortfall from measured
  empty close at support and30mmretentioncheckpoint. Pressure was disproved as
  required evidence for this cubegrasp, not as a functioning sensor generally.
  Onlyleft emptyclose commissioned atAug18; check laterbilateral status.
- Run-local measuredemptyopen is separate from arbitraryinitial fingers and
  commissionedemptyclose. Commanddescriptorzero, verifyagainstachievedemptyopen.
  Measuredcontactpayload can beginpositivelybelow5mm if no deepermovement, reaches
  free-spacefloor and exactreversereturn; no penetrating start allowed.
- Tripod runs could lift but completed lifecycle did not establish precise
  replacement on threecontacts. Tripod later REMOVED in favor prime-tower35.42x
  34.75x60mm with centered/yawalignedplacement; 11340mm/31260mm qualifiedgrasps.
- MPC history: fullphase nominaltracking→bodycorrected→movingfinalapproachonly.
  MotionGen retains global/payload/return. Absolute immutablefuturehandoff with
  predecessorhash and q/dq/ddq, livecommand-minusmeasured reanchor, validates
  predicted AND desiredpaths. Rejectedsovles don't expire healthy lowlevelcontrol;
  decelerated .8s certifiedtail ends in hold, retries bounded bymotiontimeout.
- Ideal plant replay hid persistenttrackingoffset stall; don't benchmarkonly
  measured==command. LaterAug21 endpointincompatibility: physicalgoal7.074mm
  tableclearance butdesiredcommand -1.588mm; needed6.588mm shift beyond5mmtarget
  tolerance. Testedpadding workaround REMOVED, do notretryphysically. Default
  boundaryreplanning remains commissioned choice, movingtargetMPC experimental.
- Waist-yaw study bounded ±.1–.5rad, mixedarmtravelbenefit; IK-only command-free,
  not implementedwholebodyplanning/physicalcommissioning.
- Stack coordinator initially60+40 then two60mm IDs10–15/20–25. Both supported
  armsescape, one taskarmmoves at time; source/destination/transfer mustsharesame
  grasp; reobserveactual lowerplacement. Finiteplacementproposalsinsideobserved
  segment don'tinferatableboundary. One boundedgrasp retryonlyaftercompleted
  frozenrecovery andfreshscene, excludesfailedcandidate; faultsnotretry.
- Aug20 successful40/60mm physicaltrials commissioned .2rad/s armdefault. Earlier
  .1rad/s was initialcommissioningspeed, not currentdefault.

## Findings from lines 4,941–7,403

- Stack reduced to one direct pick/place; then restored search of both directed
  cube assignments for both arms, one arm lifted at a time. Current retained
  session keeps control/resources between independent episodes; SPACE creates a
  run, Ctrl+C at between-episode wait hands back cleanly, within episode faults.
  Four upright yaw symmetries are one CuRobo goal set. Endpoint intersection
  avoids minutes of blind nested route search; candidate order retains existing
  source+destination joint-distance scores.
- August24 baseline rebuilt from physically successful Friday0a0fa0c; later
 34-candidate simulatedreleasefilter excluded. Preserve57candidatepool.
- Raw-to-LeRobot scan selects15Hz alignedmessages beforedecoding; retained
  identicalnumericaloutput, indexing325→11.67s. Rawdeletion is explicitlyguarded,
  onlyafterreload+replacementreceipt; lossytrainingepisode notfullROSarchive.
- Restingcube perception now ALL positive-depth perfaceIPPE hypotheses plus
  nonplanarmultiface,3px/20degreeface-upgates,largestconsistent3of5 subset within
 5mm/2deg. Earlier largestface-onlymethod was systematicallywrong~30deg.
- Bilateralcalibration designs change Ready-bound→reusableclosedanchorcore +
  livereversibleadapter. FullSept4 strict10mmcore79captures81edges, later requires
  regenerationforoperator-preclosedhands. Current active-onlymarker excitation,
  optionalinactive, bilateralanchors, sightlinesphysicalCADnotfittedeffective
  target, oneattemptdefault. Camera/hand-FK fit conditional, noabsoluteaccuracy.
- Septembercontrolfailures independentlyidentified: watchdogarmedbeforethree
  .2sDDSconstructors causedtimeout(.6s>.5lease); preflightqvscommand joins;
 12.3MBJSONhashing blockedinterpreter76–90ms; fingerheartbeat republishedoldhold
  duringramp; zero waistslots atfullarm_sdk causedsupportloss/loadedreturnoverlap.
  Fixes reuseexistinglifecycle, workerheavyserialization, fingercommandhelper,
  measuredwaistseedmode1Kp300Kd3. Somephysicaltransients remainedunexplained.
- Sept5T231145 acquired,55accepted/17rejected/19retries,Qreturnedreleasedtrue
  nofault; oldstandingbag6topics omittedcamera, cannotrecoverfailedframes.
  Sept7T133509 has49accepted343images andcomplete14topic28.43GBbag, butfinger
  restorationfailed. These establish laterphysicalprogress despite staleREADME
  sentences sayingwaistholdunverified. Do notattributeallimprovementtoonefix.
- FinalSept7 calibration posture is MANUALLYpreclosed, measuredholdonly, no
  automaticclose/restore; savedreference readiness .08rad/.5s/.01spread,
  preflightandpostSPACE andacquisitioncheck; shouldersearch.08/.10/.12/.14rad.
 635tests9skip, realofflineGPU10.4566mmpreparationclearance; newcoremustregenerate,
  latestlifecycle hasnohardwarevalidation.
- Sept5selected7offsetgroupCV5.43px butactive7.95; camera+targets22.95overall.
  blockedbundleexport fromuncertainanchorPnP gate: large inferredmotion notproof
  physicaldrift. Poolallframes+bothmarkers3.94mm stillnotvalidatedreplacementgate.
- Sept7 repeats highlystableaftermeasuredstatecompensation .107–.361px;
  all12A/B pairsfailmeasuredFKmatching, so causalexperimentlimited. Operator
  deliberatelymovedcamera; separaterunregistrationsmandatory. Useracceptscamera
  errorexcluded; neitherexactcommandtrackingnormorecoveragejustifiedasfix.
- RGBDsingle/tworunoptimizationscompletedno consistentheldoutimprovement.
  Planeagreementdoesn'tconstraininplaneerror; depthnotabsolutetruth.
- Two-run46conditions broadgeometry51mm hypothesis3.1701/4.3012pxheldvs46mm
 8.2807/18.8714 withsame84params; notsole5mmpatchgain. Approxphysical51mm
  directionconfirmed, exactsideuncertainty/motoridentityunresolved. Usermanual
  versionnotmotorvariant. Full5010URDF armFK equals spacing-only51hypothesis.
- OriginalAugustnativecontrolledrerun5.409→5.031px(7%); frozenparameters
  geometry-onlychange5.409→12.649held, exactly5mmpoints/noorientationdifference.
  Refittedcamera/targets/offsetsredistributeerror, notuniquephysicalidentification.
  Ledgerpreserves85entries+46models, sweep/issuepaused, patchesunapplied,
  noforearmmarkerspossible. OriginalAugustbundle remainsstackbaseline.

## AprilCube fork log

All126lines read. July13–15 fork work adds generic tangent cuboid rounding,
topology-aware solid-union opening for voxel targets after per-voxel seams,
shared printable/render/collision geometry and current marker coordinates.
Final40mmR3 replaced50mmR8; 48/48syntheticviews,14focusedtests, unrelated
AuxCamera import failure excluded. Physicalwhitecellpit was nozzlechange
hypothesis, notprovenrootcause; repairanddetectioncheck wereinstructions, not
confirmedrepair. Forkreleasehistory squashed fromupstream9d679b5. Published
claims mustcreditupstream andpreserveconditionalcontact-safety rationale.
