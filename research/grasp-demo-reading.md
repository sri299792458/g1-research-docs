# Grasp demo: complete source reading

Inspected public `sri299792458/g1-aprilcube-demo` main at
`f190470742f43101e9a22affaca80554722706ac` in an isolated clone.
Read all 3,209 running-note lines sequentially (1–310, 311–670, 671–1040,
1041–1430, 1431–1810, 1811–2200, 2201–2580, 2581–2940, 2941–3209),
and the complete 204-line README. Source-reported results were not rerun.

## Essential findings

- GraspGen-X returns object/pointcloud-from-canonical-G, not palm/wrist/pregrasp.
  Compose the descriptor's fixed G-to-palm transform once. Network consumes12
  sweep-volume values, not current URDF or per-object finger endpoints.
- Old bundled hand differs from rev1.0 Dex3. New descriptors and exact physical
  geometry preserve named/signed left-right mapping. Early literal-looking
  box conditioning was wrong. Do not repeat its claim the upstream wizard erred.
- Crossed120proposal/hand matrix: released→old110, released→current118,
  firstcurrent→old5,current16. All16boxgroup factorials isolate openextents:
  replacingonlyopenextents16→111/120. Simple53degreeframerotation0/120.
  Currentaperturesemantic467/480vsreleasedproxy472/480 onfreshseeds. Selected
  released12vector is a learnedconditioningproxy, notliteralphysicalenclosure.
  Canonicalright118/120,left116/120 intrinsiccheck, not tabletopsuccess.
- Newton hand-only prescribedroot/table tests invalid for intrinsicquality:
  bottomup grasps drivenintotable, ejectioncannotcountaslift. Separate intrinsic
  retention, support/approach geometry, fullrobotreachability/execution.
- Isaac selfcollisionUSDregression: repeatedidentical10trialsunstable→10/10
  aftersamehandselfcollisiondisabled; hand-object remains. HashallUSDsublayers,
  rootfilehashunchangedwhenphysicschanges. Preservepalmfixedlinkfortactiletrace.
- VIRAL source executed ImplicitActuator despiteidealpdYAML. 200HzTGS,
  thumb0kp2kd.1 others.5/.1, armaturex3 frictionx0; theseareSIMprofile,
  don'tcopyintohardware. Objectfriction1 cube30g; T181.1/U211.3g estimates.
- Authoritative4096/object VIRALrightatlases:45mmcube2437(59.50%)40families;
  T1240(30.27%)39; U675(16.48%)28. Earlier3223/1616/764 usesoldprofile.
  Maxnormbodypaircontact insteadsummedvector prevents cancellationmetadata;
  reran12288trials0verdictflips. Familyreplay39/40,30/39,20/28; keepredcases.
- Newtonplannedrightpickupcube/T/U passedretention withprescribedarmdynamic
  fingers/object; T/U softjointlimits exceeded up to.228rad, nothardwareproof.
- T/U/cube assembly fixedtorso28jointmodel, exactvoxelworld, symbolicmagnetic
  snap/compositeattachments. Runtime2scenes passkinematics, notrealassembly.
  Region/keepoutfields initiallyparsedbutunused, armassignmenthardcoded; final
  planner cannot bepresentedasgenericrandomflatpartassembly.
- FlatU right4/675openclear,0nativepickup; sixsupports definegeometry. Broad
 42physics0pass. Upright1837tested405discovery365replaypass,13/14visualpass.
 100Kraw(391seeds)→983broadcorridorclearphysics0pass; oneliftnear-miss203N
  hand/tablecontactinvalid. Unconditioned moresamplingnotfruitfulundercontract.
- LightningGraspadaptation returns pose+q;287solutions574supportpairs,
 14eligible0physics;20overclosuretests0. Usefulanalyticgeometry notpickup.
- GoalsetalternativesnotindependentBatchMotionPlanner problems;16/32batchOOM,
 8worksbut1240plans156s.32entrygoalsets+prefixbacktracking. Multi-toolgoalset
  pertoolindexdoesnotpreservepairedrow; pairedmatehypothesissingletontwotool.
  IK/TrajOptattachmentmanagersbothupdated. Namedjointsnotpositionalcuts.
- Cube-to-box24orientationgoalset solvedwhere8yaw-onlyfailed; openbinfivepieces
  notsolidAABB; visualizeddrop symbolicnotdynamics. Seed7/19bothkinematicpass.
- Correct40mmcube newly4096inferred,3178intrinsicpasses,15initialshortlist.
  Older45mmshortlistinvalidforactualprint. Laterstationaryclose5/57and60mm
  profiles reside tabletopsource, afterthisremotehistoryends.
- Tripod40/50/60exactfixtures324/372/394union at70/100/150approach; heightnot
  monotonicclearance. This history endsAug15; tabletoplaterremovedtripodand
  rejectedusingisaac_closed_q ashardwarecommand. SourceREADME canbeoutdated.

## Media

Numerous tracked PNG/MP4 assets exist in this clone. Not yet independently
viewed for this draft. Prefer a few clearly captioned representative assets;
never relabel kinematic replay as physical G1 footage.
