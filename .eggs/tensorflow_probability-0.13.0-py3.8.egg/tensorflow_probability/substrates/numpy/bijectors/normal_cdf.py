# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# This file is auto-generated by substrates/meta/rewrite.py
# It will be surfaced by the build system as a symlink at:
#   `tensorflow_probability/substrates/numpy/bijectors/normal_cdf.py`
# For more info, see substrate_runfiles_symlinks in build_defs.bzl
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# (This notice adds 10 to line numbering.)


# Copyright 2018 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""NormalCDF bijector."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Dependency imports
import numpy as np

from tensorflow_probability.python.internal.backend.numpy.compat import v2 as tf

from tensorflow_probability.substrates.numpy.bijectors import bijector
from tensorflow_probability.substrates.numpy.internal import assert_util
from tensorflow_probability.substrates.numpy.internal import dtype_util
from tensorflow_probability.substrates.numpy.internal import special_math

__all__ = [
    'NormalCDF',
]


@bijector.auto_composite_tensor_bijector
class NormalCDF(bijector.AutoCompositeTensorBijector):
  """Compute `Y = g(X) = NormalCDF(x)`.

  This bijector maps inputs from `[-inf, inf]` to `[0, 1]`. The inverse of the
  bijector applied to a uniform random variable `X ~ U(0, 1)` gives back a
  random variable with the
  [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution):

  ```none
  Y ~ Normal(0, 1)
  pdf(y; 0., 1.) = 1 / sqrt(2 * pi) * exp(-y ** 2 / 2)
  ```
  """

  def __init__(self,
               validate_args=False,
               name='normal'):
    """Instantiates the `NormalCDF` bijector.

    Args:
      validate_args: Python `bool` indicating whether arguments should be
        checked for correctness.
      name: Python `str` name given to ops managed by this object.
    """
    parameters = dict(locals())
    with tf.name_scope(name) as name:
      super(NormalCDF, self).__init__(
          validate_args=validate_args,
          forward_min_event_ndims=0,
          parameters=parameters,
          name=name)

  @classmethod
  def _is_increasing(cls):
    return True

  @classmethod
  def _parameter_properties(cls, dtype):
    return dict()

  def _forward(self, x):
    return special_math.ndtr(x)

  def _inverse(self, y):
    with tf.control_dependencies(self._assertions(y)):
      return tf.math.ndtri(y)

  def _forward_log_det_jacobian(self, x):
    return -0.5 * np.log(2 * np.pi) - tf.square(x) / 2.

  def _assertions(self, t):
    if not self.validate_args:
      return []
    return [
        assert_util.assert_non_negative(
            t, message='Inverse transformation input must be greater than 0.'),
        assert_util.assert_less_equal(
            t,
            dtype_util.as_numpy_dtype(t.dtype)(1.),
            message='Inverse transformation input must be less than or equal '
            'to 1.')]

