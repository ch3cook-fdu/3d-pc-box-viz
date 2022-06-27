# pc_det_visualization
Tools for visualizing pointcloud object detection results built on open3d. 
Suitable for bounding boxes with and w/o rotations since it purely based on the corners of a bounding box.

## Dependency
```
open3d
numpy
```

## Usage
If `point_cloud` is a `[npoints x 3, xyz]` matrix, the point cloud will be displayed in gray.
```python
from visualize import visualize_mesh
visualize_mesh(
    point_cloud = point_cloud, # [npoints x 3, xyz] or [npoints x 6, xyz+rgb] or [npoints x 9, xyz+rgb+normal]
    bboxes = bboxes            # [nboxes x 8 x 3]
)
```
