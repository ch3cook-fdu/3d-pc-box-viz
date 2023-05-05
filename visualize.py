import numpy as np
import open3d as o3d
from typing import Optional, Tuple, Union

COLORS = [[.8, .1, .1], [.1, .1, .8], [.1, .8, .1]]     # TODO: modify this

def visualize_mesh(
    point_cloud: Optional[Union[np.array, Tuple]]=None, 
    bboxes: Optional[Tuple[np.array]]=None
):
    lines = np.array([[0, 1], [1, 2], [2, 3], [3, 0], [0, 4], [1, 5],
                      [2, 6], [3, 7], [4, 5], [5, 6], [6, 7], [7, 4]])
    visualization_group = []
    
    if point_cloud is not None:
        if not isinstance(point_cloud, tuple):
            point_cloud = (point_cloud, )
        for pc in point_cloud:
            pcd = o3d.geometry.PointCloud()
            pcd.points = o3d.utility.Vector3dVector(pc[:, :3])
            if pc.shape[-1] >= 6:
                pcd.colors = o3d.utility.Vector3dVector(pc[:, 3:6])
            else:
                pcd.colors = o3d.utility.Vector3dVector(
                    np.ones_like(pc[:, :3]) * [0.8, 0.8, 0.8]
                )
            if pc.shape[-1] >= 9:
                pcd.normals = o3d.utility.Vector3dVector(pc[:, 6:9])
            visualization_group.append(pcd)

    if bboxes is not None:
        if not isinstance(bboxes, tuple):
            bboxes = (bboxes,)
        for idx, boxgroup in enumerate(map(np.array, bboxes)):
            corners = boxgroup.reshape(-1, 3)
            edges = lines[None, ...] \
                    + (np.ones_like(lines[None]).repeat(boxgroup.shape[0], axis=0)
                       * np.arange(0, len(corners), boxgroup.shape[1])[:, None, None])
            edges = edges.reshape(-1, 2)
            # bounding box corners and bounding box edges
            box_corner = o3d.geometry.PointCloud()
            box_corner.points = o3d.utility.Vector3dVector(corners)
            box_corner.colors = o3d.utility.Vector3dVector(
                np.ones_like(corners) * COLORS[idx]
            )
            box_edge = o3d.geometry.LineSet()
            box_edge.lines = o3d.utility.Vector2iVector(edges)
            box_edge.colors = o3d.utility.Vector3dVector(
                np.ones((len(edges), 3)) * COLORS[idx]
            )
            box_edge.points = o3d.utility.Vector3dVector(corners)
            # store #
            visualization_group.extend([box_corner, box_edge])

    o3d.visualization.draw_geometries(visualization_group)
    return None
