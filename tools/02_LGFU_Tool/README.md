# LGFU Tool [EFRI Tool]

- Add a new field for each species used in OLT LGFU SQL.
- Calculate individual species proportions based on the Species Composition (SPCOMP) field.
- Add and populate the GLSL LGFU field based on species composition proportions, STKG and SC
  
Processes forest species composition information and separates the species values into individual attribute fields. It also assigns GLSL Landscape Guide Forest Unit classifications based on species composition, stocking and site class information.

**Requirements:** Ensure the SPCOMP, STKG, SC fields are available.

**Output:** Appends numerous species codes (BW, BY, BF...) that are found in the SPCOMP string and populates with SPCOMP % composition, and a GLSL_LGFU field after applying SQL for GLSL LGFU.

**Note:** Run this tool before the other forestry analysis tools but after the AutoPolyId Tool.  The other tools rely on the parsed species composition fields.
