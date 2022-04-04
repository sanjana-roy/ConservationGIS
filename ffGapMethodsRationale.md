## Floodplain Forests

### Purpose
Identify gaps in conservation systems of floodplain forests around Middlebury and the potential of conservation elements for the protection and restoration of floodplain forest communities

### Introduction

Examining current conservation systems and identifying areas of protection will allow us to determine the next steps for the conservation and restoration of floodplain forest communities. The following document outlines the methods for analysing how floodplain forest communities, both existing and historic, conflict with current protections and agricultural lands and soils, and the potential for floodplain forests to be conserved and restored through protecting elements such as river corridors, habitat blocks, and riparian connectors. We derived layer combinations with protected, non-protected, and agricultural lands, and agricultural lands and soil types, which we then overlapped with both current and historic floodplain forest extents to determine the areas of these combinations. These areas were then graphed as percentages to visualize the differences between these combinations as percentages of floodplain forest land. We then considered the three potential protections systems for floodplain forests: habitat blocks, river corridors, and riparian connectors. As floodplain forests are mostly adjacent to rivers, we had to consider only the habitat blocks that were intersected with river corridors. After defining these blocks, we again overlapped both current and historic extents of floodplain forests with these three conservation elements and found the amount of area that lies both within and outside these protection boundaries. Through this we can determine how much floodplain forests can be both conserved and have historic extents restored through the protection of these elements.

### Data Prep

- Existing Floodplain Forests: Derived from the Floodplain Forests Current Conditions analysis found [here](floodplainForestsCurrentMethods.py)
- Historic Floodplain Forest Extents: Derived from the Floodplain Forests Current Conditions analysis found [here](floodplainForestsCurrentMethods.py) (using Natural Communities from Soils layer with filtered floodplain forests)
- Protected Lands: For comparison with current and historic floodplain forest extents
- Agriculture Lands: For comparison with current and historic floodplain forest extents
- Agricultural (PRIME) Soils: For comparison with current and historic floodplain forest extents
- Habitat Blocks: For comparison with current floodplain forest extents
- River Corridors: For comparison with current floodplain forest extents


### Data Process

#### 1. Floodplain Forests in Protected and Agricultural Lands

We wanted to compare how both existing and historic floodplain forests overlap with currently protected lands. We reclassified the protected lands layer to obtain rasters for all protected lands, protected agricultural lands, and protected non-agricultural lands.

| Layer | Protected Lands Layer Values | Protected Ag Lands Layer Values | Protected Non-Ag Lands Layer Values |
| ------| --------- | --------- | ------ |
| Non-Protected Land Features (0) | 0 | 0 | 0 |
| Protected Ag Land Features (1) | 1 | 1 | 0 |
| Protected Non Ag Land Features(2) | 1 | 0 | 1 |


We then performed zonal statistics for both current and historic floodplain forest extents on all three of these layers as well as the agriculture lands layer to obtain the amount of area that is overlapped in each combination. These values were put into a Google Sheets spreadsheet. The percentage of the overlap area was calculated for each value and these were then graphed in a bar chart.

The x-axis contains different combinations of categories for protected and agricultural lands that have been overlapped with both 'Historic Conditions' and 'Current Conditions'. The y-axis demonstrates the percentage of this overlap. Note how historic conditions largely overlap with current agricultural lands and the lack of current floodplain forest that are protected.

![protectedLands](/assets/images/protectedLands.png)

#### 2. Floodplain Forests on Agricultural Soils

As floodplain forest soils are often in conflict with prime agricultural soils, we wanted to examine the overlap between existing and historic floodplain forests and different agricultural soil types. We used the Agricultural (PRIME) soils layer and reclassified this to obtain a raster for only the three prime soil types (including b and f).

| Soil Type | Old Value | New Value |
| ------| --------- | --------- |
| Local (b) | 0 | 0 |
| Prime | 1 | 1 |
| Prime (b) | 2 | 1 |
| Prime (f) | 3 | 1 |
| Statewide | 4 | 0 |
| Statewide (a) | 5 | 0 |
| Statewide (b) | 6 | 0 |


We conducted zonal statistics on this layer for both current and historic extents and copied the overlap area values (1) and inverse area values (not prime soils) into the Google Sheets spreadsheet.

We also wanted to look at the prime soils that are used in agriculture. We intersected agricultural lands with the previously obtained prime soils layer through multiplying the two. We then followed the same process with zonal statistics. The percentage of the overlap area was calculated for each value and these were then graphed in a bar chart.

The x-axis contains different combinations of categories for prime agricultural soils and agricultural lands that have been overlapped with both 'Historic Conditions' and 'Current Conditions'.

![primeSoils](/assets/images/primeSoils.png)

#### 3. Evaluating Potential Protection Systems

We wanted to evaluate how protecting habitat blocks, river corridors, and surface-water riparian connectors could contribute to conserving floodplain forests and possibly restoring historic extents. We wanted to identify how much historic and existing floodplain forest lie both within and outside habitat blocks, river corridors, and riparian connectors.

We first identified habitat blocks that intersect with river corridors in order to consider only those blocks that would interact with river flows and floodplain communities. We clumped habitat blocks together and converted 0 to no data so that the background value is not considered during Zonal Statistics. We performed Zonal statistics with river corridors (using a maximum value) to find only the habitat blocks that intersected with river corridors. We then reconverted the background no-data values back to 0 to perform further analyses.

![hbRiverConv](/assets/images/hbRiverConv.png)

We then conducted zonal statistics for both current and historic extents on river corridors, habitat blocks, and riparian connectors. We obtained values for the area of floodplain forests that fall within and outside these corridors and blocks. Values were again entered into a Google Sheets spreadsheet and the percentage of the overlap area was calculated for each value. These were then graphed in a bar chart shown below.

The x-axis contains different combinations of categories for 'Historic Conditions' and 'Current Conditions' that fall within and outside river corridors, habitat blocks, and riparian connectors. The y-axis demonstrates the percentage of this overlap.

![hbRCProtection](/assets/images/hbRCProtection.png)


### Python Sript

We implemented this model with the [WhiteBoxTools Open Core](https://www.whiteboxgeo.com/geospatial-software/). The floodplainForestsGapMethods.py script can be found [here](floodplainForestsGapMethods.py).
