######### FLOODPLAIN FOREST CURRENT CONDITIONS ANALYSIS #########
##### Final Draft
##### Author: Sanjana Roy
##### Date: 17th December, 2021

# import tools from WBT module
from WBT.whitebox_tools import WhiteboxTools

# declare a name for the tools
wbt = WhiteboxTools()


wbt.work_dir = "/Users/sanjanaroy/Documents/CollegeProjects/GEOG310/wbt_pySpace-master/goods"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##### Data Layers from Google Earth Engine

# nc = natCommSoils.tiff
# imageBB = _buildingBuffer.tiff
# lcSimple = lcSimple.tiff
# ag = agricultureLands.tiff
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#### 1. IDENTIFY FLOODPLAIN FOREST SOILS AND HISTORIC EXTENTS

# Reclassifying "natCommSoils.tif"

wbt.reclass(
    i = "natCommSoils.tiff",
    output = "ffHistoric.tif",
    reclass_vals = "0;0;0;1;1;2;0;3;0;4;0;5;0;6;0;7;0;8",
    assign_mode=True
)


#### 2. DEFINING LAND COVER CATEGORIES


#### A. REFINE TREE CANOPY LAYER

# Reclassifying "_buildingBuffer.tiff"

wbt.reclass(
    i = "_buildingBuffer.tiff",
    output = "_buildingreclassed.tif",
    reclass_vals = "0;0;10;1",
    assign_mode=True
)

# Adding building buffer to land cover data

wbt.add(
    input1 = "_buildingreclassed.tif",
    input2 = "lcSimple.tiff",
    output = "landCoverTreeBuffer.tif"
)

# Reclassifying land cover to remove building buffer within tree canopy

wbt.reclass(
    i = "landCoverTreeBuffer.tif",
    output = "landCoverReclassed1.tif",
    reclass_vals = "1;1;2;2;3;3;4;4;5;5;0;11;2;12;3;13;4;14;5;15",
    assign_mode=True
)

#### B. ADDING AGRICULTURAL LANDS

# Reclassifying agricultural lands

wbt.reclass(
    i = "agricultureLands.tiff",
    output = "agLandsReclassed2.tif",
    reclass_vals = "0;0;10;1",
    assign_mode=True
)

# Adding agricultural lands to land cover data

wbt.add(
    input1 = "landCoverReclassed1.tif",
    input2 = "agLandsReclassed2.tif",
    output = "landCoverAg.tif"
)

# Reclassifying land cover into categories:
# - NA (0)
# - Trees (1)
# - Shrubs (2)
# - Water (3)
# - impervious surfaces/developed (4)
# - Agriculture (5)

wbt.reclass(
    i = "landCoverAg.tif",
    output = "landCoverReclassed2.tif",
    reclass_vals = "4;0;1;1;2;2;3;3;4;4;4;5;5;10;1;11;5;12;3;13;4;14;4;15",
    assign_mode=True
)


# 3. IDENTIFYING FLOODPLAIN FOREST HISTORIC LAND DEVELOPMENTS AND CURRENT EXTENTS

# Reclassifying historic floodplain forests

wbt.reclass(
    i = "ffHistoric.tif",
    output = "ffHistoricReclassed.tif",
    reclass_vals = "0;0;10;1",
    assign_mode=True
)

# Adding ffHistoric to landCover
wbt.add(
    input1 = "ffHistoricReclassed.tif",
    input2 = "landCoverReclassed2.tif",
    output = "lcHistoric.tif"
)

# Identifying current extents of floodplain forests, overlap with ag, overlap with developed
wbt.reclass(
    i = "lcHistoric.tif",
    output = "lcHistoricReclassed.tif",
    reclass_vals = "0;0;0;1;0;2;0;3;0;4;0;5;0;10;1;11;1;12;1;13;14;14;15;15",
    assign_mode=True
)

# Identifying only current floodplain forest extents
wbt.reclass(
    i = "lcHistoric.tif",
    output = "ffCurrent2.tif",
    reclass_vals = "0;0;0;1;0;2;0;3;0;4;0;5;0;10;1;11;1;12;1;13;0;14;0;15",
    assign_mode=True
)


# 4. COMPUTING AREA AND VISUALIZING CATEGORIES

# Compute Area of each of the categories

wbt.raster_area(
    i = "lcHistoricReclassed.tif",
    output= "lcHistoricArea.tif",
    out_text=False,
    units="map units",
    zero_back=True
)

# Zonal Stats

wbt.zonal_statistics(
    i = "lcHistoricArea.tif",
    features = "lcHistoricReclassed.tif",
    output=None,
    stat="minimum",
    out_table= "lcHistoricStats.html"
)
