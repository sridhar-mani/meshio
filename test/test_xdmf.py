# -*- coding: utf-8 -*-
#
import meshio
import pytest

import helpers
import legacy_reader

vtk = pytest.importorskip('vtk')


@pytest.mark.skipif(not hasattr(vtk, 'vtkXdmf3Writer'), reason='Need XDMF3')
@pytest.mark.parametrize('mesh', [
        helpers.tri_mesh,
        helpers.quad_mesh,
        helpers.tet_mesh,
        helpers.add_point_data(helpers.tri_mesh, 1),
        helpers.add_cell_data(helpers.tri_mesh, 1)
        ])
def test_xdmf3(mesh):
    helpers.write_read(
        meshio.xdmf_io.write,
        meshio.xdmf_io.read,
        mesh, 1.0e-15
        )
    return


@pytest.mark.skipif(not hasattr(vtk, 'vtkXdmf3Writer'), reason='Need XDMF3')
@pytest.mark.parametrize('mesh', [
        helpers.tri_mesh,
        helpers.quad_mesh,
        helpers.tet_mesh,
        helpers.add_point_data(helpers.tri_mesh, 1),
        helpers.add_cell_data(helpers.tri_mesh, 1)
        ])
def test_xdmf3_legacy_writer(mesh):
    # test with legacy writer
    def legacy_writer(*args, **kwargs):
        return meshio.legacy_writer.write('xdmf3', *args, **kwargs)

    helpers.write_read(
        legacy_writer,
        meshio.xdmf_io.read,
        mesh, 1.0e-15
        )
    return


@pytest.mark.skipif(not hasattr(vtk, 'vtkXdmf3Reader'), reason='Need XDMF3')
@pytest.mark.parametrize('mesh', [
        helpers.tri_mesh,
        helpers.quad_mesh,
        helpers.tet_mesh,
        helpers.add_point_data(helpers.tri_mesh, 1),
        helpers.add_cell_data(helpers.tri_mesh, 1)
        ])
def test_xdmf3_legacy_reader(mesh):
    # test with legacy reader
    def lr(filename):
        return legacy_reader.read('xdmf3', filename)

    helpers.write_read(
        meshio.xdmf_io.write,
        lr,
        mesh, 1.0e-15
        )
    return


@pytest.mark.skipif(not hasattr(vtk, 'vtkXdmfWriter'), reason='Need XDMF3')
@pytest.mark.parametrize('mesh', [
        helpers.tri_mesh,
        helpers.quad_mesh,
        helpers.tet_mesh,
        helpers.add_point_data(helpers.tri_mesh, 1),
        helpers.add_cell_data(helpers.tri_mesh, 1)
        ])
def test_xdmf2_legacy_writer(mesh):
    # test with legacy writer
    def legacy_writer(*args, **kwargs):
        return meshio.legacy_writer.write('xdmf2', *args, **kwargs)

    helpers.write_read(
        legacy_writer,
        meshio.xdmf_io.read,
        # FIXME data is only stored in single precision
        # <https://gitlab.kitware.com/vtk/vtk/issues/17037>
        mesh, 1.0e-6
        )
    return
