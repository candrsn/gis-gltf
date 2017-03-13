### 3d_tools.py

import pyassimp as pas

def model_geom(file_root, w, nextId,  opt):
        ## Read TINs from the DAE
    global bid

    dir_parts = file_root.split("/")
    if ( len(dir_parts) > 0 ):
        bid = dir_parts[len(dir_parts)-1]
    else:
        bid = "unknown"

    myProcessing = pas.postprocess.aiProcess_Triangulate | pas.postprocess.aiProcess_PreTransformVertices
    scene = pas.load(file_root + '.dae',  processing=myProcessing)
    assert len(scene.meshes),  "file has no meshes... aborting"

    if os.path.isfile(file_root + '.czml') and opt.relModelPos:
        json_data=open(file_root + '.czml', "rb")
        data = json.load(json_data)
        json_data.close()
    else:
        data = json.loads('[{"skip": "me"},{"position": {"cartographicDegrees": [0,0,0]}}]')

    [mx,my,mz] =  data[1]["position"]["cartographicDegrees"]
    mx = float(mx)
    my = float(my)
    mz = float(mz)

    g1 = "POINT (%f %f %f)" % (mx,my,mz)
    if (opt.s_srs != opt.t_srs):
        g2 = project_point(g1, opt.s_srs, opt.t_srs)
    else:
        g2 = ogr.CreateGeometryFromWkt(g1)
 
    return convert_meshes(scene, g2, opt, w)  
    
def geom_model():
    pass
    
def mesh_from_nodes():
    pass
    
    
