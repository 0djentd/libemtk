# ##### BEGIN GPL LICENSE BLOCK #####
#
# Copyright 2022, Sergey Shapochkin
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import unittest

from libemtk.clusters.cluster_trait import ClusterTrait
from libemtk.clusters.clusters_layer import ClustersLayer
from libemtk.clusters.modifiers_cluster import ModifiersCluster
from libemtk.dummy_modifiers import DummyBlenderModifier, DummyBlenderObj
from libemtk.lists.extended_modifiers_list import ExtendedModifiersList

try:
    import bpy
    _WITH_BPY = True
except ModuleNotFoundError:
    _WITH_BPY = False

# TODO: rework this tests and create different files for different modules.

MODIFIERS_DATA = [
    ('Bevel', 'BEVEL'),
    ('Bevel', 'BEVEL'),
    ('Bevel', 'BEVEL'),
    ('Bevel', 'BEVEL'),
    ('Bevel', 'BEVEL'),
    ('Bevel', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel2', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('MediumBevel', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Boolean3', 'BOOLEAN'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('Bevel2', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Bevel5', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel2', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel6', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel2', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('MediumBevel', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel2', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('MediumBevel', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Boolean3', 'BOOLEAN'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('Bevel2', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Bevel5', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Boolean3', 'BOOLEAN'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('Bevel2', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Bevel5', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel2', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel6', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Boolean3', 'BOOLEAN'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('Bevel2', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Bevel5', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel2', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel6', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel2', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('MediumBevel', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel2', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('MediumBevel', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Boolean3', 'BOOLEAN'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('Bevel2', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Bevel5', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Boolean3', 'BOOLEAN'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Bevel5', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('Bevel2', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('Bevel5', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel5', 'BEVEL'),
    ('Bevel2', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel6', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('Boolean3', 'BOOLEAN'),
    ('Bevel2', 'BEVEL'),
    ('Boolean3', 'BOOLEAN'),
    ('MediumBevel', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Bevel6', 'BEVEL'),
    ('Array', 'ARRAY'),
    ('Array', 'ARRAY'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
    ('TopBevel', 'BEVEL'),
    ('WeightedNormal', 'WEIGHTED_NORMAL'),
]


def add_modifiers(obj, count) -> list[DummyBlenderModifier]:
    """Creates list of modifiers."""
    mods = []
    if count > len(MODIFIERS_DATA):
        raise ValueError
    for i, x in enumerate(MODIFIERS_DATA):
        if i == count:
            break
        mod = obj.modifier_add(x[0], x[1])
        mods.append(mod)
    return mods


class ExtendedModifiersListTests():
    """ExtendedModifiersList tests."""

    def setUp(self):
        self.o = DummyBlenderObj()
        add_modifiers(self.o, 1)
        self.e = ExtendedModifiersList(self.o)

    def tearDown(self):
        del(self.o)
        del(self.e)

    def test_all_clusters_initialized(self):
        result = True
        for x in self.e.all_clusters():
            if not x.instance_data['initialized']:
                if not isinstance(result, list):
                    result = []
                result.append(x)
        self.assertTrue(result)

    def test_all_clusters_have_modifiers(self):
        result = True
        for x in self.e.all_clusters():
            if len(x._data) == 0:
                if not isinstance(result, list):
                    result = []
                result.append(x)
        self.assertTrue(result)

    def test_duplicate_cluster_names(self):
        result = True
        names = []
        for x in self.e.all_clusters():
            if x.name not in names:
                names.append(x.name)
            else:
                if not isinstance(result, list):
                    result = []
                result.append(x)
        self.assertTrue(result)

    def test_duplicate_clusters(self):
        result = False
        i = 0
        for x in self.e.all_clusters():
            i = 0
            for y in self.e.all_clusters():
                if y is x:
                    i += 1
                    if i != 1:
                        if not isinstance(result, list):
                            result = []
                        result.append(x)
        self.assertFalse(result)

    def test_duplicate_modifiers(self):
        result = False
        i = 0
        for x in self.e.all_modifiers():
            i = 0
            for y in self.e.all_modifiers():
                if y is x:
                    i += 1
                    if i != 1:
                        if not isinstance(result, list):
                            result = []
                        result.append(x)
        self.assertFalse(result)

    def test_all_clusters_is_clusters(self):
        result = True
        for x in self.e.all_clusters():
            if not isinstance(x, ClusterTrait):
                if not isinstance(result, list):
                    result = []
                result.append(x)
        self.assertTrue(result)

    def test_all_clusters_have_object(self):
        result = True
        for x in self.e.all_clusters():
            if x._object is None:
                if not isinstance(result, list):
                    result = []
                result.append(x)
        self.assertTrue(result)

    def test_all_clusters_have_active(self):
        result = False
        for x in self.e.all_layers():
            if x._mod is None:
                if not isinstance(result, list):
                    result = []
                result.append(x)
        self.assertFalse(result)

    def test_all_clusters_are_sane(self):
        result = False
        for x in self.e.all_clusters():
            if not x.check_this_cluster_sanity():
                if not isinstance(result, list):
                    result = []
                result.append(x)
        self.assertFalse(result)

    def test_actual_modifiers_count(self):
        self.assertEqual(len(self.e.all_modifiers()),
                         len(self.o.modifiers))

    def test_actual_modifiers_types(self):
        result = False
        for x, y in zip(self.e.all_modifiers(),
                        self.o.modifiers):
            if x.type != y.type:
                if not isinstance(result, list):
                    result = []
                result.append(x)
        self.assertFalse(result)

    def test_actual_modifiers_names(self):
        result = False
        for x, y in zip(self.e.all_modifiers(),
                        self.o.modifiers):
            if x.name != y.name:
                if not isinstance(result, list):
                    result = []
                result.append(x)
        self.assertFalse(result)

    def test_active_is_in_the_list(self):
        self.assertTrue(self.e.active in self.e)

    def test_clusters_active_is_in_the_list(self):
        result = False
        for x in self.e.all_layers():
            if self.e.active not in self.e:
                if not isinstance(result, list):
                    result = []
                result.append(x)
        self.assertFalse(result)

    def test_clusters_active_exists(self):
        result = False
        for x in self.e.all_layers():
            if x._mod is None:
                if not isinstance(result, list):
                    result = []
                result.append(x)
        self.assertFalse(result)

    def test_get_cluster(self):
        c = self.e.get_cluster()
        self.assertEqual(c, self.e[0])

    def test_get_layer(self):
        layer = self.e.get_layer()
        self.assertEqual(layer, self.e)

    def test_get_cluster_and_remove(self):
        old_l = len(self.o.modifiers)
        c = self.e.get_cluster()
        layer = self.e.get_layer()
        length = len(c.all_modifiers())
        layer.remove(c)
        new_l = len(self.o.modifiers)
        self.assertEqual(new_l, old_l-length)

    def test_remove_cluster(self):
        old_l = len(self.e._data)
        self.e.remove(self.e[0])
        new_l = len(self.e._data)
        self.assertEqual(new_l, old_l-1)

    def test_remove_modifiers(self):
        old_l = len(self.o.modifiers)
        c = self.e[0]
        length = len(c.all_modifiers())
        self.e.remove(c)
        new_l = len(self.o.modifiers)
        self.assertEqual(new_l, old_l-length)

    def test_remove_cluster_last(self):
        old_l = len(self.e._data)
        c = self.e[-1]
        length = len(c.all_modifiers())
        self.e.remove(c)
        new_l = len(self.e._data)
        self.assertEqual(new_l, old_l-length)

    def test_remove_modifiers_last(self):
        old_l = len(self.o.modifiers)
        self.e.remove(self.e[-1])
        new_l = len(self.o.modifiers)
        self.assertEqual(new_l, old_l-1)

    def test_get_cluster_and_apply(self):
        old_l = len(self.o.modifiers)
        c = self.e.get_cluster()
        layer = self.e.get_layer()
        length = len(c.all_modifiers())
        layer.apply(c)
        new_l = len(self.o.modifiers)
        self.assertEqual(new_l, old_l-length)

    def test_apply_cluster(self):
        old_l = len(self.e._data)
        self.e.apply(self.e[0])
        new_l = len(self.e._data)
        self.assertEqual(new_l, old_l-1)

    def test_apply_modifiers(self):
        old_l = len(self.o.modifiers)
        c = self.e[0]
        length = len(c.all_modifiers())
        self.e.apply(c)
        new_l = len(self.o.modifiers)
        self.assertEqual(new_l, old_l-length)

    def test_apply_cluster_last(self):
        old_l = len(self.e._data)
        c = self.e[-1]
        length = len(c.all_modifiers())
        self.e.apply(c)
        new_l = len(self.e._data)
        self.assertEqual(new_l, old_l-length)

    def test_apply_modifiers_last(self):
        old_l = len(self.o.modifiers)
        self.e.apply(self.e[-1])
        new_l = len(self.o.modifiers)
        self.assertEqual(new_l, old_l-1)


class DifferentModifiersTests(
        ExtendedModifiersListTests, unittest.TestCase):
    """No complex modifiers clusters."""

    def setUp(self):
        self.o = DummyBlenderObj()
        add_modifiers(self.o, 10)
        self.e = ExtendedModifiersList(self.o)


class LoadClustersTests(
        ExtendedModifiersListTests, unittest.TestCase):
    """Saving and loading clusters."""

    def setUp(self):
        self.o = DummyBlenderObj()
        add_modifiers(self.o, 10)
        self.e = ExtendedModifiersList(self.o)
        self.e.save_modifiers_state()
        self.e.save_clusters_state()
        self.old_clusters_state = self.e.get_clusters_state()
        del(self.e)
        self.e = ExtendedModifiersList(self.o)
        self.old_clusters_state_2 = self.e.get_clusters_state()
        del(self.e)
        self.e = ExtendedModifiersList(self.o)

    def test_number_of_clusters(self):
        self.assertEqual(len(self.e), 10)

    def test_check_clusters_state_eq(self):
        self.assertEqual(
            self.old_clusters_state, self.e.get_clusters_state())

    def test_check_clusters_state_eq_2(self):
        self.assertEqual(
            self.old_clusters_state_2, self.e.get_clusters_state())


@unittest.skip
class ProgressiveLoadClustersTests(
        ExtendedModifiersListTests, unittest.TestCase):
    """Saving and loading clusters."""

    def setUp(self):
        self.o = DummyBlenderObj()
        add_modifiers(self.o, 10)
        self.e = ExtendedModifiersList(self.o)
        self.e.save_modifiers_state()
        self.e.save_clusters_state()
        self.old_clusters_state = self.e.get_clusters_state()
        del(self.e)
        self.e = ExtendedModifiersList(self.o)
        self.old_clusters_state_2 = self.e.get_clusters_state()
        del(self.e)
        self.e = ExtendedModifiersList(self.o)

    def test_number_of_clusters(self):
        self.assertEqual(len(self.e), 7)

    def test_check_clusters_state_eq(self):
        self.assertEqual(
            self.old_clusters_state, self.e.get_clusters_state())

    def test_check_clusters_state_eq_2(self):
        self.assertEqual(
            self.old_clusters_state_2, self.e.get_clusters_state())


class LayersTests(unittest.TestCase):
    """Cluster layers and complex clusters."""

    def setUp(self):
        self.o = DummyBlenderObj()
        add_modifiers(self.o, 50)
        clusters = []

        cluster = ModifiersCluster(cluster_name='Beveled Boolean',
                                   cluster_type='BEVELED_BOOLEAN',
                                   modifiers_by_type=[
                                       ['BOOLEAN'], ['BEVEL']],
                                   modifiers_by_name=[['ANY'], ['ANY']],
                                   cluster_priority=0,
                                   cluster_createable=True,
                                   )
        clusters.append(cluster)

        cluster = ModifiersCluster(cluster_name='Triple Bevel',
                                   cluster_type='TRIPLE_BEVEL',
                                   modifiers_by_type=[
                                       ['BEVEL'], ['BEVEL'], ['BEVEL']],
                                   modifiers_by_name=[
                                       ['ANY'], ['ANY'], ['ANY']],
                                   cluster_priority=0,
                                   cluster_createable=True,
                                   )
        clusters.append(cluster)

        cluster = ClustersLayer(cluster_name='Double Triple Bevel Cluster',
                                cluster_type='BEVEL_CLUSTER',
                                modifiers_by_type=[
                                    ['TRIPLE_BEVEL'], ['TRIPLE_BEVEL']],
                                modifiers_by_name=[['ANY'], ['ANY']],
                                cluster_priority=0,
                                cluster_createable=True,
                                )
        clusters.append(cluster)

        self.e = ExtendedModifiersList(self.o, cluster_types=clusters)

    def test_first_cluster_is_double_bevel(self):
        self.assertEqual(self.e[0].type, 'BEVEL_CLUSTER')

    def test_first_cluster_has_two_triple_bevels(self):
        self.assertEqual(
            self.e[0][0].type, 'TRIPLE_BEVEL')

    def test_triple_bevel_has_bevel(self):
        self.assertEqual(
            self.e[0][0][0].type, 'BEVEL')

    def test_triple_bevel_has_three_modifiers(self):
        self.assertEqual(
            len(self.e[0][0]), 3)

    def test_trace_cluster(self):
        x = []
        x.append(self.e)
        x.append(self.e[0])
        x.append(x[1][0])
        t = self.e.get_trace_to(x[2])
        self.assertEqual(t, x[0: -1])


class MovingTests(unittest.TestCase):
    """Cluster layers and complex clusters."""

    def setUp(self):
        self.o = DummyBlenderObj()
        add_modifiers(self.o, 50)
        clusters = []

        cluster = ModifiersCluster(cluster_name='Beveled Boolean',
                                   cluster_type='BEVELED_BOOLEAN',
                                   modifiers_by_type=[
                                       ['BOOLEAN'], ['BEVEL']],
                                   modifiers_by_name=[['ANY'], ['ANY']],
                                   cluster_priority=0,
                                   cluster_createable=True,
                                   )
        clusters.append(cluster)

        cluster = ModifiersCluster(cluster_name='Triple Bevel',
                                   cluster_type='TRIPLE_BEVEL',
                                   modifiers_by_type=[
                                       ['BEVEL'], ['BEVEL'], ['BEVEL']],
                                   modifiers_by_name=[
                                       ['ANY'], ['ANY'], ['ANY']],
                                   cluster_priority=0,
                                   cluster_createable=True,
                                   )
        clusters.append(cluster)

        cluster = ClustersLayer(cluster_name='Double Triple Bevel Cluster',
                                cluster_type='BEVEL_CLUSTER',
                                modifiers_by_type=[
                                    ['TRIPLE_BEVEL'], ['TRIPLE_BEVEL']],
                                modifiers_by_name=[['ANY'], ['ANY']],
                                cluster_priority=0,
                                cluster_createable=True,
                                )
        clusters.append(cluster)

        self.e = ExtendedModifiersList(self.o, cluster_types=clusters)

        self.moved_cluster = self.e[1]
        self.moved_cluster_2 = self.e[2]
        self.e.move_down(self.moved_cluster)

    def tearDown(self):
        del self.o
        del self.e
        del self.moved_cluster
        del self.moved_cluster_2

    def test_moved_cluster_up(self):
        self.assertEqual(self.moved_cluster, self.e[2])

    def test_moved_cluster_down(self):
        self.assertEqual(self.moved_cluster_2, self.e[1])
