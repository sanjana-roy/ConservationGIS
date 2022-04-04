######### FLOODPLAIN FOREST GAP ANALYSIS #########
##### Final Draft
##### Author: Sanjana Roy
##### Date: 17th December, 2021

# import tools from WBT module

from WBT.whitebox_tools import WhiteboxTools

# declare a name for the tools
wbt = WhiteboxTools()

wbt.work_dir = "/Users/sanjanaroy/Documents/CollegeProjects/GEOG310/wbt_pySpace-master/goods"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Data Layers from Google Earth Engine
# proFlat = protectedLands.tiff
# primeImage = primeSoils.tiff
# ag = agricultureLands.tiff
# hb = habitatBlocks.tiff
# rcImage = riverCorridors.tiff
# imageRip = riparianImage.tiff
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



### 1. FLOODPLAIN FORESTS IN PROTECTED AND AGRICULTURAL LANDS

### ALL PROTECTED

# Reclassifying to all protected
wbt.reclass(
    i = "protectedLands.tiff",
    output = "protectedLandsAll.tif",
    reclass_vals = "0;0;1;1;1;2",
    assign_mode=True
)

# Zonal Stats with current floodplain forest extents
wbt.zonal_statistics(
    i = "ffCurrent2.tif",
    features = "protectedLandsAll.tif",
    output=None,
    stat='minimum',
    out_table= "stats_protAll.html"
)


# Zonal Stats with historic floodplain forest extents
wbt.zonal_statistics(
    i = "ffHistoric.tif",
    features = "protectedLandsAll.tif",
    output=None,
    stat='minimum',
    out_table= "stats_protAllHistoric.html"
)

#### PROTECTED AGRICULTURE

# Reclassifying to protected ag
wbt.reclass(
    i = "protectedLands.tiff",
    output = "protectedLandsAg.tif",
    reclass_vals = "0;0;1;1;0;2",
    assign_mode=True
)

# Zonal Stats with current floodplain forest extents

wbt.zonal_statistics(
    i = "ffCurrent2.tif",
    features = "protectedLandsAg.tif",
    output=None,
    stat='minimum',
    out_table= "stats_protAg.html"
)

# Zonal Stats with historic floodplain forest extents

wbt.zonal_statistics(
    i = "ffHistoric.tif",
    features = "protectedLandsAg.tif",
    output=None,
    stat='minimum',
    out_table= "stats_protAgHistoric.html"
)

#### PROTECTED NON-AGRICULTURE

# Reclassifying to protected non-ag
wbt.reclass(
    i = "protectedLands.tiff",
    output = "protectedLandsNonAg.tif",
    reclass_vals = "0;0;0;1;1;2",
    assign_mode=True
)

# Zonal Stats with current floodplain forest extents

wbt.zonal_statistics(
    i = "ffCurrent2.tif",
    features = "protectedLandsNonAg.tif",
    output=None,
    stat='minimum',
    out_table= "stats_protNonAg.html"
)

# Zonal Stats with historic floodplain forest extents

wbt.zonal_statistics(
    i = "ffHistoric.tif",
    features = "protectedLandsNonAg.tif",
    output=None,
    stat='minimum',
    out_table= "stats_protNonAgHistoric.html"
)

#### ALL AGRICULTURE

# Zonal Stats with current floodplain forest extents

wbt.zonal_statistics(
    i = "ffCurrent2.tif",
    features = "agricultureLands.tiff",
    output=None,
    stat='minimum',
    out_table= "stats_ag.html"
)

# Zonal Stats with historic floodplain forest extents

wbt.zonal_statistics(
    i = "ffHistoric.tif",
    features = "agricultureLands.tiff",
    output=None,
    stat='minimum',
    out_table= "stats_agHistoric.html"
)


##### 2. FLOODPLAIN FORESTS ON PRIME AGRICULTURAL SOILS


#### PRIME SOILS

# Reclassifying for only prime soils
wbt.reclass(
    i = "primeSoils.tiff",
    output = "onlyPrime.tif",
    reclass_vals = "0;0;0;1;1;2;1;3;1;4;0;5;0;6;0;7",
    assign_mode=True
)

# Zonal stats for current extents

wbt.zonal_statistics(
    i = "ffCurrent2.tif",
    features = "onlyPrime.tif",
    output=None,
    stat='minimum',
    out_table= "stats_prime.html"
)

# Zonal Stats for historic extents

wbt.zonal_statistics(
    i = "ffHistoric.tif",
    features = "onlyPrime.tif",
    output=None,
    stat='minimum',
    out_table= "stats_primeHistoric.html"
)

# PRIME SOILS IN AG AND NOT IN AG

# Multiplying with Prime soils
wbt.multiply(
    input1 = "onlyPrime.tif",
    input2 = "agricultureLands.tiff",
    output = "primeInAg.tif"
)

# Zonal stats for current extents

wbt.zonal_statistics(
    i = "ffCurrent2.tif",
    features = "primeInAg.tif",
    output=None,
    stat='minimum',
    out_table= "stats_primeAg.html"
)

# Zonal Stats for historic extents

wbt.zonal_statistics(
    i = "ffHistoric.tif",
    features = "primeInAg.tif",
    output=None,
    stat='minimum',
    out_table= "stats_primeAgHistoric.html"
)


### 3. EVALUATING POTENTIAL PROTECTION SYSTEMS

# Clumping habitat blocks together
wbt.clump(
    i = "habitatBlocks.tiff",
    output = "hbClumped.tif",
    diag=False,
    zero_back=True
)


# Setting the background of habitat blocks (0) to no data
wbt.set_nodata_value(
    i = "hbClumped.tif",
    output = "hbNoData.tif",
    back_value=0
)

# Performing Zonal Stats to identify habitat blocks that intersect with the river corridor
wbt.zonal_statistics(
    i = "riverCorridors.tiff",
    features = "hbNoData.tif",
    output= "hbRivers.tif",
    stat='maximum',
    out_table= None

)

# Reconverting no data to zero for zonal stats analysis
wbt.convert_nodata_to_zero(
    i = "hbRivers.tif",
    output = "hbRiversConv.tif"
)

# HABITAT BLOCKS

# Zonal stats for habitat blocks and current extents
wbt.zonal_statistics(
    i = "ffCurrent2.tif",
    features = "hbRiversConv.tif",
    output=None,
    stat='minimum',
    out_table= "stats_hbC.html"
)

# Zonal stats for habitat blocks and historic extents
wbt.zonal_statistics(
    i = "ffHistoric.tif",
    features = "hbRiversConv.tif",
    output=None,
    stat='minimum',
    out_table= "stats_hbH.html"
)

# RIVER CORRIDORS

# Zonal stats for river corridors and current extents
wbt.zonal_statistics(
    i = "ffCurrent2.tif",
    features = "riverCorridors.tiff",
    output=None,
    stat='minimum',
    out_table= "stats_rcC.html"
)

# Zonal stats for river corridors and historic extents
wbt.zonal_statistics(
    i = "ffHistoric.tif",
    features = "riverCorridors.tiff",
    output=None,
    stat='minimum',
    out_table= "stats_rcH.html"
)

# SURFACE WATER RIPARIAN CONNECTORS

# Zonal stats for riparian connectors and current extents
wbt.zonal_statistics(
    i = "ffCurrent2.tif",
    features = "riparianImage.tiff",
    output=None,
    stat='minimum',
    out_table= "stats_ripC.html"
)

# Zonal stats for riparian connectors and historic extents
wbt.zonal_statistics(
    i = "ffHistoric.tif",
    features = "riparianImage.tiff",
    output=None,
    stat='minimum',
    out_table= "stats_ripH.html"
)
