![PyPI](https://img.shields.io/pypi/v/libemtk)
![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/0djentd/libemtk?include_prereleases)
[![Python package](https://github.com/0djentd/libemtk/actions/workflows/python-package.yml/badge.svg)](https://github.com/0djentd/libemtk/actions/workflows/python-package.yml)
![GitHub Repo stars](https://img.shields.io/github/stars/0djentd/libemtk?style=social)

libEMTK, Extended Modifiers Tool Kit (library).
=======================================

This thing provides new level of abstraction for _Blender_ modifiers stack.

Library name is not final and probably will be changed on release.

_libemtk_ is designed to be used with [_EMTK_](https://github.com/0djentd/emtk).

Most classes and methods have docstrings.

There are some simple unittests for basic operations.

# Installation
Linux:
Symlink `~/.config/blender/3.1/scripts/modules/libemtk` to `libemtk`

Windows:
idk

Mac:
idk

# Main concepts
_Actual_ _modifier_ is an actual Blender modifier.

_Modifier_ is a cluster or actual Blender modifier.

_Cluster_ is an object that consists of any number
of modifiers or clusters.
Any subclass of _ClusterTrait_ is a _Cluster_. 

_ModifiersCluster_ is a cluster that only has
actual Blender modifiers in it.

_ClustersLayer_ is a cluster that only has
other clusters in it. This doesnt mean
that it cant contain ModifiersClusters
with actual modifiers.

_ExtendedModifiersList_ is an object representing
clusters stack. It is similar to ClustersLayer,
but doesnt have ClusterTrait attributes.
It require all modifiers in it to be on the same Blender object.

_SortingRule_ is an object that represents set of
rules that can be used to sort clusters in ExtendedModifiersList.

_ModifiersOperator_ is a mix-in class for Operator class.
It has methods for manipulating multiple
ExtendedModifiersList instances.

_ClustersCommand_ is implementation of command pattern for
some of frequently used operations.

It consists of _ClustersAction_, basic elements that have minimal information
about side effects of command.
Examble:
ClustersAction('MOVE', 'Bevel.123', {'direction': 'UP'})
This action does not included information about position of 'Bevel.123' and
other detail required to interpret action as a part of command.

ClusterCommands use _ClustersCommandsSolver_ to ask clusters for additional commands.
Example:
(using previous example)
ClustersLayer will add ClustersAction('MOVE', 'Bevel.321', {'direction': 'DOWN'}),
if 'Bevel.321' will change its index after moving 'Bevel.123'.
Then ClustersCommandsSolver will ask 'Bevel.321' if it should do something else
after moving it.

# Currently supported features # 
All basic editing, like moving, applying, removing,
duplication and switching visibility of clusters.

Serialization and deserialization of clusters state.
Full or partial resoring of clusters state.

Serialization and deserialization of clusters types definitions.

Clusters Commands and Actions.

# TODO # 
Buffering for ExtendedModifiersList controller.

Panel type subclass for panels that use
ExtendedModifiersList.

Operators for ExtendedModifiersList controller.

More clusters operation types.
