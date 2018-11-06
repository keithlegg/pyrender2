

from pygfx.render import *
from pygfx.point_ops import *
from pygfx.math_ops import  *
from pygfx.obj3d import  *



#######################################################
# test of new vec4 type 

"""
 
v3 = vec3(41,32,13)
v4 = vec4()

m44 = matrix44(1,3,4,5, 6,7,23,5, 6,3,23,3 ,5,6,7,8 )

v4.from_vec3(v3)

print( v4 )
 
"""

# print( m44.np_inverse )
# print(m44*v4)

#######################################################
# test of new quaternion type 

""" 
q1 = quaternion()
m33 = matrix33()
m33.from_euler(45,0,45)
q1.from_m33(m33)
m9 = q1.to_m33() 
obj = object3d()
obj.prim_cube()
ropr = simple_render()
ropr.render_matrix_obj( m9 , None ,     1,   100, 'custom_render.png' , obj      )
""" 

#######################################################
 

 
"""
obj = object3d()
obj.load_obj('objects/sphere.obj')
# print( obj.get_face_data(1 ) ) 
tmp =  obj.get_poly_geom( slice=(0,6), reindex=True ) 
obj2 = object3d()
obj2.insert_polygons(tmp[0], tmp[1])
obj2.save_obj("my_new_object.obj")
"""



def model_from_scratch(): 
    """ build a new polygon object from points """ 

    obj = object3d()

    # pass one - you can do as many as you like
    pts = [(1,1,1),(0,1,1),(-1,-1,1),(2,-2,1)]
    polys = [(1,2,3,4) ]
    obj.insert_polygons(polys, pts)

    # pass two - add as many times as you want 
    pts = [(0,-3,-1),(2,-2,1),(3,-1,1)]
    polys = [(3,2,1) ]
    obj.insert_polygons(polys, pts, reindex=True)

    obj.show()


    obj.save_obj("my_new_object.obj")

model_from_scratch()


#print( obj.get_face_data(1, reindex=True) ) 


#raw = obj.get_poly_geom(ids=[1])

#obj2 = object3d()
#obj2.insert( raw ) 
#obj2.save_obj('slice.obj')

# for i in range(obj.numpts):
# 
#     edges  = obj.get_face_edges(i)  
#     normal = obj.get_face_normal(i)
#     pos    = obj.get_face_centroid(i) 
# 
#     obj2.vectorlist_to_obj(edges[1])
#     obj2.vectorlist_to_obj( [normal], pos)

#obj2.save_obj("edges.obj")

#ropr = simple_render()
#ropr.render_obj((100,0,255), 0, 0, 0, 1, 150, object3d=obj2)
#ropr.save_image('simply_render.png')

 

"""
obj = object3d() 
obj.load_obj('objects/sphere2.obj')
geom = obj.get_poly_geom( (0,5) )

print( geom )
"""






#######################################################



def object_primitives():
    """ demo various built in primitive objects """

    obj = object3d() 

    position = (0,0,0)
    rotation = (0,0,0)
    size = 1 

    do_flush = False

    obj.prim_line( pos=position, rot=rotation, size=size)
    obj.save_obj("new_line.obj")
    if do_flush:
        obj.flush()

    obj.prim_triangle( pos=position, rot=rotation, size=size)
    obj.save_obj("new_triangle.obj")
    if do_flush:
        obj.flush()

    obj.prim_quad( pos=position, rot=rotation, size=size)
    obj.save_obj("new_quad.obj")
    if do_flush:
        obj.flush()

    obj.prim_circle( pos=position, rot=rotation, size=size)
    obj.save_obj("new_circle.obj")
    if do_flush:
        obj.flush()

    obj.prim_sphere( pos=position, rot=rotation, size=size)
    obj.save_obj("new_sphere.obj")
    if do_flush:
        obj.flush()

    obj.prim_cone( pos=position, rot=rotation, size=size)
    obj.save_obj("new_cone.obj")
    if do_flush:
        obj.flush()

    obj.prim_sphere( pos=position, rot=rotation, size=size)
    obj.save_obj("new_sphere.obj")
    if do_flush:
        obj.flush()

    obj.prim_locator( pos=position, rot=rotation, size=size)
    obj.save_obj("new_locator.obj")
    if do_flush:
        obj.flush()

    obj.prim_locator_xyz( pos=position, rot=rotation, size=size)
    obj.save_obj("new_locator_xyz.obj")
    if do_flush:
        obj.flush()

    #obj.prim_arrow( pos=position, rot=rotation, size=size)
    #obj.save_obj("new_arrow.obj")
    #if do_flush:
    #    obj.flush()




def build_perspective_matrix():
    #debug - NOT WORKING!  Work In Progress 

    obj = object3d()
    obj.prim_cube()
    #obj.scale_pts((3,3,30))
    obj.rotate_pts((30,30,30))
    ropr = simple_render()
    #                          fov, aspect, znear, zfar)
    #mx = m44.buildPerspProjMat( 200, 1, 1, 100)
    ropr.render_obj((100,0,255), 0, 0, 0, 1, 150, object3d=obj)
    ropr.save_image('simple_render.png')



def pass_matrix_to_render():
    """ use a 3X3 or 4X4 matrix to adjust a render 
        attempt to "visualize" a matrix 
    """

    obj = object3d()
    obj.prim_cube()
    ropr = simple_render()
    m44 = matrix44()
    m44.from_euler(45,45,0)
    ropr.render_matrix_obj( None, m44, 3, 100, 'custom_render.png' , obj      )




def three_renderers():
    """ example of the 3 main ways to render  
            - single object 
            - multi object (single in a loop)
            - scanline 
     """

    obj = object3d()
    obj.load_obj('objects/sphere2.obj')
    obj.triangulate() 

    ropr = simple_render()

    render_linecolor = (255,0,255)
    render_scale = 200 

    ####

    ## # some render properties you can tweak 
    ## ropr.SHOW_EDGES = False
    ## ropr.SHOW_FACE_CENTER = False
    ## ropr.COLOR_MODE = 'normal'
    ## ropr.COLOR_MODE = 'flat'
    ## ropr.SHOW_EDGES = True 

    ####

    # render single object 
    #ropr.render_obj((100,0,255), 0, 0, 0, 1, 150, object3d=obj)

    ####

    ##  render multiple objects
    ## obj2 = object3d()
    ## obj2.prim_quad()
    ## ropr.render_objects.append(obj) 
    ## ropr.render_objects.append(obj2) 
    ## #                GS (  color,  rx, ry, rz, linethick, scale)
    ## ropr.render_multiobj( render_linecolor, 45, 45, 45, 4, render_scale) 

    ####
    ## scanline render 
    ropr.scanline(obj, render_scale) 

    ropr.save_image('simple_render.png')




def angle_between_vectors():
    v1 = vec3(1, 0, 0)
    v2 = vec3(0, 1, 0)
    v3 = vec3()
    mu = math_util() 
    print( mu.rtd(v2.angle_between(v1))        ) 
    print( mu.rtd(v3.np_angle_between(v1, v2)) )



"""
#OLD WAY 

def model_from_scratch(): 
    # build a new polygon object from points 

    obj = object3d()

    # pass one - you can do as many as you like
    pts = [(1,1,1),(0,1,1),(-1,-1,1),(2,-2,1)]
    polys = [(1,2,3,4), (2,4,1)]
    obj._insert_poly_idxs(polys) # bug alert - do indices before points 
    obj._insert_points(pts)

    # pass two - add as many times as you want 
    pts = [(0,-3,-1),(2,-2,1),(3,-1,1)]
    polys = [(1,2,3)]
    obj._insert_poly_idxs(polys) # bug alert - do indices before points
    obj._insert_points(pts)

    obj.save_obj("my_new_object.obj")
""" 



def circle_with_cube_all_pts():
    """ make a circle with a rotated cube at each point """
    obj = object3d()
    obj.prim_circle(axis='z', pos=(0,0,0), spokes=42) 
    ctr = obj.get_face_centroid(0)
    obj.triangulate(force=True)
    pts = obj.get_face_pts(0) 
    ct = 0
    for pt in pts:
        tmp = object3d()
        tmp.prim_cube(size=.05, pos=pt, rot=(ct,ct,ct))
        ct += 10
        obj.insert(tmp)  
    obj.save_obj("cubey.obj")




def load_obj_build_another_from_it(objectpath):
    """ load an object, 
        turn its normals into another object, 
        render and save image and new object 

        load_obj_build_another_from_it('objects/sphere.obj')
        
    """

    obj = object3d()
    obj.load_obj(objectpath)

    obj2 = object3d()

    obj2.save_obj("edges.obj")

    ropr = simple_render()
    ropr.render_obj((100,0,255), 0, 0, 0, 1, 150, object3d=obj2)
    ropr.save_image('simply_render.png')




def load_obj_build_another_from_normals(objectpath):
    """ load an object, 
        turn its normals into another object, 
        render and save image and new object 

        load_obj_build_another_from_normals('objects/sphere.obj')

    """

    obj = object3d()
    obj.load_obj(objectpath)

    obj2 = object3d()
    for i in range(obj.numpts):
        edges  = obj.get_face_edges(i)  
        normal = obj.get_face_normal(i)
        pos    = obj.get_face_centroid(i) 

        obj2.vectorlist_to_obj(edges[1])
        obj2.vectorlist_to_obj( [normal], pos)

    obj2.save_obj("edges.obj")

    ropr = simple_render()
    ropr.render_obj((100,0,255), 0, 0, 0, 1, 150, object3d=obj2)
    ropr.save_image('simply_render.png')





