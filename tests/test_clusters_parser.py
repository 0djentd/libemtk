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

from libemtk.clusters.modifiers_cluster import ModifiersCluster


class ClustersSerializationClusterTests(
        unittest.TestCase):

    def setUp(self):
        self.cluster = ModifiersCluster(cluster_name='Beveled Boolean',
                                        cluster_type='BEVELED_BOOLEAN',
                                        modifiers_by_type=[
                                            ['BOOLEAN'], ['BEVEL']],
                                        modifiers_by_name=[['ANY'], ['ANY']],
                                        cluster_priority=0,
                                        cluster_createable=True,
                                        )

        self.serialized_cluster = self.cluster.\
            get_this_cluster_parser_variables()

    def tearDown(self):
        del(self.cluster)
        del(self.serialized_cluster)

    def test_getparser_variables(self):
        x = self.cluster.get_this_cluster_parser_variables()
        self.assertEqual(x, self.serialized_cluster)
