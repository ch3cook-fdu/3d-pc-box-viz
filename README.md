# pc_det_visualization
Tools for pointcloud object detection built on open3d

## Dependency

```
open3d
numpy
```

## Usage
```{python}
from visualize import visualize_mesh
visualize_mesh(
    point_cloud = point_cloud, # [npoints x 3] or [npoints x 6, xyz+rgb] or [npoints x 9, xyz+rgb+normal]
    bboxes = bboxes            # [nboxes x 8 x 3]
)
```
