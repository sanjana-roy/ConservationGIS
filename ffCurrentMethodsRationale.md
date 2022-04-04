## Floodplain Forests

### Purpose
Identify current conditions of floodplain forests around Middlebury and land developments on historic floodplain forests


### Introduction
The following document outlines the methods for identifying the existing conditions of floodplain forest communities in Middlebury and identifying the various land developments that have taken place on historic floodplain forest extents. Floodplain forests are highly threatened and fragmented communities and understanding their current extents and spatial history would assist in developing a plan for the conservation of these communities. We identified historic extents through distinguishing soils associated with the presence of floodplain forests. In order to provide a fuller picture of the existing boundaries of these communities, we decided to include not only tree canopy, but also grass, shrubs, and water. We first cleaned our land cover dataset to remove landscaped footprints around buildings under 'Tree' and 'Grass' categories and also added agricultural lands to the land cover dataset. We then categorized our desired land cover types and overlapped these with historic extents to derive existing conditions of floodplain forests. Through this overlap, we also were able to identify which areas of historic floodplain forests have been converted to agricultural lands and developed, impervious infrastructure, demonstrating the various conflicts associated with floodplain forest conservation today.


### Data Prep

- **Tree Canopy:** To identify historic extents of floodplain forests along with Natural Communities from Soils layer
- **Natural Communities from Soils:** To identify soils where floodplain forests have historically grown
- **Buildings:** To remove landscaped tree canopy within 100 feet of a building (layer includes 100 foot buffer)
- **Land Cover (Simplified):** To identify current extents of floodplain forests and land developments that have taken place on historic extents
- Export each dataset for Middlebury Study Area

### Data Process

#### 1. Identify Floodplain Forest Soils and Historic Extents

Floodplain forests are distinct communities that often flood with river waters and have specific soil types associated with their presence. In order to derive the historic extents of these communities, we used the soils layer to identify floodplain forest soils and where they may have been present pre-colonial settlement.

We derived the different types of Natural communities from the Soils layer provided by the Vermont Agency of Natural Resources Database. We identified the type of community that is associated with soil type and grouped the soil features accordingly through reclassification. We then filtered floodplain forest soils from this dataset. This is what we considered as the historic extents of floodplain forest communities.

| Old Value | New Value |
| ------| --------- |
| 0 | 0 |
| 1 | 0 |
| 2 | 1 (Floodplain Forests) |
| 3| 0 |
| 4 | 0 |
| 5 | 0 |  
| 6| 0 |
| 7| 0 |
| 8 | 0 |

![ffHistoric](/Users/sanjanaroy/Documents/CollegeProjects/GEOG310/wbt_pySpace-master/assets/images/ffHistoric.png)


#### 2. Defining land cover categories


##### A. Refine tree canopy layer

Trees and grass land cover features that are found around buildings are often part of the landscaping footprint of the building. We wanted to remove these areas around buildings so they are not counted in deriving floodplain forest extents. We used the buildings buffer layer, which includes a 100 foot buffer created around buildings from the land cover dataset.

![buildingBuffer](/Users/sanjanaroy/Documents/CollegeProjects/GEOG310/wbt_pySpace-master/assets/images/buildingBuffer.png)

We reclassified the buildings buffer layer to have a value of 10 (0-> 0, 1-> 10). We then added the building buffer layer to the simplified land cover layer, which gave us additional values from 11 to 15 that included where the buildings buffer overlapped with the first five categories. We reclassified the resulting layer to categorize trees and shrubs/grass that intersect with building buffers to have a value of 0.

| Category | Old Value | New Value |
| ------| --------- | --------- |
| Tree Canopy | 1 | 1 |
| Grass & Shrubs | 2 | 2 |
| Water | 3 | 3 |
| Impervious Surface | 4 | 4 |
| Buildings | 5 | 5 |
| Building Buffer + Trees | 11 | 0 |
| Building Buffer + Grass | 12 | 0 |
| Building Buffer + Water| 13 | 3 |
| Building Buffer + Imp. Surface | 14 | 4 |
| Building Buffer + Buildings | 15 | 5 |

![treeCanopySubtracted](/Users/sanjanaroy/Documents/CollegeProjects/GEOG310/wbt_pySpace-master/assets/images/treeCanopySubtracted.png)


##### B. Adding Agricultural Lands

We wanted to identify current conditions of the remaining floodplain forest communities, and the various land developments that have taken place on historic floodplain forest extents.

We obtained the general land cover categories we were interested in. Agricultural lands is a category we wanted to consider and was not part of the simplified land cover layer. We first reclassified agricultural lands to have a value of 10 (0->0, 1->10) and then added it to the existing land cover layer, which gave us additional values from 10 to 15 where agriculture overlapped with the initial six categories. We then reclassified this layer to obtain categories for Trees, Shrubs, Water, Developed Lands (including pavement, roads, railroads, bare soils, buildings, and landscaped areas around buildings), and Agriculture.

| Old Category | Old Value | New Value | New Category |
| ------| --------- | --------- | ------ |
| None | 0 | 4 | Imp. Surface |
| Tree Canopy | 1 | 1 | Trees |
| Grass & Shrubs | 2 | 2 | Grass |
| Water | 3 | 3 | Water |
| Impervious Surface | 4 | 4 | Imp. Surface |
| Buildings | 5 | 4 | Imp. Surface |
| Ag | 10 | 5 | Agriculture |
| Ag + Trees | 11 | 1 | Trees |
| Ag + Grass | 12 | 5 | Agriculture |
| Ag + Water| 13 | 3 | Water |
| Ag + Imp. Surface | 14 | 4 | Imp. Surface |
| Ag + Buildings | 15 | 4 | Imp. Surface |


![lcAgReclassed](/Users/sanjanaroy/Documents/CollegeProjects/GEOG310/wbt_pySpace-master/assets/images/lcAgReclassed.png)


#### 3. Identify floodplain forest historic land developments and current extents

In order to see which areas of the historic floodplain forests were converted to these different land cover categories, we performed an intersection of these two layers. We reclassified the floodplain forest historic extents to have a value of 10 (0->0, 1->10) and this was added to the previous land cover layer, which gave us values of 11 to 15 where historic extents overlapped with the first five layers. This layer was again reclassified into current extents of floodplain forests, the historic extent overlap with agriculture and with developed lands. We considered the current extents of floodplain forests to include tree canopy, shrubs, and water.

| Old Category | Old Value | New Value | New Category |
| ------| --------- | --------- | ------ |
| NA | 0 | 0 | None |
| Tree Canopy | 1 | 0 | None |
| Grass & Shrubs | 2 | 0 | None |
| Water | 3 | 0 | None |
| Impervious Surface | 4 | 0 | None |
| Ag | 5 | 0 | None |
| Historic only | 10 | 0 | None |
| Historic + Trees | 11 | 1 | Current Extents |
| Historic + Grass | 12 | 1 | Current Extents |
| Historic + Water| 13 | 1 | Current Extents |
| Historic + Imp. Surface | 14 | 14 | Historic + Developed |
| Historic + Ag | 15 | 15 | Historic + Ag |

![lcHistReclassed](/Users/sanjanaroy/Documents/CollegeProjects/GEOG310/wbt_pySpace-master/assets/images/lcHistReclassed.png)

In order to perform further analyses, we reclassified the previous layer to obtain values for only current extents (with everything other than current extents changed to a value of 0).

![ffCurrent2](/Users/sanjanaroy/Documents/CollegeProjects/GEOG310/wbt_pySpace-master/assets/images/ffCurrent2.png)

#### 4. Computing area and visualizing categories

The areas of each of these categories were calculated and zonal statistics was performed to obtain the area values. Zonal statistics is a raster analysis tool used to obtain descriptive statistics of a data layer defined by a feature definition raster within which the statistics will be calculated. This analysis uses the calculated area of categories as the base data layer with the categories itself as the feature definition raster. These values were entered into a Google Sheets spreadsheet and a pie chart was derived that visualizes the land developments that took place on historic floodplain forest extents.

From this chart, we can determine the conflicts that exist with restoring floodplain forest communities in the Middlebury Region and can begin to identify how to approach their conservation.

![currentGraph](/Users/sanjanaroy/Documents/CollegeProjects/GEOG310/wbt_pySpace-master/assets/images/currentGraph.png)


### Python Sript

We implemented this model with the [WhiteBoxTools Open Core](https://www.whiteboxgeo.com/geospatial-software/). The floodplainForestsCurrentMethods.py script can be found [here](Users/sanjanaroy/Documents/CollegeProjects/GEOG310/wbt_pySpace-master/floodplainForestsCurrentMethods.py).
