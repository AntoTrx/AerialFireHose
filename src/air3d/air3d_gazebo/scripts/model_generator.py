from sdf_generator import *
import numpy as np


def multiple_drones(name='multiple_drones', N=4):
    sdfgen = SDFGenerator(name, folder='../models/')
    sdfgen.generateConfigFile()
    sdfgen.open()
    for i in range(N):
        xy_ = 2*np.random.randn(2)
        pose_ = np.array([xy_[0], xy_[1], 0., 0., 0., 0.])
        sdfgen.addline(sdfgen.includeDrone(
            "drone"+str(i), pose_, updateRate=500.0))
    sdfgen.close()


def flexible_cable(name='flexible_cable', l=1, r=0.00125, mass=0.1, N=10):
    body_length = l/float(N)
    half_body_length = body_length/2.0
    body_mass = mass/float(N)
    k = 0
    c = 0.01
    sdfgen = SDFGenerator(name=name, folder='../models/')
    sdfgen.generateConfigFile()
    sdfgen.open()

    #  link_name, pose, l=1, r=0.1, mass=0.005, ixx=0.0001,
    #  iyy=0.0001, izz=0.0001, ixy=0., ixz=0., iyz=0., material='Yellow'
    sdfgen.addline(sdfgen.addCylinder(
        link_name="link_0", pose=np.zeros(6), l=body_length, r=r, mass=body_mass))
    for i in range(N-1):
        pose_ = np.zeros(6)
        pose_[0] = (i+1)*body_length
        sdfgen.addline(sdfgen.addCylinder(
            link_name="link_"+str(i+1), pose=pose_, l=body_length, r=r, mass=body_mass))

        joint_name = "joint_"+str(i)
        link1_name = "link_"+str(i)
        link2_name = "link_"+str(i+1)
        rel_pose_ = np.array([-half_body_length, 0., 0., 0., 0., 0.])
        sdfgen.addline(sdfgen.addUniversalJoint(
            joint_name, link1_name, link2_name, rel_pose_, k=k, c=c))
    sdfgen.close()


def air3d_model(name='air3d', L=4, N=40, rho=0.1):
    """
    12awg ~ 0.1 kg/meter
    """
    # flexible cable
    cable_length = L
    cable_radius = 0.00125
    cable_num_links = N
    cable_mass = L*rho
    segment_length = cable_length/cable_num_links
    flexible_cable(name='lumped_tether', l=cable_length,
                   r=cable_radius, mass=cable_mass, N=cable_num_links)

    sdfgen = SDFGenerator(name=name, folder='../models/')
    sdfgen.generateConfigFile()
    sdfgen.open()

    # adding the tether to the model
    sdfgen.addline(sdfgen.includeObject(
        "lumped_tether", np.array([0.5*segment_length, 0, 0., 0., 0., 0.]), "lumped_tether"))

    # fixing the tether to the static base
    sdfgen.addline(sdfgen.addBallJoint("fixed_to_base",
                                       "world", "lumped_tether::link_0",
                                       np.array([-0.5*segment_length, 0.0, 0., 0., 0., 0.]), c=0.01))

    # adding end-effector drone
    pose_ = np.array([L, 0, 0.03, 0., 0., 0.])
    sdfgen.addline(sdfgen.includeDrone(
        "droneEndEffector", pose_, updateRate=500.0))

    # creating a ball joint between end-effector drone and the tether
    # MIGHT HAVE TO CHANGE TO FIXED JOINT (future work)
    sdfgen.addline(sdfgen.addBallJoint("drone_cable_joint_end_effector",
                                       "droneEndEffector::base_link", "lumped_tether::link_" +
                                       str(cable_num_links-1),
                                       np.array([0.5*segment_length, 0.0, 0., 0., 0., 0.]), c=0.01))

    # adding intermediate drone
    # adding intermediate drone at (25/N)*L distance from the static base
    intermedia_link_index = 24
    pose_ = np.array(
        [((intermedia_link_index+1)*segment_length), 0, 0.03, 0., 0., 0.])
    sdfgen.addline(sdfgen.includeDrone(
        "droneIntermediate", pose_, updateRate=500.0))

    # creating a ball joint between intermedia link and the tether at link intermedia_link_index
    # MIGHT HAVE TO CHANGE TO FIXED JOINT (future work)
    sdfgen.addline(sdfgen.addBallJoint("drone_cable_joint_intermediate",
                                       "droneIntermediate::base_link", "lumped_tether::link_" +
                                       str(intermedia_link_index),
                                       np.array([0.5*segment_length, 0.0, 0., 0., 0., 0.]), c=0.01))

    sdfgen.close()


if __name__ == '__main__':
    # multiple_drones(N=3)
    # flexible_cable(name='sample', N=20)
    air3d_model(name='air3d', L=4, N=40)
