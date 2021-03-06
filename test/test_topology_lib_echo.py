# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Test suite for module topology_lib_echo.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock

from topology_lib_echo.library import echo


def test_echo():
    """
    Test that the echo command is constructed properly.
    """
    node_mock = Mock()

    echo(
        node_mock, 'I am echoed!', trailing_newline=True,
        backslash_escape=False, shell='bash'
    )

    node_mock.assert_called_with('echo "I am echoed!"', shell='bash')

    echo(
        node_mock, 'I am echoed!', trailing_newline=False,
        backslash_escape=True, shell='bash'
    )

    node_mock.assert_called_with('echo -n -e "I am echoed!"', shell='bash')
